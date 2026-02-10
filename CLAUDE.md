---
uri: chittycanon://docs/tech/spec/chittyos-github
namespace: chittycanon://docs/tech
type: spec
version: 1.0.0
status: CERTIFIED
registered_with: chittycanon://core/services/canon
title: ChittyOS .github Development Guide
author: ChittyOS Team
created: 2026-02-09T00:00:00Z
modified: 2026-02-09T00:00:00Z
visibility: PUBLIC
tags: [org-config, workflows, agents, compliance]
---

# ChittyOS .github

Organization-wide GitHub configuration for all CHITTYOS repositories.

## What This Repo Contains

| Directory | Purpose |
|-----------|---------|
| `.github/agents/` | GitHub Copilot custom agents (org-wide) |
| `.github/workflows/` | Reusable workflows inherited by all repos |
| `profile/` | Organization README (public profile) |
| `scripts/` | Preflight and verification tooling |

## Workflows

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| `documentation_check.yml` | PR | Validates documentation standards |
| `metadata_check.yml` | PR | Validates metadata and frontmatter |
| `new_repo_setup.yml` | Repository creation | Bootstraps compliance files |
| `sync-evidence.yml` | Schedule | Syncs evidence artifacts |
| `sync-governance.yml` | Schedule | Syncs governance docs |
| `sync-operations.yml` | Schedule | Syncs operations config |
| `sync-property.yml` | Schedule | Syncs property records |

## Copilot Agent

The `@chittyos` agent (`chittyos.md`) is available org-wide in GitHub Copilot. It covers:
- Ecosystem navigation (62+ services, 6 tiers)
- Compliance guidance (7 dimensions)
- Service onboarding walkthrough
- Architecture explanation

## Development

```bash
# Clone
gh repo clone CHITTYOS/.github

# Edit workflows or agents
# Push to main (changes apply org-wide immediately)
```

## Testing Changes

- Workflow changes: Create a PR and check the Actions tab in any CHITTYOS repo
- Agent changes: Open Copilot chat in any CHITTYOS repo and invoke `@chittyos`
- Profile changes: View at github.com/CHITTYOS

## Security

- No secrets in this repo -- all credentials flow through ChittyConnect
- Workflow secrets are configured at the org level in GitHub Settings
- The `new_repo_setup.yml` workflow uses `GITHUB_TOKEN` (automatic)
