# Toolbot

A makerspace tool scheduling service with Slack-based reservations and a public read-only availability website.

## Quick Start

```bash
cp .env.example .env
make docker-up
make migrate
make seed
make routes
make open-local
```

The app runs at <http://localhost:8080>.

## Slack Setup

For local Slack testing:

1. Create a Slack app.
2. In **Basic Information > App-Level Tokens**, create an app-level token with `connections:write`.
3. In **Socket Mode**, enable Socket Mode and select the app-level token.
4. In **OAuth & Permissions**, add the bot token scopes needed for app mentions and replies:
   - `app_mentions:read`
   - `chat:write`
5. In **Event Subscriptions**, enable events.
   - Leave **Request URL** blank. Socket Mode does not use an HTTP request URL.
   - Under **Subscribe to bot events**, add `app_mention`.
   - Click **Save Changes** after adding the bot event.
6. In **OAuth & Permissions**, install or reinstall the app to the workspace after changing scopes or event subscriptions.
7. Invite the bot to any channel where you want to test it.
8. Set these values in `.env`:

```bash
SLACK_BOT_TOKEN=xoxb-...
SLACK_APP_TOKEN=xapp-...
```

`SLACK_BOT_TOKEN` must be the Bot User OAuth Token from **OAuth & Permissions** and should start with `xoxb-`. `SLACK_APP_TOKEN` must be the app-level token from **Basic Information** and should start with `xapp-`.

The Docker app service sets `SLACK_SOCKET_MODE_CONNECT=true`, so Slack Socket Mode connects when both tokens are present. Mention the bot with `@bot ping` and it replies `pong`.

## Make Commands

Run `make` to see the available development commands.

Database schema changes are managed with Flask-Migrate/Alembic:

```bash
make migrate
```

`make migrate` runs against the Docker Compose app and MariaDB services. To create a new revision, run
`docker compose exec app flask --app toolbot:create_app db migrate -m "describe change"`.

Local starter data is managed with a Flask CLI command:

```bash
make seed
```

This creates or updates the starter tool records for Bronte, Glowforge, and Wood Lathes.

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
