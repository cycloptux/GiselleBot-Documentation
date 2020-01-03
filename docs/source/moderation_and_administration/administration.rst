.. _administration:

*********************
Server Administration
*********************

The Administration module contains tools used to manage a Discord server and its members.

.. seealso::
    NaviKing#3820 wrote a very good guide about a few real use cases of using the administration module. You can find it here: :ref:`guide-administration`

....

Bot Prefix
==========

.. _prefix:

|bot_prefix|\ prefix
--------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ prefix [new prefix]

Command Description
^^^^^^^^^^^^^^^^^^^
Sets the bot prefix for all bot commands within the current server.

Using the command without any argument will show the current prefix.

.. warning::
    The prefix cannot contain spaces. If spaces are used, only the first "word" will be considered.

.. note::
    Generally speaking, there will never be a space in between the prefix and the command itself.
    A common prefix being used is a mention of the bot. If the bot mention is used, a space will be automatically added after the mention. This only applies if the bot mention is used, while any other mention will be considered as a normal character string.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ prefix
    |bot_prefix|\ prefix b?
    
....

.. _log-command:

Server Activity Logging
=======================

|bot_prefix|\ log
-----------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal:: 
    
    |bot_prefix|\ log [type(s)]

Command Description
^^^^^^^^^^^^^^^^^^^
Toggles one or more logger types in the current channel. Available loggers are:

* **Members**: User joined/left the server.
* **Users**: Username change, nickname change, avatar change.
* **Roles**: Role added to user, role removed from user, role created, role edited, role deleted.
* **Channels**: Channel created, channel edited\*, channel deleted.
* **Server**: Server info updated*, emoji created, emoji deleted, emoji updated.
* **Messages**: Message deleted, message edited, message pinned, message unpinned.
* **Voice**: User connected to/disconnected from/switched voice channel.
* **Moderation**: Auto-moderation actions, administrators/moderators using a sensitive command, user struck by a moderation action (warn/kick/ban/mute/...), user evaded from a moderation action\*\*.
* **Warning**: This one is a more verbose version the moderation log, focused on moderation actions. Activating this logger enables the case/scoring system.
* **ALL**: Activates all available loggers in the current channel.

You can also print the list of available loggers within Discord by using |bot_prefix|\ log without any additional argument.

.. admonition:: Premium

    The **Members**, **Messages**, **Roles**, **Channels**, **Moderation** and **Warning** loggers are publicly available. If you want to enable **Users**, **Server** and **Voice** loggers, you can unlock them as a **Premium** feature (see: :ref:`premium-perks`).

| :sub:`\*: Due to the high amount of info that can be edited, these commands are limited to monitoring the main parameters.`
| :sub:`\*\*: Evasion is intended as leaving and re-joining a server while a permanent or time-based mute/ban action is taken on the user, in an attempt to clear the moderation roles. The roles will be reapplied and the administrators/moderators will be notified.`

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ log members
    |bot_prefix|\ log voice messages
    |bot_prefix|\ log ALL

....

|bot_prefix|\ logignore
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ logignore (logger type) [entity id/mention/q_name]

Command Description
^^^^^^^^^^^^^^^^^^^

.. admonition:: Premium

    This feature is only available to **Premium**-enabled servers (see: :ref:`premium-perks`).

Add a filter to skip logging certain events. Any action that comes from a user/channel/role that is added to the filter won't generate a logging entry. Please refer to the list below for a list of supported filters:

* **Members**: Users.
* **Users**: Users.
* **Roles**: Roles.
* **Channels**: Channels.
* **Server**: *N/A*.
* **Messages**: Users, Channels.
* **Voice**: Users, Channels.
* **Moderation**: Users.
* **Warning**: Users.

You can also print the list of currently set filters by using |bot_prefix|\ logignore (logger type) without any additional argument.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ logignore members @cycloptux#1543
    |bot_prefix|\ logignore channels #admin-chat
    
....

|bot_prefix|\ logmatt
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ logmatt

Command Description
^^^^^^^^^^^^^^^^^^^
Toggles message attachments logging on deleted messages.

By default, deleting a message that contains an image as attachment will trigger an automatic reupload of said image into the Messages logging channel. If you don't want images to be saved, you can turn this feature off. Use the same command again to re-enable this feature.

....

New Members Management
======================

|bot_prefix|\ greet
-------------------

Command Description
^^^^^^^^^^^^^^^^^^^
Toggles announcements on the current channel when someone joins the server.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

....

|bot_prefix|\ greetdm
---------------------

Command Description
^^^^^^^^^^^^^^^^^^^
Toggles announcements via Direct Message when someone joins the server (this is separate from greet - you can have both, any or neither enabled).

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

....

|bot_prefix|\ greetmsg
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetmsg [message]

Command Description
^^^^^^^^^^^^^^^^^^^
Sets a new join announcement message which will be shown in the server's channel. Using it with no message will show the current greet message.

You can use one (or more) of these placeholders in your message:

* **%user%**: This will be replaced with a mention of the user.
* **%server%**: This will be replaced with the server name.
* **%now%**: This will be replaced with the current time, with format ``YYYY-MM-DD HH:mm:ss (UTC)``.
* **%server\_time%**: This will be replaced with the current time, with format ``HH:mm UTC``.

You can use embed json from https://eb.nadeko.bot/ instead of a regular text, if you want the message to be embedded.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetmsg Welcome, %user%.

....

|bot_prefix|\ greetdmmsg
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetdmmsg [message]

Command Description
^^^^^^^^^^^^^^^^^^^
Sets a new join announcement message which will be sent to the user who joined. Using it with no message will show the current DM greet message.

You can use one (or more) of these placeholders in your message:

* **%user%**: This will be replaced with a mention of the user.
* **%server%**: This will be replaced with the server name.
* **%now%**: This will be replaced with the current time, with format ``YYYY-MM-DD HH:mm:ss (UTC)``.
* **%server\_time%**: This will be replaced with the current time, with format ``HH:mm UTC``.

You can use embed json from https://eb.nadeko.bot/ instead of a regular text, if you want the message to be embedded.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetdmmsg Welcome to %server%, %user%.

....

|bot_prefix|\ greetdel
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetdel (seconds)

Command Description
^^^^^^^^^^^^^^^^^^^
Sets the time it takes (in seconds) for **in-server** greet messages to be auto-deleted. Set it to 0 to disable automatic deletion. The maximum time you can set is 1800 (30 minutes).

.. note::
    This does not apply to DM greet messages.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetdel 0
    |bot_prefix|\ greetdel 30

....

Automated Roles Assignment/Removal
==================================

|bot_prefix|\ autoassignrole
----------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ autoassignrole [role id(s)/mention(s)/q_name(s)]

Command Description
^^^^^^^^^^^^^^^^^^^
Automaticaly assigns one or more specified roles to every user who joins the server.

Providing one or more role identifiers will toggle whether or not users will receive that role upon joining the server, for each role.

.. note::
    In other words, after activating a role, use the same command on that role to disable the auto assignment on join.

Provide no parameters to show the current settings.

Permissions Needed
^^^^^^^^^^^^^^^^^^

| **User**: Manage Roles
| **Bot**: Manage Roles

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ aar
    |bot_prefix|\ aar RoleName1 RoleName2
    
....

|bot_prefix|\ autoremoverole
----------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ arr [time code] [role id(s)/mention(s)/q_name(s)]

Command Description
^^^^^^^^^^^^^^^^^^^
Automaticaly removes one or more specified roles from any user after the specified amount of time, no matter how that role was gained.

Providing one or more role identifiers **and a time code** will set the expiration time of those roles.

Providing one or more role identifiers **without a time code** will disable the expiration of those roles.

Provide no parameters to show the current settings.

Permissions Needed
^^^^^^^^^^^^^^^^^^

| **User**: Manage Roles
| **Bot**: Manage Roles

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ arr
    |bot_prefix|\ arr 1h RoleName1 RoleName2
    |bot_prefix|\ arr RoleName2
    
....

|bot_prefix|\ vcrole
--------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ vcrole [role id/mention/q_name]

Command Description
^^^^^^^^^^^^^^^^^^^
Automaticaly assigns a role to users who join the voice channel you're in when you run this command. Provide no role identifier to disable.

Provide no parameters to disable this feature.

.. warning::
    You must be in a voice channel to run this command.

Permissions Needed
^^^^^^^^^^^^^^^^^^

| **User**: Manage Roles
| **Bot**: Manage Roles

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ vcrole
    |bot_prefix|\ vcrole VoiceRoleName
    
....

|bot_prefix|\ vcrolelist
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ vcrolelist

Command Description
^^^^^^^^^^^^^^^^^^^
Shows a list of currently set voice channel roles.
    
....
    
.. _self-assignable-roles:

Self-assignable Roles
=====================

**IMPORTANT NOTE**: The bot will be able to assign a role only if it has both "Manage Roles" permissions **AND** if the role it's trying to assign is **lower** than the highest role the bot has. Please arrange your roles accordingly.

Before we delve into the actual self-assignable roles, it's very important that you become familiar with **role groups**.

A role group is a group of Discord roles that will share the same set of assignment rules.

Each role group can be configured by editing the following settings:

* **Name**: Custom name for the group.
* **Mode**: Given a group of Discord roles, the assignment mode defines how roles will be assigned to users:

  * **Single Mode**: Users can only have 1 role within this group.
  * **Multiple Mode**: Users can have a minimum and a maximum number of roles within this group.
  * **None**: No specific rules are applied. Required and ignored roles (see below) still apply.
  
* **Required Roles**: This setting requires users to have **at least one** of the specified roles to be able to self-assign one role within this group.
* **Ignored Roles**: This setting requires users **not** to have **any** of the specified roles to be able to self-assign one role within this group. Or, in other words, users with at least one of the specified roles won't have access to this group.

In **Single** or **Multiple** mode, you'll also have access to additional, optional settings:

**Single Mode Settings**

* **Require 1 role in group at all times (after initial assignment)**: Whether the role is assigned by a 3rd party or self-assigned, users won't be able to self-remove **all** of the roles in the group.
* **Remove existing role when assigning another role in group**: Self-assigning a role within this group will remove any other group role from the user.

**Multiple Mode Settings**

* **Minimum number of roles**: Users won't be able to self-remove a role if the removal would bring them under this threshold of group roles.
* **Maximum number of roles**: Users won't be able to self-assign a role if the assignment would bring them over this threshold of group roles.

.. warning::
    **One role can be assigned to more than one group**. While technically possible, this is generally not recommended unless you know what you are doing. In such cases, you must design your settings to avoid conflicts between the different group settings. **Conflicting settings will cause unpredictable behaviors**.

Once a role group is configured, two ways of self-assigning a group will be available to users:

* **Role Menus**: Interactive menus using Discord emoji reactions to assign and remove roles. Role menus can be created from scratch using bot commands (see below) or "attached" to an existing user message.
* **Manual Commands**: The |bot_prefix|\ iam and |bot_prefix|\ iamnot commands will **always** be available to anyone. Specific permissions will need to be handled by using the "Required Roles" and "Ignored Roles" settings.

Here's the full list of available commands for this sub-module:

|bot_prefix|\ sargs
-------------------

Command Description
^^^^^^^^^^^^^^^^^^^
Opens the self-assignable roles (i.e. role groups) interactive setup menu. Use the menu items to configure the above settings.

.. note::
    Mode-specific settings will only work if the corresponding mode is currently set as active.

....

|bot_prefix|\ asar
------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal:: 
    
    |bot_prefix|\ asar [group id] (role id(s)/mention(s)/q_name(s))

Command Description
^^^^^^^^^^^^^^^^^^^
Adds one or more roles to the specified group. If the group ID is omitted, group **0** will be used as target role group.

Permissions Needed
^^^^^^^^^^^^^^^^^^

| **User**: Manage Roles
| **Bot**: Manage Roles

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ asar "Group 1"
    |bot_prefix|\ asar 2 @Testing123
    |bot_prefix|\ asar 12 123456789098765432 

....

|bot_prefix|\ rsar
------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal:: 
    
    |bot_prefix|\ rsar [group id] (role id(s)/mention(s)/q_name(s))

Command Description
^^^^^^^^^^^^^^^^^^^
Removes one or more roles from the specified group. If the group ID is omitted, the role(s) will be removed from **all** role groups.

Permissions Needed
^^^^^^^^^^^^^^^^^^

| **User**: Manage Roles
| **Bot**: Manage Roles

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rsar "Group 1"
    |bot_prefix|\ rsar 2 @Testing123
    |bot_prefix|\ rsar 12 123456789098765432 

....

.. _lsar:

|bot_prefix|\ lsar
------------------

Command Description
^^^^^^^^^^^^^^^^^^^
Prints a list of all role groups and the relative self-assignable groups.

.. note::
    This command is always available to everyone.

....

|bot_prefix|\ adsarm
--------------------

Command Description
^^^^^^^^^^^^^^^^^^^
Toggles the automatic deletion of the "public" self-assignable roles-related messages upon using the |bot_prefix|\ iam and |bot_prefix|\ iamnot commands.

Only successful messages will be deleted.

The user-sent message will be deleted immediately. The confirmation message will be deleted after 5 seconds.

Permissions Needed
^^^^^^^^^^^^^^^^^^

| **User**: Manage Messages
| **Bot**: Manage Messages

....

|bot_prefix|\ sarmr
-------------------

Command Description
^^^^^^^^^^^^^^^^^^^
Toggles the **periodic monitoring of role requirements** for self-assigned roles.

The configuration of self-assignable roles allows for preventing users with certain roles from receiving roles from a certain group, or to only receive roles from a group if they already have (one or more) different, particular role(s).

By default, the monitoring feature is **disabled** and prerequisite checks only happen upon the assignment (or removal) of the role.

Upon activating the periodic monitoring feature, self-assignable roles are re-checked automatically so that if a user fails the prerequisite checks (e.g. by either having an ignored role, or losing a required role, or having multiple roles from a group in "Single" mode), they will lose the previously acquired role.

Since one role can be in multiple groups, and these groups may have different settings, a role will only be removed if that role fails **all** of the prerequisite checks among the different group settings.

.. note::
    This check only happens every 15-30 minutes.

Permissions Needed
^^^^^^^^^^^^^^^^^^

| **User**: Manage Roles
| **Bot**: Manage Roles

....

.. _iam:

|bot_prefix|\ iam
-----------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal:: 
    
    |bot_prefix|\ iam (role id/mention/name)

Command Description
^^^^^^^^^^^^^^^^^^^
Assings one role among those that are flagged as self-assignable, provided the requirements are met.

.. note::
    This command is always available to everyone.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ iam Group 1
    |bot_prefix|\ iam @Testing123
    |bot_prefix|\ iam 123456789098765432 
    
....

.. _iamnot:

|bot_prefix|\ iamnot
--------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal:: 
    
    |bot_prefix|\ iamnot (role id/mention/name)

Command Description
^^^^^^^^^^^^^^^^^^^
Removes one role among those that are flagged as self-assignable, provided the requirements are met.

.. note::
    This command is always available to everyone.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ iamnot Group 1
    |bot_prefix|\ iamnot @Testing123
    |bot_prefix|\ iamnot 123456789098765432 
    
....

|bot_prefix|\ rmcreate
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal:: 
    
    |bot_prefix|\ rmcreate [group id] [--m {message id}]

Command Description
^^^^^^^^^^^^^^^^^^^
Starts an interactive process to build a role menu (i.e. a message whose reactions will assign or remove the roles in the specified role group). The bot will guide you through the process of creating the role menu, follow the in-Discord instructions.

If a valid message ID is specified through the dedicated parameter, the role menu will be created on the target message.

If the group ID is omitted, group **0** will be used as source role group.

Permissions Needed
^^^^^^^^^^^^^^^^^^

| **User**: Manage Roles
| **Bot**: Manage Roles

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rmcreate
    |bot_prefix|\ rmcreate 1 --m 123456789098765432
    
....

|bot_prefix|\ rmremove
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal:: 
    
    |bot_prefix|\ rmremove [message id]

Command Description
^^^^^^^^^^^^^^^^^^^
Removes a role menu from an existing message. The message itself won't be deleted, nor the existing reactions will be removed, but the bot will now not do anything with reactions on that message.

If the message ID is omitted (or is invalid), the bot will attempt to pick the latest role menu in the current channel.

Permissions Needed
^^^^^^^^^^^^^^^^^^

| **User**: Manage Roles
| **Bot**: Manage Roles

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rmremove 123456789098765432
    
....

|bot_prefix|\ rmupdate
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal:: 
    
    |bot_prefix|\ rmupdate [message id]

Command Description
^^^^^^^^^^^^^^^^^^^
Updates a role menu with a new reaction if a role was added to the particular role group.

.. note::
    In order to remove a role from a role menu, you'll need to delete the role menu and create a new one.

If the message ID is omitted (or is invalid), the bot will attempt to pick the latest role menu in the current channel.

Permissions Needed
^^^^^^^^^^^^^^^^^^

| **User**: Manage Roles
| **Bot**: Manage Roles

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rmupdate 123456789098765432
