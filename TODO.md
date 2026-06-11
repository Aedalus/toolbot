# TODO

High-level feature tickets for fanning out Toolbot implementation work. Each item should be a vertical slice that includes the user-facing behavior plus the backend, tests, and docs needed to make it work.

## 1. Slack Member Reservations

- [ ] Build the `/tools` Slack home flow so members can see reservable tools, current availability, and actions from Slack.
- [ ] Build the Slack one-tool availability view so members can inspect available ranges before reserving.
- [ ] Build the Slack reservation flow so a member can reserve a tool for a valid local-time slot and receive a confirmation.
- [ ] Build the Slack conflict flow so a member gets useful alternatives when the requested reservation time is unavailable.
- [ ] Build the Slack "my reservations" flow so a member can view their upcoming reservations in local makerspace time.
- [ ] Build the Slack cancellation flow so a member can cancel one of their own future reservations and receive a confirmation.

## 2. Admin And Setup

- [ ] Build database migrations so Docker Compose environments can create and upgrade the MariaDB schema.
- [ ] Build local seed data so contributors can start Docker Compose and immediately try sample tools and reservations.
- [ ] Build the Slack admin action menu so admins can choose tool, reservation, and user-management actions.
- [ ] Build the admin add-tool flow so admins can create a reservable tool with booking window, duration, granularity, and enabled settings.
- [ ] Build the admin edit-tool flow so admins can update a tool's reservation settings without breaking existing history.
- [ ] Build the admin disable/enable flow so admins can control whether a tool accepts new reservations and see affected future reservations.
- [ ] Build the admin reservation management flow so admins can cancel or adjust member reservations.
- [ ] Build the admin promotion flow so an existing admin can promote another Slack user.

## 3. Public Website And Operations

- [ ] Build the public availability page so visitors can see upcoming tool availability without signing in.
- [ ] Build per-tool public pages so visitors can inspect one tool's availability using a stable slug URL.
- [ ] Build public privacy behavior so reserved blocks display as `Reserved` unless a future product decision changes that.
- [ ] Build public empty and disabled-tool states so the site is useful when tools are missing, disabled, or fully booked.
- [ ] Add enough CSS for the public pages to be usable on desktop and mobile.
- [ ] Build basic operational visibility so maintainers can check app health, version/build info, and reservation/Slack failures.

## Open Questions

- Should public availability ever show member names or initials?
- Should members have active reservation limits?
- Are reminders, calendar invites, or calendar feeds in scope?
- Should disabled tools appear on public availability pages?
- What is the final product name?
