# Slack Flow Wireframes

## Purpose

These wireframes show what the Slack scheduling experience could feel like for members and admins. They are not final copy or visual design; they are examples of screens, choices, and message flow.

## Contents

| Flow | Description |
| --- | --- |
| [Flow 1](#flow-1-check-tool-availability) | Check tool availability |
| [Flow 2](#flow-2-view-one-tool-availability) | View availability ranges for one tool |
| [Flow 3](#flow-3-create-reservation) | Create a reservation |
| [Flow 4](#flow-4-view-my-reservations) | View upcoming reservations |
| [Flow 5](#flow-5-cancel-reservation) | Cancel a reservation |
| [Flow 6](#flow-6-admin-tool-availability) | Disable or enable a tool |
| [Flow 7](#flow-7-add-a-new-tool) | Add a new tool |
| [Flow 8](#flow-8-edit-a-tool) | Edit a tool |
| [Flow 9](#flow-9-promote-another-admin) | Promote another admin |
| [Flow 10](#flow-10-daily-schedule-summary) | Daily schedule summary |

## Flow 1: Check Tool Availability

Member types:

```text
/tools
```

Slack response:

```text
+------------------------------------------------------------+
| Makerspace Tools                                           |
|                                                            |
| Choose a tool to view availability or start a reservation. |
|                                                            |
| Laser Cutter                                               |
| Status: Available now                                      |
| [Reserve] [Availability]                                   |
|                                                            |
| CNC Router                                                 |
| Status: Reserved until 2:30 PM                             |
| [Reserve] [Availability]                                   |
|                                                            |
| 3D Printer                                                 |
| Status: Unavailable                                        |
| [Availability]                                             |
|                                                            |
| [My reservations]                                          |
+------------------------------------------------------------+
```

## Flow 2: View One Tool Availability

Member clicks `Availability` for Laser Cutter.

```text
+------------------------------------------------------------+
| Laser Cutter Availability                                  |
|                                                            |
| Current status: Available                                  |
|                                                            |
| Today                                                      |
| 10:00 AM-12:15 PM                                          |
| 1:30 PM-3:45 PM                                            |
| 4:15 PM-6:00 PM                                            |
|                                                            |
| Tomorrow                                                   |
| 9:00 AM-11:30 AM                                           |
| 2:00 PM-5:00 PM                                            |
|                                                            |
| Friday                                                     |
| No availability                                            |
|                                                            |
| [Reserve] [View calendar]                                  |
+------------------------------------------------------------+
```

## Flow 3: Create Reservation

Member clicks `Reserve`.

```text
+------------------------------------------------------------+
| Reserve a Tool                                             |
|                                                            |
| Tool                                                       |
| [Laser Cutter                                      v]      |
|                                                            |
| Date                                                       |
| [Tuesday, June 16                                  v]      |
|                                                            |
| Start time                                                 |
| [2:15 PM                                          v]       |
|                                                            |
| Duration                                                   |
| [75 minutes                                       v]       |
|                                                            |
| Notes, optional                                            |
| [________________________________________________]         |
|                                                            |
|                              [Cancel] [Reserve tool]       |
+------------------------------------------------------------+
```

After submit, if successful:

```text
+------------------------------------------------------------+
| Reservation confirmed                                      |
|                                                            |
| Tool: Laser Cutter                                         |
| Time: Tuesday, June 16, 2:15 PM to 3:30 PM                 |
|                                                            |
| [Cancel reservation] [View my reservations]                |
+------------------------------------------------------------+
```

If the time is unavailable:

```text
+------------------------------------------------------------+
| That time is no longer available.                          |
|                                                            |
| Laser Cutter is already reserved from 2:15 PM to 3:30 PM.  |
|                                                            |
| Available alternatives:                                    |
| 10:00 AM to 12:15 PM                       [Reserve]       |
| 1:30 PM to 3:45 PM                         [Reserve]       |
|                                                            |
| [Choose another time]                                      |
+------------------------------------------------------------+
```

## Flow 4: View My Reservations

Member types:

```text
/tools mine
```

Slack response:

```text
+------------------------------------------------------------+
| Your Upcoming Reservations                                 |
|                                                            |
| Laser Cutter                                               |
| Tuesday, June 16, 2:15 PM to 3:30 PM                       |
| [Cancel]                                                   |
|                                                            |
| CNC Router                                                 |
| Friday, June 19, 10:00 AM to 12:00 PM                      |
| [Cancel]                                                   |
|                                                            |
| [Reserve another tool]                                     |
+------------------------------------------------------------+
```

## Flow 5: Cancel Reservation

Member clicks `Cancel`.

```text
+------------------------------------------------------------+
| Cancel reservation?                                        |
|                                                            |
| Laser Cutter                                               |
| Tuesday, June 16, 2:15 PM to 3:30 PM                       |
|                                                            |
| This will make the time available to other members.        |
|                                                            |
|                         [Keep reservation] [Cancel it]     |
+------------------------------------------------------------+
```

After confirmation:

```text
+------------------------------------------------------------+
| Reservation canceled                                       |
|                                                            |
| Laser Cutter is no longer reserved for                     |
| Tuesday, June 16, 2:15 PM to 3:30 PM.                      |
|                                                            |
| [Reserve another tool] [View availability]                 |
+------------------------------------------------------------+
```

## Flow 6: Admin Tool Availability

Admin types:

```text
/tools admin
```

Slack response:

```text
+------------------------------------------------------------+
| Admin Scheduling                                           |
|                                                            |
| Choose an admin action.                                    |
|                                                            |
| [Add a tool]                                               |
| [Edit a tool]                                              |
| [Cancel member reservation]                                |
| [Disable a tool]                                           |
| [Enable a tool]                                            |
| [Promote admin]                                            |
+------------------------------------------------------------+
```

Admin clicks `Disable a tool`.

```text
+------------------------------------------------------------+
| Disable a Tool                                             |
|                                                            |
| Tool                                                       |
| [3D Printer                                       v]       |
|                                                            |
| Reason, optional                                           |
| [Replacing nozzle________________________________]         |
|                                                            |
|                              [Cancel] [Disable tool]       |
+------------------------------------------------------------+
```

If existing reservations are affected:

```text
+------------------------------------------------------------+
| Tool disabled                                              |
|                                                            |
| 3D Printer is unavailable for new reservations.            |
|                                                            |
| Existing future reservations: 2                            |
|                                                            |
| [View affected reservations]                               |
+------------------------------------------------------------+
```

## Flow 7: Add A New Tool

Admin types:

```text
/tools admin
```

Admin clicks `Add a tool`.

```text
+------------------------------------------------------------+
| Add a Tool                                                 |
|                                                            |
| Name                                                       |
| [Vinyl Cutter____________________________________]         |
|                                                            |
| Slug                                                       |
| [vinyl-cutter____________________________________]         |
|                                                            |
| Description                                                |
| [For cutting adhesive vinyl and heat-transfer film]        |
|                                                            |
| Advance booking window                                     |
| [120 minutes                                      v]       |
|                                                            |
| Minimum duration                                           |
| [15 minutes                                       v]       |
|                                                            |
| Maximum duration                                           |
| [120 minutes                                      v]       |
|                                                            |
| Enabled                                                    |
| [x] Available for reservations                             |
|                                                            |
|                                  [Cancel] [Add tool]       |
+------------------------------------------------------------+
```

After submit:

```text
+------------------------------------------------------------+
| Tool added                                                 |
|                                                            |
| Vinyl Cutter is now available for reservations.            |
|                                                            |
| [View availability] [Back to admin tools]                  |
+------------------------------------------------------------+
```

## Flow 8: Edit A Tool

Admin types:

```text
/tools admin
```

Admin clicks `Edit a tool`.

```text
+------------------------------------------------------------+
| Choose Tool To Edit                                        |
|                                                            |
| Tool                                                       |
| [Vinyl Cutter                                     v]       |
|                                                            |
|                                      [Cancel] [Continue]   |
+------------------------------------------------------------+
```

Slack opens a modal with current values filled in.

```text
+------------------------------------------------------------+
| Edit Tool                                                  |
|                                                            |
| Name                                                       |
| [Vinyl Cutter____________________________________]         |
|                                                            |
| Slug                                                       |
| [vinyl-cutter____________________________________]         |
|                                                            |
| Description                                                |
| [For cutting adhesive vinyl and heat-transfer film]        |
|                                                            |
| Advance booking window                                     |
| [120 minutes                                      v]       |
|                                                            |
| Minimum duration                                           |
| [15 minutes                                       v]       |
|                                                            |
| Maximum duration                                           |
| [120 minutes                                      v]       |
|                                                            |
| Enabled                                                    |
| [x] Available for reservations                             |
|                                                            |
|                                [Cancel] [Save changes]     |
+------------------------------------------------------------+
```

After submit:

```text
+------------------------------------------------------------+
| Tool updated                                               |
|                                                            |
| Vinyl Cutter settings have been saved.                     |
|                                                            |
| [View availability] [Back to admin tools]                  |
+------------------------------------------------------------+
```

## Flow 9: Promote Another Admin

Admin types:

```text
/tools admin
```

Admin clicks `Promote admin`.

```text
+------------------------------------------------------------+
| Promote Admin                                              |
|                                                            |
| Member                                                     |
| [Choose a Slack user                              v]       |
|                                                            |
| This member will be able to manage tools, cancel           |
| reservations, and promote other admins.                    |
|                                                            |
|                              [Cancel] [Promote admin]      |
+------------------------------------------------------------+
```

Slack asks for confirmation:

```text
+------------------------------------------------------------+
| Confirm admin promotion                                    |
|                                                            |
| Promote Jordan Lee to admin?                               |
|                                                            |
| They will be able to manage scheduling settings and        |
| perform admin-only actions.                                |
|                                                            |
|                              [Cancel] [Confirm promote]    |
+------------------------------------------------------------+
```

After confirmation:

```text
+------------------------------------------------------------+
| Admin promoted                                             |
|                                                            |
| Jordan Lee can now manage makerspace scheduling.           |
|                                                            |
| [Back to admin tools]                                      |
+------------------------------------------------------------+
```

The newly promoted admin receives a direct message:

```text
+------------------------------------------------------------+
| You are now a scheduling admin                             |
|                                                            |
| You can manage tool availability, cancel reservations,     |
| and help administer makerspace scheduling.                 |
|                                                            |
| [Open admin tools]                                         |
+------------------------------------------------------------+
```

## Flow 10: Daily Schedule Summary

Optional scheduled Slack post:

```text
+------------------------------------------------------------+
| Today's Tool Schedule                                      |
|                                                            |
| Laser Cutter                                               |
| 10:00 AM-12:15 PM                                          |
| 1:30 PM-3:45 PM                                            |
| 4:15 PM-6:00 PM                                            |
|                                                            |
| CNC Router                                                 |
| 1:00 PM-5:00 PM                                            |
|                                                            |
| 3D Printer                                                 |
| Unavailable                                                |
|                                                            |
| [View calendar]                                            |
+------------------------------------------------------------+
```

## Notes

- Recommended command entry points:
  - `/tools`
  - `/tools reserve`
  - `/tools mine`
  - `/tools admin`
- Slack interactions may use slash commands, buttons, and modals.
- Slack requests should be verified before the system processes them.
- Slack interactions should respond quickly. If an action takes longer, acknowledge it first and send a follow-up message.
- Most member messages should be visible only to the member using Slack ephemeral messages or direct messages.
- Members should receive Slack confirmation when reservations are created or canceled.
- Member notifications for admin changes are a stretch goal.
- Public channel posts should be limited to summaries or changes that are useful to the whole makerspace.
