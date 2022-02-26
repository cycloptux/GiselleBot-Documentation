.. _moderation-module:

**************************
Server Moderation (Manual)
**************************

A special thanks to my friend and partner, NaviKing#3820, for the design of this module.

The purpose of this module is to warn users, track their infractions, and give the moderators the power to punish users accordingly.

In order to fully take advantage of this module, enabling the case/scoring system is suggested. The scoring system is enabled if the **Warning** log is enabled in a server channel. Please refer to the :ref:`log-command` section in the **Administration** module documentation.

....

Configuration Commands
======================

These configuration commands are only enabled for those with Manage Server permissions. The usage of these commands will be recorded in the **Moderation** log.

.. _moderation-role:

|bot_prefix|\ modrole
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ modrole [add/remove] [role id(s)/mention(s)/q_name(s)]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Adds or removes a role as a moderator role (Mod Role), enabling/disabling them to use the moderation module regardless of other permissions on their roles. Provide no arguments to show the current mod roles.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ modrole
    |bot_prefix|\ modrole add "Discord Moderators" "Discord Officers"
    |bot_prefix|\ modrole remove @Reddit Moderators

....

|bot_prefix|\ modimmunity
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ modimmunity
    
Command Description
^^^^^^^^^^^^^^^^^^^
Toggles whether or not users with the mod role can be affected by moderation commands. Default state: **off**.

If enabled, attempting to take moderation actions on a moderator will return an error.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

....

|bot_prefix|\ modanonymization
------------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ modanon
    
Command Description
^^^^^^^^^^^^^^^^^^^
Toggles whether or not users that are affected by a moderation action will also be informed of the identity of the moderator using the command. Default state: **off** (i.e. moderators **will not** be anonymized).

If enabled, the name of the moderator will be omitted on the DM that a user receives upon being hit by a moderation action, and a shield emoji (🛡️) will appear next to the "Performed By" field of the corresponding warning log embed to remind that moderators' protection is on for that case.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

....

|bot_prefix|\ modnotification
-----------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ modnotif
    
Command Description
^^^^^^^^^^^^^^^^^^^
Toggles whether or not moderators will be informed with a mention in the Moderation/Warning logger in case of missing parameters when applying a moderation action with an "incomplete" syntax. Default state: **on** (i.e. moderators **will** be notified with a mention).

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

....

|bot_prefix|\ muterole
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ muterole [role id/mention/q_name]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Defines a role to be used as the mute role. Attempting to set a mute role that is higher than either the command user's highest role or the bot's highest role will result in an error being thrown. Provide no arguments to show the current mute role.

Channel permissions for the mute role will be automatically set and updated every time the configuration or moderation command is used.

Muted users will have the following permissions disabled for every channel (besides the "mute chat", see below): **Send Messages**, **Attach Files**, **Add Reactions**, **Use Public Threads**, **Use Private Threads**, **Speak**.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server
| **Bot**: Manage Roles, Mute Members

....

|bot_prefix|\ mutechat
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ mutechat [channel id(s)/mention(s)/q_name(s)]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Sets one (or more) channel(s) for muted users to be able to speak for the purposes of discussing the moderation action taken against them.

When the bot sets channel permissions for the mute role, this special channel(s) will have the following permissions:

* **Read Messages**: Enabled
* **Send Messages**: Enabled
* **Read Message History**: Disabled
* **Add Reactions**: Disabled
* **Attach Files**: Enabled
* **Speak**: Disabled

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

....

|bot_prefix|\ imagebanrole
--------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ imagebanrole [role id/mention/q_name]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Defines a role to be used as the image ban role. Attempting to set a image ban role that is higher than either the command user's highest role or the bot's highest role will result in an error being thrown. Provide no arguments to show the current image ban role.

Channel permissions for the image ban role will be automatically set and updated every time the configuration or moderation command is used.

Image banned users will have the following permissions disabled for every channel: **Embed Links**, **Attach Files**.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server
| **Bot**: Manage Roles

....

|bot_prefix|\ channelbanrole
----------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ cbanrole [channel id/mention/q_name] [role id/mention/q_name]
    
Command Description
^^^^^^^^^^^^^^^^^^^
**For the specified channel**, defines a role to be used as the channel ban role. Attempting to set a channel ban role that is higher than either the command user's highest role or the bot's highest role will result in an error being thrown. Provide no arguments to show the current channel ban roles.

Channel permissions for the channel ban role will be automatically set and updated every time the configuration or moderation command is used.

Channel banned users will have the following permissions disabled for the specified channel: **Read Messages**, **View Channel**.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server
| **Bot**: Manage Roles

....

|bot_prefix|\ channelmuterole
-----------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ cmuterole [channel id/mention/q_name] [role id/mention/q_name]
    
Command Description
^^^^^^^^^^^^^^^^^^^
**For the specified channel**, defines a role to be used as the mute role. Attempting to set a mute role that is higher than either the command user's highest role or the bot's highest role will result in an error being thrown. Provide no arguments to show the current mute roles.

Channel permissions for the mute role will be automatically set and updated every time the configuration or moderation command is used.

Muted users will have the following permissions disabled for the specified channel: **Send Messages**, **Attach Files**, **Add Reactions**, **Use Public Threads**, **Use Private Threads**, **Speak**.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server
| **Bot**: Manage Roles, Mute Members

....

|bot_prefix|\ channelimagebanrole
---------------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ cimagebanrole [channel id/mention/q_name] [role id/mention/q_name]
    
Command Description
^^^^^^^^^^^^^^^^^^^
**For the specified channel**, defines a role to be used as the image ban role. Attempting to set a image ban role that is higher than either the command user's highest role or the bot's highest role will result in an error being thrown. Provide no arguments to show the current image ban roles.

Channel permissions for the image ban role will be automatically set and updated every time the configuration or moderation command is used.

Image banned users will have the following permissions disabled for the specified channel: **Embed Links**, **Attach Files**.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server
| **Bot**: Manage Roles

....

.. _moderation:

Moderation Commands
===================

These moderation commands are the actual commands that are used to apply moderation actions. Each one of the following commands will be very similar in nature, and thus the common features of the commands will be discussed together in this section, and the specifics of each command in subsections.

Collectively, these commands will be referred to as "warning commands".

The list of "warning commands" is the following:

* |bot_prefix|\ warn
* |bot_prefix|\ kick
* |bot_prefix|\ ban
* |bot_prefix|\ delayban
* |bot_prefix|\ mute
* |bot_prefix|\ imageban
* |bot_prefix|\ cban
* |bot_prefix|\ cmute
* |bot_prefix|\ cimageban

By default, warning commands will generate a new case if the **Warning** log is active. Upon generating a case, a DM will be sent to the target user(s), notifying them of the moderation action that has been triggered on them, who issued the moderation action and the specifics of the rules that are broken, if applicable. Please refer to the "Warning Point System" section below for more details about the rules system.

These commands support being used on multiple users at once: if more than one user is targeted by these commands, the parameters will be parallelized for all of the users, while multiple cases will be generated.

The following commands also support being set as "automatically expiring after X time":

* |bot_prefix|\ mute
* |bot_prefix|\ delayban
* |bot_prefix|\ imageban
* |bot_prefix|\ cban
* |bot_prefix|\ cmute
* |bot_prefix|\ cimageban

This is achieved by **prepending** the target users with a time code.

.. note::
    This time setting will overwrite the previous setting each time the command is run on a specified user: this also applies to converting a permanent action into a timed one and vice-versa, without removing the role on the target user.

(Common) Command Syntax
-----------------------
.. parsed-literal::

    |bot_prefix|\ {warning command} [duration timecode] [channel id/mention/q_name {only for channel-specific commands}] (user id(s)/mention(s)/q_name(s)) [--rule {rule id/name/alias}] [--reason {textual description}] [--attachments {urls}] [--padj {signed/unsigned number}] [--justification {textual justification}] [--skip-case] [--skip-dm]
    

(Common) Command Description
----------------------------

Informs the user(s) via DM that they have been warned/muted/banned/etc., including the rule that they broke, the specific reason, attachments, and who warned them. These arguments are all optional when running warning commands (only the user identifier is required). If applicable, the ``--reason`` parameter will appear in the Discord native audit log as well.

If all of these arguments are skipped, the message will simply read "You were warned/muted/banned by [moderator].".

Channel specific commands which are missing the channel parameter will default to being targeted to the current channel. Channels that support time-based expiration (see above) will be treated as permanent if the timecode is missing.

You can skip generating a case by appending the ``--skip-case`` tag. You can skip sending the DM (but still generate a case) by appending the ``--skip-dm`` tag. ``--skip-case`` also implies ``--skip-dm``.

.. note::
    When ``--skip-dm`` is used, a small 🔕 emoji will appear on the corresponding notification and warning log embed footer to track the fact that the action was "silent".

Every warning, by default, will be worth a certain number of points based on the rule broken (as described in the "Warning Point System" section below.

The ``--padj``, or "points added/subtracted" argument, is completely optional and will not be included in the DM even if it is included in the command. Any signed number ("+" or "-") will be treated as a "delta" value over the default rule score, while an unsigned number will be treated as a fixed, absolute value and used as the actual warning score. The justification for points added/subtracted is invalid if no points were added or subtracted and should be ignored if the moderator does not add or subtract any points.

Each one of the command parameters has one or more aliases. Here are the available aliases:

* ``--rule``: ``--r``
* ``--reason``: ``--rs``
* ``--attachments``: ``--attachment`` ``--att`` ``--a``
* ``--padj``: ``--pa`` ``--p``
* ``--justification``: ``--just`` ``--j``
* ``--skip-case``: ``--skipcase`` ``--nocase`` ``--no-case``
* ``--skip-dm``: ``--skipdm`` ``--nodm`` ``--no-dm``

Running the command as the "description" of a Discord attachment (e.g. by drag-and-dropping an image over the Discord client) will automatically add that object as the warning case attachment, even if the ``--attachments`` parameter is skipped.

As said above, these commands will automatically generate a server-specific case ID that can be used as reference in other commands. An embed including the following information will also be generated and put into the warning log:

* Warning Type (warn/mute/ban/etc.)
* Warned user's name
* Warned user's ID
* Mod Name
* Rule broken
* Reason
* Attachment (as embed's image, if applicable)
* Points added/subtracted (optional)
* Justification (only if points are added/subtracted)
* Total unexpired points as of warning for this user
* **Suggested moderation action & number of points to next warning threshold**
* Case ID & timestamp (in footer)

If any of the rule, reason or attachments parameters are missing, the bot will tag the moderator upon action log generation prompting them to fill in the missing arguments using the |bot_prefix|\ edit command. The bot will also tag the moderator the first time that the user reaches a suggested action threshold.

Some moderation action commands have a "un-" version that reverts the corresponding moderation action. "un-" commands will follow a similar syntax but will never generate a new case, hence rendering the set of warning parameters (every parameter after the user identifier(s)) useless.

What follows is a list of all of the commands in this section. As already said, each command description and syntax will be a diff over the common syntax shown here.

....

|bot_prefix|\ warn
------------------

Command Description
^^^^^^^^^^^^^^^^^^^

|bot_prefix|\ warn does nothing but DM the user(s) with their warning. Its purpose is to officially record an infraction so that the accumulation of infractions can later be used to justify a mute or a ban (see the "Warning Point System" described later).

Refer to :ref:`moderation` for the exact command syntax.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ warn @cycloptux#1543 --rule Discord ToS --reason The user is under 13 years of age --padj -2 --justification Testing the command
    
....    

|bot_prefix|\ kick
------------------

Command Description
^^^^^^^^^^^^^^^^^^^

Kicks the target user(s) from the current server. The user may be able to join the server again through a working invite.

Refer to :ref:`moderation` for the exact command syntax.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Kick Members
| **Bot**: Kick Members

....  

|bot_prefix|\ mute
------------------

Command Description
^^^^^^^^^^^^^^^^^^^

|bot_prefix|\ mute applies the role configured in |bot_prefix|\ muterole (or creates a default "Muted Users" role at the bottom of the role list with no permissions if the mute role is not configured) to the target user(s) and sets all channel permissions (except for the ones configured as mute chat(s)) for the mute role, as described in the previous sections.

The specific permissions for this command will be set (or checked/updated) every time the command is run, hence making the command slightly slower than usual. This is normal.

The mute can be permanent (users will be muted until manual removal) or timed (users will be unmuted automatically after a certain time span).

Refer to :ref:`moderation` for the exact command syntax.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Roles, Mute Members
| **Bot**: Manage Roles, Mute Members

....

|bot_prefix|\ ban
-----------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ ban [24/7] ...

Command Description
^^^^^^^^^^^^^^^^^^^

|bot_prefix|\ ban has one additional, optional argument before the user identifier(s): either the number 24, or the number 7. If this argument is omitted, the user is banned without their message history being deleted. Otherwise, the bot uses the native ban API to delete the last 24 hours or 7 days of the banned users' message history.

The same parameter can also be passed by using the ``--days`` argument (e.g. ``--days 1`` or ``--days 7``). ``--days`` also has the following aliases: ``--msgdays`` ``--delmsg`` ``--purge`` ``--d``

This command also works for banning users that are currently not in the server, as long as the user is known/cached by the bot. It is advised to use the user ID for that.

Refer to :ref:`moderation` for the exact command syntax.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Ban Members
| **Bot**: Ban Members

....

|bot_prefix|\ timeban
---------------------

Command Description
^^^^^^^^^^^^^^^^^^^

|bot_prefix|\ timeban bans a user from the current server for the specified amount of time.

Once the ban period has ended, as long as the user hasn't been permanently banned by "overwriting" the timed ban with a fully fledged |bot_prefix|\ ban (or manually re-allowed through |bot_prefix|\ unban), the ban will be automatically lifted. If the time argument is omitted, it will default to 24 hours.

Please allow for up to 1 extra minute before the ban is actually lifted after it has officially expired.

This command also works for banning users that are currently not in the server, as long as the user is known/cached by the bot. It is advised to use the user ID for that.

Refer to :ref:`moderation` for the exact command syntax.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Ban Members
| **Bot**: Ban Members

....

|bot_prefix|\ delayban
----------------------

Command Description
^^^^^^^^^^^^^^^^^^^

|bot_prefix|\ delayban mutes a user for the specified amount of time. If this mute status isn't removed with |bot_prefix|\ cancelban before the timer is out, the user will be banned from the server. If the time argument is omitted, it will default to 24 hours.

Refer to :ref:`moderation` for the exact command syntax.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Roles, Mute Members, Ban Members
| **Bot**: Manage Roles, Mute Members, Ban Members

....

|bot_prefix|\ imageban
----------------------

Command Description
^^^^^^^^^^^^^^^^^^^

|bot_prefix|\ imageban applies the role configured in |bot_prefix|\ imagebanrole (or creates a default "Image Banned Users" role at the bottom of the role list with no permissions if the image ban role is not configured) to the target user(s) and sets all channel permissions for the image ban role, as described in the previous sections.

The specific permissions for this command will be set (or checked/updated) every time the command is run, hence making the command slightly slower than usual. This is normal.

The image ban can be permanent (users will be image banned until manual removal) or timed (users will be image unbanned automatically after a certain time span).

Refer to :ref:`moderation` for the exact command syntax.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Roles
| **Bot**: Manage Roles

....

|bot_prefix|\ cban
------------------

Command Description
^^^^^^^^^^^^^^^^^^^

|bot_prefix|\ cban applies the role configured in |bot_prefix|\ channelbanrole (or creates a default "#%channel% Banned Users" role at the bottom of the role list with no permissions if the channel ban role is not configured) to the target user(s) and sets the channel permissions for the ban role, as described in the previous sections.

The specific permissions for this command will be set (or checked/updated) every time the command is run, hence making the command slightly slower than usual. This is normal.

The channel ban can be permanent (users will be channel banned until manual removal) or timed (users will be channel unbanned automatically after a certain time span).

Refer to :ref:`moderation` for the exact command syntax.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Roles
| **Bot**: Manage Roles

....

|bot_prefix|\ cmute
-------------------

Command Description
^^^^^^^^^^^^^^^^^^^

|bot_prefix|\ cmute applies the role configured in |bot_prefix|\ channelmuterole (or creates a default "#%channel% Muted Users" role at the bottom of the role list with no permissions if the channel mute role is not configured) to the target user(s) and sets the channel permissions for the mute role, as described in the previous sections.

The specific permissions for this command will be set (or checked/updated) every time the command is run, hence making the command slightly slower than usual. This is normal.

The channel mute can be permanent (users will be channel muted until manual removal) or timed (users will be channel unmuted automatically after a certain time span).

Refer to :ref:`moderation` for the exact command syntax.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Roles, Mute Members
| **Bot**: Manage Roles, Mute Members

....

|bot_prefix|\ cimageban
-----------------------

Command Description
^^^^^^^^^^^^^^^^^^^

|bot_prefix|\ cimageban applies the role configured in |bot_prefix|\ channelimagebanrole (or creates a default "#%channel% Image Banned Users" role at the bottom of the role list with no permissions if the channel image ban role is not configured) to the target user(s) and sets the channel permissions for the image ban role, as described in the previous sections.

The specific permissions for this command will be set (or checked/updated) every time the command is run, hence making the command slightly slower than usual. This is normal.

The channel image ban can be permanent (users will be channel image banned until manual removal) or timed (users will be channel image unbanned automatically after a certain time span).

Refer to :ref:`moderation` for the exact command syntax.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Roles
| **Bot**: Manage Roles

....

|bot_prefix|\ unmute
--------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ unmute (user id(s)/mention(s)/q_name(s))

Command Description
^^^^^^^^^^^^^^^^^^^

Lifts the mute role from the target user(s). 

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Roles, Mute Members
| **Bot**: Manage Roles, Mute Members

....

|bot_prefix|\ unban
-------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ unban (user id(s)/mention(s)/q_name(s))

Command Description
^^^^^^^^^^^^^^^^^^^

Lifts the ban status from the target user(s). 

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Ban Members
| **Bot**: Ban Members

....

|bot_prefix|\ cancelban
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ cancelban (user id(s)/mention(s)/q_name(s))

Command Description
^^^^^^^^^^^^^^^^^^^

Lifts the mute role from the target user(s), and cancels the corresponding timed ban. 

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Ban Members
| **Bot**: Ban Members

....

|bot_prefix|\ imageunban
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ imageunban (user id(s)/mention(s)/q_name(s))
    
Command Description
^^^^^^^^^^^^^^^^^^^

Lifts the image ban role from the target user(s). 

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Roles
| **Bot**: Manage Roles

....

|bot_prefix|\ cunmute
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ cunmute [channel id/mention/q_name] (user id(s)/mention(s)/q_name(s))

Command Description
^^^^^^^^^^^^^^^^^^^

Lifts the channel mute role from the target user(s). Omission of the channel identifier will result in the current channel being considered by the command.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Roles, Mute Members
| **Bot**: Manage Roles, Mute Members

....

|bot_prefix|\ cunban
--------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ cunban [channel id/mention/q_name] (user id(s)/mention(s)/q_name(s))

Command Description
^^^^^^^^^^^^^^^^^^^

Lifts the channel ban role from the target user(s). Omission of the channel identifier will result in the current channel being considered by the command.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Roles
| **Bot**: Manage Roles

....

|bot_prefix|\ cimageunban
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ cimageunban [channel id/mention/q_name] (user id(s)/mention(s)/q_name(s))

Command Description
^^^^^^^^^^^^^^^^^^^

Lifts the channel image ban role from the target user(s). Omission of the channel identifier will result in the current channel being considered by the command.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Roles
| **Bot**: Manage Roles

....

Utility Commands
================

These moderation commands may be used in conjunction with the rest of the moderation module to keep your server clean.

|bot_prefix|\ prune
-------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ prune (# of messages) [filter item] [--ignore {filter ignore}]

Command Description
^^^^^^^^^^^^^^^^^^^

Deletes a certain number of messages from the channel in which the command is run. For security reasons, the bot caps this number to **250** messages.

The filter items serve to delete/ignore a subset of messages in the set of messages specified by the integer argument. The list of available filters is:

* ``images``: deletes all images in the set of messages
* ``bots``: deletes all messages from bots in the set of messages
* ``links``: deletes all messages with links in the set of messages
* ``emojis``: deletes all messages with emojis in the set of messages
* ``reactions``: deletes all of the reactions off of the messages in the set of messages, **not the messages themselves**
* ``embeds``: deletes all embeds in the set of messages (this doesn't include embeds that are generated by links, see ``links`` for that)
* ``text``: deletes messages that only contain plain text in the set of messages
* ``invites``: deletes messages containing Discord invites in the set of messages
* ``mentions``: deletes messages containing a mention to a user, role, "@everyone" or "@here" in the set of messages
* ``{user mention}``: deletes messages sent by the specified user in the set of messages
* ``{any text string}``: deletes messages containing matching text from the supplied text string in the set of messages (for example, |bot_prefix|\ prune 100 "donald trump" would delete all messages containing "donald trump" in the last 100 messages)

You can add an ``--ignore`` tag, combined with the aforementioned filter items, to ignore (and not delete) messages meeting that criteria. For example "|bot_prefix|\ purge 100 bots --ignore embeds" would delete all bot messages that weren't embeds.


Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Messages
| **Bot**: Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ prune 100
    |bot_prefix|\ purge 250 bots
    |bot_prefix|\ clear 150 @cycloptux#1543 --ignore images

....

|bot_prefix|\ slowmode
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ slowmode [time code] [channel id(s)/mention(s)/q_name(s)] [--admode]

Command Description
^^^^^^^^^^^^^^^^^^^

Sets slow mode for the current, or the selected, channels. This command leverages 2 different systems:

* If the slow mode time code is within Discord's native slow mode time limit (less than 6 hours), the native slow mode is applied.
* If the slow mode time code exceeds Discord's native time limit (more than 6 hours, up to 1 year), the bot will apply an "extended slow mode" status.

The **extended slow mode** applies a minimal native slow mode to make sure the "Slowmode is enabled" message is shown. At the same time, each message sent by an unauthorized user will be automatically deleted, and the user will be notified of the applied slow mode.

The extended slow mode doesn't have a higher cap.

Using the command without any argument will show the current settings for the server. Using the command with **0** in place of the time code will disable the slow mode for the current, or the selected, channel(s).

The usage of the optional ``--admode`` parameter will enable the **Auto-Delete** mode, a.k.a. **Bump Mode**. If the **extended slow mode** is active (this mode will not work on native slow mode), each message that is **successfully** sent into the slowed channel will **also** trigger an automatic deletion of the previous message sent by the user while slow mode is active.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Messages
| **Bot**: Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ sm 1h45m #slow-channel
    |bot_prefix|\ sm 0 #slow-channel-1 #slow-channel-2
    |bot_prefix|\ slowmode

....

Evasion Actions
===============

In addition to the active behavior of the warning commands, the following commands also support a special "evasion" action log:

* |bot_prefix|\ mute
* |bot_prefix|\ imageban
* |bot_prefix|\ cban
* |bot_prefix|\ cmute
* |bot_prefix|\ cimageban

An "evasion" action happens when a user that is hit with one of these moderation actions leaves the server and rejoins while the corresponding role is still supposed to be up (either because the timed role still has to expire, or the role has been set as permanent by skipping the corresponding time code).

If still applicable, the role will be applied again as soon as the user rejoins the server and an "evasion" log will appear in the warning log.

....

Warning Point System
====================

To account for the nature and severity of various infractions, users will incur a certain number of points based on which rule they break. Moderators will be able to use their judgment to adjust the default value of an infraction by adding or subtracting points from the warning. At certain point thresholds, it is recommended that certain moderation actions (such as a mute or ban) be taken against the user.

This section will describe the details of the "default" warning point system backend as well as point out options or commands to configure parts of the system.

.. _point-accumulation:

Point Accumulation and Thresholds
---------------------------------

In addition to a user's total points being the sum of the points of their infractions, the following rules apply to points:

* Warning points expire after **90 days**, at which point the value of the infraction decreases to **1**.
* The first warning for a particular rule is considered to be a "soft warning" and worth half points (e.g., if a user broke the toxic attitudes rule and the NSFW rule, both infractions would be recorded at half points, but breaking the toxic attitudes rule twice would result in the second infraction being recorded at full points). This behavior can be configured with :ref:`half-logic`.
* Each case score can be manually adjusted (``--padj``) but it must always be >= 0. Validation rules are in place for a score not to be negative. Any adjustment that brings the score to a negative value will make the score account for 0.
* In order to preserve the severity of a banned user's warning history, points for banned users will not expire **while the user is banned**. Unbanning a user will make the points behave as usual again.

The following thresholds apply to the point total of a user. A user reaching one of these thresholds will cause the action log message related to that warning to include a tag of the issuing moderator informing him/her of the user reaching the threshold.

* 18 **unexpired** points: The bot will recommend in the action log that the user in question be muted.
* 27 **unexpired** points: The bot will recommend in the action log that the user in question be banned.
* 54 points **total, even if expired**: The bot will recommend in the action log that the user in question be banned. This is referred to as the "absolute ban threshold".
* *(not implemented yet)* **Three channel specific warnings**: The bot will recommend in the action log that the user be banned from that specific channel, regardless of the total point value. A user can simultaneously reach this threshold and the point thresholds, and the message in the action log should be constructed accordingly.

The justification for these thresholds are as follows:

* Rules are given point values based on a severity from 1 to 10.
* Since the first infraction is worth half points, only even numbers should be used for rule values.
* 6 is the average rule value.
* A "full warning" (i.e., one soft warning and one regular warning) would be 9 points on average.
* Two "full warnings" should result in a mute, and three should result in a ban.
* The absolute ban threshold is twice the ban threshold, a considerable feat even in one's lifetime of the server.

Default Rules and Points
------------------------

Ideally, users would configure their own rules and point values. However, there are definitely some rules that are common among servers and can be provided as a default hard-coded table. The default table is provided to use as a base:

+-------------------------------------------------------------------+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Rule Name                                                         | Rule Alias        | Rule Description                                                                                                                                                                                                                                                                                                                                                                                                                            | Rule Points |
+===================================================================+===================+=============================================================================================================================================================================================================================================================================================================================================================================================================================================+=============+
| No Toxic Attitudes                                                | Toxic Attitudes   | Treat everyone with respect and politeness on the server. Being disruptive, aggressive, disrespectful, creepy, or otherwise making a nuisance of yourself on the server or in your interactions with server members is strictly prohibited.                                                                                                                                                                                                 | 6           |
+-------------------------------------------------------------------+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| No Offensive Content, Hate Speech or Sensitive Material           | Offensive Content | All forms of discrimination and hate speech are strictly prohibited. This includes any slurs or discriminatory messages related to race, ethnicity, gender identity, sex, or other protected characteristics in Discord's Community Guidelines (https://discord.com/guidelines). Furthermore, please refrain from discussion of sensitive content such as politics, religion, acts of violence, and other serious topics.                   | 8           |
+-------------------------------------------------------------------+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| No Harassment                                                     | Harassment        | Repeated aggressive or passive-aggressive behavior against other members of the server to make them feel belittled or unwelcome is not tolerated.                                                                                                                                                                                                                                                                                           | 8           |
+-------------------------------------------------------------------+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Be Respectful to Moderators                                       | Arguing           | If a server staff member has warned you or otherwise asked you to stop doing something, please do not create drama about it in public channels. Derailing chat to complain about your warning or otherwise causing a scene will result in additional action. Abuse of methods to contact server staff team will also not be tolerated, and any attempts to evade punishments enacted by server staff may result in removal from the server. | 8           |
+-------------------------------------------------------------------+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Do Not Incite Others to Break The Rules                           | Incitement        | Encouraging conflict, or any type of rule-breaking is prohibited and will result in consequences both for those breaking the rules and those encouraging the situation.                                                                                                                                                                                                                                                                     | 10          |
+-------------------------------------------------------------------+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Do Not Spam the Server or its Members                             | Spam              | Please avoid sending repetitive messages and excessive images, links, emojis, or mentions on the server. Furthermore, sending malicious links or other types of scams on the server or in server member DMs is strictly prohibited and may result in removal from the server.                                                                                                                                                               | 8           |
+-------------------------------------------------------------------+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Do Not Share Other People's Personal Information                  | Personal Info     | Please do not share other people's personal information such as real names, addresses, other social media accounts, etc. without their permission. Sharing this with malicious intent may be construed as doxxing, which may result in removal from the server.                                                                                                                                                                             | 8           |
+-------------------------------------------------------------------+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| No Advertising                                                    | Advertising       | Please refrain from disruptive self-promotion and disruptive promotion of other Discord servers/social media, products, and services. This also applies to unsolicited direct messages of this nature to other server members.                                                                                                                                                                                                              | 6           |
+-------------------------------------------------------------------+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Follow Channel Rules                                              | Channel Rules     | Some channels may have channel-specific rules that add, modify, or exempt rules within a channel. Please read channel descriptions and pins, and comply with these channel-specific rules.                                                                                                                                                                                                                                                  | 6           |
+-------------------------------------------------------------------+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Do Not Violate The Game's Terms of Service                        | Game ToS          | Any violation of the game's terms of service is strictly prohibited and may result in removal from the server depending on the seriousness of the offense.                                                                                                                                                                                                                                                                                  | 54          |
+-------------------------------------------------------------------+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Do Not Violate Discord's Community Guidelines or Terms of Service | Discord ToS       | Please keep in mind that Discord itself has specific behavioral and content guidelines that you can read at https://discord.com/guidelines. Some of these violations may result in an instant ban. Of particular note are the following:                                                                                                                                                                                                    | 10          |
|                                                                   |                   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |             |
|                                                                   |                   | - You must be at least 13 years of age to use Discord                                                                                                                                                                                                                                                                                                                                                                                       |             |
|                                                                   |                   | - Sharing sexually explicit content of minors, both real and animated/drawn, is prohibited                                                                                                                                                                                                                                                                                                                                                  |             |
|                                                                   |                   | - Glorifying self harm or suicide                                                                                                                                                                                                                                                                                                                                                                                                           |             |
|                                                                   |                   | - Sharing pirated or illegally acquired content is prohibited                                                                                                                                                                                                                                                                                                                                                                               |             |
+-------------------------------------------------------------------+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| User Profile Must Meet Certain Criteria                           | User Profile      | All aspects of your user profile including (but not limited to) your profile picture and display name (i.e., your server nickname if you have one set, or your actual username if not) should be compliant with the rules of the server. Please avoid unreadable or disruptive names. Additionally, impersonating another user, staff member, or other public figure or organization is prohibited.                                         | 4           |
+-------------------------------------------------------------------+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| No NSFW or Gore Content                                           | NSFW              | NSFW (Not Safe For Work) content is prohibited, which includes text or media featuring excessive gore/extreme violence, content related to self harm or harming others, pornography or excessively sexual content. As with all rules, server staff may reserve the right to judge violations of this rule on a case by case basis.                                                                                                          | 8           |
+-------------------------------------------------------------------+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Please Speak English                                              | English           | The official language of the server is English. Please converse with others in this language on the server as this best enables everyone to understand each other.                                                                                                                                                                                                                                                                          | 4           |
+-------------------------------------------------------------------+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Informational Message                                             | None              | This message is informational only and does not progress you closer to a server ban.                                                                                                                                                                                                                                                                                                                                                        | 0           |
+-------------------------------------------------------------------+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+

....

Warning System Commands
=======================

This section will describe all those commands that are needed to use (and configure, to a certain extent) the warning system, as described in the previous section.

....

|bot_prefix|\ warnhistory
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ warnhistory (user id(s)/mention(s)/q_name(s))

Command Description
^^^^^^^^^^^^^^^^^^^

Shows the warning history of one (or more) user(s) in reverse chronological order. By default, this only includes a short summary for each warning. Warn histories longer than 2000 characters are paginated via reaction "buttons".

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ warnhistory 123456789098765432
    |bot_prefix|\ history @cycloptux#1543

....

|bot_prefix|\ case
------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ case (case id(s))

Command Description
^^^^^^^^^^^^^^^^^^^

Prints a detailed log embed for the selected case(s).

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ case 2
    |bot_prefix|\ case 12 15 34

....

|bot_prefix|\ edit
------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ edit (case id) [--rule {rule id/name/alias}] [--reason {textual description}] [--attachments {urls}] [--padj {signed/unsigned number}] [--justification {textual justification}] [--skip-dm]


Command Description
^^^^^^^^^^^^^^^^^^^

Edits an existing case. You cannot edit a case type (e.g. turning a warn into a mute). Only the original case owner (the issuing moderator) or a server administrator can edit a case.

Editing a case will generate a new warning log entry with the new details. The old entry will be edited with a clickable link that will bring you to the new edit.

Please refer to :ref:`moderation` for more details about the individual parameters and their aliases.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ edit 3 --reason Spamming phishing links in the #general channel --padj +4 --just For repeated spamming despite being warned about it

....

|bot_prefix|\ delete
--------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ delete (case id(s))

Command Description
^^^^^^^^^^^^^^^^^^^

Deletes one (or more) existing case(s). Deleted cases are never actually removed from the bot memory and can be restored in the future if you remember the case ID(s).

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ delete 3 4 10

....

|bot_prefix|\ restore
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ restore (case id(s))

Command Description
^^^^^^^^^^^^^^^^^^^

Restores one (or more) previously deleted case(s).

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ restore 3 4

....

.. _listrules:

|bot_prefix|\ listrules
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ listrules [rule id/name/alias] [--server] [--channel [channel id/mention/q_name]] [--mod]

Command Description
^^^^^^^^^^^^^^^^^^^

Lists the rules (both custom and default sets) of the server in order by Rule ID, including the Rule Title and Description for each rule. Provide an ID/Name/Alias to show a specific rule only. By default, the list will show both server wide and channel-specific rules. Use ``--server`` to limit the rules to the server wide ones. Use ``--channel`` with a channel tag to show only channel specific rules for that channel (omitting the channel identifier will show the rules for the current channel).

The rule alias and points will be shown if a moderator or administrator appends the ``--mod`` parameter to the command. 

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ listrules
    |bot_prefix|\ listrules --channel #general
    |bot_prefix|\ listrules NSFW --mod

....

|bot_prefix|\ addrule
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ addrule (--name {rule name}) (--alias {rule alias}) (--description {rule description}) (--points {rule points (number)}) [--channel [channel id/mention/q_name]]

Command Description
^^^^^^^^^^^^^^^^^^^

Adds a custom rule to the rules list. Adding a custom rule generates a server-specific rule ID for that rule automatically, starting from ``s_1``. Adding a channel identifier will assign that rule as being channel-specific (this is primarily used to track how close a user is to reaching a channel ban threshold)

.. note::
    Channel ban thresholds are not implemented yet.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

....

|bot_prefix|\ deleterule
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ delrule (rule(s) id/name/alias)

Command Description
^^^^^^^^^^^^^^^^^^^

Deletes a custom rule from the list of rules. Use |bot_prefix|\ toggleglobalrule to hide a default rule from the list of rules (see below).

.. note::
    In order to preserve the history of users that were previously moderated according to a specific rule, "deleted" rules are never actually deleted. "Deleted" rules are instead **hidden**, and running the |bot_prefix|\ deleterule again on the same rule ID will restore the rule in its previous, visible state.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

....

|bot_prefix|\ toggleglobalrule
------------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ toggleglobalrule (rule(s) id/name/alias)

Command Description
^^^^^^^^^^^^^^^^^^^

Deletes (hides) a default native rule from the list of rules. Use |bot_prefix|\ deleterule to hide a custom rule from the list of rules (see above).

.. note::
    In order to preserve the history of users that were previously moderated according to a specific rule, "deleted" rules are never actually deleted. "Deleted" rules are instead **hidden**, and running the |bot_prefix|\ toggleglobalrule again on the same rule ID will restore the rule in its previous, visible state.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

....

|bot_prefix|\ editrule
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ editrule (rule id/name/alias) [--name {rule name}] [--alias {rule alias}] [--description {rule description}] [--points {rule points (number)}] [--channel [-/channel id/mention/q_name]]

Command Description
^^^^^^^^^^^^^^^^^^^

Updates one or more fields of an existing rule to the new values.

Use ``--channel -`` to convert a channel-specific rule into a server wide rule.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

....

.. _half-logic:

|bot_prefix|\ halflogic
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ halflogic (none/first/first-with-points/each)

Command Description
^^^^^^^^^^^^^^^^^^^

As described in :ref:`point-accumulation`, the first warning for a particular rule is considered to be a "soft warning" and worth half points by default. This behavior can be configured as follows:

* **none**: Don't halve the points for any warnings.
* **first**: Only halve the first warning a user receives (server-wide).
* **first-with-points**: Only halve the first warning a user receives **excluding 0-points rules warnings** (server-wide).
* **each**: Halve the first warning a user receives under each rule (default).

Using the command with no arguments will show the current settings for the server.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

....

|bot_prefix|\ warnexpiry *(not implemented yet)*
------------------------------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ warnexpiry (# of days)

Command Description
^^^^^^^^^^^^^^^^^^^

Sets the number of days after which warnings will expire for a particular server. Provide no arguments to reset to the default.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

....

|bot_prefix|\ expirypoints *(not implemented yet)*
--------------------------------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ expirypoints (# of points)

Command Description
^^^^^^^^^^^^^^^^^^^

Sets the number of points a warning will decay to after they expire. Provide no arguments to reset to the default.

Any warnings worth fewer points than the |bot_prefix|\ expirypoints value will not decay.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

....

|bot_prefix|\ setthreshold *(not implemented yet)*
--------------------------------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ setthreshold ("mute"/"ban"/"absban") (# of points)

Command Description
^^^^^^^^^^^^^^^^^^^

Sets the number of points at which a mute, ban, or "absolute ban" is recommended. Integrity checks should ensure that mute points < ban points < absolute ban points.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server
