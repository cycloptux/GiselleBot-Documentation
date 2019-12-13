****************
Twitch Connector
****************

The Twitch module & connector offers two macro-features:

* A set of commands to interact with Twitch to get info about users and games.
* A notification service which can monitor Twitch streamers going live and offline, sending these notifications to one (or more) of the webhooks configured in your Discord server.

Commands
========

|bot_prefix|\ twcuser
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ twcuser (Twitch username)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Shows generic info about a user on Twitch. The username is case-insensitive.
    
Examples
^^^^^^^^
.. parsed-literal::
    
    |bot_prefix|\ twcuser cycloptux
    
....

|bot_prefix|\ twcstream
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ twcstream (Twitch username)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Shows specific details about the stream properties of a user's channel. This command will not work if the target user is not streaming. The username is case-insensitive.
    
Examples
^^^^^^^^
.. parsed-literal::
    
    |bot_prefix|\ twcstream cycloptux
    
....

|bot_prefix|\ twcwatch
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ twcwatch (Twitch username)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Posts an URL to the user's channel. Discord includes a native auto-preview which lets users play the Twitch stream live in the current channel.
    
Examples
^^^^^^^^
.. parsed-literal::
    
    |bot_prefix|\ twcwatch cycloptux
    
....

Twitch Notifications
====================

.. seealso::
    In order to better understand this module (and the rest of the connector modules), it's very important that you are familiar with Discord webhooks. For more details about this Discord feature, please take a look at `this official guide <https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks>`_.

By default, each notification will be posted to the webhook by using the Twitch account username as author, and Twitch avatar as Discord profile picture. These settings (and other details) can be customized for each stream.

Twitch profile URLs will be posted to Discord, while the Twitch stream preview will leverage the native parsing of Twitch content offered by Discord.

.. note::
    Due to inconsistencies and limitations within the Twitch API, this module may have some extra delay between the actual event and the Discord notification, and/or miss a few notifications every once in a while, and/or send duplicate notifications. Additional checks are in place to minimize the amount occurrencies of duplicate notifications.
    
|bot_prefix|\ twchook
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ twchook (Twitch username) (webhook URL) [customization params]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Starts a notification service for the selected Twitch account. If a user starts or ends a Live stream a notification will be sent to the specified webhook service.

.. warning::
    Discord webhooks are a very powerful feature, but they (currently) lack 2-way authentication of messages. This means that a malicious user knowing a webhook URL will be able, with some effort, to forge a message containing any kind of content using external tools and send that message to the webhook.
    In order to protect yourself from this (rare) occasion, make sure you run this command in non-public channels.

**Customization Params**

``--game (first game) [second game] [...]``
""""""""""""""""""""""""""""""""""""""""""""""

Adds a **whitelist**, **inclusive** filter for game names to the service. Notifications for the selected user will only be sent if the streamed game is equal to one of the filtered games. Actions related to other games will be skipped.

You can also set "composite words" (two or more words as a single game name) by quoting them: ``"league of legends" fortnite`` will count as 2 game filter elements: ``league of legends`` and ``fortnite``. All filters are case-insensitive, but the game name has to be exact for the filter to work correctly.

.. warning::
    This parameter will only work for games that are set at the beginning of a stream. Changing the game throughout a stream will not trigger the additional "Live" notification.

**Default**: No filter

``--header (message)``
""""""""""""""""""""""

Adds a custom header message when notifications are posted. Custom headers can have a maximum of **1024** characters.

Custom headers support a few dynamic tags that are replaced with their respective "real" value during run-time. These are:

* **%display\_name%**: This will be replaced with the display name of an account, including proper formatting of letter cases (e.g. ``Cycloptux``)
* **%username%**: This will be replaced with the "URL" username of a Twitch user (tipically, lowercase). E.g. ``cycloptux``
* **%game%**: This will be replaced with the name of the streamed game (e.g. ``Fortnite``)
* **%status%**: This will be replaced with the description that is usually added below a game title during a stream.
* **%stream\_status%**: This will be replaced with one of the two values: ``Live`` upon a "going Live" notification, ``Offline`` upon a stream end.
* **%timestamp% or %timestamp\_utc%**: This will be replaced with the UTC time of the start of the event, with format ``YYYY-MM-DD HH:mm:ss (UTC)``.
* **%timestamp\_pst%**: This will be replaced with the current PST time of the start of the event, with format ``YYYY-MM-DD HH:mm:ss (PST)``.
* **%url%**: This will be replaced with the Twitch profile URL. See below for more info.

By default, without an explicit use of ``%url%``, all headers will be followed by the actual Twitch profile URL on a new line; rendering of that URL will be done by Discord.

If the ``%url%`` parameter is used, the default URL will **not** be appended to the custom header.

The default header has two different modes for online and offline. Setting a custom header will use the header on both messages: make use of the ``%stream_status%`` tag to differentiate between the two messages.

**Default**: ``:red_circle: Now Live on Twitch: %display_name% | :video_game: Playing %game%.`` and ``Stream Offline: %display_name% | :video_game: Playing %game%.``

``--webhook-name (custom name)``
""""""""""""""""""""""""""""""""

Adds a custom username to the webhook when notifications are sent. Custom usernames can have a maximum of 32 characters.

**Default**: New notifications will be sent by a webhook with the display name of the Twitch account

``--no-username-overwrite``
"""""""""""""""""""""""""""

Removes any custom name from the webhook. The real webhook name (the one that you assigned when creating the webhook in Discord) will be used.

**Default**: ``false`` (Custom or automated names will be applied)

``--no-avatar-overwrite``
"""""""""""""""""""""""""

Removes any custom avatar from the webhook. The real webhook avatar (the one that you assigned when creating the webhook in Discord) will be used.

**Default**: ``false`` (Automated avatars will be applied)

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ twchook cycloptux https://discordapp.com/api/webhooks/123456789098765432/LONG_WEBHOOK_TOKEN
    |bot_prefix|\ twchook cycloptux https://discordapp.com/api/webhooks/123456789098765432/LONG_WEBHOOK_TOKEN --header %user% is now %stream_status%! Game: %game%

....

|bot_prefix|\ twcehook
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ twcehook (Twitch username/stream index) [new customization params]

Command Description
^^^^^^^^^^^^^^^^^^^
**Replaces** all previously set customization params for the selected Twitch notification service with a new set of customization params. The stream index is the number shown with |bot_prefix|\ twclhook.

.. warning::
    Editing the webhook will not change the existing params, it will completely replace them. Take note of the existing params first, and use them in the command!

|bot_prefix|\ twcrhook
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ twcrhook (Twitch username/stream index)

Command Description
^^^^^^^^^^^^^^^^^^^
Stops a previously set Twitch notification service and removes its link to the server webhook. The stream index is the number shown with |bot_prefix|\ twclhook.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ twcrhook cycloptux
    |bot_prefix|\ twcrhook 2

....

|bot_prefix|\ twclhook
----------------------
    
Command Description
^^^^^^^^^^^^^^^^^^^
Prints a list of all the Twitch notification services that are linked to webhooks in the current server.
