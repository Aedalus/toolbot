# Toolbot

A makerspace tool scheduling service with Slack-based reservations and a public read-only availability website.

## Quick Start

```bash
cp .env.example .env
make docker-up
make routes
make open-local
```

The app runs at <http://localhost:8080>.

## Make Commands

Run `make` to see the available development commands.

## Architecture

| Component | Responsibility |
| --- | --- |
| Python Flask service | Slack interactions, reservation writes, admin actions, public read endpoints |
| MariaDB | Tools, users, reservations, audit events |
| Public website | Read-only availability display backed by the service |

## Planning Docs

- [Product requirements](docs/design.md)
- [Technical design](docs/technical-design.md)
- [Slack wireframes](docs/slack-wireframes.md)
- [TODO](TODO.md)
