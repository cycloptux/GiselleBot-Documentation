**************
Administration
**************

The Administration module contains tools used to manage a Discord server and its members.

Partially inspired by `Logger <https://discordbots.org/bot/298822483060981760>`_ and `NadekoBot <https://nadeko.bot/>`_.

....

.. _log-warning:

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
* **Moderation**: Administrators/moderators using a sensitive command, user struck by a moderation action (warn/kick/ban/mute/...), user evaded from a moderation action\*\*.
* **Warning**: This one is a more verbose version the moderation log, focused on moderation actions. Activating this logger enables the case/scoring system.
* **ALL**: Activates all loggers in the current channel.

You can also print the list of available loggers within Discord by using ``|bot_prefix|\ log`` without any additional argument.

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

You can also print the list of currently set filters by using ``|bot_prefix|\ logignore (logger type)`` without any additional argument.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ logignore members @cycloptux#1543
    |bot_prefix|\ logignore channels #admin-chat
    
....

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
Sets the time it takes (in seconds) for greet messages to be auto-deleted. Set it to 0 to disable automatic deletion. The maximum time you can set is 1800 (30 minutes).

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetdel 0
    |bot_prefix|\ greetdel 30

....

|bot_prefix|\ autoassignrole
----------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ autoassignrole [role id/mention/q_name]

Command Description
^^^^^^^^^^^^^^^^^^^
Automaticaly assigns a specified role to every user who joins the server. Provide no parameters to disable.

Permissions Needed
^^^^^^^^^^^^^^^^^^

| **User**: Manage Roles
| **Bot**: Manage Roles

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ aar
    |bot_prefix|\ aar RoleName
    
    