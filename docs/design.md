# Product Requirements

Makerspace tool scheduling with Slack-based writes and a public read-only availability site.

Baseline scheduling is assumed: members can reserve available tool time, view their reservations, cancel future reservations, and cannot double-book a tool.

## Key Decisions

| Area | Decision |
| --- | --- |
| Write interface | Slack is the primary interface for members and admins. |
| Public website | Read-only availability display; no sign-in required. |
| Time granularity | Reservations use 15-minute start times, end times, and durations. |
| Tool settings | Booking window, duration limits, and enabled state are configured per tool. |
| Default booking window | 2 hours. |
| Public privacy | Reservation blocks default to `Reserved`, not member names. |
| Admin access | Admins can promote other admins. |

## Required Slack Flows

Detailed examples are in [Slack wireframes](slack-wireframes.md).

- Check tool availability.
- Create a reservation.
- View my reservations.
- Cancel a reservation.
- Add or edit tools.
- Disable or enable tools.
- Promote another admin.

## Admin Capabilities

- Add and edit tool definitions.
- Disable or enable tools.
- Cancel or adjust reservations.
- Promote other admins.

## Notifications

Required:

- Confirm reservation creation in Slack.
- Confirm reservation cancellation in Slack.

Nice to have:

- Remind members before upcoming reservations.
- Send calendar invites or expose calendar feeds.
- Notify members when admin actions affect existing reservations.
- Post a daily Slack schedule summary.

## Open Questions

- Should public availability ever show names or initials?
- Should members have active reservation limits?
