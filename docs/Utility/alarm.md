Alarms & Reminders
==================

This module includes tools to set timed reminders.

remind
------

### Command Syntax

::: {.parsed-literal}
remind (recipient) (time code) (message)
:::

### Command Description

Sends a message to you (via DM) or a channel within the current server,
after certain amount of time.

The recipient parameter can be either `me`, `here`, or a channel mention
or name.

### Examples

::: {.parsed-literal}
remind \#party-chat 2h It\'s party time!
:::

------------------------------------------------------------------------

remindlist
----------

### Command Syntax

::: {.parsed-literal}
remindlist
:::

### Command Description

Lists all reminders you created within the server.

### Examples

::: {.parsed-literal}
remindls
:::

------------------------------------------------------------------------

reminddel
---------

### Command Syntax

::: {.parsed-literal}
reminddel (reminder index)
:::

### Command Description

Deletes a reminder on the specified index, as shown by remindlist.

### Examples

::: {.parsed-literal}
reminddel 1 remindrm 3
:::

------------------------------------------------------------------------

remindtemplate
--------------

### Command Syntax

::: {.parsed-literal}
remindtemplate (reminder message)
:::

### Command Description

**This command is currently not active.**

Sets message template for when a reminder is triggered.

You can use one (or more) of these placeholders in your response
message:

-   **%message%**: The message specified in the remind command. This
    placeholder is **mandatory**.
-   **%target%**: The target channel of the remind command.
-   **%botname%**: The name of the bot.
-   **%user%**: This will be replaced with a mention of the user who ran
    the command.
-   **%server%**: This will be replaced with the server name.

### Permissions Needed

| **User**: Bot Owner

### Examples

::: {.parsed-literal}
remindtemplate Hello %user%\~! %botname% here to tell you %message%!
:::

------------------------------------------------------------------------

repeat
------

### Command Syntax

::: {.parsed-literal}
repeat (time in minutes) (message) repeat (time of day, HH:mm, UTC
timezone) (message) repeat (\--message/\--m {message to repeat})
\[\--no-redundant/\--n\] \[\--interval/\--i {time code}\]
\[\--channel/\--c {channel id/mention/q\_name}\]
:::

### Command Description

Repeat a message periodically in a channel.

This command has a quick syntax (with 2 variations) and a full syntax.
It is advised to use the full syntax if you want take advantage of the
advanced settings. Some advanced parameters will still work with the
quick syntaxes, but using that mix is not officially supported.

Embed support is only available with the full syntax.

::: {.admonition}
Premium

Each server can have a maximum of 5 repeating messages. If you need more
repeating messages, you can unlock more as a **Premium** feature (see:
`premium-perks`{.interpreted-text role="ref"}).
:::

The default interval time is set to 1 day, and the first message will
begin being sent after the first time interval has passed.

The `--no-redundant` parameter will instruct the bot to skip sending a
repeating message if the latest message in the channel is still the last
repeating message.

::: {.note}
::: {.title}
Note
:::

Using the 2nd syntax (the one that specifies the time of the day) will
automatically set the interval to 1 day, and repeat the message everyday
around the same clock time.
:::

### Permissions Needed

| **User**: Manage Messages

### Examples

::: {.parsed-literal}
repeat 120 2 hours have passed since my last message. repeat 8:00
Everyone, wake up! repeat \--m This is not a spam channel, please behave
correctly. \--c \#serious-chat \--i 6h \--no-redundant
:::

------------------------------------------------------------------------

repeatlist
----------

### Command Syntax

::: {.parsed-literal}
repeatlist
:::

### Command Description

Lists all repeating messages within the server.

### Examples

::: {.parsed-literal}
repls
:::

------------------------------------------------------------------------

repeatremove
------------

### Command Syntax

::: {.parsed-literal}
repeatremove (repeating message index)
:::

### Command Description

Deletes a repeating message on the specified index, as shown by
repeatlist.

### Permissions Needed

| **User**: Manage Messages

### Examples

::: {.parsed-literal}
reprm 3
:::

------------------------------------------------------------------------

repeatinvoke
------------

### Command Syntax

::: {.parsed-literal}
repeatinvoke (repeating message index)
:::

### Command Description

Immediately invokes (sends) a repeating message on the specified index,
as shown by remindlist.

Invoking a message also restarts its timer, hence potentially changing
the clock time when the next reminders are going to show.

### Permissions Needed

| **User**: Manage Messages

### Examples

::: {.parsed-literal}
repinv 3
:::
