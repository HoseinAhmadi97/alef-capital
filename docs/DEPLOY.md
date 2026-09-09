# Server setup — alefcapital.ir

---

## Decision summary

At this stage the site is **fully static**: 18 HTML files. For 100 users this is almost no load at all.

| | Choice | Why |
|---|---|---|
| Web server | **Caddy** | Gets HTTPS automatically and renews it automatically. One 30-line config file instead of nginx + certbot + cron. |
| Runtime | **Docker Compose** | Comes up with one command, portable to any server. |
| Updates | `git pull && make build` | The `dist/` folder is mounted as a volume; **no image rebuild is needed, and no restart**. A content change goes live in seconds. |
| Server | 1 vCPU / 2GB RAM | More than enough for this volume. |

---

## 1. Server

A simple VPS is enough. Suggested specs to start with:

- **1 CPU core, 2 GB RAM, 20 GB disk**
- Ubuntu 22.04 or 24.04
- Preferably a **datacenter inside Iran** — network latency for Iranian users directly affects the conversion rate

> ⚠️ **Do not bring the site up on the trading algorithm's server.**
> A public web server on the machine that runs the algorithm and the brokerage connection
> opens up the attack surface for no reason. Keep the two separate.

Installing the prerequisites:

```bash
sudo apt update && sudo apt install -y git make python3 docker.io docker-compose-plugin
sudo usermod -aG docker $USER   # then log out and log back in once
```

---

## 2. Domain

In your domain registrar's panel (IRNIC or a reseller), create two A records:

| Type | Name | Value |
|---|---|---|
| A | `@` | Server IP |
| A | `www` | Server IP |

DNS propagation usually takes a few minutes to a few hours. To check:

```bash
dig +short alefcapital.ir
```

> Caddy must be reachable on port 80 to obtain a certificate from Let's Encrypt.
> If you put a CDN (such as ArvanCloud) in front of the site, **bring it up without the CDN first** so the certificate is issued,
> then enable the CDN.

---

## 3. Bringing it up

First check whether ports 80 and 443 are free — this determines which path you take:

```bash
sudo ss -ltnp | grep -E ':(80|443)\s'
```

### Case A — the ports are free (fresh server)

```bash
sudo mkdir -p /srv && cd /srv
git clone <your repository URL> alef-capital
cd alef-capital

make build
docker compose -f deploy/docker-compose.yml up -d
```

That's it. A few seconds later `https://alefcapital.ir` is up with a valid certificate.

```bash
docker compose -f deploy/docker-compose.yml logs -f caddy
```

### Case B — nginx is already on the server

If the `ss` output showed nginx sitting on 80/443 (for Grafana, say),
Caddy cannot bind. Add the site to that same nginx — Docker is not needed.

> ⚠️ Do not bring Docker onto such a machine: Docker writes its own iptables rules
> and bypasses ufw. On a server that has Postgres, `ports:` in
> docker-compose can open something you think is closed.

```bash
sudo mkdir -p /srv && sudo chown $USER /srv
cd /srv && git clone <your repository URL> alef-capital
cd alef-capital && make build

sudo ln -sfn /srv/alef-capital/dist /srv/site
sudo cp deploy/nginx.conf /etc/nginx/sites-available/alefcapital.ir
sudo ln -s /etc/nginx/sites-available/alefcapital.ir /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```

`nginx -t` must return `syntax is ok`; if it does not, do not reload, so the
existing sites stay healthy.

Then the certificate (once the A records have propagated):

```bash
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d alefcapital.ir -d www.alefcapital.ir
sudo certbot renew --dry-run
```

certbot only changes this block and leaves nginx's other blocks alone.

> Until certbot has run, `https://alefcapital.ir` will take you to another service
> with a certificate error — because that is the only 443 block. After certbot it is fixed.

---

## 4. Your day-to-day workflow

This is the most important section, because you are going to be working on the site constantly.

**On the laptop:**

```bash
make serve          # http://localhost:8000 — see your changes
make check          # make sure nothing broke
git commit -am "change the gold plan price"
git push
```

**On the server:**

```bash
./deploy/deploy.sh
```

This script runs `git pull`, builds the site, checks the links, and that's it.
It detects on its own whether you have nginx or Caddy.

**Neither a restart nor a reload is needed** — in both cases the web server reads the files directly
from `dist/`. If you prefer to do it by hand, these two commands are enough:

```bash
cd /srv/alef-capital && git pull && make build
```

If you want this automated too, `.github/workflows/deploy.yml` is ready:
create three Secrets (`SSH_HOST`, `SSH_USER`, `SSH_KEY`) in the repository settings, and every
push to `main` publishes the site automatically.

---

## 5. Capacity — why 100 users is not a problem

Let's put numbers on it:

| | Value |
|---|---|
| Size of each page (HTML with inline CSS) | about 55 KB |
| After gzip/zstd compression | about 12 KB |
| 100 users opening a page **at the same time** | about 1.2 MB |
| Processing required | just reading a file from disk |

A single CPU core serves several thousand static requests per second. 100 concurrent users
do not even consume 1 percent of this server's capacity. **Your bottleneck is bandwidth and network
latency, not CPU.**

Three things that genuinely help speed (all three are configured in `deploy/Caddyfile`):

1. **Compression** — 55 KB down to 12 KB
2. **Asset caching** — fonts and images are cached for a year, HTML is not cached
3. **HTTP/2 and HTTP/3** — enabled by default

The biggest speed win is something that has nothing to do with the server: **self-hosting the font**
(`make fonts`). The font from Google Fonts can take several seconds for an Iranian user,
or never arrive at all.

---

## 6. When the API is added

The site is static for now, but the dashboards need live data. Proposed architecture:

```
                    ┌─────────────┐
   User browser ───►│    Caddy    │
                    └──────┬──────┘
                     ┌─────┴─────┐
                     ▼           ▼
              dist/ (static)  FastAPI
                                 │
                    ┌────────────┼────────────┐
                    ▼            ▼            ▼
                 Redis      PostgreSQL  Market reader
               (1s cache)  (TimescaleDB) (one process)
```

**One point that changes everything:** put a Redis cache with a one-second lifetime
between the API and the database. Then 100 users fetching data every 5 seconds
hit the API with roughly 20 requests per second but only **about 1 query per second**
reaches the database. Without that cache, those same 20 requests land straight on the database.

The general rule: **one process reads from the market, everyone else reads from the cache.**
Never let the number of users affect the number of requests to the data source.

For this stage:

- Upgrade the server to **2 cores / 4 GB RAM**
- Uvicorn with 2 to 4 workers is enough
- For real-time data, SSE is simpler than WebSocket and sufficient for a one-way stream
- The `api.alefcapital.ir` block in the `Caddyfile` is commented out and ready

---

## 7. Backups

At this stage only two things are worth keeping:

1. **The git repository itself** — the whole site is rebuilt from it
2. **The volume named `caddy_data`** — the TLS certificates are in it

```bash
docker run --rm -v alef-capital_caddy_data:/data -v $(pwd):/backup \
  alpine tar czf /backup/caddy-data.tar.gz /data
```

The `dist/` folder needs no backup; a single `make build` recreates it.

---

## 8. Checklist before going public

- [ ] `make fonts` and `SELF_HOSTED_FONT = True`
- [ ] The data layer is connected to a real API (the `LIVE DATA LAYER` comment on each page)
- [ ] The `{{ }}` placeholders are filled in: team name, registration number, address, minimum capital
- [ ] `make check` is green
- [ ] DNS records have propagated and the HTTPS certificate has been issued
- [ ] Electronic trust symbol (eNamad) — required for a financial site that sells subscriptions
- [ ] Legal texts reviewed: `legal-risk`, `legal-terms` and `legal-privacy`
