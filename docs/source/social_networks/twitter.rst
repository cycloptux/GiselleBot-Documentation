*****************
Twitter Connector
*****************

The Twitter connector offers an easy way to stream tweets from any Twitter account to one (or more) of the webhooks configured in your Discord server.

.. seealso::
    In order to better understand this module (and the rest of the connector modules), it's very important that you are familiar with Discord webhooks. For more details about this Discord feature, please take a look at `this official guide <https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks>`_.

By default, each tweet will be posted to the webhook by using the Twitter account username as author, and Twitter avatar as Discord profile picture. These settings (and other details) can be customized for each stream.

Tweet URLs will be posted to Discord, while the tweet preview will leverage the native parsing of Twitter content offered by Discord.

.. note::
    The goal of this module is offering a **free alternative** to something that is usually only achieved through the use of paid services. On the other hand, due to limitations that are applied to the free Twitter API, this module might suffer from command cooldowns and/or miss a few tweets every once in a while.
    
    
|bot_prefix|\ twthook
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ twthook (Twitter username) (webhook URL or --channel (channel id/mention/q_name)) [customization params]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Starts a streaming service for the selected Twitter account. If a new tweet is found, it will be sent to the specified webhook service.

.. warning::
    Discord webhooks are a very powerful feature, but they (currently) lack 2-way authentication of messages. This means that a malicious user knowing a webhook URL will be able, with some effort, to forge a message containing any kind of content using external tools and send that message to the webhook.
    In order to protect yourself from this (rare) occasion, make sure you run this command in non-public channels.
    
.. note::
    Alternatively, you can replace the webhook URL with the ``--channel (channel id/mention/q_name)`` parameter: a new (unique) webhook will be created and the URL from the new webhook will be automatically used for this feed.
    
    This alternative option requires |bot_name| to have "Manage Webhooks" permissions.

**Customization Params**

``--nsfw [censor/skip/only]``
"""""""""""""""""""""""""""""

Twitter streams may be parsed to look for "bad words" or "possibly sensitive" content before being posted.

Depending on the selected parameter, these are the NSFW behaviors:

* **censor** will post a NSFW URL surrounded by ``< >`` angle brackets, disabling the default Discord URL auto-embed preview.
* **skip** will completely ignore NSFW-flagged items, "cleaning" the stream from NSFW items.
* **only** will only post NSFW-flagged items and skip the rest. The items will not be censored. You can use this mode to create a complementary NSFW stream of the previous "clean" stream.

.. note::
    This check is unaccurate. If you know that the Twitter account you are going to stream is "safe for work", you can safely skip this check. This is usually the suggested behavior if you know what you're doing.

**Default**: ``false`` (both SFW and NSFW -uncensored- items will be posted), or ``censor`` if ``--nsfw`` is used without any specific mode.

``--filter (first word) [second word] [...]``
"""""""""""""""""""""""""""""""""""""""""""""

Adds a **whitelist** filter to the stream. In this example, if the tweet contains ``first word`` and/or (see below) ``second word``, the tweet will be sent to the webhook, otherwise it will ignored. You can set one or more words, case-insensitive.

You can also set "composite words" (two or more words as a single filter) by quoting them: ``"foo bar" test`` will count as 2 filter elements: ``foo bar`` and ``test``.

The filter works on partial words (e.g. "announce" will work on both "announcement" and "announced").

**Default**: No filter

``--mode (AND/OR)``
"""""""""""""""""""

Sets the filter behavior when more than 1 word is added to the whitelist filter.

* ``AND`` will only allow tweets that contain *all* of the filtered words.
* ``OR`` will allow tweets that cointain at least one of the filtered words.

**Default**: ``OR``

``--include`` or ``--exclude``
""""""""""""""""""""""""""""""

Sets the filter behavior one or more words are added to the whitelist filter.

* ``--include`` will only allow tweets that contain the filtered word(s).
* ``--exclude`` will only allow tweets that **do not** contain the filtered word(s).

These parameters will work together with ``--mode (AND/OR)``, allowing the Twitter connector to filter based on INCLUDING the filter items (e.g., at least one filter item (OR) or all filter items (AND) are included in the tweet) or EXCLUDING filter items (e.g., post if all filter items are absent from the tweet (AND) or at least one filter item is absent from the tweet (OR)).

**Default**: ``--include``

.. note::
    Using both parameters in the same command will give ``--include`` the strict priority and ignore ``--exclude``.

``--header (message)``
""""""""""""""""""""""

Adds a custom header message when tweets are posted. Custom headers can have a maximum of **1024** characters.

Custom headers support a few dynamic tags that are replaced with their respective "real" value during run-time. These are:

* **%screen\_name%**: This will be replaced with the ``@`` name of an account, minus the ``@`` (e.g. ``cnnbrk``)
* **%name%**: This will be replaced with the actual name of an account. E.g. ``CNN Breaking News``
* **%timestamp% or %timestamp\_utc%**: This will be replaced with the current UTC time, with format ``YYYY-MM-DD HH:mm:ss (UTC)``.
* **%timestamp\_pst%**: This will be replaced with the current PST time, with format ``YYYY-MM-DD HH:mm:ss (PST)``.
* **%url%**: This will be replaced with the Twitter status URL. See below for more info.

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

By default, without an explicit use of ``%url%``, all headers will be followed by the actual Twitter status URL on a new line; rendering of that URL will be done by Discord.

If the ``%url%`` parameter is used, the default URL will **not** be appended to the custom header.

The Twitter module adds three extra, dynamic placeholders. These dynamic placeholders will be replaced with the corresponding value if the runtime value is present/applicable, or **deleted** if they are not applicable.

These three tags are:

* **%media\_url%**: This will be replaced with the direct URLs to all medias posted in the tweet, each one on a new line.
* **%media\_all\_url\_if\_multiple%**: This will be replaced with the direct URLs to all medias posted in the tweet, each one on a new line, **only if there's more than 1 media in the tweet**.
* **%media\_extra\_url\_if\_multiple%**: This will be replaced with the direct URLs to all medias posted in the tweet **minus the first one**, each one on a new line, **only if there's more than 1 media in the tweet**.

By default, the first media on a tweet is shown in the default Discord preview of the tweet. This means that, by using ``%media_url%`` or ``%media_all_url_if_multiple%``, you will get a duplicate preview of the first available media (one from the Twitter preview itself, one from the direct link preview.

By using ``%media_extra_url_if_multiple%`` you can avoid the first media URL from being posted, hence having the default Twitter preview for the first media, and the direct URLs for the 2nd onwards.

**Default**: ``New tweet from %name%!``

``--webhook-name (custom name)``
""""""""""""""""""""""""""""""""

Adds a custom username to the webhook when tweets are posted. Custom usernames can have a maximum of 32 characters.

**Default**: New tweets will be displayed by a webhook with the screen name of the Twitter account (the ``@`` name of that account, minus the ``@``)

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

    |bot_prefix|\ twthook cnnbrk https://discordapp.com/api/webhooks/123456789098765432/LONG_WEBHOOK_TOKEN --nsfw
    |bot_prefix|\ twthook pokemon https://discordapp.com/api/webhooks/123456789098765432/LONG_WEBHOOK_TOKEN --header A wild tweet appeared!

....

|bot_prefix|\ twtehook
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ twtehook (Twitter username/stream index) [new customization params]

Command Description
^^^^^^^^^^^^^^^^^^^
**Replaces** all previously set customization params for the selected Twitter stream with a new set of customization params. The stream index is the number shown with |bot_prefix|\ twtlhook.

.. warning::
    Editing the webhook will not change the existing params, it will completely replace them. Take note of the existing params first, and use them in the command!

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Webhooks

....

|bot_prefix|\ twtrhook
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ twtrhook (Twitter username/stream index)

Command Description
^^^^^^^^^^^^^^^^^^^
Stops a previously set Twitter stream and removes its link to the server webhook. The stream index is the number shown with |bot_prefix|\ twtlhook.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Webhooks

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ twtrhook pokemon
    |bot_prefix|\ twtrhook 2

....

|bot_prefix|\ twtlhook
----------------------
    
Command Description
^^^^^^^^^^^^^^^^^^^
Prints a list of all the Twitter streams that are linked to webhooks in the current server.
