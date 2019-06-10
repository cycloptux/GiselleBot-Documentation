**********
Moderation
**********

A special thanks to my friend and partner, NaviKing#3820, for the design of this module.

The purpose of this module is to warn users, track their infractions, and give the moderators the power to punish users accordingly.

In order to fully take advantage of this module, enabling the case/scoring system is suggested. The scoring system is enabled if the **Warning** log is enabled in a server channel. Please refer to the :ref:`log-warning` section in the **Administration** module documentation.

....

Configuration Commands
======================

These configuration commands are only enabled for those with Administrator permissions. The usage of these commands will be recorded in the **Moderation** log.

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
| **User**: Administrator

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
| **User**: Administrator

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

Muted users will have the following permissions disabled for every channel (besides the "mute chat", see below): **Send Messages**, **Attach Files**, **Add Reactions**, **Speak**.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Administrator
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
| **User**: Administrator

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
| **User**: Administrator
| **Bot**: Manage Roles

....

|bot_prefix|\ channelbanrole
----------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ channelbanrole [channel id/mention/q_name] [role id/mention/q_name]
    
Command Description
^^^^^^^^^^^^^^^^^^^
**For the specified channel**, defines a role to be used as the channel ban role. Attempting to set a channel ban role that is higher than either the command user's highest role or the bot's highest role will result in an error being thrown. Provide no arguments to show the current channel ban roles.

Channel permissions for the channel ban role will be automatically set and updated every time the configuration or moderation command is used.

Channel banned users will have the following permissions disabled for the specified channel: **Read Messages**, **View Channel**.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Administrator
| **Bot**: Manage Roles

....

|bot_prefix|\ channelmuterole
-----------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ channelmuterole [channel id/mention/q_name] [role id/mention/q_name]
    
Command Description
^^^^^^^^^^^^^^^^^^^
**For the specified channel**, defines a role to be used as the mute role. Attempting to set a mute role that is higher than either the command user's highest role or the bot's highest role will result in an error being thrown. Provide no arguments to show the current mute roles.

Channel permissions for the mute role will be automatically set and updated every time the configuration or moderation command is used.

Muted users will have the following permissions disabled for the specified channel: **Send Messages**, **Attach Files**, **Add Reactions**, **Speak**.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Administrator
| **Bot**: Manage Roles, Mute Members

....

|bot_prefix|\ channelimagebanrole
---------------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ channelimagebanrole [channel id/mention/q_name] [role id/mention/q_name]
    
Command Description
^^^^^^^^^^^^^^^^^^^
**For the specified channel**, defines a role to be used as the image ban role. Attempting to set a image ban role that is higher than either the command user's highest role or the bot's highest role will result in an error being thrown. Provide no arguments to show the current image ban roles.

Channel permissions for the image ban role will be automatically set and updated every time the configuration or moderation command is used.

Image banned users will have the following permissions disabled for the specified channel: **Embed Links**, **Attach Files**.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Administrator
| **Bot**: Manage Roles

....

.. _moderation:

Moderation Commands
===================

These moderation commands are the actual commands that are used to apply moderation actions. Each one of the following commands will be very similar in nature, and thus the common features of the commands will be discussed together in this section, and the specifics of each command in subsections.

Collectively, these commands will be referred to as "warning commands".

The list of "warning commands" is the following:

* |bot_prefix|\ warn
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

This is achieved by **prepending** the target users with a time code. Please note that this time setting will overwrite the previous setting each time the command is run on a specified user: this also applies to converting a permanent action into a timed one and vice-versa, without removing the role on the target user.

(Common) Command Syntax
-----------------------
.. parsed-literal::

    |bot_prefix|\ {warning command} [duration timecode] [channel id/mention/q_name {only for channel-specific commands}] (user id(s)/mention(s)/q_name(s)) [--rule {rule id/name/alias}] [--reason {textual description}] [--attachment/--att {urls}] [--padj {signed/unsigned number}] [--just/--justification {textual justification}] [--skip-case] [--skip-dm]
    

(Common) Command Description
----------------------------

Informs the user(s) via DM that they have been warned/muted/banned/etc., including the rule that they broke, the specific reason, attachments, and who warned them. These arguments are all optional when running warning commands (only the user identifier is required). If applicable, the ``--reason`` parameter will appear in the Discord native audit log as well.

If all of these arguments are skipped, the message will simply read "You were warned/muted/banned by [moderator].".

Channel specific commands which are missing the channel parameter will default to being targeted to the current channel. Channels that support time-based expiration (see above) will be treated as permanent if the timecode is missing.

You can skip generating a case by appending the ``--skip-case`` tag. You can skip sending the DM (but still generate a case) by appending the ``--skip-dm`` tag.

Every warning, by default, will be worth a certain number of points based on the rule broken (as described in the "Warning Point System" section below.

The ``--padj``, or "points added/subtracted" argument, is completely optional and will not be included in the DM even if it is included in the command. Any signed number ("+" or "-") will be treated as a "delta" value over the default rule score, while an unsigned number will be treated as a fixed, absolute value and used as the actual warning score. The justification for points added/subtracted is invalid if no points were added or subtracted and should be ignored if the moderator does not add or subtract any points.

Running the command as the "description" of a Discord attachment (e.g. by drag-and-dropping an image over the Discord client) will automatically add that object as the warning case attachment, even if the ``--attachment`` parameter is skipped.

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

Each command has a "un-" version that reverts the active warning command. "un-" commands will follow a similar syntax but will never generate a new case, hence rendering the set of warning parameters (every parameter after the user identifier(s)) useless.

What follows is a list of all of the commands in this section. As already said, each command description and syntax will be a diff over the common syntax shown here.

....

|bot_prefix|\ warn
------------------

Command Description
^^^^^^^^^^^^^^^^^^^

|bot_prefix|\ warn does nothing but DM the user(s) with their warning. Its purpose is to officially record an infraction so that the accumulation of infractions can later be used to justify a mute or a ban (see the "Warning Point System" described later).

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ warn @cycloptux#1543 --rule Discord ToS --reason The user is under 13 years of age --padj -2 --justification Testing the command
    
....    

|bot_prefix|\ mute
------------------

Command Description
^^^^^^^^^^^^^^^^^^^

|bot_prefix|\ mute applies the role configured in |bot_prefix|\ muterole (or creates a default "Muted Users" role at the bottom of the role list with no permissions if the mute role is not configured) to the target user(s) and sets all channel permissions (except for the ones configured as mute chat(s)) for the mute role, as described in the previous sections.

The specific permissions for this command will be set (or checked/updated) every time the command is run, hence making the command slightly slower than usual. This is normal.

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

This also works banning users that are currently not in the server. It is advised to use the user ID for that.

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
| **User**: Manage Roles
| **Bot**: Manage Roles

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

|bot_prefix|\ kick
------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ kick (user id(s)/mention(s)/q_name(s)) [--reason {textual description}] 

Command Description
^^^^^^^^^^^^^^^^^^^

Kicks the target user(s) from the current server. The ``--reason`` tag is used to specify a reason that will appear in the native Discord audit log.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Kick Members
| **Bot**: Kick Members

....

|bot_prefix|\ prune
-------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ prune (# of messages) [filter item] [--ignore {filter ignore}] [--force]

Command Description
^^^^^^^^^^^^^^^^^^^

Deletes a certain number of messages from the channel in which the command is run. For security reasons, the bot caps this number to **500** messages. If you need to delete more than 500, you can append ``--force`` to remove the cap.

**BEWARE**: There isn't a higher cap. This command could potentially nuke a whole channel if ``--force`` is used. For this reason, the usage of the ``--force`` parameter is restricted to those with **Administrator** permissions.

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
    |bot_prefix|\ purge 500 bots
    |bot_prefix|\ clear 2500 @cycloptux#1543 --ignore images

....

|bot_prefix|\ slowmode
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ slowmode [time code] [channel id(s)/mention(s)/q_name(s)]

Command Description
^^^^^^^^^^^^^^^^^^^

Sets slow mode for the current, or the selected, channels. This command leverages 2 different systems:

* If the slow mode time code is within Discord's native slow mode time limit, the native slow mode is applied.
* If the slow mode time code exceeds Discord's native time limit, the bot will apply an "extended slow mode" status.

The **extended slow mode** applies a minimal native slow mode to make sure the "Slowmode is enabled" message is shown. At the same time, each message sent by an unauthorized user will be automatically deleted, and the user will be notified of the applied slow mode.

The extended slow mode doesn't have a higher cap.

Using the command without any argument will show the current settings for the server. Using the command with **0** in place of the time code will disable the slow mode for the current, or the selected, channel(s).

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

+---------------------------------------------------------+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Rule Name                                               | Rule Alias        | Rule Description                                                                                                                                                                                                                                                                                                                                                                                                     | Rule Points |
+=========================================================+===================+======================================================================================================================================================================================================================================================================================================================================================================================================================+=============+
| No Toxic Attitudes                                      | Toxic Attitudes   | Please behave and do not make a nuisance of yourself on the server, including "trolling" or otherwise being disruptive or making others feel uncomfortable.                                                                                                                                                                                                                                                          | 6           |
+---------------------------------------------------------+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| No Offensive Content, Hate Speech or Sensitive Material | Offensive Content | Please refrain from posting offensive content such as politics, religion, acts of violence, rape, suicide, school shootings, and other serious topics. Also keep in mind that hate speech including racial slurs or derivatives thereof, sexist or homophobic statements, and other similar types of behavior is not tolerated on this server.                                                                       | 8           |
+---------------------------------------------------------+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| No Harassment                                           | Harassment        | This applies both to DMs and public chat channels, and includes insults or other actions that target a specific user in order to make them feel uncomfortable or unwelcome.                                                                                                                                                                                                                                          | 8           |
+---------------------------------------------------------+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Be Respectful to Moderators                             | Arguing           | While measured discussion and questions regarding why you were warned for something is fine, attacking the moderators or becoming belligerent over being warned will likely result in another warning. You are welcome to provide feedback in the relevant channels on the Discord server if your concern is general, or you may DM a moderator or administrator regarding your warning if your concern is specific. | 8           |
+---------------------------------------------------------+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Do Not Incite Others to Break The Rules                 | Incitement        | Encouraging the breaking of rules, inciting others to be blatantly rude and offensive, or otherwise promoting and/or encouraging conflicts between other members will result in punitive measures for both rulebreakers and those encouraging rule breaking.                                                                                                                                                         | 10          |
+---------------------------------------------------------+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Do Not Spam the Server or its Members                   | Spam              | Spam is a broad term used to define unsolicited or repetitious messages received electronically. Spamming is prohibited on this server and in DMs to server members. This includes image spam, text/link/emoji spam, and tag spam.                                                                                                                                                                                   | 8           |
+---------------------------------------------------------+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Do Not Share Other People’s Personal Information        | Personal Info     | Please do not share other people’s personal information such as real names, addresses, other social media accounts, etc. without their permission. Sharing this with malicious intent may be construed as doxxing, which will result in an instant ban.                                                                                                                                                              | 8           |
+---------------------------------------------------------+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| No Advertising                                          | Advertising       | Advertisement of other discord servers, giveaways, unofficial tournaments, or one’s own social media/content creation channels is prohibited without approval from a Discord Moderator. This includes advertisement in group channels as well as in Direct Messages (DMs) to server members.                                                                                                                         | 6           |
+---------------------------------------------------------+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Follow Channel Rules                                    | Channel Rules     | Please remember to read channel descriptions and pins, and comply with channel specific rules.                                                                                                                                                                                                                                                                                                                       | 6           |
+---------------------------------------------------------+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Violating Game ToS                                      | Game ToS          | Violation of the game’s terms of service, especially hacking or modding the game, will result in an instant ban from the Discord server and possibly within the game as well.                                                                                                                                                                                                                                        | 54          |
+---------------------------------------------------------+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Violating Discord ToS                                   | Discord ToS       | Please keep in mind that Discord itself has specific behavioral and content guidelines that you can read at https://discordapp.com/guidelines. Some of these violations may result in an instant ban. Of particular note are the following:                                                                                                                                                                          | 10          |
|                                                         |                   |                                                                                                                                                                                                                                                                                                                                                                                                                      |             |
|                                                         |                   | - You must be at least 13 years of age to use Discord                                                                                                                                                                                                                                                                                                                                                                |             |
|                                                         |                   | - Sharing sexually explicit content of minors, both real and animated/drawn, is prohibited                                                                                                                                                                                                                                                                                                                           |             |
|                                                         |                   | - Glorifying self harm or suicide                                                                                                                                                                                                                                                                                                                                                                                    |             |
|                                                         |                   | - Sharing pirated or illegally acquired content is prohibited                                                                                                                                                                                                                                                                                                                                                        |             |
+---------------------------------------------------------+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| User Profile Must Meet Certain Criteria                 | User Profile      | Your profile picture and display name (i.e., your server nickname if you have one set, or your actual username if not) should be compliant with the rules of the server. In addition, your display name must not imitate another user and meet the following criteria:                                                                                                                                               | 4           |
|                                                         |                   |                                                                                                                                                                                                                                                                                                                                                                                                                      |             |
|                                                         |                   | - Easily taggable/readable                                                                                                                                                                                                                                                                                                                                                                                           |             |
|                                                         |                   | - Contains no inappropriate content                                                                                                                                                                                                                                                                                                                                                                                  |             |
|                                                         |                   | - Does not deliberately hoist you to the top of the online list                                                                                                                                                                                                                                                                                                                                                      |             |
+---------------------------------------------------------+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| No NSFW Content                                         | NSFW              | Dissemination of NSFW content in any form is prohibited in all chats and includes excessive gore/extreme violence, content related to self harm or harming others, pornography or excessively sexual content. Any in game art is exempt from this rule unless otherwise noted.This rule applies to both images and text, although some leniency will be allowed for text content.                                    | 8           |
+---------------------------------------------------------+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+

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

    |bot_prefix|\ edit (case id) [--rule {rule id/name/alias}] [--reason {textual description}] [--attachment/--att {urls}] [--padj {signed/unsigned number}] [--just/--justification {textual justification}]

Command Description
^^^^^^^^^^^^^^^^^^^

Edits an existing case. You cannot edit a case type (e.g. turning a warn into a mute). Only the original case owner (the issuing moderator) or a server administrator can edit a case.

Editing a case will generate a new warning log entry with the new details. The old entry will be edited with a clickable link that will bring you to the new edit.

Please refer to :ref:`moderation` for more details about the individual parameters. Please also note that editing a case won't send a new DM to the target user, nor generate a new case ID.

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
| **User**: Administrator

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
| **User**: Administrator

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ restore 3 4

....

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

Adds a custom rule to the rules list. Adding a custom rule generates a server-specific rule ID for that rule automatically, starting from ``s_1``. Adding a channel identifier will assign that rule as being channel-specific (this is primarily used to track how close a user is to reaching a channel ban threshold, *please note that channel ban thresholds are not implemented yet*).

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Administrator

....

|bot_prefix|\ deleterule
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ delrule (rule id/name/alias)

Command Description
^^^^^^^^^^^^^^^^^^^

Deletes a custom rule from the list of rules. Use |bot_prefix|\ toggleglobalrule to hide a default rule from the list of rules (see below).

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Administrator

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
| **User**: Administrator

....

.. _half-logic:

|bot_prefix|\ halflogic
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ halflogic (none/first/each)

Command Description
^^^^^^^^^^^^^^^^^^^

As described in :ref:`point-accumulation`, the first warning for a particular rule is considered to be a "soft warning" and worth half points by default. This behavior can be configured as follows:

* **none**: Don't halve the points for any warnings.
* **first**: Only halve the first warning a user receives (server-wide).
* **each**: Halve the first warning a user receives under each rule (default).

Using the command with no arguments will show the current settings for the server.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Administrator

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
| **User**: Administrator

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

Any warnings worth fewer points than the !expirypoints value will not decay.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Administrator

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
| **User**: Administrator

....

Auto Moderation
===============

An auto moderation feature is available. The current auto moderator currently supports **4** triggers (messages or actions performed by users) and **5** actions (actions performed on the offending user and/or message). Each trigger can be configured with an extra whitelist, as described below.

By default, administrators and moderators (refer to :ref:`moderation-role`) are immune to auto moderation triggers.

**Supported triggers**

* **Server Invites**: recognizes Discord server invites in user messages; this trigger supports **shortened** URLs (e.g. Discord invites hidden behind a bit.ly shortening service), and ignores invites pointing to the current server.
* **Mass Mention**: counts the number of mentions (roles, users or everyone/here) in a message and triggers if the number of mentions is over a threshold. The default threshold is **10**, but can be configured in each server.
* **Banned Words**: checks the message against a list of words, configured by the user, and triggers if one or more words are found within the message. Punctuation and letter case are ignored. The parser can be configured to trigger on an "exact match" (e.g. banned word: ``test``, matching word: ``test``), if the banned word is found at the "beginning of a word" within the message (e.g. banned word: ``test``, matching word: ``testing``), or "anywhere in word" (e.g. banned word: ``test``, matching word: ``attestation``).
* **Anti-Spam**: counts the number of messages **with the same content** sent by a user within a certain span of time and triggers if the number of identical message is over a threshold. The default threshold is **3** messages in **10** seconds, but can be configured in each server. Please note that Discord lag can cause false positives.

**Supported actions**

* **Automatic deletion of the offending message**.
* **Auto-warn**: Automatically apply a generic warning on the offending user. Specify a rule with the dedicated option.
* **Auto-mute**: Automatically mute the offending user. The applied mute is a temporary, 2 hours long, mute.
* **Auto-kick**: Automatically kick the offending user.
* **Auto-ban**: Automatically ban the offending user.


**Whitelisting options**

* **Users**: Ignore messages/actions performed by specific users in a server.
* **Roles**: Ignore messages/actions performed by specific roles in a server.
* **Channels**: Ignore messages sent in specific channels in a server.
* **Servers (Server Invites only)**: Ignore Discord server invites pointing to a specific server. You need to use the server ID to add this kind of whitelisting option. Applying this whitelist rule enables instant, temporary or permanent invites (including vanity URLs) for one or more server(s).

**Extra options**

* **Moderators alerting**: 
* **Moderation rule**: 

....

|bot_prefix|\ automodsetup
--------------------------

Command Description
^^^^^^^^^^^^^^^^^^^

Opens the auto moderation setup menu. Use the menu items to configure the above settings. Please note that not all of the settings will have a meaning in all of the triggers.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ amset

