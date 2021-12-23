Twitch Connector
================

The Twitch module & connector offers two macro-features:

-   A set of commands to interact with Twitch to get info about users
    and games.
-   A notification service which can monitor Twitch streamers going live
    and offline, sending these notifications to one (or more) of the
    webhooks configured in your Discord server.

Commands
--------

### twcuser

#### Command Syntax

::: {.parsed-literal}
twcuser (Twitch username)
:::

#### Command Description

Shows generic info about a user on Twitch. The username is
case-insensitive.

#### Examples

::: {.parsed-literal}
twcuser cycloptux
:::

------------------------------------------------------------------------

### twcstream

#### Command Syntax

::: {.parsed-literal}
twcstream (Twitch username)
:::

#### Command Description

Shows specific details about the stream properties of a user\'s channel.
This command will not work if the target user is not streaming. The
username is case-insensitive.

#### Examples

::: {.parsed-literal}
twcstream cycloptux
:::

------------------------------------------------------------------------

### twcwatch

#### Command Syntax

::: {.parsed-literal}
twcwatch (Twitch username)
:::

#### Command Description

Posts an URL to the user\'s channel. Discord includes a native
auto-preview which lets users play the Twitch stream live in the current
channel.

#### Examples

::: {.parsed-literal}
twcwatch cycloptux
:::

------------------------------------------------------------------------

### twcrndgame

#### Command Syntax

::: {.parsed-literal}
twcrndgame (game name)
:::

#### Command Description

Posts an URL to a random user\'s channel, playing the selected game.
Discord includes a native auto-preview which lets users play the Twitch
stream live in the current channel.

#### Examples

::: {.parsed-literal}
twcrndgame fortnite
:::

------------------------------------------------------------------------

Twitch Notifications
--------------------

::: {.seealso}
In order to better understand this module (and the rest of the connector
modules), it\'s very important that you are familiar with Discord
webhooks. For more details about this Discord feature, please take a
look at [this official
guide](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks).
:::

By default, each notification will be posted to the webhook by using the
Twitch account username as author, and Twitch avatar as Discord profile
picture. These settings (and other details) can be customized for each
stream.

Twitch profile URLs will be posted to Discord, while the Twitch stream
preview will leverage the native parsing of Twitch content offered by
Discord.

::: {.note}
::: {.title}
Note
:::

Due to inconsistencies and limitations within the Twitch API, this
module may have some extra delay between the actual event and the
Discord notification, and/or miss a few notifications every once in a
while, and/or send duplicate notifications. Additional checks are in
place to minimize the amount occurrencies of duplicate notifications.
:::

### twchook

#### Command Syntax

::: {.parsed-literal}
twchook (Twitch username) (webhook URL or \--channel (channel
id/mention/q\_name)) \[customization params\]
:::

#### Command Description

Starts a notification service for the selected Twitch account. If a user
starts or ends a Live stream a notification will be sent to the
specified webhook service.

::: {.warning}
::: {.title}
Warning
:::

Discord webhooks are a very powerful feature, but they (currently) lack
2-way authentication of messages. This means that a malicious user
knowing a webhook URL will be able, with some effort, to forge a message
containing any kind of content using external tools and send that
message to the webhook. In order to protect yourself from this (rare)
occasion, make sure you run this command in non-public channels.
:::

::: {.note}
::: {.title}
Note
:::

Alternatively, you can replace the webhook URL with the
`--channel (channel id/mention/q_name)` parameter: a new dedicated
webhook will be created and the URL from the new webhook will be
automatically used for this feed.

This alternative option requires to have \"Manage Webhooks\"
permissions.
:::

**Customization Params**

##### `--game (first game) [second game] [...]`

Adds a **whitelist**, **inclusive** filter for game names to the
service. Notifications for the selected user will only be sent if the
streamed game is equal to one of the filtered games. Actions related to
other games will be skipped.

You can also set \"composite words\" (two or more words as a single game
name) by quoting them: `"league of legends" fortnite` will count as 2
game filter elements: `league of legends` and `fortnite`. All filters
are case-insensitive, but the game name has to be exact for the filter
to work correctly.

::: {.warning}
::: {.title}
Warning
:::

This parameter will only work for games that are set at the beginning of
a stream. Changing the game throughout a stream will not trigger the
additional \"Live\" notification.
:::

**Default**: No filter

##### `--event (first event) [second event] [...]`

Adds a **whitelist**, **inclusive** filter for specific events to the
service. Notifications will only be sent if the actual notification
event is equal to one of the filtered events.

The **only** supported events for this feed are:

-   `live`, corresponding to Twitch users going live on a game;
-   `offline`, corresponding to Twitch users ending their stream.

**Default**: No filter

##### `--header (message)`

Adds a custom header message when notifications are posted. Custom
headers can have a maximum of **1024** characters.

Custom headers **can** be formatted as embeds by following a very
specific syntax. Do know that both and Discord are very sensitive to
this specific syntax, which is easily \"broken\" by special characters:
for this reason, using embeds as header is not suggested, nor directly
supported. **Use them at your own risk!** If you are brave enough, I
suggest the usage of [this embed
generator](https://leovoel.github.io/embed-visualizer/) (click on the
**\"Enable webhook mode\"** button at the bottom of the page).

Custom headers support a few dynamic tags that are replaced with their
respective \"real\" value during run-time. These are:

-   **%display\_name%**: This will be replaced with the display name of
    an account, including proper formatting of letter cases (e.g.
    `Cycloptux`)
-   **%username%**: This will be replaced with the \"URL\" username of a
    Twitch user (typically, lowercase). E.g. `cycloptux`
-   **%game%**: This will be replaced with the name of the streamed game
    (e.g. `Fortnite`)
-   **%status%**: This will be replaced with the description that is
    usually added below a game title during a stream.
-   **%stream\_status%**: This will be replaced with one of the two
    values: `Live` upon a \"going Live\" notification, `Offline` upon a
    stream end.
-   **%timestamp% or %timestamp\_utc%**: This will be replaced with the
    UTC time of the start of the event, with format
    `YYYY-MM-DD HH:mm:ss (UTC)`.
-   **%timestamp\_iso%**: This will be replaced with the UTC time of the
    start of the event, as ISO8601 string.
-   **%timestamp\_pst%**: This will be replaced with the current PST
    time of the start of the event, with format
    `YYYY-MM-DD HH:mm:ss (PST)`.
-   **%url%**: This will be replaced with the Twitch profile URL. See
    below for more info.

Timestamp tags also support custom time zones. You can replace the `utc`
part with either:

-   A different **valid** time zone identifier: use the
    `searchtz`{.interpreted-text role="ref"} command to look for a valid
    time zone name.

-   An **UTC offset**, in the form of
    `[UTC/GMT](+/-)(hours)[:][minutes]`. Here are some valid examples:

    > -   %timestamp\_Europe/London%
    > -   %timestamp\_America/Los\_Angeles%
    > -   %timestamp\_Japan%
    > -   %timestamp\_PST8PDT%
    > -   %timestamp\_+0800%
    > -   %timestamp\_-10:30%
    > -   %timestamp\_UTC+2%

By default, without an explicit use of `%url%`, all headers will be
followed by the actual Twitch profile URL on a new line; rendering of
that URL will be done by Discord.

If the `%url%` parameter is used, the default URL will **not** be
appended to the custom header.

The default header has two different modes for online and offline.
Setting a custom header will use the header on both messages: make use
of the `%stream_status%` tag to differentiate between the two messages.

**Default**:
`:red_circle: Now Live on Twitch: %display_name% | :video_game: Playing %game%.`
and `Stream Offline: %display_name% | :video_game: Playing %game%.`

##### `--webhook-name (custom name)`

Adds a custom username to the webhook when notifications are sent.
Custom usernames can have a maximum of 32 characters.

**Default**: New notifications will be sent by a webhook with the
display name of the Twitch account

##### `--no-username-overwrite`

Removes any custom name from the webhook. The real webhook name (the one
that you assigned when creating the webhook in Discord) will be used.

**Default**: `false` (Custom or automated names will be applied)

##### `--no-avatar-overwrite`

Removes any custom avatar from the webhook. The real webhook avatar (the
one that you assigned when creating the webhook in Discord) will be
used.

**Default**: `false` (Automated avatars will be applied)

#### Permissions Needed

| **User**: Manage Webhooks

#### Examples

::: {.parsed-literal}
twchook cycloptux
<https://discord.com/api/webhooks/123456789098765432/LONG_WEBHOOK_TOKEN>
twchook cycloptux
<https://discord.com/api/webhooks/123456789098765432/LONG_WEBHOOK_TOKEN>
\--header %user% is now %stream\_status%! Game: %game%
:::

------------------------------------------------------------------------

### twcehook

#### Command Syntax

::: {.parsed-literal}
twcehook (Twitch username/stream index) \[new customization params\]
:::

#### Command Description

**Replaces** all previously set customization params for the selected
Twitch notification service with a new set of customization params. The
stream index is the number shown with twclhook.

::: {.warning}
::: {.title}
Warning
:::

Editing the webhook will not change the existing params, it will
completely replace them. Take note of the existing params first, and use
them in the command!
:::

#### Permissions Needed

| **User**: Manage Webhooks

------------------------------------------------------------------------

### twcrhook

#### Command Syntax

::: {.parsed-literal}
twcrhook (Twitch username/stream index)
:::

#### Command Description

Stops a previously set Twitch notification service and removes its link
to the server webhook. The stream index is the number shown with
twclhook.

#### Permissions Needed

| **User**: Manage Webhooks

#### Examples

::: {.parsed-literal}
twcrhook cycloptux twcrhook 2
:::

------------------------------------------------------------------------

### twclhook

#### Command Description

Prints a list of all the Twitch notification services that are linked to
webhooks in the current server.
