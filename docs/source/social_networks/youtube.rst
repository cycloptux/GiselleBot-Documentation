*****************
YouTube Connector
*****************

The YouTube module & connector offers two macro-features:

* A set of commands to interact with YouTube to get info about videos and channels/users.
* A notification service which can monitor YouTube channels/users uploading new videos (or updating their titles and descriptions), sending these notifications to one (or more) of the webhooks configured in your Discord server.

.. note::
    Throughout the documentation, the **YouTube channel identifier** refers to:

    * The ID of the channel, which is usually the ``XXXXXX`` part of the YouTube URL ``https://www.youtube.com/channel/XXXXXXXXXXXXXXXXXXXXXXXX``.
    * The name (or handle) of the channel, which is usually the ``YYYYYY`` part of the YouTube URL ``https://www.youtube.com/YYYYYYYYYY`` (sometimes prepended with a ``@``).
    * The display name of the channel, which is usually the name you can see above the username of the YouTube user on the home page of a channel.

Commands
========

|bot_prefix|\ ytchannel
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ ytchannel (YouTube channel identifier)

Command Description
^^^^^^^^^^^^^^^^^^^
Searches for YouTube channels (formerly, users) based on the selected identifier (the ID, or the username, or the channel display name), and returns detailed info about the top result.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ ytchannel vsauce
    |bot_prefix|\ ytchannel UC6nSFpj9HTCZ5t-N3Rm3-HA
    |bot_prefix|\ ytchannel https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA
    
....

|bot_prefix|\ ytvideo
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ ytvideo (YouTube video identifier)

Command Description
^^^^^^^^^^^^^^^^^^^
Searches for a YouTube video based on the selected identifier (the ID, or the video name), and returns detailed info about the top result.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ ytvideo p-VDVI1GMZk
    |bot_prefix|\ ytvideo https://youtu.be/p-VDVI1GMZk
    
....

|bot_prefix|\ ytsearch
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ ytsearch (search string)

Command Description
^^^^^^^^^^^^^^^^^^^
Searches for YouTube videos based on the selected lookup string, and returns basic info about the found videos.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ ytsearch veritasium
    
....

|bot_prefix|\ ytwatch
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ ytwatch (search string)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Searches for YouTube videos based on the selected lookup string and posts an URL to the top result. Discord includes a native auto-preview which lets users play the YouTube video in the current channel.
    
Examples
^^^^^^^^
.. parsed-literal::
    
    |bot_prefix|\ ytwatch despacito
    
....

YouTube Notifications
=====================

.. seealso::
    In order to better understand this module (and the rest of the connector modules), it's very important that you are familiar with Discord webhooks. For more details about this Discord feature, please take a look at `this official guide <https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks>`_.

By default, each notification will be posted to the webhook by using the YouTube channel name as author, and YouTube channel thumbnail as Discord profile picture. These settings (and other details) can be customized for each stream.

YouTube video URLs will be posted to Discord, while the YouTube video preview will leverage the native parsing of YouTube content offered by Discord.

|bot_prefix|\ ythook
--------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ ythook (YouTube channel identifier) (webhook URL or --channel (channel id/mention/q_name)) [customization params]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Starts a notification service for the selected YouTube channel. If a new video is uploaded on the channel, a notification will be sent to the specified webhook service.

.. warning::
    Discord webhooks are a very powerful feature, but they (currently) lack 2-way authentication of messages. This means that a malicious user knowing a webhook URL will be able, with some effort, to forge a message containing any kind of content using external tools and send that message to the webhook.
    In order to protect yourself from this (rare) occasion, make sure you run this command in non-public channels.
    
.. note::
    Alternatively, you can replace the webhook URL with the ``--channel (channel id/mention/q_name)`` parameter: a new dedicated webhook will be created and the URL from the new webhook will be automatically used for this feed.
    
    This alternative option requires |bot_name| to have "Manage Webhooks" permissions.

**Customization Params**

``--nsfw [censor/skip/only]``
"""""""""""""""""""""""""""""

YouTube videos may be flagged as "age-restricted content". When this setting is applied on the uploaded video, the video will be flagged as "NSFW" within the notifications stream.

Depending on the selected parameter, these are the NSFW behaviors:

* **censor** will post a NSFW URL surrounded by ``< >`` angle brackets, disabling the default Discord URL auto-embed preview.
* **skip** will completely ignore NSFW-flagged items, "cleaning" the stream from NSFW items.
* **only** will only post NSFW-flagged items and skip the rest. The items will not be censored. You can use this mode to create a complementary NSFW stream of the previous "clean" stream.

**Default**: ``false`` (both SFW and NSFW -uncensored- items will be posted), or ``censor`` if ``--nsfw`` is used without any specific mode.

``--filter (first word) [second word] [...]``
"""""""""""""""""""""""""""""""""""""""""""""

Adds a **whitelist** filter to the stream. In this example, if the YouTube video title contains ``first word`` and/or (see below) ``second word``, the notification will be sent to the webhook, otherwise it will be ignored. You can set one or more words, case-insensitive.

You can also set "composite words" (two or more words as a single filter) by quoting them: ``"foo bar" test`` will count as 2 filter elements: ``foo bar`` and ``test``.

The filter works on partial words (e.g. "announce" will work on both "announcement" and "announced").

**Default**: No filter

``--mode (AND/OR)``
"""""""""""""""""""

Sets the filter behavior when more than 1 word is added to the whitelist filter.

* ``AND`` will only allow YouTube videos that contain *all* of the filtered words in their title.
* ``OR`` will allow YouTube videos that cointain at least one of the filtered words in their title.

**Default**: ``OR``

``--include`` or ``--exclude``
""""""""""""""""""""""""""""""

Sets the filter behavior one or more words are added to the whitelist filter.

* ``--include`` will only allow YouTube videos that contain the filtered word(s) in their title.
* ``--exclude`` will only allow YouTube videos that **do not** contain the filtered word(s) in their title.

These parameters will work together with ``--mode (AND/OR)``, allowing the YouTube connector to filter based on INCLUDING the filter items (e.g., at least one filter item (OR) or all filter items (AND) are included in the video title) or EXCLUDING filter items (e.g., post if all filter items are absent from the video title (AND) or at least one filter item is absent from the video title (OR)).

**Default**: ``--include``

.. note::
    Using both parameters in the same command will give ``--include`` the strict priority and ignore ``--exclude``.

``--header (message)``
""""""""""""""""""""""

Sets a new message template for when notifications are posted. Custom headers can have a maximum of **1024** characters.

Custom headers **can** be formatted as embeds by following a very specific syntax. Do know that both |bot_name| and Discord are very sensitive to this specific syntax, which is easily "broken" by special characters: for this reason, using embeds as header is not suggested, nor directly supported. **Use them at your own risk!** If you are brave enough, I suggest the usage of `this embed generator <https://leovoel.github.io/embed-visualizer/>`_ (click on the **"Enable webhook mode"** button at the bottom of the page).

Custom headers support a few dynamic tags that are replaced with their respective "real" value during run-time. These are:

* **%title%**: This will be replaced with the YouTube video title.
* **%channel%**: This will be replaced with the YouTube channel name.
* **%duration%**: This will be replaced with the YouTube video duration.
* **%timestamp% or %timestamp\_utc%**: This will be replaced with the video upload timestamp in UTC time, with format ``YYYY-MM-DD HH:mm:ss (UTC)``.
* **%timestamp\_iso%**: This will be replaced with the video upload timestamp in UTC time, as ISO8601 string.
* **%timestamp\_pst%**: This will be replaced with the video upload timestamp in PST time, with format ``YYYY-MM-DD HH:mm:ss (PST)``.
* **%url%**: This will be replaced with the YouTube video URL. See below for more info.

Timestamp tags also support custom time zones. You can replace the ``utc`` part with either:

* A different **valid** time zone identifier: use the :ref:`searchtz` command to look for a valid time zone name.
* An **UTC offset**, in the form of ``[UTC/GMT](+/-)(hours)[:][minutes]``. Here are some valid examples:

    * %timestamp\_Europe/London%
    * %timestamp\_America/Los_Angeles%
    * %timestamp\_Japan%
    * %timestamp\_PST8PDT%
    * %timestamp\_+0800%
    * %timestamp\_-10:30%
    * %timestamp\_UTC+2%

By default, without an explicit use of ``%url%``, all headers will be followed by the actual YouTube video URL on a new line; rendering of that URL will be done by Discord.

If the ``%url%`` parameter is used, the default URL will **not** be appended to the custom header.

The YouTube module also supports a few extra, dynamic placeholders. These dynamic placeholders will be replaced with the corresponding value if the runtime value is present/applicable, or **deleted** if they are not applicable:

* **%description%**: This will be replaced with the description of the video, if present and not empty (the description length is truncated at 1024 characters).
* **%short\_description%**: This will be replaced with a shorter version of the description of the video, if present and not empty (the description length is truncated at 256 characters).
* **%tags%**: This will be replaced with a space-delimited list of tags applied to the video, if at least one tag is applied. The tags will be surrounded by \` \` characters.
* **%thumbnail%**: This will be replaced with the direct URL of the video thumbnail, unless the thumbnail is absent (this is not supposed to happen, but might happen for unknown reasons).

**Default**: ``%channel% just %video_status% a video!`` followed by the video Title, Description, Duration and Tags

``--webhook-name (custom name)``
""""""""""""""""""""""""""""""""

Adds a custom username to the webhook when notifications are posted. Custom usernames can have a maximum of 32 characters.

**Default**: Notifications will be posted by a webhook named after the YouTube channel name

``--no-username-overwrite``
"""""""""""""""""""""""""""

Removes any custom name from the webhook. The real webhook name (the one that you assigned when creating the webhook in Discord) will be used.

**Default**: ``false`` (Custom or automated names will be applied)

``--no-avatar-overwrite``
"""""""""""""""""""""""""

Removes any custom avatar from the webhook. The real webhook avatar (the one that you assigned when creating the webhook in Discord) will be used.

**Default**: ``false`` (Automated avatars will be applied)

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Webhooks

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ ythook vsauce https://discord.com/api/webhooks/123456789098765432/LONG_WEBHOOK_TOKEN --nsfw
    |bot_prefix|\ ythook NASAgovVideo https://discord.com/api/webhooks/123456789098765432/LONG_WEBHOOK_TOKEN --header Recognized activity in %channel%!

....

|bot_prefix|\ ytehook
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ ytehook (YouTube channel identifier/stream index) [new customization params]

Command Description
^^^^^^^^^^^^^^^^^^^
**Replaces** all previously set customization params for the selected YouTube notification service with a new set of customization params. The stream index is the number shown with |bot_prefix|\ ytlhook.

.. warning::
    Editing the webhook will not change the existing params, it will completely replace them. Take note of the existing params first, and use them in the command!

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Webhooks

....

|bot_prefix|\ ytrhook
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ ytrhook (YouTube channel identifier/stream index)

Command Description
^^^^^^^^^^^^^^^^^^^
Stops a previously set YouTube notification service and removes its link to the server webhook. The stream index is the number shown with |bot_prefix|\ ytlhook.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Webhooks

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ ytrhook vsauce
    |bot_prefix|\ ytrhook 2

....

|bot_prefix|\ ytlhook
---------------------
    
Command Description
^^^^^^^^^^^^^^^^^^^
Prints a list of all the YouTube notification services that are linked to webhooks in the current server.
