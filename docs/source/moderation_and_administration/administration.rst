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

.. note::
    If you happen to forget the prefix for |bot_name|\ , try using "@\ |bot_name| hprefix". This reaction will only work if the :ref:`custreact` module is enabled.

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
* **Threads**: Thread created, thread edited\*\*, thread deleted.
* **Server**: Server info updated*, emoji created, emoji deleted, emoji updated.
* **Messages**: Message deleted, message edited, message pinned, message unpinned.
* **Voice**: User connected to/disconnected from/switched voice channel.
* **Moderation**: Auto-moderation actions, administrators/moderators using a sensitive command, user struck by a moderation action (warn/kick/ban/mute/...), user evaded from a moderation action\*\*\*.
* **Warning**: This one is a more verbose version the moderation log, focused on moderation actions. Activating this logger enables the case/scoring system.
* **ALL**: Activates all available loggers in the current channel.

You can also print the list of available loggers within Discord by using |bot_prefix|\ log without any additional argument.

.. admonition:: Premium

    The **Members**, **Messages**, **Roles**, **Channels**, **Moderation** and **Warning** loggers are publicly available. If you want to enable **Users**, **Server** and **Voice** loggers, you can unlock them as a **Premium** feature (see: :ref:`premium-perks`). The "Invites Tracking" feature of the **Members** logger is only available as a **Premium** feature.

| :sub:`\*: Due to the high amount of info that can be edited, these commands are limited to monitoring the main parameters.`
| :sub:`\*\*: Thread editing will track thread archival and unarchival events.`
| :sub:`\*\*\*: Evasion is intended as leaving and re-joining a server while a permanent or time-based mute/ban action is taken on the user, in an attempt to clear the moderation roles. The roles will be reapplied and the administrators/moderators will be notified.`

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ log members
    |bot_prefix|\ log voice messages
    |bot_prefix|\ log ALL

....

|bot_prefix|\ logstatus
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ logstatus

Command Description
^^^^^^^^^^^^^^^^^^^
Prints a summary of the enabled loggers, showing which logger(s) are enabled in which channel(s).

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

.. 
    ....
..
    |bot_prefix|\ logmatt
    ---------------------
..
    Command Syntax
    ^^^^^^^^^^^^^^
    .. parsed-literal::
..
        |bot_prefix|\ logmatt
..
    Command Description
    ^^^^^^^^^^^^^^^^^^^
    Opens an interactive menu to configure the message attachments logging feature on deleted messages.
..
    By default, deleting a message that contains an image as attachment will trigger an automatic reupload of said image into the Messages logging channel.
..
    Within the configuration menu, users will be able to enable or disable this feature, and to limit the feature to certain channels (**whitelist** mode) or exclude certain channels from this extra logging feature (**blacklist** mode).

....

Greet Messages
==============

The Greet Messages submodule lets server managers configure automatic and configurable messages that |bot_name| still send when a user joins/leaves your server, or obtains a specific role.

All use cases (minus the "goodbye" messages) can be configured to send greet messages to a channel or to the user through a Direct Message.

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
Toggles announcements via Direct Message when someone joins the server (this is separate from greet - you can have both, any, or neither enabled).

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

....

|bot_prefix|\ greetmsg
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetmsg [message content]

Command Description
^^^^^^^^^^^^^^^^^^^
Sets a new join announcement message which will be shown in the server's channel. Using it with no message will show the current greet message.

You can use one (or more) of these placeholders in your message:

* **%user%**: This will be replaced with a mention of the user.
* **%username%**: This will be replaced with the username of the user, without the discriminator (e.g. cycloptux).
* **%discriminator%**: This will be replaced with the discriminator of the user, without the ``#`` character (e.g. 1543).
* **%fullusername%**: This will be replaced with the username of the user, including the discriminator (e.g. cycloptux#1543).
* **%user\_avatar\_url%**: This will be replaced with the current user global avatar URL (in WebP or GIF format).
* **%user\_server\_avatar\_url%**: This will be replaced with the current user server avatar URL, if set, or the global avatar URL (in WebP or GIF format).
* **%bot%**: This will be replaced with a mention of the bot.
* **%botname%**: This will be replaced with the username of the bot, without the discriminator.
* **%botdiscriminator%**: This will be replaced with the discriminator of the bot, without the ``#`` character.
* **%fullbotname%**: This will be replaced with the username of the bot, including the discriminator.
* **%bot\_avatar\_url%**: This will be replaced with the current bot avatar URL (in WebP or GIF format).
* **%server%**: This will be replaced with the server name.
* **%now%**: This will be replaced with the current time, with format ``YYYY-MM-DD HH:mm:ss (UTC)``.
* **%now\_iso%**: This will be replaced with the current time, as ISO8601 string.
* **%server\_time%**: This will be replaced with the current time, with format ``HH:mm UTC``.
* **%server\_icon\_url%**: This will be replaced with the current server icon URL (in WebP or GIF format).
* **%server\_banner\_url%**: This will be replaced with the current server icon URL (in WebP format).
* **%server\_splash\_url%**: This will be replaced with the current server icon URL (in WebP format).
* **%server\_member\_count%**: This will be replaced with the current amount of members in the server.
* **%boost\_level%**: This will be replaced with the current Nitro Server Boost level for the server.
* **%boost\_number%**: This will be replaced with the current number of Nitro Server Boosts that the server received.

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

    |bot_prefix|\ greetdmmsg [message content]

Command Description
^^^^^^^^^^^^^^^^^^^
Sets a new join announcement message which will be sent to the user who joined, via DM. Using it with no message will show the current DM greet message.

You can use one (or more) of these placeholders in your message:

* **%user%**: This will be replaced with a mention of the user.
* **%username%**: This will be replaced with the username of the user, without the discriminator (e.g. cycloptux).
* **%discriminator%**: This will be replaced with the discriminator of the user, without the ``#`` character (e.g. 1543).
* **%fullusername%**: This will be replaced with the username of the user, including the discriminator (e.g. cycloptux#1543).
* **%user\_avatar\_url%**: This will be replaced with the current user global avatar URL (in WebP or GIF format).
* **%user\_server\_avatar\_url%**: This will be replaced with the current user server avatar URL, if set, or the global avatar URL (in WebP or GIF format).
* **%bot%**: This will be replaced with a mention of the bot.
* **%botname%**: This will be replaced with the username of the bot, without the discriminator.
* **%botdiscriminator%**: This will be replaced with the discriminator of the bot, without the ``#`` character.
* **%fullbotname%**: This will be replaced with the username of the bot, including the discriminator.
* **%bot\_avatar\_url%**: This will be replaced with the current bot avatar URL (in WebP or GIF format).
* **%server%**: This will be replaced with the server name.
* **%now%**: This will be replaced with the current time, with format ``YYYY-MM-DD HH:mm:ss (UTC)``.
* **%now\_iso%**: This will be replaced with the current time, as ISO8601 string.
* **%server\_time%**: This will be replaced with the current time, with format ``HH:mm UTC``.
* **%server\_icon\_url%**: This will be replaced with the current server icon URL (in WebP or GIF format).
* **%server\_banner\_url%**: This will be replaced with the current server icon URL (in WebP format).
* **%server\_splash\_url%**: This will be replaced with the current server icon URL (in WebP format).
* **%server\_member\_count%**: This will be replaced with the current amount of members in the server.
* **%boost\_level%**: This will be replaced with the current Nitro Server Boost level for the server.
* **%boost\_number%**: This will be replaced with the current number of Nitro Server Boosts that the server received.

You can use embed json from https://eb.nadeko.bot/ instead of a regular text, if you want the message to be embedded.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetdmmsg Welcome to %server%, %user%.

....

|bot_prefix|\ greetdelay
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetdelay (seconds)

Command Description
^^^^^^^^^^^^^^^^^^^
Sets the time (delay) it takes (in seconds) for **in-server** greet messages to be sent. Set it to 0 to disable send delay.

The maximum time you can set is 300 (5 minutes).

.. admonition:: Premium

    You can extend the maximum time to 900 (15 minutes) as a **Premium** feature (see: :ref:`premium-perks`).

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetdelay 0
    |bot_prefix|\ greetdelay 10

....

|bot_prefix|\ greetdmdelay
--------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetdmdelay (seconds)

Command Description
^^^^^^^^^^^^^^^^^^^
Sets the time (delay) it takes (in seconds) for **Direct Message** greet messages to be sent. Set it to 0 to disable send delay.

The maximum time you can set is 300 (5 minutes).

.. admonition:: Premium

    You can extend the maximum time to 900 (15 minutes) as a **Premium** feature (see: :ref:`premium-perks`).

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetdmdelay 0
    |bot_prefix|\ greetdmdelay 10

....

|bot_prefix|\ greetdel
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetdel (seconds)

Command Description
^^^^^^^^^^^^^^^^^^^
Sets the time it takes (in seconds) for **in-server** greet messages to be auto-deleted after being sent. Set it to 0 to disable automatic deletion.

The maximum time you can set is 300 (5 minutes).

.. admonition:: Premium

    You can extend the maximum time to 900 (15 minutes) as a **Premium** feature (see: :ref:`premium-perks`).

.. note::
    This setting does not apply to DM greet messages.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetdel 0
    |bot_prefix|\ greetdel 30

....

|bot_prefix|\ goodbye
---------------------

Command Description
^^^^^^^^^^^^^^^^^^^
Toggles announcements on the current channel when someone leaves the server.

.. note::
    Due to Discord's caching system, some or all of the information needed to correctly fill the goodbye message might be missing at the time of leaving of a user. |bot_name| will still attempt to create the message with the info that can be fetched from the cache, but the information might be incomplete or incorrect. **This is not a bug**.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

....

|bot_prefix|\ goodbyemsg
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ goodbyemsg [message content]

Command Description
^^^^^^^^^^^^^^^^^^^
Sets a new leave announcement message which will be shown in the server's channel. Using it with no message will show the current goodbye message.

You can use one (or more) of these placeholders in your message:

* **%user%**: This will be replaced with a mention of the user.
* **%username%**: This will be replaced with the username of the user, without the discriminator (e.g. cycloptux).
* **%discriminator%**: This will be replaced with the discriminator of the user, without the ``#`` character (e.g. 1543).
* **%fullusername%**: This will be replaced with the username of the user, including the discriminator (e.g. cycloptux#1543).
* **%user\_avatar\_url%**: This will be replaced with the current user global avatar URL (in WebP or GIF format).
* **%user\_server\_avatar\_url%**: This will be replaced with the current user server avatar URL, if set, or the global avatar URL (in WebP or GIF format).
* **%bot%**: This will be replaced with a mention of the bot.
* **%botname%**: This will be replaced with the username of the bot, without the discriminator.
* **%botdiscriminator%**: This will be replaced with the discriminator of the bot, without the ``#`` character.
* **%fullbotname%**: This will be replaced with the username of the bot, including the discriminator.
* **%bot\_avatar\_url%**: This will be replaced with the current bot avatar URL (in WebP or GIF format).
* **%server%**: This will be replaced with the server name.
* **%now%**: This will be replaced with the current time, with format ``YYYY-MM-DD HH:mm:ss (UTC)``.
* **%now\_iso%**: This will be replaced with the current time, as ISO8601 string.
* **%server\_time%**: This will be replaced with the current time, with format ``HH:mm UTC``.
* **%server\_icon\_url%**: This will be replaced with the current server icon URL (in WebP or GIF format).
* **%server\_banner\_url%**: This will be replaced with the current server icon URL (in WebP format).
* **%server\_splash\_url%**: This will be replaced with the current server icon URL (in WebP format).
* **%server\_member\_count%**: This will be replaced with the current amount of members in the server.
* **%boost\_level%**: This will be replaced with the current Nitro Server Boost level for the server.
* **%boost\_number%**: This will be replaced with the current number of Nitro Server Boosts that the server received.

You can use embed json from https://eb.nadeko.bot/ instead of a regular text, if you want the message to be embedded.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ goodbyemsg See you soon, %fullusername%!

....

|bot_prefix|\ goodbyedelay
--------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ goodbyedelay (seconds)

Command Description
^^^^^^^^^^^^^^^^^^^
Sets the time (delay) it takes (in seconds) for **in-server** goodbye messages to be sent. Set it to 0 to disable send delay.

The maximum time you can set is 300 (5 minutes).

.. admonition:: Premium

    You can extend the maximum time to 900 (15 minutes) as a **Premium** feature (see: :ref:`premium-perks`).

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ goodbyedelay 0
    |bot_prefix|\ goodbyedelay 10

....

|bot_prefix|\ goodbyedel
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ goodbyedel (seconds)

Command Description
^^^^^^^^^^^^^^^^^^^
Sets the time it takes (in seconds) for **in-server** goodbye messages to be auto-deleted after being sent. Set it to 0 to disable automatic deletion.

The maximum time you can set is 300 (5 minutes).

.. admonition:: Premium

    You can extend the maximum time to 900 (15 minutes) as a **Premium** feature (see: :ref:`premium-perks`).

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ goodbyedel 0
    |bot_prefix|\ goodbyedel 30

....

|bot_prefix|\ greetrole
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetrole (role id/mention/q_name)

Command Description
^^^^^^^^^^^^^^^^^^^
Toggles announcements on the current channel when someone obtains a certain role.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetrole @Beta Tester
    |bot_prefix|\ greetrole 123456789098765432
    |bot_prefix|\ greetrole "Top Secret Pass"

....

|bot_prefix|\ greetroledm
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetroledm (role id/mention/q_name)

Command Description
^^^^^^^^^^^^^^^^^^^
Toggles announcements via Direct Message when someone obtains a certain role (this is separate from greetrole - you can have both, any, or neither enabled).

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetroledm @Beta Tester
    |bot_prefix|\ greetroledm 123456789098765432
    |bot_prefix|\ greetroledm "Top Secret Pass"

....

|bot_prefix|\ greetrolemsg
--------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetrolemsg (role id/mention/q_name) [message content]

Command Description
^^^^^^^^^^^^^^^^^^^
Sets a new role greeting message which will be shown in the server's channel. Using it with no message will show the current greet message.

You can use one (or more) of these placeholders in your message:

* **%role%**: This will be replaced with the name (in plain text) of the obtained role.
* **%role\_mention%**: This will be replaced with the mention of the obtained role.
* **%user%**: This will be replaced with a mention of the user.
* **%username%**: This will be replaced with the username of the user, without the discriminator (e.g. cycloptux).
* **%discriminator%**: This will be replaced with the discriminator of the user, without the ``#`` character (e.g. 1543).
* **%fullusername%**: This will be replaced with the username of the user, including the discriminator (e.g. cycloptux#1543).
* **%user\_avatar\_url%**: This will be replaced with the current user global avatar URL (in WebP or GIF format).
* **%user\_server\_avatar\_url%**: This will be replaced with the current user server avatar URL, if set, or the global avatar URL (in WebP or GIF format).
* **%bot%**: This will be replaced with a mention of the bot.
* **%botname%**: This will be replaced with the username of the bot, without the discriminator.
* **%botdiscriminator%**: This will be replaced with the discriminator of the bot, without the ``#`` character.
* **%fullbotname%**: This will be replaced with the username of the bot, including the discriminator.
* **%bot\_avatar\_url%**: This will be replaced with the current bot avatar URL (in WebP or GIF format).
* **%server%**: This will be replaced with the server name.
* **%now%**: This will be replaced with the current time, with format ``YYYY-MM-DD HH:mm:ss (UTC)``.
* **%now\_iso%**: This will be replaced with the current time, as ISO8601 string.
* **%server\_time%**: This will be replaced with the current time, with format ``HH:mm UTC``.
* **%server\_icon\_url%**: This will be replaced with the current server icon URL (in WebP or GIF format).
* **%server\_banner\_url%**: This will be replaced with the current server icon URL (in WebP format).
* **%server\_splash\_url%**: This will be replaced with the current server icon URL (in WebP format).
* **%server\_member\_count%**: This will be replaced with the current amount of members in the server.
* **%boost\_level%**: This will be replaced with the current Nitro Server Boost level for the server.
* **%boost\_number%**: This will be replaced with the current number of Nitro Server Boosts that the server received.

You can use embed json from https://eb.nadeko.bot/ instead of a regular text, if you want the message to be embedded.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetrolemsg @VIP Congratulations for obtaining the **%role%** role, %user%! With great power comes great responsibility...
    |bot_prefix|\ greetrolemsg 123456789098765432 Welcome %user%, you are now a member of this server!

....

|bot_prefix|\ greetroledmmsg
----------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetroledmmsg (role id/mention/q_name) [message content]

Command Description
^^^^^^^^^^^^^^^^^^^
Sets a new role greeting message which will be sent to the user who obtained the role, via DM. Using it with no message will show the current DM greet message.

You can use one (or more) of these placeholders in your message:

* **%role%**: This will be replaced with the name (in plain text) of the obtained role.
* **%role\_mention%**: This will be replaced with the mention of the obtained role.
* **%user%**: This will be replaced with a mention of the user.
* **%username%**: This will be replaced with the username of the user, without the discriminator (e.g. cycloptux).
* **%discriminator%**: This will be replaced with the discriminator of the user, without the ``#`` character (e.g. 1543).
* **%fullusername%**: This will be replaced with the username of the user, including the discriminator (e.g. cycloptux#1543).
* **%user\_avatar\_url%**: This will be replaced with the current user global avatar URL (in WebP or GIF format).
* **%user\_server\_avatar\_url%**: This will be replaced with the current user server avatar URL, if set, or the global avatar URL (in WebP or GIF format).
* **%bot%**: This will be replaced with a mention of the bot.
* **%botname%**: This will be replaced with the username of the bot, without the discriminator.
* **%botdiscriminator%**: This will be replaced with the discriminator of the bot, without the ``#`` character.
* **%fullbotname%**: This will be replaced with the username of the bot, including the discriminator.
* **%bot\_avatar\_url%**: This will be replaced with the current bot avatar URL (in WebP or GIF format).
* **%server%**: This will be replaced with the server name.
* **%now%**: This will be replaced with the current time, with format ``YYYY-MM-DD HH:mm:ss (UTC)``.
* **%now\_iso%**: This will be replaced with the current time, as ISO8601 string.
* **%server\_time%**: This will be replaced with the current time, with format ``HH:mm UTC``.
* **%server\_icon\_url%**: This will be replaced with the current server icon URL (in WebP or GIF format).
* **%server\_banner\_url%**: This will be replaced with the current server icon URL (in WebP format).
* **%server\_splash\_url%**: This will be replaced with the current server icon URL (in WebP format).
* **%server\_member\_count%**: This will be replaced with the current amount of members in the server.
* **%boost\_level%**: This will be replaced with the current Nitro Server Boost level for the server.
* **%boost\_number%**: This will be replaced with the current number of Nitro Server Boosts that the server received.

You can use embed json from https://eb.nadeko.bot/ instead of a regular text, if you want the message to be embedded.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetroledmmsg @VIP Congratulations for obtaining the **%role%** role in **%server%**, %user%! With great power comes great responsibility...
    |bot_prefix|\ greetroledmmsg 123456789098765432 Welcome %user%, you are now a member of the %server% server!

....

|bot_prefix|\ greetroledelay
----------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetroledelay (role id/mention/q_name) (seconds)

Command Description
^^^^^^^^^^^^^^^^^^^
Sets the time (delay) it takes (in seconds) for **in-server** role greet messages to be sent. Set it to 0 to disable send delay.

The maximum time you can set is 300 (5 minutes).

.. admonition:: Premium

    You can extend the maximum time to 900 (15 minutes) as a **Premium** feature (see: :ref:`premium-perks`).

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetroledelay @VIP 0
    |bot_prefix|\ greetroledelay 123456789098765432 10

....

|bot_prefix|\ greetroledmdelay
------------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetroledmdelay (role id/mention/q_name) (seconds)

Command Description
^^^^^^^^^^^^^^^^^^^
Sets the time (delay) it takes (in seconds) for **Direct Message** role greet messages to be sent. Set it to 0 to disable send delay.

The maximum time you can set is 300 (5 minutes).

.. admonition:: Premium

    You can extend the maximum time to 900 (15 minutes) as a **Premium** feature (see: :ref:`premium-perks`).

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetroledmdelay @VIP 0
    |bot_prefix|\ greetroledmdelay 123456789098765432 10

....

|bot_prefix|\ greetroledel
--------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetroledel (role id/mention/q_name) (seconds)

Command Description
^^^^^^^^^^^^^^^^^^^
Sets the time it takes (in seconds) for **in-server** role greet messages to be auto-deleted after being sent. Set it to 0 to disable automatic deletion.

The maximum time you can set is 300 (5 minutes).

.. admonition:: Premium

    You can extend the maximum time to 900 (15 minutes) as a **Premium** feature (see: :ref:`premium-perks`).

.. note::
    This setting does not apply to DM greet messages.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greetroledel @Beta Tester 0
    |bot_prefix|\ greetroledel "Top Secret Pass" 30

....

|bot_prefix|\ goodbyerole
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ goodbyerole (role id/mention/q_name)

Command Description
^^^^^^^^^^^^^^^^^^^
Toggles announcements on the current channel when someone loses a certain role.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ goodbyerole @Beta Tester
    |bot_prefix|\ goodbyerole 123456789098765432
    |bot_prefix|\ goodbyerole "Top Secret Pass"

....

|bot_prefix|\ goodbyeroledm
---------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ goodbyeroledm (role id/mention/q_name)

Command Description
^^^^^^^^^^^^^^^^^^^
Toggles announcements via Direct Message when someone loses a certain role (this is separate from goodbyerole - you can have both, any, or neither enabled).

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ goodbyeroledm @Beta Tester
    |bot_prefix|\ goodbyeroledm 123456789098765432
    |bot_prefix|\ goodbyeroledm "Top Secret Pass"

....

|bot_prefix|\ goodbyerolemsg
----------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ goodbyerolemsg (role id/mention/q_name) [message content]

Command Description
^^^^^^^^^^^^^^^^^^^
Sets a new role goodbye message which will be shown in the server's channel. Using it with no message will show the current goodbye message.

You can use one (or more) of these placeholders in your message:

* **%role%**: This will be replaced with the name (in plain text) of the lost role.
* **%role\_mention%**: This will be replaced with the mention of the lost role.
* **%user%**: This will be replaced with a mention of the user.
* **%username%**: This will be replaced with the username of the user, without the discriminator (e.g. cycloptux).
* **%discriminator%**: This will be replaced with the discriminator of the user, without the ``#`` character (e.g. 1543).
* **%fullusername%**: This will be replaced with the username of the user, including the discriminator (e.g. cycloptux#1543).
* **%user\_avatar\_url%**: This will be replaced with the current user global avatar URL (in WebP or GIF format).
* **%user\_server\_avatar\_url%**: This will be replaced with the current user server avatar URL, if set, or the global avatar URL (in WebP or GIF format).
* **%bot%**: This will be replaced with a mention of the bot.
* **%botname%**: This will be replaced with the username of the bot, without the discriminator.
* **%botdiscriminator%**: This will be replaced with the discriminator of the bot, without the ``#`` character.
* **%fullbotname%**: This will be replaced with the username of the bot, including the discriminator.
* **%bot\_avatar\_url%**: This will be replaced with the current bot avatar URL (in WebP or GIF format).
* **%server%**: This will be replaced with the server name.
* **%now%**: This will be replaced with the current time, with format ``YYYY-MM-DD HH:mm:ss (UTC)``.
* **%now\_iso%**: This will be replaced with the current time, as ISO8601 string.
* **%server\_time%**: This will be replaced with the current time, with format ``HH:mm UTC``.
* **%server\_icon\_url%**: This will be replaced with the current server icon URL (in WebP or GIF format).
* **%server\_banner\_url%**: This will be replaced with the current server icon URL (in WebP format).
* **%server\_splash\_url%**: This will be replaced with the current server icon URL (in WebP format).
* **%server\_member\_count%**: This will be replaced with the current amount of members in the server.
* **%boost\_level%**: This will be replaced with the current Nitro Server Boost level for the server.
* **%boost\_number%**: This will be replaced with the current number of Nitro Server Boosts that the server received.

You can use embed json from https://eb.nadeko.bot/ instead of a regular text, if you want the message to be embedded.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ goodbyerolemsg @VIP Sorry to hear you losing the **%role%** role, %user%!
    |bot_prefix|\ goodbyerolemsg 123456789098765432 %user%, you are no longer a member of this club!

....

|bot_prefix|\ goodbyeroledmmsg
------------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ goodbyeroledmmsg (role id/mention/q_name) [message content]

Command Description
^^^^^^^^^^^^^^^^^^^
Sets a new role goodbye message which will be sent to the user who lost the role, via DM. Using it with no message will show the current DM goodbye message.

You can use one (or more) of these placeholders in your message:

* **%role%**: This will be replaced with the name (in plain text) of the lost role.
* **%role\_mention%**: This will be replaced with the mention of the lost role.
* **%user%**: This will be replaced with a mention of the user.
* **%username%**: This will be replaced with the username of the user, without the discriminator (e.g. cycloptux).
* **%discriminator%**: This will be replaced with the discriminator of the user, without the ``#`` character (e.g. 1543).
* **%fullusername%**: This will be replaced with the username of the user, including the discriminator (e.g. cycloptux#1543).
* **%user\_avatar\_url%**: This will be replaced with the current user global avatar URL (in WebP or GIF format).
* **%user\_server\_avatar\_url%**: This will be replaced with the current user server avatar URL, if set, or the global avatar URL (in WebP or GIF format).
* **%bot%**: This will be replaced with a mention of the bot.
* **%botname%**: This will be replaced with the username of the bot, without the discriminator.
* **%botdiscriminator%**: This will be replaced with the discriminator of the bot, without the ``#`` character.
* **%fullbotname%**: This will be replaced with the username of the bot, including the discriminator.
* **%bot\_avatar\_url%**: This will be replaced with the current bot avatar URL (in WebP or GIF format).
* **%server%**: This will be replaced with the server name.
* **%now%**: This will be replaced with the current time, with format ``YYYY-MM-DD HH:mm:ss (UTC)``.
* **%now\_iso%**: This will be replaced with the current time, as ISO8601 string.
* **%server\_time%**: This will be replaced with the current time, with format ``HH:mm UTC``.
* **%server\_icon\_url%**: This will be replaced with the current server icon URL (in WebP or GIF format).
* **%server\_banner\_url%**: This will be replaced with the current server icon URL (in WebP format).
* **%server\_splash\_url%**: This will be replaced with the current server icon URL (in WebP format).
* **%server\_member\_count%**: This will be replaced with the current amount of members in the server.
* **%boost\_level%**: This will be replaced with the current Nitro Server Boost level for the server.
* **%boost\_number%**: This will be replaced with the current number of Nitro Server Boosts that the server received.

You can use embed json from https://eb.nadeko.bot/ instead of a regular text, if you want the message to be embedded.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ goodbyeroledmmsg @VIP Sorry to hear you losing the **%role%** role, %user%!
    |bot_prefix|\ goodbyeroledmmsg 123456789098765432 %user%, you are no longer a member of this club!

....

|bot_prefix|\ goodbyeroledelay
------------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ goodbyeroledelay (role id/mention/q_name) (seconds)

Command Description
^^^^^^^^^^^^^^^^^^^
Sets the time (delay) it takes (in seconds) for **in-server** role goodbye messages to be sent. Set it to 0 to disable send delay.

The maximum time you can set is 300 (5 minutes).

.. admonition:: Premium

    You can extend the maximum time to 900 (15 minutes) as a **Premium** feature (see: :ref:`premium-perks`).

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ goodbyeroledelay @VIP 0
    |bot_prefix|\ goodbyeroledelay 123456789098765432 10

....

|bot_prefix|\ goodbyeroledmdelay
--------------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ goodbyeroledmdelay (role id/mention/q_name) (seconds)

Command Description
^^^^^^^^^^^^^^^^^^^
Sets the time (delay) it takes (in seconds) for **Direct Message** role goodbye messages to be sent. Set it to 0 to disable send delay.

The maximum time you can set is 300 (5 minutes).

.. admonition:: Premium

    You can extend the maximum time to 900 (15 minutes) as a **Premium** feature (see: :ref:`premium-perks`).

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ goodbyeroledmdelay @VIP 0
    |bot_prefix|\ goodbyeroledmdelay 123456789098765432 10

....

|bot_prefix|\ goodbyeroledel
----------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ goodbyeroledel (role id/mention/q_name) (seconds)

Command Description
^^^^^^^^^^^^^^^^^^^
Sets the time it takes (in seconds) for **in-server** role goodbye messages to be auto-deleted after being sent. Set it to 0 to disable automatic deletion.

The maximum time you can set is 300 (5 minutes).

.. admonition:: Premium

    You can extend the maximum time to 900 (15 minutes) as a **Premium** feature (see: :ref:`premium-perks`).

.. note::
    This setting does not apply to DM goodbye messages.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ goodbyeroledel @Beta Tester 0
    |bot_prefix|\ goodbyeroledel "Top Secret Pass" 30

....

Automated Roles Assignment/Removal
==================================

.. _autoassignrole:

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

Self-Assignable Roles
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
* **Prerequisites Check**: Toggles the **periodic monitoring of role requirements** for self-assigned roles.

  * The configuration of self-assignable roles allows for preventing users with certain roles from receiving roles from a certain group, or to only receive roles from a group if they already have (one or more) different, particular role(s).
  * By default, the monitoring feature is **disabled** and prerequisite checks only happen upon the assignment (or removal) of the role.
  * Upon activating the periodic monitoring feature, self-assignable roles **within the selected group** are re-checked automatically so that if a user fails the prerequisite checks (e.g. by either having an ignored role, or losing a required role, or having multiple roles from a group in "Single" mode), they will lose the previously acquired role.

.. note::
    Prerequisites checks only happen every 15-30 minutes.

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

If a valid message ID is specified through the dedicated parameter, the role menu will be created on the target message. If specified, the message ID must refer to a message in the same channel where the command is run.

If the group ID is omitted, group **0** will be used as source role group.

Permissions Needed
^^^^^^^^^^^^^^^^^^

| **User**: Manage Roles
| **Bot**: Manage Roles, Add Reactions

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rmcreate
    |bot_prefix|\ rmcreate 1 --m 123456789098765432

....

|bot_prefix|\ rmdmtoggle
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rmdmtoggle [message id]

Command Description
^^^^^^^^^^^^^^^^^^^
Toggles the Direct Message confirmation for **successfully added or removed** self-assigned roles on a specific role menu, making them "silent" or re-enabling the verbose message confirmation. Roles not being assigned will still trigger the DM.

If the message ID is omitted (or is invalid), the bot will attempt to pick the latest role menu in the current channel. If specified, the message ID must refer to a message in the same channel where the command is run.

Permissions Needed
^^^^^^^^^^^^^^^^^^

| **User**: Manage Roles
| **Bot**: Manage Roles

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rmdmtoggle 123456789098765432

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

If the message ID is omitted (or is invalid), the bot will attempt to pick the latest role menu in the current channel. If specified, the message ID must refer to a message in the same channel where the command is run.

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

If the message ID is omitted (or is invalid), the bot will attempt to pick the latest role menu in the current channel. If specified, the message ID must refer to a message in the same channel where the command is run.

Permissions Needed
^^^^^^^^^^^^^^^^^^

| **User**: Manage Roles
| **Bot**: Manage Roles

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rmupdate 123456789098765432

....

Nitro Server Boost Notifications
================================

With Server Boosts, Discord added a way for you and your community to work together to unlock fresh new and improved collective perks for a server of your choice, each month, and share those epic perks to the rest of the server community.

.. seealso::
    You can find everything about Server Boosts at this link: https://support.discord.com/hc/en-us/articles/360028038352

With |bot_name|\ , Server Boosts can now be tracked efficiently, and your members can be greeted through a custom message when they gift your server with a Boost!

.. note::
    Due to technical issues (specifically, the lack of a real "event" in case of a Server Boost), |bot_name| will do its best to keep track of the Boosts that are gifted to your server. That said, users gifting more than 1 Boost to your server will not trigger the Boost event, and the removal of a Boost won't always be able to track down who removed the Boost.

Here's the full list of available commands for this sub-module:

|bot_prefix|\ nsbaddnotif
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ nsbaddnotif [channel id(s)/mention(s)/q_name(s)]

Command Description
^^^^^^^^^^^^^^^^^^^
Toggles Nitro Server Boost announcements, on the selected channel(s), when someone **Boosts** the server.

If used without any (valid) argument, the command will show which channels are currently enabled for these announcements.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ nsbaddnotif
    |bot_prefix|\ nsbaddnotif 123456789098765432 234567890987654321

....

|bot_prefix|\ nsbaddtemplate
----------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ nsbaddtemplate [message content]

Command Description
^^^^^^^^^^^^^^^^^^^
Sets a new Nitro Server Boost announcement message which will be shown in the selected server's channel(s) when someone **Boosts** the server. Using it with no message will show the current template.

You can use one (or more) of these placeholders in your message:

* **%user%**: This will be replaced with a mention of the user.
* **%username%**: This will be replaced with the username of the user, without the discriminator (e.g. cycloptux).
* **%discriminator%**: This will be replaced with the discriminator of the user, without the ``#`` character (e.g. 1543).
* **%fullusername%**: This will be replaced with the username of the user, including the discriminator (e.g. cycloptux#1543).
* **%user\_avatar\_url%**: This will be replaced with the current user global avatar URL (in WebP or GIF format).
* **%user\_server\_avatar\_url%**: This will be replaced with the current user server avatar URL, if set, or the global avatar URL (in WebP or GIF format).
* **%bot%**: This will be replaced with a mention of the bot.
* **%botname%**: This will be replaced with the username of the bot, without the discriminator.
* **%botdiscriminator%**: This will be replaced with the discriminator of the bot, without the ``#`` character.
* **%fullbotname%**: This will be replaced with the username of the bot, including the discriminator.
* **%bot\_avatar\_url%**: This will be replaced with the current bot avatar URL (in WebP or GIF format).
* **%server%**: This will be replaced with the server name.
* **%now%**: This will be replaced with the current time, with format ``YYYY-MM-DD HH:mm:ss (UTC)``.
* **%now\_iso%**: This will be replaced with the current time, as ISO8601 string.
* **%server\_time%**: This will be replaced with the current time, with format ``HH:mm UTC``.
* **%server\_icon\_url%**: This will be replaced with the current server icon URL (in WebP or GIF format).
* **%server\_banner\_url%**: This will be replaced with the current server icon URL (in WebP format).
* **%server\_splash\_url%**: This will be replaced with the current server icon URL (in WebP format).
* **%server\_member\_count%**: This will be replaced with the current amount of members in the server.
* **%boost\_level%**: This will be replaced with the current Nitro Server Boost level for the server.
* **%boost\_number%**: This will be replaced with the current number of Nitro Server Boosts that the server received.

You can use embed json from https://eb.nadeko.bot/ instead of a regular text, if you want the message to be embedded.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ nsbaddtemplate
    |bot_prefix|\ nsbaddtemplate %user% just boosted the server! Thanks a bunch!
        The total Boost count for **%server%** is now **%boost_number%**.

....

|bot_prefix|\ nsbremnotif
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ nsbremnotif [channel id(s)/mention(s)/q_name(s)]

Command Description
^^^^^^^^^^^^^^^^^^^
Toggles Nitro Server Boost announcements, on the selected channel(s), when someone **removes a Boost** for the server.

If used without any (valid) argument, the command will show which channels are currently enabled for these announcements.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ nsbremnotif
    |bot_prefix|\ nsbremnotif 123456789098765432 234567890987654321

....

|bot_prefix|\ nsbremtemplate
----------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ nsbremtemplate [message content]

Command Description
^^^^^^^^^^^^^^^^^^^
Sets a new Nitro Server Boost announcement message which will be shown in the selected server's channel(s) when someone **removes a Boost** for the server. Using it with no message will show the current template.

You can use one (or more) of these placeholders in your message:

* **%user%**: This will be replaced with a mention of the user.
* **%username%**: This will be replaced with the username of the user, without the discriminator (e.g. cycloptux).
* **%discriminator%**: This will be replaced with the discriminator of the user, without the ``#`` character (e.g. 1543).
* **%fullusername%**: This will be replaced with the username of the user, including the discriminator (e.g. cycloptux#1543).
* **%user\_avatar\_url%**: This will be replaced with the current user global avatar URL (in WebP or GIF format).
* **%user\_server\_avatar\_url%**: This will be replaced with the current user server avatar URL, if set, or the global avatar URL (in WebP or GIF format).
* **%bot%**: This will be replaced with a mention of the bot.
* **%botname%**: This will be replaced with the username of the bot, without the discriminator.
* **%botdiscriminator%**: This will be replaced with the discriminator of the bot, without the ``#`` character.
* **%fullbotname%**: This will be replaced with the username of the bot, including the discriminator.
* **%bot\_avatar\_url%**: This will be replaced with the current bot avatar URL (in WebP or GIF format).
* **%server%**: This will be replaced with the server name.
* **%now%**: This will be replaced with the current time, with format ``YYYY-MM-DD HH:mm:ss (UTC)``.
* **%now\_iso%**: This will be replaced with the current time, as ISO8601 string.
* **%server\_time%**: This will be replaced with the current time, with format ``HH:mm UTC``.
* **%server\_icon\_url%**: This will be replaced with the current server icon URL (in WebP or GIF format).
* **%server\_banner\_url%**: This will be replaced with the current server icon URL (in WebP format).
* **%server\_splash\_url%**: This will be replaced with the current server icon URL (in WebP format).
* **%server\_member\_count%**: This will be replaced with the current amount of members in the server.
* **%boost\_level%**: This will be replaced with the current Nitro Server Boost level for the server.
* **%boost\_number%**: This will be replaced with the current number of Nitro Server Boosts that the server received.

You can use embed json from https://eb.nadeko.bot/ instead of a regular text, if you want the message to be embedded.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ nsbremtemplate
    |bot_prefix|\ nsbremtemplate Oh no! %user% has just withdrawn a boost!\nThe total Boost count for **%server%** is now **%boost_number%**.

....

|bot_prefix|\ nsbdmnotif
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ nsbdmnotif

Command Description
^^^^^^^^^^^^^^^^^^^
Toggles Nitro Server Boost "thank you" messages, sent to the users who **Boost** the server, via Direct Message.

....

|bot_prefix|\ nsbdmtemplate
---------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ nsbdmtemplate [message content]

Command Description
^^^^^^^^^^^^^^^^^^^
Sets a new Nitro Server Boost "thank you" message which will be sent to the user who boost the server. Using it with no message will show the current template.

You can use one (or more) of these placeholders in your message:

* **%user%**: This will be replaced with a mention of the user.
* **%username%**: This will be replaced with the username of the user, without the discriminator (e.g. cycloptux).
* **%discriminator%**: This will be replaced with the discriminator of the user, without the ``#`` character (e.g. 1543).
* **%fullusername%**: This will be replaced with the username of the user, including the discriminator (e.g. cycloptux#1543).
* **%user\_avatar\_url%**: This will be replaced with the current user global avatar URL (in WebP or GIF format).
* **%user\_server\_avatar\_url%**: This will be replaced with the current user server avatar URL, if set, or the global avatar URL (in WebP or GIF format).
* **%bot%**: This will be replaced with a mention of the bot.
* **%botname%**: This will be replaced with the username of the bot, without the discriminator.
* **%botdiscriminator%**: This will be replaced with the discriminator of the bot, without the ``#`` character.
* **%fullbotname%**: This will be replaced with the username of the bot, including the discriminator.
* **%bot\_avatar\_url%**: This will be replaced with the current bot avatar URL (in WebP or GIF format).
* **%server%**: This will be replaced with the server name.
* **%now%**: This will be replaced with the current time, with format ``YYYY-MM-DD HH:mm:ss (UTC)``.
* **%now\_iso%**: This will be replaced with the current time, as ISO8601 string.
* **%server\_time%**: This will be replaced with the current time, with format ``HH:mm UTC``.
* **%server\_icon\_url%**: This will be replaced with the current server icon URL (in WebP or GIF format).
* **%server\_banner\_url%**: This will be replaced with the current server icon URL (in WebP format).
* **%server\_splash\_url%**: This will be replaced with the current server icon URL (in WebP format).
* **%server\_member\_count%**: This will be replaced with the current amount of members in the server.
* **%boost\_level%**: This will be replaced with the current Nitro Server Boost level for the server.
* **%boost\_number%**: This will be replaced with the current number of Nitro Server Boosts that the server received.

You can use embed json from https://eb.nadeko.bot/ instead of a regular text, if you want the message to be embedded.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ nsbdmtemplate
    |bot_prefix|\ nsbdmtemplate Thanks for boosting **%server%**! Our total Boost count is now **%boost_number%**.

....

|bot_prefix|\ nsblist
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ nsblist

Command Description
^^^^^^^^^^^^^^^^^^^
Lists all members that contributed with at least one Server Boost in the current server.

....

.. _emoji-submission:

Emoji Submissions
=================

Through the "Emoji Submissions" sub-module, you can let your members submit new emojis to be used your server.

You can configure one or more roles that will be allowed to submit new emojis. If a user tries to submit an emoji while having more than one role up, **only the highest role will be considered** in order to avoid unpredictable conflicts.

For each role, you will be able to configure:

* Whether the role will be allowed to submit emojis without further verification.

  * By setting a verification channel, authorized users (more on that below) will be able to accept or reject an emoji submission before it's actually uploaded.
  * By disabling the verification channel, the emoji will be immediately uploaded without further verification.
  * By **default**, the additional verification step is **disabled**.

* Which roles will be able to accept or reject an emoji submission, provided you enabled the verification channel.

  * These roles will also be mentioned (optional, see below) within the verification channel when a submission is received.
  * Users that are enabled to use the administration module using the :ref:`permissions` will always be authorized to accept or reject any emoji submission.
  * By **default**, **no additional roles** are enabled to accept or reject emoji submissions.

* How many emojis (submitted through this system) the role will be allowed to have up at any given time.

  * If the verification step is active, users are virtually allowed to submit any number of emojis. By setting a maximum number of emojis through the dedicated setting, you are locking the maximum number of **accepted** emojis.
  * By **default**, there is no limit to how many active emojis a user can have.

* Whether the **periodic monitoring of prerequisites** is active for this role.

  * If this option is active, the emojis will be deleted if the user leaves the server and/or if the user loses the role that they "used" to submit the emoji. For example, you can have Nitro Boosters submit one or more emojis, and then have their emoji removed if they stop boosting the server (hence losing the Nitro Boost role).
  * Even if this option is disabled, emojis that are manually deleted will also be removed from this system.
  * By **default**, this option is disabled.

.. note::
    Prerequisites checks only happen every 15-30 minutes.

* Whether the authorized role(s) will be **mentioned** when a new emoji submission is received.

  * By **default**, this option is enabled.

Here's the full list of available commands for this sub-module:

|bot_prefix|\ esubrole
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ esubrole [role id(s)/mention(s)/q_name(s)]

Command Description
^^^^^^^^^^^^^^^^^^^
Toggles the "emoji submitter" status of the selected role(s).

If used without any (valid) argument, the command will show which roles are currently enabled to submit new emojis.

.. note::
    If you want to add the "everyone" role as a submitter role, you must either use the mention (which will obviously ping everyone) or the **server ID**.


Permissions Needed
^^^^^^^^^^^^^^^^^^

| **User**: Manage Emojis and Stickers
| **Bot**: Manage Emojis and Stickers

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ esubrole
    |bot_prefix|\ esubrole 123456789098765432 234567890987654321

....

|bot_prefix|\ esubsetup
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ esubset (role id/mention/q_name)

Command Description
^^^^^^^^^^^^^^^^^^^
Opens the interactive setup menu for the selected role. Use the menu items to configure the settings shown in :ref:`emoji-submission`.

Permissions Needed
^^^^^^^^^^^^^^^^^^

| **User**: Manage Emojis and Stickers
| **Bot**: Manage Emojis and Stickers

....

|bot_prefix|\ esublist
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ esublist [user id/mention/name]

Command Description
^^^^^^^^^^^^^^^^^^^
Lists all **active/accepted** submitted emojis that users submitted through this system.

If this command is used with a user identifier, it will filter the output on emojis submitted by the specified user.

....

|bot_prefix|\ esubpending
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ esubpending [user id/mention/name]

Command Description
^^^^^^^^^^^^^^^^^^^
Lists all **pending** submitted emojis that users submitted through this system, with a quick link to jump to the verification channel message.

If this command is used with a user identifier, it will filter the output on emojis submitted by the specified user.

....

.. _emojisubmit:

|bot_prefix|\ emojisubmit
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ emojisubmit [existing emoji, or image URL] (valid emoji name)

Command Description
^^^^^^^^^^^^^^^^^^^
Lets users submit a new emoji, provided they have at least one of the "emoji submitter" roles.

.. note::
    This command is always available to everyone. A proper configuration of the emoji submitter roles will avoid an improper use of this command.

    Users won't need "Manage Emojis and Stickers" permissions to run this command, but |bot_name| will still check for its own "Manage Emojis and Stickers" permissions to be sure it can upload the emoji upon a successful verification, if any.

    By default, no role is set as emoji submitter role (before a proper configuration) and this command will not have any effect.

The emoji image can be provided by using an existing emoji **(this will only work if the bot has access to the emoji from another server)**, or a valid image URL, or an image provided in forms of an attachment to the submit message. Emoji images must be under 256 KB in size and one of these formats: ``.jpg``, ``.jpeg``, ``.png``, ``.gif``.

Emoji names must be at least 2 characters long (and no more than 32 characters long) and can only contain alphanumeric characters and underscores. **You must not include the colon (:) characters in the emoji name.** Users are also not allowed to submit an emoji that has the same name of an existing server emoji.

|bot_name| will attempt to limit the amount of duplicate emoji submissions by checking, wherever possible, the ID of the submitted emoji with the IDs of already active server emojis.

In order to avoid unpredictable conflicts, if a user tries to submit an emoji while having more than one "emoji submitter" role up, **only the highest role will be considered** for the optional limits/configurations.

Permissions Needed
^^^^^^^^^^^^^^^^^^

| **Bot**: Manage Emojis and Stickers

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ emojisubmit https://cdn.discordapp.com/emojis/614486002291048459.gif?v=1 amegablobsweats

....

Image Gallery Channels
======================

Through the "Image Gallery Channels" sub-module, you can set one or more channels to only "accept" image attachments, hence becoming a virtual gallery.

You can configure one or more channels as image galleries. When a channel is configured as a gallery, only those messages containing **image attachments and no text at all** will be kept, while everything else will be deleted. This check also happens on edited messages.

Users with **Manage Messages, Manage Channels or Administrator** permissions (on their role and/or through channel overrides) will be able to post messages that contain text.

Here's the full list of available commands for this sub-module:

|bot_prefix|\ imggallery
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ imggallery [channel id(s)/mention(s)/q_name(s)]

Command Description
^^^^^^^^^^^^^^^^^^^
Toggles the Image Gallery mode on the selected channel(s).

If used without any (valid) argument, the command will show which channels are currently enabled as image galleries.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ imggallery
    |bot_prefix|\ imggallery 123456789098765432 234567890987654321


Permissions Needed
^^^^^^^^^^^^^^^^^^

| **User**: Manage Messages
| **Bot**: Manage Messages
