**********
Moderation
**********

A special thanks to my friend, NaviKing#3820, for the design of this module.

The purpose of this module is to warn users, track their infractions, and give the moderators the power to punish users accordingly.

In order to fully take advantage of this module, enabling the case/scoring system is suggested. The scoring system is enabled if the **Warning** log is enabled in a server channel. Please refer to the :ref:`log-warning` section in the **Administration** module documentation.

....

Configuration Commands
======================

These configuration commands are only enabled for those with Administrator permissions. The usage of these commands will be recorded in the **Moderation** log.

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

Moderation Commands
===================

These moderation commands are the actual commands that are used to apply moderation actions. Each one of the following commands will be very similar in nature, and thus the common features of the commands will be discussed together in this section, and the specifics of each command in subsections.

Collectively, these commands will be referred to as "warning commands".

The list of "warning commands" is the following:

* |bot_prefix|\ warn
* |bot_prefix|\ ban
* |bot_prefix|\ mute
* |bot_prefix|\ imageban
* |bot_prefix|\ cban
* |bot_prefix|\ cmute
* |bot_prefix|\ cimageban

By default, warning commands will generate a new case if the **Warning** log is active. Upon generating a case, a DM will be sent to the target user(s), notifying them of the moderation action that has been triggered on them, who issued the moderation action and the specifics of the rules that are broken, if applicable. Please refer to the "Warning Point System" section below for more details about the rules system.

These commands support being used on multiple users at once: if more than one user is targeted by these commands, the parameters will be parallelized for all of the users, while multiple cases will be generated.

The following commands also support being set as "automatically expiring after X time":

* |bot_prefix|\ mute
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