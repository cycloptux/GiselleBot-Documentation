Server Moderation (AutoModerator)
=================================

offers an auto moderation feature to be used alongside normal, manual
moderation. The current auto moderator currently supports **8** triggers
(messages or actions performed by users) and **5** actions (actions
performed on the offending user and/or message). Each trigger can be
configured with an extra whitelist, as described below.

::: {.warning}
::: {.title}
Warning
:::

This guide assumes you are familiar with the manual moderation module of
. If you have any doubt about one or more of the actions or parameters
that are used within the AutoModerator module, try checking
`moderation-module`{.interpreted-text role="ref"} first.
:::

By default, administrators and moderators (refer to
`moderation-role`{.interpreted-text role="ref"}) are immune to auto
moderation triggers.

------------------------------------------------------------------------

Supported Triggers
------------------

-   **Server Invites**: recognizes Discord server invites in user
    messages; this trigger supports **shortened** URLs (e.g. Discord
    invites hidden behind a bit.ly/gisl.eu shortening service), and
    ignores invites pointing to the current server.
-   **Anti-Phishing**: recognizes known phishing domains in user
    messages; this trigger supports **shortened** URLs (e.g. phishing
    domains hidden behind a bit.ly/gisl.eu shortening service). The list
    is updated on an hourly basis with new domains, and powered by
    cactus\#0523\'s phishing domains list.
-   **Mass Mention**: counts the number of mentions (roles, users or
    everyone/here) sent by a user, in a channel, within a certain span
    of time and triggers if the number of mentions is over a threshold.
    The default (allowed) threshold pair is **5** mentions in **30**
    seconds, but can be configured in each server.
-   **Banned Words**: checks the message against a list of words,
    configured by the user, and triggers if one or more words are found
    within the message. Punctuation and letter case are ignored. The
    parser can be configured to trigger on an \"exact match\" (e.g.
    banned word: `test`, matching word: `test`), if the banned word is
    found at the \"beginning of a word\" within the message (e.g. banned
    word: `test`, matching word: `testing`), or \"anywhere in word\"
    (e.g. banned word: `test`, matching word: `attestation`).
-   **Anti-Spam**: counts the number of messages **with the same
    content** sent by a user, in a channel, within a certain span of
    time and triggers if the number of identical message is over a
    threshold. The default (allowed) threshold pair is **3** messages in
    **10** seconds, but can be configured in each server.
-   **Anti-Emoji Spam**: counts the number of **emojis** sent by a user,
    in a channel, within a certain span of time (native or custom, in
    one or more messages) and triggers if the number of emojis is over a
    threshold. The default (allowed) threshold pair is **5** attachments
    in **10** seconds, but can be configured in each server.
-   **Anti-Attachment Spam**: counts the number of **attachments** sent
    by a user, in a channel, within a certain span of time and triggers
    if the number of attachments is over a threshold. The default
    (allowed) threshold pair is **5** attachments in **10** seconds, but
    can be configured in each server.
-   **NSFW Images**: recognizes possible NSFW images sent by posting
    URLs in a message, or using message attachments, and triggers if at
    least one of the images posted is over the NSFW threshold for the
    server. Refer to `nsfwjs`{.interpreted-text role="ref"} for a deeper
    explanation of this detection system, and to
    `nsfwthreshold`{.interpreted-text role="ref"} to configure the
    server threshold.
-   **QR Codes**: recognizes QR codes contained in images sent by
    posting URLs in a message, or using message attachments, and
    triggers if at least one of the images posted is confirmed to
    contain a QR code. This check works on **both screenshots and
    pictures** (taken by a camera/webcam), even though the recognition
    rate of pictures may be affected by the quality of the image.
-   **Anti-Raid**: counts the number of users (either new, or existing
    users leaving and re-joining) joining your server within a certain
    span of time and triggers if the number server joins is over a
    threshold. The default (allowed) threshold pair is **5** users in
    **15** seconds, but can be configured in each server.
-   **Anti-Young Accounts**: checks the Discord account age (time from
    the account creation date) of each user joining your server and
    triggers if the account age is lower than a set threshold. The
    default threshold is **1 hour**, but can be configured in each
    server.

::: {.note}
::: {.title}
Note
:::

Discord lag or connection problems can cause Anti-Spam and
Anti-Attachment Spam false positives.
:::

::: {.note}
::: {.title}
Note
:::

The Server Invites, Anti-Phishing, Banned Words, NSFW Images and QR
Codes triggers also support message editing: messages will be re-checked
upon being edited.
:::

::: {.warning}
::: {.title}
Warning
:::

The NSFW Images trigger, by no means, is supposed to reliably recognize
all NSFW images. Use it at your own risk, and only as an additional tool
to support humans in better moderating the server.
:::

When more then one trigger is active and a message is potentially
breaking more than one of the active triggers, this priority order will
apply:
`Server Invites > Anti-Phishing > Mass Mentions > Banned Words > Anti-Spam > Anti-Attachment Spam > QR Codes > NSFW Images`.

For automoderation triggers that apply on **messages**, you can also
have scan server reference messages (a.k.a. messages coming from
\"followed channels\" from other servers) by enabling **Scan \"Followed
Channels\" messages**.

------------------------------------------------------------------------

Supported Actions
-----------------

-   **Automatic deletion of the offending message**.
-   **Auto-warn**: Automatically apply a generic warning on the
    offending user. Specify a rule with the dedicated option.
-   **Auto-mute**: Automatically mute the offending user. By default,
    the applied mute is a temporary (2 hours long) mute, but can be
    configured for each moderation trigger.
-   **Auto-kick**: Automatically kick the offending user.
-   **Auto-ban**: Automatically ban the offending user.

When more then one action is configured on a trigger, this priority
order will apply: `Ban > Mute > Kick > Warn`.

If **Scan \"Followed Channels\" messages** is enabled, the only option
that will be applied on server reference messages is the **Automatic
deletion of the offending message** (if it\'s enabled).

------------------------------------------------------------------------

Whitelisting Options
--------------------

-   **Users**: Ignore messages/actions performed by specific users in a
    server.
-   **Roles**: Ignore messages/actions performed by specific roles in a
    server.
-   **Channels**: Ignore messages sent in specific channels in a server.
-   **Servers (Server Invites only)**: Ignore Discord server invites
    pointing to a specific server. You need to use the server ID to add
    this kind of whitelisting option. Applying this whitelist rule
    enables instant, temporary or permanent invites (including vanity
    URLs) for one or more server(s).

::: {.note}
::: {.title}
Note
:::

When adding or removing roles and channels through
`automodsetup`{.interpreted-text role="ref"}, other than toggling
individual roles and channels, you can quickly add or remove all roles
and/or channels from the list by using the following special tags:
**ALL\_ROLES**, **ALL\_CHANNELS**, **NO\_ROLES**, **NO\_CHANNELS**.
:::

------------------------------------------------------------------------

Extra Options
-------------

-   **Moderators alerting**: Each auto moderator action will be logged
    into the **Moderation** logger (refer to
    `log-command`{.interpreted-text role="ref"}). If this option is
    enabled, each log entry will also include a mention to the current
    moderator role(s).
-   **Moderation rule**: If a moderation action is taken against the
    offending user, this option will let you select one rule to use for
    that action.

------------------------------------------------------------------------

AutoModerator Configuration
---------------------------

Configuration of the auto moderation feature is achieved by using the
following command. It will open an interactive menu within the current
channel, using which you\'ll be able to setup the module.

You must save the changes you applied (option **1** of the menu) in
order for them to be applied.

::: {.note}
::: {.title}
Note
:::

The AutoModerator will also be configurable through the online
dashboard, as soon as it\'s available for public use.
:::

### automodsetup

#### Command Syntax

::: {.parsed-literal}
amset
:::

#### Command Description

Opens the auto moderation interactive setup menu. Use the menu items to
configure the above settings.

::: {.note}
::: {.title}
Note
:::

Not all of the settings will have a meaning in all of the triggers. Read
the above descriptions to understand what each option means within the
specific trigger.
:::
