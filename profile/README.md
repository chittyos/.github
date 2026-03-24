# ChittyOS

**Trust infrastructure and intelligent operating system for verification, identity, and evidence.**

ChittyOS is a distributed platform of Cloudflare Workers powering identity resolution, evidence processing, trust scoring, and service orchestration across the Chitty ecosystem.

## Architecture

Services are organized by tier, where lower tiers have no upstream dependencies:

| Tier | Services | Purpose |
|------|----------|---------|
| **0** | ChittyID, ChittyTrust, ChittySchema | Trust anchors — identity, trust resolution, schema governance |
| **1** | ChittyAuth, ChittyCert, ChittyRegister | Core identity — authentication, certification, service registration |
| **2** | ChittyConnect, ChittyRouter, ChittyAPI | Platform — API gateway, MCP server, intelligent routing |
| **3** | ChittyMonitor, ChittyTrack, ChittyBeacon | Operational — observability, logging, distributed tracking |
| **4** | ChittyEvidence, ChittyIntel, ChittyScore | Domain — evidence processing, intelligence, scoring |
| **5** | ChittyCases, ChittyDashboard, ChittyCommand | Application — case management, dashboards, automation |

Every service exposes a health endpoint at `https://{service}.chitty.cc/health` and follows the compliance triad: `CHARTER.md` (contract) + `CHITTY.md` (architecture) + `CLAUDE.md` (dev guide).

## Key Projects

| Project | What It Does |
|---------|-------------|
| [**ChittyConnect**](https://github.com/chittyos/chittyconnect) | AI-intelligent spine with ContextConsciousness and MemoryCloude — REST API, MCP server, GitHub App |
| [**ChittyCore**](https://github.com/chittyos/chittycore) | Shared `@chittyos/core` package — ID, auth, verification, beacon, brand, canon, agents |
| [**ChittyRouter**](https://github.com/chittyos/chittyrouter) | Intelligent gateway with prompt-lookup, circuit breaking, and AI-powered routing |
| [**ChittyMCP**](https://github.com/chittyos/chittymcp) | Consolidated Model Context Protocol servers for Claude integration |
| [**ChittyRegistry**](https://github.com/chittyos/chittyregistry) | Universal service registry with discovery, search, and AI-driven recommendations |
| [**ChittyMarket**](https://github.com/chittyos/chittymarket) | Claude Code ecosystem marketplace — skills, agents, hooks, MCP servers |

## Stack

- **Runtime**: Cloudflare Workers (V8 isolates)
- **Database**: Neon PostgreSQL + Cloudflare D1
- **Storage**: Cloudflare R2 + KV
- **Auth**: ChittyAuth with ChittyID entity ontology (P/L/T/E/A)
- **Observability**: ChittyTrack tail workers + ChittyMonitor
- **CI/CD**: GitHub Actions with compliance gates

## Ecosystem

ChittyOS is the platform layer of a broader ecosystem:

- [**ChittyFoundation**](https://github.com/chittyfoundation) — Non-profit trust infrastructure (ChittyChain, ChittyDNA)
- [**ChittyApps**](https://github.com/chittyapps) — End-user applications (ChittyFinance, ChittyBrand, DocuMint)
- [**ChittyCorp**](https://github.com/chittycorp) — Corporate services and internal tools

## Contributing

Each repository has its own `CLAUDE.md` with development commands and patterns. Start there.

---

[chitty.cc](https://chitty.cc) · [registry.chitty.cc](https://registry.chitty.cc)
