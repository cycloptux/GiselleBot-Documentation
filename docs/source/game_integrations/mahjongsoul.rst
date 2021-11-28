************************
Mahjong Soul Integration
************************

This module contains a few commands used to get information about **Mahjong Soul**, a Japanese mahjong game platform developed by Cat Food Studio and distributed, in its English and Japanese version, by Yostar. The game is available as a browser game, with Android and iOS mobile apps to be released in the future.

The game was released in 3 regions/versions:

* **CN** (Chinese)
* **JP** (Japanese)
* **EN** (English/Global)

Commands
========

|bot_prefix|\ mjsstatus
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ mjsstatus [--region {region code}]
    
Command Description
^^^^^^^^^^^^^^^^^^^

Checks the status of Mahjong Soul's game servers. Omitting the region code will assume ``--region en`` and show the status of the (4, at the time of writing this page) English servers.

Examples
^^^^^^^^
.. parsed-literal::
    
    |bot_prefix|\ mjsstatus
    |bot_prefix|\ mjsstatus --region cn
    
....

Server Status Live Feed
=======================

The Mahjong Soul Server Status Feed offers an easy way to monitor Mahjong Soul servers availability for **any region**, and be notified when something changes on one (or more) of the webhooks configured in your Discord server.

.. seealso::
    In order to better understand this module, it's very important that you are familiar with Discord webhooks. For more details about this Discord feature, please take a look at `this official guide <https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks>`_.

By default, the status feed mascot will be the Mahjong Soul character **Ichihime**, and all of the feed messages will be Mahjong Soul-themed.

The full list of feed messages and monitored transitions can be found `in this Google Spreadsheet <https://docs.google.com/spreadsheets/d/1Pp-jVN2KOlx0e0sg0lUldqfNBqtKXs1cUGXdhHHjpLQ/edit?usp=sharing>`_.

.. note::
    The spreadsheet contains a few yellow lines that are currently not used for technical reasons. These will be populated if/when they'll be applicable.

Each message will be followed by a list of hashtags, that users may use to filter the specific messages they are interested into, indicating:

* The region code whom the message refers to: ``#cn`` ``#en`` ``#jp``
* The current status of the region, using a technical status tag: ``#gateway_error`` ``#maintenance`` ``#partial_maintenance`` ``#server_outage`` ``#operational``
* If maintenance notes are found, the message will print the maintenance notes (and track their changes throughout a maintenance).
* The quote ID (refer to the `Mahjong Soul Server Status Feed Sentences Google Spreadsheet <https://docs.google.com/spreadsheets/d/1Pp-jVN2KOlx0e0sg0lUldqfNBqtKXs1cUGXdhHHjpLQ/edit?usp=sharing>`_) for the region status transition and/or server status transition: e.g. ``#r_01`` ``#r_02`` ``s_02`` ...

.. image:: ../images/mahjongsoul_image_00.png
    :width: 600
    :align: center
    :alt: Mahjong Soul Status Feed Example
    
|bot_prefix|\ mjshook
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ mjshook (webhook URL or --channel (channel id/mention/q_name)) [customization params]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Starts a live feed on the specified webhook. When a new transition is found, its notification will be sent to the specified webhook service.

.. warning::
    Discord webhooks are a very powerful feature, but they (currently) lack 2-way authentication of messages. This means that a malicious user knowing a webhook URL will be able, with some effort, to forge a message containing any kind of content using external tools and send that message to the webhook.
    In order to protect yourself from this (rare) occasion, make sure you run this command in non-public channels.
    
.. note::
    Alternatively, you can replace the webhook URL with the ``--channel (channel id/mention/q_name)`` parameter: a new dedicated webhook will be created and the URL from the new webhook will be automatically used for this feed.
    
    This alternative option requires |bot_name| to have "Manage Webhooks" permissions.

**Customization Params**

``--region (first region code) [second region code] [...]``
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Adds a **whitelist**, **inclusive** filter for Mahjong Soul server regions to the stream. Transitions that are referring to (one of) the selected region(s) will be sent to the webhook, while the rest will be skipped.

This parameter only supports these region codes: ``cn`` ``en`` ``jp``

Region codes are case-insensitive.

**Default**: No filter (all regions)

``--filter (first word) [second word] [...]``
"""""""""""""""""""""""""""""""""""""""""""""

Adds a **whitelist** filter to the feed. In this example, if the status quote contains ``first word`` and/or (see below) ``second word``, the submission will be sent to the webhook, otherwise it will ignored. You can set one or more words, case-insensitive. This is especially effective if you are using the provided hashtags to filter specific events of interest.

You can also set "composite words" (two or more words as a single filter) by quoting them: ``"foo bar" test`` will count as 2 filter elements: ``foo bar`` and ``test``.

The filter works on partial words (e.g. "announce" will work on both "announcement" and "announced").

The filter only checks the "quote text", column **G** of the `Mahjong Soul Server Status Feed Sentences Google Spreadsheet <https://docs.google.com/spreadsheets/d/1Pp-jVN2KOlx0e0sg0lUldqfNBqtKXs1cUGXdhHHjpLQ/edit?usp=sharing>`_, and the additional message hashtags (if you filter by hashtag, you must include the "#").

**Default**: No filter

``--mode (AND/OR)``
"""""""""""""""""""

Sets the filter behavior when more than 1 word is added to the whitelist filter.

* ``AND`` will only allow status transition notifications that contain *all* of the filtered words.
* ``OR`` will allow status transition notifications that cointain at least one of the filtered words.

**Default**: ``OR``

``--include`` or ``--exclude``
""""""""""""""""""""""""""""""

Sets the filter behavior one or more words are added to the whitelist filter.

* ``--include`` will only allow status transition notifications that contain the filtered word(s).
* ``--exclude`` will only allow status transition notifications that **do not** contain the filtered word(s).

These parameters will work together with ``--mode (AND/OR)``, allowing the server status feed to filter based on INCLUDING the filter items (e.g., at least one filter item (OR) or all filter items (AND) are included in the submission) or EXCLUDING filter items (e.g., post if all filter items are absent from the submission (AND) or at least one filter item is absent from the submission (OR)).

**Default**: ``--include``

.. note::
    Using both parameters in the same command will give ``--include`` the strict priority and ignore ``--exclude``.

``--header (message)``
""""""""""""""""""""""

Adds a custom header message when status transition notifications are posted. Custom headers can have a maximum of **1024** characters.

Custom headers **can** be formatted as embeds by following a very specific syntax. Do know that both |bot_name| and Discord are very sensitive to this specific syntax, which is easily "broken" by special characters: for this reason, using embeds as header is not suggested, nor directly supported. **Use them at your own risk!** If you are brave enough, I suggest the usage of `this embed generator <https://leovoel.github.io/embed-visualizer/>`_ (click on the **"Enable webhook mode"** button at the bottom of the page).

Custom headers support a few dynamic tags that are replaced with their respective "real" value during run-time. These are:

* **%region%**: This will be replaced with the region name, capitalized (e.g. ``Chinese``, ``English``, ...)
* **%region\_code%**: This will be replaced with the region code, uppercase (e.g. ``CN``, ``EN``, ...)
* **%timestamp% or %timestamp\_utc%**: This will be replaced with the status transition UTC time, with format ``YYYY-MM-DD HH:mm:ss (UTC)``.
* **%timestamp\_iso%**: This will be replaced with the status transition UTC time, as ISO8601 string.
* **%timestamp\_pst%**: This will be replaced with the status transition PST time, with format ``YYYY-MM-DD HH:mm:ss (PST)``.

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

All headers will be followed by the actual quote text, including the additional hashtags.

**Default**: ``Jyanashi Sama, Ichihime here with an important message for you from the %region% region!``

``--webhook-name (custom name)``
""""""""""""""""""""""""""""""""

Adds a custom username to the webhook when status transition notifications are posted. Custom usernames can have a maximum of 32 characters.

**Default**: "MahjongSoul雀魂 Status Feed :: Offered by |bot_name|\ "

``--no-username-overwrite``
"""""""""""""""""""""""""""

Removes any custom name from the webhook. The real webhook name (the one that you assigned when creating the webhook in Discord) will be used.

**Default**: ``false`` (Custom or default names will be applied)

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

    |bot_prefix|\ mjshook https://discord.com/api/webhooks/123456789098765432/LONG_WEBHOOK_TOKEN
    |bot_prefix|\ mjshook https://discord.com/api/webhooks/123456789098765432/LONG_WEBHOOK_TOKEN --region en --header %region\_code% server status changed at %timestamp%

....

|bot_prefix|\ mjsehook
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ mjsehook (feed index) [new customization params]

Command Description
^^^^^^^^^^^^^^^^^^^
**Replaces** all previously set customization params for the selected feed with a new set of customization params. The feed index is the number shown with |bot_prefix|\ mjslhook.

.. warning::
    Editing the webhook will not change the existing params, it will completely replace them. Take note of the existing params first, and use them in the command!

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Webhooks

....

|bot_prefix|\ mjsrhook
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ mjsrhook (feed index)

Command Description
^^^^^^^^^^^^^^^^^^^
Stops a previously set feed and removes its link to the server webhook. The stream index is the number shown with |bot_prefix|\ mjslhook.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Webhooks

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ mjsrhook 1

....

|bot_prefix|\ mjslhook
----------------------
    
Command Description
^^^^^^^^^^^^^^^^^^^
Prints a list of all feeds that are linked to webhooks in the current server.
