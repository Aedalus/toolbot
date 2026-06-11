# Technical Design

One Python service should support both the Slack bot and public API. The backend is the source of truth for reservations; clients should not implement scheduling rules.

Python is preferred due to its historical use at the makerspace.

## Architecture

| Component | Responsibility |
| --- | --- |
| Python Flask service | Slack interactions, reservation writes, admin actions, public read endpoints |
| MariaDB | Tools, users, reservations, audit events |
| Public website | Read-only availability display backed by the service |

## Data Structures

### tools

Reservable makerspace equipment.

| Field | Notes |
| --- | --- |
| `id` | Internal identifier |
| `name` | Display name |
| `slug` | Public URL identifier |
| `description` | Short tool description |
| `enabled` | Disabled tools cannot receive new reservations |
| `advance_booking_window_minutes` | Default `120` |
| `min_duration_minutes` | Per-tool minimum |
| `max_duration_minutes` | Per-tool maximum |
| `slot_granularity_minutes` | Default `15` |

### users

Local records linked to Slack identities.

| Field | Notes |
| --- | --- |
| `id` | Internal identifier |
| `slack_user_id` | Slack identity |
| `display_name` | Snapshot for UI/history |
| `role` | `member` or `admin` |

### reservations

Time-bounded bookings for one user and one tool.

| Field | Notes |
| --- | --- |
| `id` | Internal identifier |
| `tool_id` | Reserved tool |
| `user_id` | Reserving user |
| `starts_at` | Stored in UTC |
| `ends_at` | Stored in UTC |
| `status` | `active` or `canceled` |
| `notes` | Optional member/admin note |
| `created_via` | `slack` or `admin` |
| `canceled_at` | Set when canceled |
| `canceled_by_user_id` | User who canceled it |

Rules:

- Display reservation times in the makerspace timezone.
- Active reservations must not overlap for the same tool.
- Start and end times must align to the tool's slot granularity.
- Canceled and past reservations stay in history.

### audit_events

History of meaningful user or admin actions.

| Field | Notes |
| --- | --- |
| `id` | Internal identifier |
| `actor_user_id` | User who performed the action |
| `action` | Event name |
| `entity_type` | Affected object type |
| `entity_id` | Affected object ID |
| `metadata` | Extra structured context |
| `created_at` | Event timestamp |

Initial actions: `reservation_created`, `reservation_canceled`, `tool_disabled`, `tool_enabled`, `admin_promoted`.

## System Rules

- Members can create reservations and cancel their own future reservations.
- Admins can cancel reservations, disable or enable tools, and promote other admins.
- Reservation creation must be atomic so two users cannot book the same tool at the same time.
- Public views should show availability without exposing member details by default.
