****************
Reddit Connector
****************

The Reddit connector offers an easy way to stream new submissions from any subreddit to one (or more) of the webhooks configured in your Discord server.

In order to better understand this module (and the rest of the connector modules), it's very important that you are familiar with Discord webhooks. For more details about this Discord feature, please take a look at `this official guide <https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks>`_.

By default, each submission will be posted to the webhook by using the subreddit name (prefixed with ``/r/``) as author, and the subreddit mobile icon (if present) as Discord profile picture. These settings (and other details) can be customized for each stream.

Permalink URLs will be posted to Discord, while the submission preview will leverage the native parsing of Reddit content offered by Discord.

.. note::
    The goal of this module is offering a **free alternative** to something that is usually only achieved through the use of paid services. On the other hand, due to limitations that are applied to the free Reddit API, this module might suffer from delays (new posts will be checked **every 5~15 minutes**) and/or miss a few posts in high-traffic subreddits (**the module will only catch up to 100 new posts in each check window**).
    
.. warning::
    Checks are in place to minimize the amount of duplicate posts that might happen due to a few inconsistencies in the Reddit API. These checks may be less effective when a subreddit is first added, but are built to get better over time.


|bot_prefix|\ reddhook
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ reddhook (subreddit name) (webhook URL) [customization params]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Starts a streaming service for the selected subreddit. If a new submission is found, it will be sent to the specified webhook service.

The subreddit name shall not contain the ``/r/`` or ``r/`` prefixes, but the command should work even if those are used.

**Customization Params**

``--nsfw [censor/skip/only]``
"""""""""""""""""""""""""""""

Reddit submissions might be natively flagged as "NSFW".

Depending on the selected parameter, these are the NSFW behaviors:

* **censor** will post a NSFW URL surrounded by ``< >`` angle brackets, disabling the default Discord URL auto-embed preview. **This censorship will also be applied to the content URL, if it's added to the header using the corresponding placeholder.** Refer to the ``--header`` param for more info.
* **skip** will completely ignore NSFW-flagged items, "cleaning" the stream from NSFW items.
* **only** will only post NSFW-flagged items and skip the rest. The items will not be censored. You can use this mode to create a complementary NSFW stream of the previous "clean" stream.

.. note::
    This check relies on the author (or a very fast moderator) flagging the submission as NSFW. If you know that the subreddit you are going to stream is "safe for work", you can safely skip this check. This is usually the suggested behavior if you know what you're doing.

**Default**: ``false`` (both SFW and NSFW -uncensored- items will be posted), or ``censor`` if ``--nsfw`` is used without any specific mode.

``--flair (first flair) [second flair] [...]``
""""""""""""""""""""""""""""""""""""""""""""""

Adds a **whitelist**, **inclusive** filter for submission flairs to the stream. Links or posts that are flagged with (one of) the selected flair(s) will be sent to the webhook, while the rest will be skipped.

You can also set "composite words" (two or more words as a single flair) by quoting them: ``"foo bar" test`` will accont as 2 flairs filter elements: ``foo bar`` and ``test``. All filters are case-insensitive.

.. warning::
    This parameter will only work for flairs that are present at the time of checking the subreddit. Flairs added at a later date may not work.

**Default**: No filter

``--filter (first word) [second word] [...]``
"""""""""""""""""""""""""""""""""""""""""""""

Adds a **whitelist** filter to the stream. In this example, if the submission contains ``first word`` and/or (see below) ``second word``, the submission will be sent to the webhook, otherwise it will ignored. You can set one or more words, case-insensitive.

You can also set "composite words" (two or more words as a single filter) by quoting them: ``"foo bar" test`` will accont as 2 filter elements: ``foo bar`` and ``test``.

The filter works on partial words (e.g. "announce" will work on both "announcement" and "announced").

**Default**: No filter

``--mode (AND/OR)``
"""""""""""""""""""

Sets the filter behavior when more than 1 word is added to the whitelist filter.

* ``AND`` will only allow submissions that contain *all* of the filtered words.
* ``OR`` will allow submissions that cointain at least one of the filtered words.

**Default**: ``OR``

``--include`` or ``--exclude``
""""""""""""""""""""""""""""""

Sets the filter behavior one or more words are added to the whitelist filter.

* ``--include`` will only allow submissions that contain the filtered word(s).
* ``--exclude`` will only allow submissions that **do not** contain the filtered word(s).

These parameters will work together with ``--mode (AND/OR)``, allowing the Reddit connector to filter based on INCLUDING the filter items (e.g., at least one filter item (OR) or all filter items (AND) are included in the submission) or EXCLUDING filter items (e.g., post if all filter items are absent from the submission (AND) or at least one filter item is absent from the submission (OR)).

**Default**: ``--include``

.. note::
    Using both parameters in the same command will give ``--include`` the strict priority and ignore ``--exclude``.

``--header (message)``
""""""""""""""""""""""

Adds a custom header message when submissions are posted. Custom headers can have a maximum of **1024** characters.

Custom headers support a few dynamic tags that are replaced with their respective "real" value during run-time. These are:

* **%subreddit%**: This will be replaced with the subreddit "technical" name, excluding any prefix (``/r/`` or ``r/``) (e.g. ``askreddit``)
* **%subreddit\_fullname%**: This will be replaced with the subreddit "display" name (e.g. ``Ask Reddit...``)
* **%author%**: This will be replaced with the Reddit account name of the author of the post, excluding any prefix (``/u/`` or ``u/``) (e.g. ``cycloptux``)
* **%title%**: This will be replaced with the title of the submission (e.g. ``Without saying what the category is, what are your top five?``)
* **%flair%**: This will be replaced with the name of the flair assigned to the post, if present, or "*None*" if no flair is assigned
* **%content\_url%**: This will be replaced with the "URL" parameter of a post, which will be an URL to the comments if the post is a text post, or the URL of the content (image, video, link...) otherwise
* **%timestamp% or %timestamp\_utc%**: This will be replaced with the submission creation UTC time, with format ``YYYY-MM-DD HH:mm:ss (UTC)``.
* **%timestamp\_pst%**: This will be replaced with the submission creation PST time, with format ``YYYY-MM-DD HH:mm:ss (PST)``.
* **%url%**: This will be replaced with the Reddit post permalink URL. See below for more info.

By default, without an explicit use of ``%url%``, all headers will be followed by the actual Reddit post permalink URL on a new line; rendering of that URL will be done by Discord.

If the ``%url%`` parameter is used, the default URL will **not** be appended to the custom header.

**Default**: ``New submission in /r/%subreddit% from /u/%author%!``

``--webhook-name (custom name)``
""""""""""""""""""""""""""""""""

Adds a custom username to the webhook when submissions are posted. Custom usernames can have a maximum of 32 characters.

**Default**: New submissions will be displayed by a webhook with the ``/r/`` name of the subreddit (including the prefix itself)

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

    |bot_prefix|\ reddhook tifu https://discordapp.com/api/webhooks/123456789098765432/LONG_WEBHOOK_TOKEN --nsfw
    |bot_prefix|\ reddhook pokemon https://discordapp.com/api/webhooks/123456789098765432/LONG_WEBHOOK_TOKEN --header A wild submission appeared!

....

|bot_prefix|\ reddehook
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ reddehook (subreddit name/stream index) [new customization params]

Command Description
^^^^^^^^^^^^^^^^^^^
**Replaces** all previously set customization params for the selected Reddit stream with a new set of customization params. The stream index is the number shown with |bot_prefix|\ reddlhook.

.. warning::
    Editing the webhook will not change the existing params, it will completely replace them. Take note of the existing params first, and use them in the command!

|bot_prefix|\ reddrhook
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ reddrhook (subreddit name/stream index)

Command Description
^^^^^^^^^^^^^^^^^^^
Stops a previously set Reddit stream and removes its link to the server webhook. The stream index is the number shown with |bot_prefix|\ reddlhook.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ reddrhook pokemon
    |bot_prefix|\ reddrhook 2

....

|bot_prefix|\ reddlhook
-----------------------
    
Command Description
^^^^^^^^^^^^^^^^^^^
Prints a list of all the Reddit streams that are linked to webhooks in the current server.
