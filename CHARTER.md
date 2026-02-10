---
uri: chittycanon://gov/charter/chittyos-github
namespace: chittycanon://gov
type: charter
version: 1.0.0
status: CERTIFIED
registered_with: chittycanon://core/services/canon
title: ChittyOS .github Charter
author: ChittyOS Governance
certifier: chittycanon://gov/authority/chittygov
created: 2026-02-09T00:00:00Z
---

# ChittyOS .github Charter

## Mission

Provide consistent, org-wide GitHub configuration including reusable workflows, Copilot agents, compliance templates, and repository bootstrapping for all CHITTYOS repositories.

## Scope

This repository governs:
- Organization-wide workflow inheritance
- GitHub Copilot custom agent definitions
- New repository bootstrapping automation
- Cross-repo sync workflows (evidence, governance, operations, property)
- Organization public profile

## Classification

- **Tier**: Infrastructure (not a deployable service)
- **Organization**: CHITTYOS
- **Domain**: N/A (org-wide configuration)
- **Compliance Profile**: `documentation` (Canon required, other dimensions optional)

## Principles

### 1. Org-Wide Impact

Changes to this repo affect all CHITTYOS repositories immediately. All changes require review.

### 2. Minimal Footprint

Only include configuration that genuinely benefits from org-wide inheritance. Repo-specific config belongs in individual repos.

### 3. Compliance First

This repo bootstraps compliance for other repos via `new_repo_setup.yml`. It must itself be compliant.

## Governance

### Authority

- **ChittyGov**: Approves charter amendments
- **Platform Team**: Maintains workflows and agents
- **CODEOWNERS**: Enforces review requirements

### Review Process

1. All changes via PR (no direct pushes to main)
2. Required review from CODEOWNERS
3. Workflow changes tested in a fork or test repo first
4. Agent changes validated via Copilot chat

## Dependencies

- **ChittyConnect**: Credential provisioning for workflows
- **ChittyCanon**: Documentation and naming standards
- **GitHub Actions**: Workflow runtime

## Amendments

This charter may be amended by PR with ChittyGov approval.
