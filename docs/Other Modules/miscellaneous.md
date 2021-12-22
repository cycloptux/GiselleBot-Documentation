Miscellaneous
=============

This module contains generally safe, atomic commands that aren\'t
otherwise categorized into a dedicated module.

------------------------------------------------------------------------

Bot Information
---------------

### invite

#### Command Syntax

::: {.parsed-literal}
invite
:::

#### Command Description

Creates and shows an invite to get the bot into a Discord server you
manage.

------------------------------------------------------------------------

### stats

#### Command Syntax

::: {.parsed-literal}
stats
:::

#### Command Description

Shows technical info about the bot and the infrastructure it\'s running
on.

------------------------------------------------------------------------

### ping

#### Command Syntax

::: {.parsed-literal}
ping
:::

#### Command Description

Tests the bot ping response.

Calculates ping between sending a message and editing it, giving a nice
round-trip latency.

The second ping is an average latency between the bot and the websocket
server (one-way, not round-trip).
