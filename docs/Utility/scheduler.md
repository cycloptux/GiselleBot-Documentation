Command Scheduler
=================

This module lets users delay the usage of a command to a later date.

When delaying a command, the permission checks for the target command
will be checked **both** during the first scheduling request, and then
re-checked at run-time. This means that any user willing to schedule an
administrator-locked command, will have to have administrator
permissions when running the initial scheduler command, and still have
administrator permissions by the time the command is scheduled to run.
Failing either checks will reject the command run (either by not letting
the user schedule the command at all, or failing at run-time). It
doesn\'t matter if a user temporarily loses permissions in between the
scheduler command and the actual target command, as long as they have
enough permissions when the scheduler is due.

The scheduled command will be ignored if the user is not in the server,
or loses \"Read Messages\" or \"Send Messages\" permissions in the
channel they run the scheduler command into, by the time the command is
due to run. Again, it doesn\'t matter if the user temporarily leaves the
server or loses those permissions, as long as they are back up when the
scheduler is due.

will notify the channel where the scheduler command was run into as soon
as the command is due. The bot **must** still have \"Read Messages\" and
\"Send Messages\" permissions in that channel to notify the command run
before actually running the scheduled command. Failing the notification
will also abort the actual command run.

The current implementation of the command is experimental. As soon as
it\'s stable and hardened, 2 more features will be added:

-   Scheduling a command as **\"recurring\"**, hence being run **every N
    minutes**.
-   Scheduling a command to be run on a different channel than the one
    where you originally set the scheduler into.

::: {.admonition}
Premium

By default, each server is limited to scheduling commands within a time
interval of no more than **1 hour**. You can unlock higher interval
times as a **Premium** feature (see: `premium-perks`{.interpreted-text
role="ref"}):

-   **Tier 1** patron servers will have their cap increased to **12
    hours**.
-   **Tier 2** patron servers will have their cap increased to **1
    week** (7 days).
-   **Tier 3** patron servers will have their cap increased to **1
    month** (31 days).
:::

::: {.admonition}
Possible Use Cases

This command enables for quite a few interesting use cases. Here are
some commands that may get a good boost out of this feature:

-   Scheduling announcements, using `msgsend`{.interpreted-text
    role="ref"}
-   Scheduling (massive) addition and/or removal of roles, using
    `addrole`{.interpreted-text role="ref"} and
    `remrole`{.interpreted-text role="ref"}
-   Scheduling repeating message to fire at an exact time and then
    repeating every X minutes/hours (the default limitation for that use
    case in the native command is that the repeating message defaults to
    running every 24 hours) using `repeat`{.interpreted-text role="ref"}
:::

schedule
--------

### Command Syntax

::: {.parsed-literal}
schedule (time code) (command or message)
:::

### Command Description

Runs a command within the current server, after certain amount of time.
See above for the full description of this scheduler.

will treat the command (or message) as if it was sent in the current
channel, after the specified amount of time.

Permissions for the target command will be checked when initially
scheduling, and at run-time. Although, the actual correct formatting of
the command will only be checked at run-time, so be sure to test the
commands beforehand if you are not sure about their correctness.

Limitations apply to the maximum interval of time you can set for the
scheduler, and can be increased for **Premium**-enabled servers servers.
See above.

::: {.note}
::: {.title}
Note
:::

Up to **5** schedulers can be active at any time for each user within a
server. This limitation cannot (currently) be increased.
:::

### Examples

::: {.parsed-literal}
schedule 5m ping schedule 2d msgsend \#announcements \@everyone A new
update is live! schedule 14d remrole \@Moderator\_In\_Training\#1234
\"Moderator\"
:::

------------------------------------------------------------------------

schedulelist
------------

### Command Syntax

::: {.parsed-literal}
schedulelist
:::

### Command Description

Lists all schedulers that the user created within the server. Server
managers (users with \"Manage Server\" permissions) will be able to see
all schedulers created by anyone within the current server.

It may take up to a few seconds before a newly added scheduler appears
in the list.

### Examples

::: {.parsed-literal}
schedlist schedls
:::

------------------------------------------------------------------------

scheduleremove
--------------

### Command Syntax

::: {.parsed-literal}
scheduleremove (scheduler index)
:::

### Command Description

Deletes a scheduler on the specified index, as shown by schedulelist.
Users can only remove their own schedulers. Server managers (users with
\"Manage Server\" permissions) can remove any scheduler created by
anyone within the current server.

### Examples

::: {.parsed-literal}
scheddel 1 schedrm 3
:::
