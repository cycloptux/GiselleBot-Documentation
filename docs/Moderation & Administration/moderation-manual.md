Server Moderation (Manual)
==========================

A special thanks to my friend and partner, NaviKing\#3820, for the
design of this module.

The purpose of this module is to warn users, track their infractions,
and give the moderators the power to punish users accordingly.

In order to fully take advantage of this module, enabling the
case/scoring system is suggested. The scoring system is enabled if the
**Warning** log is enabled in a server channel. Please refer to the
`log-command`{.interpreted-text role="ref"} section in the
**Administration** module documentation.

------------------------------------------------------------------------

Configuration Commands
----------------------

These configuration commands are only enabled for those with Manage
Server permissions. The usage of these commands will be recorded in the
**Moderation** log.

### modrole

#### Command Syntax

::: {.parsed-literal}
modrole \[add/remove\] \[role id(s)/mention(s)/q\_name(s)\]
:::

#### Command Description

Adds or removes a role as a moderator role (Mod Role),
enabling/disabling them to use the moderation module regardless of other
permissions on their roles. Provide no arguments to show the current mod
roles.

#### Permissions Needed

| **User**: Manage Server

#### Examples

::: {.parsed-literal}
modrole modrole add \"Discord Moderators\" \"Discord Officers\" modrole
remove \@Reddit Moderators
:::

------------------------------------------------------------------------

### modimmunity

#### Command Syntax

::: {.parsed-literal}
modimmunity
:::

#### Command Description

Toggles whether or not users with the mod role can be affected by
moderation commands. Default state: **off**.

If enabled, attempting to take moderation actions on a moderator will
return an error.

#### Permissions Needed

| **User**: Manage Server

------------------------------------------------------------------------

### modanonymization

#### Command Syntax

::: {.parsed-literal}
modanon
:::

#### Command Description

Toggles whether or not users that are affected by a moderation action
will also be informed of the identity of the moderator using the
command. Default state: **off** (i.e. moderators **will not** be
anonymized).

If enabled, the name of the moderator will be omitted on the DM that a
user receives upon being hit by a moderation action, and a shield emoji
(🛡️) will appear next to the \"Performed By\" field of the corresponding
warning log embed to remind that moderators\' protection is on for that
case.

#### Permissions Needed

| **User**: Manage Server

------------------------------------------------------------------------

### modnotification

#### Command Syntax

::: {.parsed-literal}
modnotif
:::

#### Command Description

Toggles whether or not moderators will be informed with a mention in the
Moderation/Warning logger in case of missing parameters when applying a
moderation action with an \"incomplete\" syntax. Default state: **on**
(i.e. moderators **will** be notified with a mention).

#### Permissions Needed

| **User**: Manage Server

------------------------------------------------------------------------

### muterole

#### Command Syntax

::: {.parsed-literal}
muterole \[role id/mention/q\_name\]
:::

#### Command Description

Defines a role to be used as the mute role. Attempting to set a mute
role that is higher than either the command user\'s highest role or the
bot\'s highest role will result in an error being thrown. Provide no
arguments to show the current mute role.

Channel permissions for the mute role will be automatically set and
updated every time the configuration or moderation command is used.

Muted users will have the following permissions disabled for every
channel (besides the \"mute chat\", see below): **Send Messages**,
**Attach Files**, **Add Reactions**, **Use Public Threads**, **Use
Private Threads**, **Speak**.

#### Permissions Needed

| **User**: Manage Server
| **Bot**: Manage Roles, Mute Members

------------------------------------------------------------------------

### mutechat

#### Command Syntax

::: {.parsed-literal}
mutechat \[channel id(s)/mention(s)/q\_name(s)\]
:::

#### Command Description

Sets one (or more) channel(s) for muted users to be able to speak for
the purposes of discussing the moderation action taken against them.

When the bot sets channel permissions for the mute role, this special
channel(s) will have the following permissions:

-   **Read Messages**: Enabled
-   **Send Messages**: Enabled
-   **Read Message History**: Disabled
-   **Add Reactions**: Disabled
-   **Attach Files**: Enabled
-   **Speak**: Disabled

#### Permissions Needed

| **User**: Manage Server

------------------------------------------------------------------------

### imagebanrole

#### Command Syntax

::: {.parsed-literal}
imagebanrole \[role id/mention/q\_name\]
:::

#### Command Description

Defines a role to be used as the image ban role. Attempting to set a
image ban role that is higher than either the command user\'s highest
role or the bot\'s highest role will result in an error being thrown.
Provide no arguments to show the current image ban role.

Channel permissions for the image ban role will be automatically set and
updated every time the configuration or moderation command is used.

Image banned users will have the following permissions disabled for
every channel: **Embed Links**, **Attach Files**.

#### Permissions Needed

| **User**: Manage Server
| **Bot**: Manage Roles

------------------------------------------------------------------------

### channelbanrole

#### Command Syntax

::: {.parsed-literal}
cbanrole \[channel id/mention/q\_name\] \[role id/mention/q\_name\]
:::

#### Command Description

**For the specified channel**, defines a role to be used as the channel
ban role. Attempting to set a channel ban role that is higher than
either the command user\'s highest role or the bot\'s highest role will
result in an error being thrown. Provide no arguments to show the
current channel ban roles.

Channel permissions for the channel ban role will be automatically set
and updated every time the configuration or moderation command is used.

Channel banned users will have the following permissions disabled for
the specified channel: **Read Messages**, **View Channel**.

#### Permissions Needed

| **User**: Manage Server
| **Bot**: Manage Roles

------------------------------------------------------------------------

### channelmuterole

#### Command Syntax

::: {.parsed-literal}
cmuterole \[channel id/mention/q\_name\] \[role id/mention/q\_name\]
:::

#### Command Description

**For the specified channel**, defines a role to be used as the mute
role. Attempting to set a mute role that is higher than either the
command user\'s highest role or the bot\'s highest role will result in
an error being thrown. Provide no arguments to show the current mute
roles.

Channel permissions for the mute role will be automatically set and
updated every time the configuration or moderation command is used.

Muted users will have the following permissions disabled for the
specified channel: **Send Messages**, **Attach Files**, **Add
Reactions**, **Use Public Threads**, **Use Private Threads**, **Speak**.

#### Permissions Needed

| **User**: Manage Server
| **Bot**: Manage Roles, Mute Members

------------------------------------------------------------------------

### channelimagebanrole

#### Command Syntax

::: {.parsed-literal}
cimagebanrole \[channel id/mention/q\_name\] \[role id/mention/q\_name\]
:::

#### Command Description

**For the specified channel**, defines a role to be used as the image
ban role. Attempting to set a image ban role that is higher than either
the command user\'s highest role or the bot\'s highest role will result
in an error being thrown. Provide no arguments to show the current image
ban roles.

Channel permissions for the image ban role will be automatically set and
updated every time the configuration or moderation command is used.

Image banned users will have the following permissions disabled for the
specified channel: **Embed Links**, **Attach Files**.

#### Permissions Needed

| **User**: Manage Server
| **Bot**: Manage Roles

------------------------------------------------------------------------

Moderation Commands
-------------------

These moderation commands are the actual commands that are used to apply
moderation actions. Each one of the following commands will be very
similar in nature, and thus the common features of the commands will be
discussed together in this section, and the specifics of each command in
subsections.

Collectively, these commands will be referred to as \"warning
commands\".

The list of \"warning commands\" is the following:

-   warn
-   kick
-   ban
-   delayban
-   mute
-   imageban
-   cban
-   cmute
-   cimageban

By default, warning commands will generate a new case if the **Warning**
log is active. Upon generating a case, a DM will be sent to the target
user(s), notifying them of the moderation action that has been triggered
on them, who issued the moderation action and the specifics of the rules
that are broken, if applicable. Please refer to the \"Warning Point
System\" section below for more details about the rules system.

These commands support being used on multiple users at once: if more
than one user is targeted by these commands, the parameters will be
parallelized for all of the users, while multiple cases will be
generated.

The following commands also support being set as \"automatically
expiring after X time\":

-   mute
-   delayban
-   imageban
-   cban
-   cmute
-   cimageban

This is achieved by **prepending** the target users with a time code.

::: {.note}
::: {.title}
Note
:::

This time setting will overwrite the previous setting each time the
command is run on a specified user: this also applies to converting a
permanent action into a timed one and vice-versa, without removing the
role on the target user.
:::

### (Common) Command Syntax

::: {.parsed-literal}
{warning command} \[duration timecode\] \[channel id/mention/q\_name
{only for channel-specific commands}\] (user
id(s)/mention(s)/q\_name(s)) \[\--rule {rule id/name/alias}\]
\[\--reason {textual description}\] \[\--attachments {urls}\] \[\--padj
{signed/unsigned number}\] \[\--justification {textual justification}\]
\[\--skip-case\] \[\--skip-dm\]
:::

### (Common) Command Description

Informs the user(s) via DM that they have been warned/muted/banned/etc.,
including the rule that they broke, the specific reason, attachments,
and who warned them. These arguments are all optional when running
warning commands (only the user identifier is required). If applicable,
the `--reason` parameter will appear in the Discord native audit log as
well.

If all of these arguments are skipped, the message will simply read
\"You were warned/muted/banned by \[moderator\].\".

Channel specific commands which are missing the channel parameter will
default to being targeted to the current channel. Channels that support
time-based expiration (see above) will be treated as permanent if the
timecode is missing.

You can skip generating a case by appending the `--skip-case` tag. You
can skip sending the DM (but still generate a case) by appending the
`--skip-dm` tag. `--skip-case` also implies `--skip-dm`.

::: {.note}
::: {.title}
Note
:::

When `--skip-dm` is used, a small 🔕 emoji will appear on the
corresponding notification and warning log embed footer to track the
fact that the action was \"silent\".
:::

Every warning, by default, will be worth a certain number of points
based on the rule broken (as described in the \"Warning Point System\"
section below.

The `--padj`, or \"points added/subtracted\" argument, is completely
optional and will not be included in the DM even if it is included in
the command. Any signed number (\"+\" or \"-\") will be treated as a
\"delta\" value over the default rule score, while an unsigned number
will be treated as a fixed, absolute value and used as the actual
warning score. The justification for points added/subtracted is invalid
if no points were added or subtracted and should be ignored if the
moderator does not add or subtract any points.

Each one of the command parameters has one or more aliases. Here are the
available aliases:

-   `--rule`: `--r`
-   `--reason`: `--rs`
-   `--attachments`: `--attachment` `--att` `--a`
-   `--padj`: `--pa` `--p`
-   `--justification`: `--just` `--j`
-   `--skip-case`: `--skipcase` `--nocase` `--no-case`
-   `--skip-dm`: `--skipdm` `--nodm` `--no-dm`

Running the command as the \"description\" of a Discord attachment (e.g.
by drag-and-dropping an image over the Discord client) will
automatically add that object as the warning case attachment, even if
the `--attachments` parameter is skipped.

As said above, these commands will automatically generate a
server-specific case ID that can be used as reference in other commands.
An embed including the following information will also be generated and
put into the warning log:

-   Warning Type (warn/mute/ban/etc.)
-   Warned user\'s name
-   Warned user\'s ID
-   Mod Name
-   Rule broken
-   Reason
-   Attachment (as embed\'s image, if applicable)
-   Points added/subtracted (optional)
-   Justification (only if points are added/subtracted)
-   Total unexpired points as of warning for this user
-   **Suggested moderation action & number of points to next warning
    threshold**
-   Case ID & timestamp (in footer)

If any of the rule, reason or attachments parameters are missing, the
bot will tag the moderator upon action log generation prompting them to
fill in the missing arguments using the edit command. The bot will also
tag the moderator the first time that the user reaches a suggested
action threshold.

Some moderation action commands have a \"un-\" version that reverts the
corresponding moderation action. \"un-\" commands will follow a similar
syntax but will never generate a new case, hence rendering the set of
warning parameters (every parameter after the user identifier(s))
useless.

What follows is a list of all of the commands in this section. As
already said, each command description and syntax will be a diff over
the common syntax shown here.

------------------------------------------------------------------------

### warn

#### Command Description

warn does nothing but DM the user(s) with their warning. Its purpose is
to officially record an infraction so that the accumulation of
infractions can later be used to justify a mute or a ban (see the
\"Warning Point System\" described later).

Refer to `moderation`{.interpreted-text role="ref"} for the exact
command syntax.

#### Examples

::: {.parsed-literal}
warn \@cycloptux\#1543 \--rule Discord ToS \--reason The user is under
13 years of age \--padj -2 \--justification Testing the command
:::

------------------------------------------------------------------------

### kick

#### Command Description

Kicks the target user(s) from the current server. The user may be able
to join the server again through a working invite.

Refer to `moderation`{.interpreted-text role="ref"} for the exact
command syntax.

#### Permissions Needed

| **User**: Kick Members
| **Bot**: Kick Members

------------------------------------------------------------------------

### mute

#### Command Description

mute applies the role configured in muterole (or creates a default
\"Muted Users\" role at the bottom of the role list with no permissions
if the mute role is not configured) to the target user(s) and sets all
channel permissions (except for the ones configured as mute chat(s)) for
the mute role, as described in the previous sections.

The specific permissions for this command will be set (or
checked/updated) every time the command is run, hence making the command
slightly slower than usual. This is normal.

The mute can be permanent (users will be muted until manual removal) or
timed (users will be unmuted automatically after a certain time span).

Refer to `moderation`{.interpreted-text role="ref"} for the exact
command syntax.

#### Permissions Needed

| **User**: Manage Roles, Mute Members
| **Bot**: Manage Roles, Mute Members

------------------------------------------------------------------------

### ban

#### Command Syntax

::: {.parsed-literal}
ban \[24/7\] \...
:::

#### Command Description

ban has one additional, optional argument before the user identifier(s):
either the number 24, or the number 7. If this argument is omitted, the
user is banned without their message history being deleted. Otherwise,
the bot uses the native ban API to delete the last 24 hours or 7 days of
the banned users\' message history.

The same parameter can also be passed by using the `--days` argument
(e.g. `--days 1` or `--days 7`). `--days` also has the following
aliases: `--msgdays` `--delmsg` `--purge` `--d`

This command also works for banning users that are currently not in the
server, as long as the user is known/cached by the bot. It is advised to
use the user ID for that.

Refer to `moderation`{.interpreted-text role="ref"} for the exact
command syntax.

#### Permissions Needed

| **User**: Ban Members
| **Bot**: Ban Members

------------------------------------------------------------------------

### timeban

#### Command Description

timeban bans a user from the current server for the specified amount of
time.

Once the ban period has ended, as long as the user hasn\'t been
permanently banned by \"overwriting\" the timed ban with a fully fledged
ban (or manually re-allowed through unban), the ban will be
automatically lifted. If the time argument is omitted, it will default
to 24 hours.

Please allow for up to 1 extra minute before the ban is actually lifted
after it has officially expired.

This command also works for banning users that are currently not in the
server, as long as the user is known/cached by the bot. It is advised to
use the user ID for that.

Refer to `moderation`{.interpreted-text role="ref"} for the exact
command syntax.

#### Permissions Needed

| **User**: Ban Members
| **Bot**: Ban Members

------------------------------------------------------------------------

### delayban

#### Command Description

delayban mutes a user for the specified amount of time. If this mute
status isn\'t removed with cancelban before the timer is out, the user
will be banned from the server. If the time argument is omitted, it will
default to 24 hours.

Refer to `moderation`{.interpreted-text role="ref"} for the exact
command syntax.

#### Permissions Needed

| **User**: Manage Roles, Mute Members, Ban Members
| **Bot**: Manage Roles, Mute Members, Ban Members

------------------------------------------------------------------------

### imageban

#### Command Description

imageban applies the role configured in imagebanrole (or creates a
default \"Image Banned Users\" role at the bottom of the role list with
no permissions if the image ban role is not configured) to the target
user(s) and sets all channel permissions for the image ban role, as
described in the previous sections.

The specific permissions for this command will be set (or
checked/updated) every time the command is run, hence making the command
slightly slower than usual. This is normal.

The image ban can be permanent (users will be image banned until manual
removal) or timed (users will be image unbanned automatically after a
certain time span).

Refer to `moderation`{.interpreted-text role="ref"} for the exact
command syntax.

#### Permissions Needed

| **User**: Manage Roles
| **Bot**: Manage Roles

------------------------------------------------------------------------

### cban

#### Command Description

cban applies the role configured in channelbanrole (or creates a default
\"\#%channel% Banned Users\" role at the bottom of the role list with no
permissions if the channel ban role is not configured) to the target
user(s) and sets the channel permissions for the ban role, as described
in the previous sections.

The specific permissions for this command will be set (or
checked/updated) every time the command is run, hence making the command
slightly slower than usual. This is normal.

The channel ban can be permanent (users will be channel banned until
manual removal) or timed (users will be channel unbanned automatically
after a certain time span).

Refer to `moderation`{.interpreted-text role="ref"} for the exact
command syntax.

#### Permissions Needed

| **User**: Manage Roles
| **Bot**: Manage Roles

------------------------------------------------------------------------

### cmute

#### Command Description

cmute applies the role configured in channelmuterole (or creates a
default \"\#%channel% Muted Users\" role at the bottom of the role list
with no permissions if the channel mute role is not configured) to the
target user(s) and sets the channel permissions for the mute role, as
described in the previous sections.

The specific permissions for this command will be set (or
checked/updated) every time the command is run, hence making the command
slightly slower than usual. This is normal.

The channel mute can be permanent (users will be channel muted until
manual removal) or timed (users will be channel unmuted automatically
after a certain time span).

Refer to `moderation`{.interpreted-text role="ref"} for the exact
command syntax.

#### Permissions Needed

| **User**: Manage Roles, Mute Members
| **Bot**: Manage Roles, Mute Members

------------------------------------------------------------------------

### cimageban

#### Command Description

cimageban applies the role configured in channelimagebanrole (or creates
a default \"\#%channel% Image Banned Users\" role at the bottom of the
role list with no permissions if the channel image ban role is not
configured) to the target user(s) and sets the channel permissions for
the image ban role, as described in the previous sections.

The specific permissions for this command will be set (or
checked/updated) every time the command is run, hence making the command
slightly slower than usual. This is normal.

The channel image ban can be permanent (users will be channel image
banned until manual removal) or timed (users will be channel image
unbanned automatically after a certain time span).

Refer to `moderation`{.interpreted-text role="ref"} for the exact
command syntax.

#### Permissions Needed

| **User**: Manage Roles
| **Bot**: Manage Roles

------------------------------------------------------------------------

### unmute

#### Command Syntax

::: {.parsed-literal}
unmute (user id(s)/mention(s)/q\_name(s))
:::

#### Command Description

Lifts the mute role from the target user(s).

#### Permissions Needed

| **User**: Manage Roles, Mute Members
| **Bot**: Manage Roles, Mute Members

------------------------------------------------------------------------

### unban

#### Command Syntax

::: {.parsed-literal}
unban (user id(s)/mention(s)/q\_name(s))
:::

#### Command Description

Lifts the ban status from the target user(s).

#### Permissions Needed

| **User**: Ban Members
| **Bot**: Ban Members

------------------------------------------------------------------------

### cancelban

#### Command Syntax

::: {.parsed-literal}
cancelban (user id(s)/mention(s)/q\_name(s))
:::

#### Command Description

Lifts the mute role from the target user(s), and cancels the
corresponding timed ban.

#### Permissions Needed

| **User**: Ban Members
| **Bot**: Ban Members

------------------------------------------------------------------------

### imageunban

#### Command Syntax

::: {.parsed-literal}
imageunban (user id(s)/mention(s)/q\_name(s))
:::

#### Command Description

Lifts the image ban role from the target user(s).

#### Permissions Needed

| **User**: Manage Roles
| **Bot**: Manage Roles

------------------------------------------------------------------------

### cunmute

#### Command Syntax

::: {.parsed-literal}
cunmute \[channel id/mention/q\_name\] (user
id(s)/mention(s)/q\_name(s))
:::

#### Command Description

Lifts the channel mute role from the target user(s). Omission of the
channel identifier will result in the current channel being considered
by the command.

#### Permissions Needed

| **User**: Manage Roles, Mute Members
| **Bot**: Manage Roles, Mute Members

------------------------------------------------------------------------

### cunban

#### Command Syntax

::: {.parsed-literal}
cunban \[channel id/mention/q\_name\] (user id(s)/mention(s)/q\_name(s))
:::

#### Command Description

Lifts the channel ban role from the target user(s). Omission of the
channel identifier will result in the current channel being considered
by the command.

#### Permissions Needed

| **User**: Manage Roles
| **Bot**: Manage Roles

------------------------------------------------------------------------

### cimageunban

#### Command Syntax

::: {.parsed-literal}
cimageunban \[channel id/mention/q\_name\] (user
id(s)/mention(s)/q\_name(s))
:::

#### Command Description

Lifts the channel image ban role from the target user(s). Omission of
the channel identifier will result in the current channel being
considered by the command.

#### Permissions Needed

| **User**: Manage Roles
| **Bot**: Manage Roles

------------------------------------------------------------------------

Utility Commands
----------------

These moderation commands may be used in conjunction with the rest of
the moderation module to keep your server clean.

### prune

#### Command Syntax

::: {.parsed-literal}
prune (\# of messages) \[filter item\] \[\--ignore {filter ignore}\]
:::

#### Command Description

Deletes a certain number of messages from the channel in which the
command is run. For security reasons, the bot caps this number to
**250** messages.

The filter items serve to delete/ignore a subset of messages in the set
of messages specified by the integer argument. The list of available
filters is:

-   `images`: deletes all images in the set of messages
-   `bots`: deletes all messages from bots in the set of messages
-   `links`: deletes all messages with links in the set of messages
-   `emojis`: deletes all messages with emojis in the set of messages
-   `reactions`: deletes all of the reactions off of the messages in the
    set of messages, **not the messages themselves**
-   `embeds`: deletes all embeds in the set of messages (this doesn\'t
    include embeds that are generated by links, see `links` for that)
-   `text`: deletes messages that only contain plain text in the set of
    messages
-   `invites`: deletes messages containing Discord invites in the set of
    messages
-   `mentions`: deletes messages containing a mention to a user, role,
    \"\@everyone\" or \"\@here\" in the set of messages
-   `{user mention}`: deletes messages sent by the specified user in the
    set of messages
-   `{any text string}`: deletes messages containing matching text from
    the supplied text string in the set of messages (for example, prune
    100 \"donald trump\" would delete all messages containing \"donald
    trump\" in the last 100 messages)

You can add an `--ignore` tag, combined with the aforementioned filter
items, to ignore (and not delete) messages meeting that criteria. For
example \"purge 100 bots \--ignore embeds\" would delete all bot
messages that weren\'t embeds.

#### Permissions Needed

| **User**: Manage Messages
| **Bot**: Manage Messages

#### Examples

::: {.parsed-literal}
prune 100 purge 250 bots clear 150 \@cycloptux\#1543 \--ignore images
:::

------------------------------------------------------------------------

### slowmode

#### Command Syntax

::: {.parsed-literal}
slowmode \[time code\] \[channel id(s)/mention(s)/q\_name(s)\]
\[\--admode\]
:::

#### Command Description

Sets slow mode for the current, or the selected, channels. This command
leverages 2 different systems:

-   If the slow mode time code is within Discord\'s native slow mode
    time limit (less than 6 hours), the native slow mode is applied.
-   If the slow mode time code exceeds Discord\'s native time limit
    (more than 6 hours, up to 1 year), the bot will apply an \"extended
    slow mode\" status.

The **extended slow mode** applies a minimal native slow mode to make
sure the \"Slowmode is enabled\" message is shown. At the same time,
each message sent by an unauthorized user will be automatically deleted,
and the user will be notified of the applied slow mode.

The extended slow mode doesn\'t have a higher cap.

Using the command without any argument will show the current settings
for the server. Using the command with **0** in place of the time code
will disable the slow mode for the current, or the selected, channel(s).

The usage of the optional `--admode` parameter will enable the
**Auto-Delete** mode, a.k.a. **Bump Mode**. If the **extended slow
mode** is active (this mode will not work on native slow mode), each
message that is **successfully** sent into the slowed channel will
**also** trigger an automatic deletion of the previous message sent by
the user while slow mode is active.

#### Permissions Needed

| **User**: Manage Messages
| **Bot**: Manage Messages

#### Examples

::: {.parsed-literal}
sm 1h45m \#slow-channel sm 0 \#slow-channel-1 \#slow-channel-2 slowmode
:::

------------------------------------------------------------------------

Evasion Actions
---------------

In addition to the active behavior of the warning commands, the
following commands also support a special \"evasion\" action log:

-   mute
-   imageban
-   cban
-   cmute
-   cimageban

An \"evasion\" action happens when a user that is hit with one of these
moderation actions leaves the server and rejoins while the corresponding
role is still supposed to be up (either because the timed role still has
to expire, or the role has been set as permanent by skipping the
corresponding time code).

If still applicable, the role will be applied again as soon as the user
rejoins the server and an \"evasion\" log will appear in the warning
log.

------------------------------------------------------------------------

Warning Point System
--------------------

To account for the nature and severity of various infractions, users
will incur a certain number of points based on which rule they break.
Moderators will be able to use their judgment to adjust the default
value of an infraction by adding or subtracting points from the warning.
At certain point thresholds, it is recommended that certain moderation
actions (such as a mute or ban) be taken against the user.

This section will describe the details of the \"default\" warning point
system backend as well as point out options or commands to configure
parts of the system.

### Point Accumulation and Thresholds
In addition to a user\'s total points being the sum of the points of
their infractions, the following rules apply to points:

-   Warning points expire after **90 days**, at which point the value of
    the infraction decreases to **1**.
-   The first warning for a particular rule is considered to be a \"soft
    warning\" and worth half points (e.g., if a user broke the toxic
    attitudes rule and the NSFW rule, both infractions would be recorded
    at half points, but breaking the toxic attitudes rule twice would
    result in the second infraction being recorded at full points). This
    behavior can be configured with `half-logic`{.interpreted-text
    role="ref"}.
-   Each case score can be manually adjusted (`--padj`) but it must
    always be \>= 0. Validation rules are in place for a score not to be
    negative. Any adjustment that brings the score to a negative value
    will make the score account for 0.
-   In order to preserve the severity of a banned user\'s warning
    history, points for banned users will not expire **while the user is
    banned**. Unbanning a user will make the points behave as usual
    again.

The following thresholds apply to the point total of a user. A user
reaching one of these thresholds will cause the action log message
related to that warning to include a tag of the issuing moderator
informing him/her of the user reaching the threshold.

-   18 **unexpired** points: The bot will recommend in the action log
    that the user in question be muted.
-   27 **unexpired** points: The bot will recommend in the action log
    that the user in question be banned.
-   54 points **total, even if expired**: The bot will recommend in the
    action log that the user in question be banned. This is referred to
    as the \"absolute ban threshold\".
-   *(not implemented yet)* **Three channel specific warnings**: The bot
    will recommend in the action log that the user be banned from that
    specific channel, regardless of the total point value. A user can
    simultaneously reach this threshold and the point thresholds, and
    the message in the action log should be constructed accordingly.

The justification for these thresholds are as follows:

-   Rules are given point values based on a severity from 1 to 10.
-   Since the first infraction is worth half points, only even numbers
    should be used for rule values.
-   6 is the average rule value.
-   A \"full warning\" (i.e., one soft warning and one regular warning)
    would be 9 points on average.
-   Two \"full warnings\" should result in a mute, and three should
    result in a ban.
-   The absolute ban threshold is twice the ban threshold, a
    considerable feat even in one\'s lifetime of the server.

### Default Rules and Points

Ideally, users would configure their own rules and point values.
However, there are definitely some rules that are common among servers
and can be provided as a default hard-coded table. The default table is
provided to use as a base:

+-------+---+---------------------------------------------------------+---+
| Rule  | R | Rule Description                                        | R |
| Name  | u |                                                         | u |
|       | l |                                                         | l |
|       | e |                                                         | e |
|       | A |                                                         | P |
|       | l |                                                         | o |
|       | i |                                                         | i |
|       | a |                                                         | n |
|       | s |                                                         | t |
|       |   |                                                         | s |
+=======+===+=========================================================+===+
| No    | T | Please behave and do not make a nuisance of yourself on | 6 |
| Toxic | o | the server, including \"trolling\" or otherwise being   |   |
| Atti  | x | disruptive or making others feel uncomfortable.         |   |
| tudes | i |                                                         |   |
|       | c |                                                         |   |
|       | A |                                                         |   |
|       | t |                                                         |   |
|       | t |                                                         |   |
|       | i |                                                         |   |
|       | t |                                                         |   |
|       | u |                                                         |   |
|       | d |                                                         |   |
|       | e |                                                         |   |
|       | s |                                                         |   |
+-------+---+---------------------------------------------------------+---+
| No    | O | Please refrain from posting offensive content such as   | 8 |
| Offe  | f | politics, religion, acts of violence, rape, suicide,    |   |
| nsive | f | school shootings, and other serious topics. Also keep   |   |
| Con   | e | in mind that hate speech including racial slurs or      |   |
| tent, | n | derivatives thereof, sexist or homophobic statements,   |   |
| Hate  | s | and other similar types of behavior is not tolerated on |   |
| S     | i | this server.                                            |   |
| peech | v |                                                         |   |
| or    | e |                                                         |   |
| Sens  | C |                                                         |   |
| itive | o |                                                         |   |
| Mat   | n |                                                         |   |
| erial | t |                                                         |   |
|       | e |                                                         |   |
|       | n |                                                         |   |
|       | t |                                                         |   |
+-------+---+---------------------------------------------------------+---+
| No    | H | This applies both to DMs and public chat channels, and  | 8 |
| Haras | a | includes insults or other actions that target a         |   |
| sment | r | specific user in order to make them feel uncomfortable  |   |
|       | a | or unwelcome.                                           |   |
|       | s |                                                         |   |
|       | s |                                                         |   |
|       | m |                                                         |   |
|       | e |                                                         |   |
|       | n |                                                         |   |
|       | t |                                                         |   |
+-------+---+---------------------------------------------------------+---+
| Be    | A | While measured discussion and questions regarding why   | 8 |
| Respe | r | you were warned for something is fine, attacking the    |   |
| ctful | g | moderators or becoming belligerent over being warned    |   |
| to    | u | will likely result in another warning. You are welcome  |   |
| Moder | i | to provide feedback in the relevant channels on the     |   |
| ators | n | Discord server if your concern is general, or you may   |   |
|       | g | DM a moderator or administrator regarding your warning  |   |
|       |   | if your concern is specific.                            |   |
+-------+---+---------------------------------------------------------+---+
| Do    | I | Encouraging the breaking of rules, inciting others to   | 1 |
| Not   | n | be blatantly rude and offensive, or otherwise promoting | 0 |
| I     | c | and/or encouraging conflicts between other members will |   |
| ncite | i | result in punitive measures for both rulebreakers and   |   |
| O     | t | those encouraging rule breaking.                        |   |
| thers | e |                                                         |   |
| to    | m |                                                         |   |
| Break | e |                                                         |   |
| The   | n |                                                         |   |
| Rules | t |                                                         |   |
+-------+---+---------------------------------------------------------+---+
| Do    | S | Spam is a broad term used to define unsolicited or      | 8 |
| Not   | p | repetitious messages received electronically. Spamming  |   |
| Spam  | a | is prohibited on this server and in DMs to server       |   |
| the   | m | members. This includes image spam, text/link/emoji      |   |
| S     |   | spam, and tag spam.                                     |   |
| erver |   |                                                         |   |
| or    |   |                                                         |   |
| its   |   |                                                         |   |
| Me    |   |                                                         |   |
| mbers |   |                                                         |   |
+-------+---+---------------------------------------------------------+---+
| Do    | P | Please do not share other people's personal information | 8 |
| Not   | e | such as real names, addresses, other social media       |   |
| Share | r | accounts, etc. without their permission. Sharing this   |   |
| Other | s | with malicious intent may be construed as doxxing,      |   |
| Peo   | o | which will result in an instant ban.                    |   |
| ple's | n |                                                         |   |
| Per   | a |                                                         |   |
| sonal | l |                                                         |   |
| I     | I |                                                         |   |
| nform | n |                                                         |   |
| ation | f |                                                         |   |
|       | o |                                                         |   |
+-------+---+---------------------------------------------------------+---+
| No    | A | Advertisement of other discord servers, giveaways,      | 6 |
| A     | d | unofficial tournaments, or one's own social             |   |
| dvert | v | media/content creation channels is prohibited without   |   |
| ising | e | approval from a Discord Moderator. This includes        |   |
|       | r | advertisement in group channels as well as in Direct    |   |
|       | t | Messages (DMs) to server members.                       |   |
|       | i |                                                         |   |
|       | s |                                                         |   |
|       | i |                                                         |   |
|       | n |                                                         |   |
|       | g |                                                         |   |
+-------+---+---------------------------------------------------------+---+
| F     | C | Please remember to read channel descriptions and pins,  | 6 |
| ollow | h | and comply with channel specific rules.                 |   |
| Ch    | a |                                                         |   |
| annel | n |                                                         |   |
| Rules | n |                                                         |   |
|       | e |                                                         |   |
|       | l |                                                         |   |
|       | R |                                                         |   |
|       | u |                                                         |   |
|       | l |                                                         |   |
|       | e |                                                         |   |
|       | s |                                                         |   |
+-------+---+---------------------------------------------------------+---+
| Viol  | G | Violation of the game's terms of service, especially    | 5 |
| ating | a | hacking or modding the game, will result in an instant  | 4 |
| Game  | m | ban from the Discord server and possibly within the     |   |
| ToS   | e | game as well.                                           |   |
|       | T |                                                         |   |
|       | o |                                                         |   |
|       | S |                                                         |   |
+-------+---+---------------------------------------------------------+---+
| Viol  | D | Please keep in mind that Discord itself has specific    | 1 |
| ating | i | behavioral and content guidelines that you can read at  | 0 |
| Di    | s | <https://discord.com/guidelines>. Some of these         |   |
| scord | c | violations may result in an instant ban. Of particular  |   |
| ToS   | o | note are the following:                                 |   |
|       | r |                                                         |   |
|       | d | -   You must be at least 13 years of age to use Discord |   |
|       | T | -   Sharing sexually explicit content of minors, both   |   |
|       | o |     real and animated/drawn, is prohibited              |   |
|       | S | -   Glorifying self harm or suicide                     |   |
|       |   | -   Sharing pirated or illegally acquired content is    |   |
|       |   |     prohibited                                          |   |
+-------+---+---------------------------------------------------------+---+
| User  | U | Your profile picture, status message, and display name  | 4 |
| Pr    | s | (i.e., your server nickname if you have one set, or     |   |
| ofile | e | your actual username if not) should be compliant with   |   |
| Must  | r | the rules of the server. In addition, your display name |   |
| Meet  | P | must not imitate another user and meet the following    |   |
| Ce    | r | criteria:                                               |   |
| rtain | o |                                                         |   |
| Cri   | f | -   Easily taggable/readable                            |   |
| teria | i | -   Contains no inappropriate content                   |   |
|       | l | -   Does not deliberately hoist you to the top of the   |   |
|       | e |     online list                                         |   |
+-------+---+---------------------------------------------------------+---+
| No    | N | Dissemination of NSFW content in any form is prohibited | 8 |
| NSFW  | S | in all chats and includes excessive gore/extreme        |   |
| Co    | F | violence, content related to self harm or harming       |   |
| ntent | W | others, pornography or excessively sexual content. Any  |   |
|       |   | in game art is exempt from this rule unless otherwise   |   |
|       |   | noted.This rule applies to both images and text,        |   |
|       |   | although some leniency will be allowed for text         |   |
|       |   | content.                                                |   |
+-------+---+---------------------------------------------------------+---+

------------------------------------------------------------------------

Warning System Commands
-----------------------

This section will describe all those commands that are needed to use
(and configure, to a certain extent) the warning system, as described in
the previous section.

------------------------------------------------------------------------

### warnhistory

#### Command Syntax

::: {.parsed-literal}
warnhistory (user id(s)/mention(s)/q\_name(s))
:::

#### Command Description

Shows the warning history of one (or more) user(s) in reverse
chronological order. By default, this only includes a short summary for
each warning. Warn histories longer than 2000 characters are paginated
via reaction \"buttons\".

#### Examples

::: {.parsed-literal}
warnhistory 123456789098765432 history \@cycloptux\#1543
:::

------------------------------------------------------------------------

### case

#### Command Syntax

::: {.parsed-literal}
case (case id(s))
:::

#### Command Description

Prints a detailed log embed for the selected case(s).

#### Examples

::: {.parsed-literal}
case 2 case 12 15 34
:::

------------------------------------------------------------------------

### edit

#### Command Syntax

::: {.parsed-literal}
edit (case id) \[\--rule {rule id/name/alias}\] \[\--reason {textual
description}\] \[\--attachments {urls}\] \[\--padj {signed/unsigned
number}\] \[\--justification {textual justification}\] \[\--skip-dm\]
:::

#### Command Description

Edits an existing case. You cannot edit a case type (e.g. turning a warn
into a mute). Only the original case owner (the issuing moderator) or a
server administrator can edit a case.

Editing a case will generate a new warning log entry with the new
details. The old entry will be edited with a clickable link that will
bring you to the new edit.

Please refer to `moderation`{.interpreted-text role="ref"} for more
details about the individual parameters and their aliases.

#### Examples

::: {.parsed-literal}
edit 3 \--reason Spamming phishing links in the \#general channel
\--padj +4 \--just For repeated spamming despite being warned about it
:::

------------------------------------------------------------------------

### delete

#### Command Syntax

::: {.parsed-literal}
delete (case id(s))
:::

#### Command Description

Deletes one (or more) existing case(s). Deleted cases are never actually
removed from the bot memory and can be restored in the future if you
remember the case ID(s).

#### Permissions Needed

| **User**: Manage Server

#### Examples

::: {.parsed-literal}
delete 3 4 10
:::

------------------------------------------------------------------------

### restore

#### Command Syntax

::: {.parsed-literal}
restore (case id(s))
:::

#### Command Description

Restores one (or more) previously deleted case(s).

#### Permissions Needed

| **User**: Manage Server

#### Examples

::: {.parsed-literal}
restore 3 4
:::

------------------------------------------------------------------------

### listrules

#### Command Syntax

::: {.parsed-literal}
listrules \[rule id/name/alias\] \[\--server\] \[\--channel \[channel
id/mention/q\_name\]\] \[\--mod\]
:::

#### Command Description

Lists the rules (both custom and default sets) of the server in order by
Rule ID, including the Rule Title and Description for each rule. Provide
an ID/Name/Alias to show a specific rule only. By default, the list will
show both server wide and channel-specific rules. Use `--server` to
limit the rules to the server wide ones. Use `--channel` with a channel
tag to show only channel specific rules for that channel (omitting the
channel identifier will show the rules for the current channel).

The rule alias and points will be shown if a moderator or administrator
appends the `--mod` parameter to the command.

#### Examples

::: {.parsed-literal}
listrules listrules \--channel \#general listrules NSFW \--mod
:::

------------------------------------------------------------------------

### addrule

#### Command Syntax

::: {.parsed-literal}
addrule (\--name {rule name}) (\--alias {rule alias}) (\--description
{rule description}) (\--points {rule points (number)}) \[\--channel
\[channel id/mention/q\_name\]\]
:::

#### Command Description

Adds a custom rule to the rules list. Adding a custom rule generates a
server-specific rule ID for that rule automatically, starting from
`s_1`. Adding a channel identifier will assign that rule as being
channel-specific (this is primarily used to track how close a user is to
reaching a channel ban threshold)

::: {.note}
::: {.title}
Note
:::

Channel ban thresholds are not implemented yet.
:::

#### Permissions Needed

| **User**: Manage Server

------------------------------------------------------------------------

### deleterule

#### Command Syntax

::: {.parsed-literal}
delrule (rule(s) id/name/alias)
:::

#### Command Description

Deletes a custom rule from the list of rules. Use toggleglobalrule to
hide a default rule from the list of rules (see below).

::: {.note}
::: {.title}
Note
:::

In order to preserve the history of users that were previously moderated
according to a specific rule, \"deleted\" rules are never actually
deleted. \"Deleted\" rules are instead **hidden**, and running the
deleterule again on the same rule ID will restore the rule in its
previous, visible state.
:::

#### Permissions Needed

| **User**: Manage Server

------------------------------------------------------------------------

### toggleglobalrule

#### Command Syntax

::: {.parsed-literal}
toggleglobalrule (rule(s) id/name/alias)
:::

#### Command Description

Deletes (hides) a default native rule from the list of rules. Use
deleterule to hide a custom rule from the list of rules (see above).

::: {.note}
::: {.title}
Note
:::

In order to preserve the history of users that were previously moderated
according to a specific rule, \"deleted\" rules are never actually
deleted. \"Deleted\" rules are instead **hidden**, and running the
toggleglobalrule again on the same rule ID will restore the rule in its
previous, visible state.
:::

#### Permissions Needed

| **User**: Manage Server

------------------------------------------------------------------------

### editrule

#### Command Syntax

::: {.parsed-literal}
editrule (rule id/name/alias) \[\--name {rule name}\] \[\--alias {rule
alias}\] \[\--description {rule description}\] \[\--points {rule points
(number)}\] \[\--channel \[-/channel id/mention/q\_name\]\]
:::

#### Command Description

Updates one or more fields of an existing rule to the new values.

Use `--channel -` to convert a channel-specific rule into a server wide
rule.

#### Permissions Needed

| **User**: Manage Server

------------------------------------------------------------------------

### halflogic

#### Command Syntax

::: {.parsed-literal}
halflogic (none/first/first-with-points/each)
:::

#### Command Description

As described in `point-accumulation`{.interpreted-text role="ref"}, the
first warning for a particular rule is considered to be a \"soft
warning\" and worth half points by default. This behavior can be
configured as follows:

-   **none**: Don\'t halve the points for any warnings.
-   **first**: Only halve the first warning a user receives
    (server-wide).
-   **first-with-points**: Only halve the first warning a user receives
    **excluding 0-points rules warnings** (server-wide).
-   **each**: Halve the first warning a user receives under each rule
    (default).

Using the command with no arguments will show the current settings for
the server.

#### Permissions Needed

| **User**: Manage Server

------------------------------------------------------------------------

### warnexpiry *(not implemented yet)*

#### Command Syntax

::: {.parsed-literal}
warnexpiry (\# of days)
:::

#### Command Description

Sets the number of days after which warnings will expire for a
particular server. Provide no arguments to reset to the default.

#### Permissions Needed

| **User**: Manage Server

------------------------------------------------------------------------

### expirypoints *(not implemented yet)*

#### Command Syntax

::: {.parsed-literal}
expirypoints (\# of points)
:::

#### Command Description

Sets the number of points a warning will decay to after they expire.
Provide no arguments to reset to the default.

Any warnings worth fewer points than the expirypoints value will not
decay.

#### Permissions Needed

| **User**: Manage Server

------------------------------------------------------------------------

### setthreshold *(not implemented yet)*

#### Command Syntax

::: {.parsed-literal}
setthreshold (\"mute\"/\"ban\"/\"absban\") (\# of points)
:::

#### Command Description

Sets the number of points at which a mute, ban, or \"absolute ban\" is
recommended. Integrity checks should ensure that mute points \< ban
points \< absolute ban points.

#### Permissions Needed

| **User**: Manage Server
