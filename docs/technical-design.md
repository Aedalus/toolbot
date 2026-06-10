# Technical Design

Use one TypeScript backend service for both the Slack bot and public API. The backend is the source of truth for reservations; clients should not implement scheduling rules.

Typescript was chosen as there is a well supported official Slack SDK, while also easily supporting necessary frontend requirements.

## Architecture

- TypeScript service handles Slack interactions, reservation writes, admin actions, and public read endpoints.
- PostgreSQL stores tools, users, reservations, and audit events.
- Public website reads availability from the same service.

## Data Structures

### tools

Reservable makerspace equipment.

```text
id
name
slug
description
enabled
advance_booking_window_minutes, default 120
min_duration_minutes
max_duration_minutes
slot_granularity_minutes, default 15
```

- `slug` is for public URLs.
- `enabled=false` prevents new reservations.
- Booking window, duration limits, and slot granularity are per tool.

### users

Local user records linked to Slack identities.

```text
id
slack_user_id
display_name
role: member | admin
```

- Slack is the identity source.
- Local users store app-specific roles and stable historical references.

### reservations

Time-bounded bookings for one user and one tool.

```text
id
tool_id
user_id
starts_at
ends_at
status: active | canceled
notes
created_via: slack | admin
canceled_at
canceled_by_user_id
```

- Store times in UTC.
- Display times in the makerspace timezone.
- Active reservations must not overlap for the same tool.
- Start and end times must align to the tool's slot granularity.
- Canceled and past reservations stay in history.

### audit_events

History of meaningful user or admin actions.

```text
id
actor_user_id
action
entity_type
entity_id
metadata
created_at
```

- `reservation_created`
- `reservation_canceled`
- `tool_disabled`
- `tool_enabled`
- `admin_promoted`

## System Rules

- Members can create reservations and cancel their own future reservations.
- Admins can cancel reservations, disable or enable tools, and promote other admins.
- Reservation creation must be atomic so two users cannot book the same tool at the same time.
- Public views should show availability without exposing member details by default.
