RSS Reader
==========

The RSS (Really Simple Syndication) reader offers an easy way to stream
new items from any RSS (XML, Atom) feed to one (or more) of the webhooks
configured in your Discord server.

::: {.seealso}
In order to better understand this module (and the rest of the connector
modules), it\'s very important that you are familiar with Discord
webhooks. For more details about this Discord feature, please take a
look at [this official
guide](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks).
:::

By default, each item will be posted to the webhook by using the RSS
feed name (if present in the feed, falling back to the website URL or
feed URL otherwise) as author, and the feed image (if present, falling
back to a default RSS logo image) as Discord profile picture. These
settings (and other details) can be customized for each stream.

The item URL offered by the feed will be posted to Discord, while the
item preview will leverage the native parsing of web content offered by
Discord.

::: {.note}
::: {.title}
Note
:::

The goal of this module is offering a **free alternative** to something
that is usually only achieved through the use of paid services. On the
other hand, due to limitations that are applied to the RSS protocol
itself, this module might suffer from delays (new posts will be checked
**every 5\~15 minutes**).
:::

::: {.warning}
::: {.title}
Warning
:::

**The RSS protocol is highly inconsistent by nature/implementation**,
especially due to the amount of different protocols (and versions) that
were built over time under the generic \"RSS\" name (i.e. RSS 0.91, RSS
0.92, RSS 1.0, RSS 2.0, Atom 0.3, Atom 1.0). Checks are in place to
minimize the amount of duplicate posts that might happen due to said
inconsistencies. These checks may be less effective when a feed is first
added, but are built to get better over time. Also, due to this, a few
RSS feeds may not work. This is usually not an error on the bot\'s end,
but if that happens, try approaching the developer on Discord
(cycloptux\#1543, join our official support server on Discord with this
invite: ) to see if the error can be solved.
:::

rsshook
-------

### Command Syntax

::: {.parsed-literal}
rsshook (RSS feed URL) (webhook URL or \--channel (channel
id/mention/q\_name)) \[customization params\]
:::

### Command Description

Starts a streaming service for the selected RSS feed. If a new item is
found, it will be sent to the specified webhook service.

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

#### `--nsfw [censor/skip/only]`

RSS feeds may be parsed to look for \"bad words\" or \"crude language\"
in their title or content before being posted.

Depending on the selected parameter, these are the NSFW behaviors:

-   **censor** will post a NSFW URL surrounded by `< >` angle brackets,
    disabling the default Discord URL auto-embed preview.
-   **skip** will completely ignore NSFW-flagged items, \"cleaning\" the
    stream from NSFW items.
-   **only** will only post NSFW-flagged items and skip the rest. The
    items will not be censored. You can use this mode to create a
    complementary NSFW stream of the previous \"clean\" stream.

::: {.note}
::: {.title}
Note
:::

This check is unaccurate. If you know that the RSS feed you are going to
stream is \"safe for work\", you can safely skip this check. This is
usually the suggested behavior if you know what you\'re doing.
:::

**Default**: `false` (both SFW and NSFW -uncensored- items will be
posted), or `censor` if `--nsfw` is used without any specific mode.

#### `--filter (first word) [second word] [...]`

Adds a **whitelist** filter to the stream. In this example, if the item
contains `first word` and/or (see below) `second word` **in its title**,
the item will be sent to the webhook, otherwise it will ignored. You can
set one or more words, case-insensitive.

You can also set \"composite words\" (two or more words as a single
filter) by quoting them: `"foo bar" test` will count as 2 filter
elements: `foo bar` and `test`.

The filter works on partial words (e.g. \"announce\" will work on both
\"announcement\" and \"announced\").

**Default**: No filter

#### `--mode (AND/OR)`

Sets the filter behavior when more than 1 word is added to the whitelist
filter.

-   `AND` will only allow items whose title contain *all* of the
    filtered words.
-   `OR` will allow items whose title cointain at least one of the
    filtered words.

**Default**: `OR`

#### `--include` or `--exclude`

Sets the filter behavior one or more words are added to the whitelist
filter.

-   `--include` will only allow items whose title contain the filtered
    word(s).
-   `--exclude` will only allow items whose title **do not** contain the
    filtered word(s).

These parameters will work together with `--mode (AND/OR)`, allowing the
RSS reader to filter based on INCLUDING the filter items (e.g., at least
one filter item (OR) or all filter items (AND) are included in the item)
or EXCLUDING filter items (e.g., post if all filter items are absent
from the item (AND) or at least one filter item is absent from the item
(OR)).

**Default**: `--include`

::: {.note}
::: {.title}
Note
:::

Using both parameters in the same command will give `--include` the
strict priority and ignore `--exclude`.
:::

#### `--header (message)`

Adds a custom header message when items are posted. Custom headers can
have a maximum of **1024** characters.

Custom headers **can** be formatted as embeds by following a very
specific syntax. Do know that both and Discord are very sensitive to
this specific syntax, which is easily \"broken\" by special characters:
for this reason, using embeds as header is not suggested, nor directly
supported. **Use them at your own risk!** If you are brave enough, I
suggest the usage of [this embed
generator](https://leovoel.github.io/embed-visualizer/) (click on the
**\"Enable webhook mode\"** button at the bottom of the page).

Custom headers support a few dynamic tags that are replaced with their
respective \"real\" (as defined into the RSS feed) value during
run-time.

::: {.warning}
::: {.title}
Warning
:::

Due to the inconsistencies of the RSS protocol and feeds, some or all of
these parameters may not exist in an RSS feed item. Fallbacks values are
implemented, but you\'re encouraged to check the feed yourself and build
your header accordingly.
:::

Here\'s the list of supported tags:

-   **%feed\_name%**: This will be replaced with the RSS feed name
    (fallback: the website URL, or the feed URL)
-   **%author%**: This will be replaced with the name of the author of
    the item (fallback: *Unknown*)
-   **%title%**: This will be replaced with the title of the item
    (fallback: *Unknown*)
-   **%content%**: This will be replaced with the content
    (\"description\") of the item, with an automated attempt to
    **properly convert HTML formatting to markdown** (fallback: *None*)
-   **%content\_clean%**: This will be replaced with the content
    (\"description\") of the item, stripped off all HTML tags (i.e. just
    plain text) (fallback: *None*)
-   **%media\_url%**: This will be replaced with the direct URL to the
    media content of the item, if available (fallback: *Empty String*)
-   **%categories%**: This will be replaced with the tags
    (\"categories\") assigned to an item, as a comma-separated list
    (fallback: *None*)
-   **%timestamp% or %timestamp\_utc%**: This will be replaced with the
    item creation UTC time, with format `YYYY-MM-DD HH:mm:ss (UTC)`.
-   **%timestamp\_iso%**: This will be replaced with the item creation
    UTC time, as ISO8601 string.
-   **%timestamp\_pst%**: This will be replaced with the item creation
    PST time, with format `YYYY-MM-DD HH:mm:ss (PST)`.
-   **%url%**: This will be replaced with the item URL. See below for
    more info.

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
followed by the actual item URL on a new line; rendering of that URL
will be done by Discord.

If the `%url%` parameter is used, the default URL will **not** be
appended to the custom header.

**Default**: `New item found in %feed_name%!`

#### `--webhook-name (custom name)`

Adds a custom username to the webhook when new items are posted. Custom
usernames can have a maximum of 32 characters.

**Default**: New items will be displayed by a webhook with the name of
the feed

#### `--no-username-overwrite`

Removes any custom name from the webhook. The real webhook name (the one
that you assigned when creating the webhook in Discord) will be used.

**Default**: `false` (Custom or automated names will be applied)

#### `--no-avatar-overwrite`

Removes any custom avatar from the webhook. The real webhook avatar (the
one that you assigned when creating the webhook in Discord) will be
used.

**Default**: `false` (Automated avatars will be applied)

### Permissions Needed

| **User**: Manage Webhooks

### Examples

::: {.parsed-literal}
rsshook <http://xkcd.com/atom.xml>
<https://discord.com/api/webhooks/123456789098765432/LONG_WEBHOOK_TOKEN>
rsshook <https://www.pokemon.com/us/pokemon-news/rss>
<https://discord.com/api/webhooks/123456789098765432/LONG_WEBHOOK_TOKEN>
\--header A wild item appeared!
:::

------------------------------------------------------------------------

rssehook
--------

### Command Syntax

::: {.parsed-literal}
rssehook (RSS feed URL/stream index) \[new customization params\]
:::

### Command Description

**Replaces** all previously set customization params for the selected
RSS feed stream with a new set of customization params. The stream index
is the number shown with rsslhook.

::: {.warning}
::: {.title}
Warning
:::

Editing the webhook will not change the existing params, it will
completely replace them. Take note of the existing params first, and use
them in the command!
:::

### Permissions Needed

| **User**: Manage Webhooks

------------------------------------------------------------------------

rssrhook
--------

### Command Syntax

::: {.parsed-literal}
rssrhook (RSS feed URL/stream index)
:::

### Command Description

Stops a previously set RSS feed stream and removes its link to the
server webhook. The stream index is the number shown with rsslhook.

### Permissions Needed

| **User**: Manage Webhooks

### Examples

::: {.parsed-literal}
rssrhook pokemon rssrhook 2
:::

------------------------------------------------------------------------

rsslhook
--------

### Command Description

Prints a list of all the RSS feed streams that are linked to webhooks in
the current server.
