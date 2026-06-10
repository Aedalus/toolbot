# Product Requirements

This project is a makerspace scheduling system. Baseline scheduling behavior is assumed: members can book available tool time, view their own upcoming reservations, cancel future reservations, and cannot double-book the same tool. Admins can resolve exceptions. Public visitors can view availability but cannot make changes.

## Product Decisions

### Slack Is the Write Interface

Members and admins should manage scheduling from Slack rather than a dedicated logged-in web app. Slack flows should cover reservation creation, cancellation, personal reservation lookup, tool availability changes, and admin promotion.

Detailed Slack examples are in `docs/slack-wireframes.md`.

### Public Website Is Read-Only

The website exists for quick availability checks. It should show current and upcoming tool availability without requiring sign-in.

Public reservation blocks should default to `Reserved`, not member names, unless the makerspace later chooses otherwise.

### Tool Scheduling Rules

All reservation start times, end times, and durations use 15-minute increments.

Each tool may define its own:

- advance booking window;
- minimum reservation duration;
- maximum reservation duration;
- enabled or disabled state.

The default advance booking window is 2 hours.

### Admin Model

Admins can:

- disable or enable tools;
- cancel or adjust reservations;
- promote other admins.

### Notifications

Slack should confirm reservation creation and cancellation.

A daily Slack schedule summary is optional.

## Nice To Have

- Slack reminders before upcoming reservations.
- Calendar invites or calendar feeds for reservations.
- Member notifications when admin actions affect existing reservations.

## Open Questions

- Should public availability ever show names or initials?
- Should members have active reservation limits?
