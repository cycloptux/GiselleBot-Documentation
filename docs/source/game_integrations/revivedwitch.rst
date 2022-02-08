***********************
Revived Witch Connector
***********************

This module sends news from **Revived Witch**, a pixel-art RPG mobile game distributed by Yostar, to the specified webhook or channel.

.. seealso::
    In order to better understand this module, it's very important that you are familiar with Discord webhooks. For more details about this Discord feature, please take a look at `this official guide <https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks>`_.

    
|bot_prefix|\ rwhook
--------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rwhook (webhook URL or --channel (channel id/mention/q_name)) [customization params]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Starts a live feed on the specified webhook. When some news is found, they will be sent to the specified webhook service.

.. warning::
    Discord webhooks are a very powerful feature, but they (currently) lack 2-way authentication of messages. This means that a malicious user knowing a webhook URL will be able, with some effort, to forge a message containing any kind of content using external tools and send that message to the webhook.
    In order to protect yourself from this (rare) occasion, make sure you run this command in non-public channels.
    
.. note::
    Alternatively, you can replace the webhook URL with the ``--channel (channel id/mention/q_name)`` parameter: a new dedicated webhook will be created and the URL from the new webhook will be automatically used for this feed.
    
    This alternative option requires |bot_name| to have "Manage Webhooks" permissions.

**Customization Params**

``--event (first event) [second event] [...]``
""""""""""""""""""""""""""""""""""""""""""""""

Adds a **whitelist**, **inclusive** filter for specific news events to the service. News will only be sent if the actual news type is equal to one of the filtered events.

The **only** supported events for this feed are: ``Updates``, ``Event``, ``Notice``

**Default**: No filter

``--filter (first word) [second word] [...]``
"""""""""""""""""""""""""""""""""""""""""""""

Adds a **whitelist** filter to the feed. In this example, if the news title contains ``first word`` and/or (see below) ``second word``, the event will be sent to the webhook, otherwise it will be ignored. You can set one or more words, case-insensitive.

You can also set "composite words" (two or more words as a single filter) by quoting them: ``"foo bar" test`` will count as 2 filter elements: ``foo bar`` and ``test``.

The filter works on partial words (e.g. "announce" will work on both "announcement" and "announced").

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

Sets a new message template for when status transition notifications are posted. Custom headers can have a maximum of **1024** characters.

Custom headers **can** be formatted as embeds by following a very specific syntax. Do know that both |bot_name| and Discord are very sensitive to this specific syntax, which is easily "broken" by special characters: for this reason, using embeds as header is not suggested, nor directly supported. **Use them at your own risk!** If you are brave enough, I suggest the usage of `this embed generator <https://leovoel.github.io/embed-visualizer/>`_ (click on the **"Enable webhook mode"** button at the bottom of the page).

Custom headers support a few dynamic tags that are replaced with their respective "real" value during run-time. These are:

* **%title%**: This will be replaced with the news title.
* **%content%**: This will be replaced with the news content (truncated at 1024 characters).
* **%short\_content%**: This will be replaced with a shorter version of the news content (truncated at 256 characters).
* **%banner%**: This will be replaced with the news banner URL, if present.
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

**Default**: ``Dear Master, some news was just published!``

``--webhook-name (custom name)``
""""""""""""""""""""""""""""""""

Adds a custom username to the webhook when status transition notifications are posted. Custom usernames can have a maximum of 32 characters.

**Default**: "Revived Witch News Feed :: Offered by |bot_name|\ "

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

    |bot_prefix|\ rwhook https://discord.com/api/webhooks/123456789098765432/LONG_WEBHOOK_TOKEN
    |bot_prefix|\ rwhook https://discord.com/api/webhooks/123456789098765432/LONG_WEBHOOK_TOKEN --event Updates --header An update notification was just published at %timestamp%

....

|bot_prefix|\ rwehook
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rwehook (feed index) [new customization params]

Command Description
^^^^^^^^^^^^^^^^^^^
**Replaces** all previously set customization params for the selected feed with a new set of customization params. The feed index is the number shown with |bot_prefix|\ rwlhook.

.. warning::
    Editing the webhook will not change the existing params, it will completely replace them. Take note of the existing params first, and use them in the command!

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Webhooks

....

|bot_prefix|\ rwrhook
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rwrhook (feed index)

Command Description
^^^^^^^^^^^^^^^^^^^
Stops a previously set feed and removes its link to the server webhook. The stream index is the number shown with |bot_prefix|\ rwlhook.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Webhooks

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rwrhook 1

....

|bot_prefix|\ rwlhook
---------------------
    
Command Description
^^^^^^^^^^^^^^^^^^^
Prints a list of all feeds that are linked to webhooks in the current server.
