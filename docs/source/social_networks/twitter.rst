*****************
Twitter Connector
*****************

The Twitter connector offers an easy way to stream tweets from any Twitter account to one (or more) of the webhooks configured in your Discord server.

In order to better understand this module (and the rest of the connector modules), it's very important that you are familiar with Discord webhooks. For more details about this Discord feature, please take a look at `this official guide <https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks>`_.

By default, each tweet will be posted to the webhook by using the Twitter account username as author, and Twitter avatar as Discord profile picture. These settings (and other details) can be customized for each stream.

Tweet URLs will be posted to Discord, while the tweet preview will leverage the native parsing of Twitter content offered by Discord.

.. note::
    The goal of this module is offering a **free alternative** to something that is usually only achieved through the use of paid services. On the other hand, due to limitations that are applied to the free Twitter API, this module might suffer from command cooldowns and/or miss a few tweets every once in a while.

|bot_prefix|\ twthook
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ twthook (twitter username) (webhook URL) [customization params]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Starts a streaming service for the selected Twitter account. If a new tweet is found, it will be sent to the specified webhook service.

**Customization Params**

``--nsfw``
""""""""""

Twitter streams may be parsed to look for "bad words" or "possibly sensitive" content before being posted. If this parameter is used, any content that triggers the sensitive check will still sent to your webhook, but the URL will be flagged with a short description of the alarm that was triggered and the tweet won't be previewed in Discord.

.. note::
    This check is unaccurate. If you know that the Twitter account you are going to stream is "safe for work", you can safely skip this check. This is usually the suggested behavior if you know what you're doing.

**Default**: ``false`` (tweets won't be censored)

``--filter (first word) [second word] [...]``
"""""""""""""""""""""""""""""""""""""""""""""

Adds a **whitelist** filter to the stream. In this example, if the tweet contains ``first word`` and/or (see below) ``second word``, the tweet will be sent to the webhook, otherwise it will ignored. You can set one or more words, case-insensitive.

You can also set "composite words" (two or more words as a single filter) by quoting them: ``"foo bar" test`` will accont as 2 filter elements: ``foo bar`` and ``test``.

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

All headers will be followed by the actual Twitter status URL, rendering of that URL will be done by Discord.

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

|bot_prefix|\ twtrhook
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ twtrhook (Twitter username/stream index)

Command Description
^^^^^^^^^^^^^^^^^^^
Stops a previously set Twitter stream and removes its link to the server webhook. The stream index is the number shown with |bot_prefix|\ twtlhook.

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
