*******************
Instagram Connector
*******************

The Instagram connector offers an easy way to stream new posts and stories from any Instagram account to one (or more) of the webhooks configured in your Discord server.

.. seealso::
    In order to better understand this module (and the rest of the connector modules), it's very important that you are familiar with Discord webhooks. For more details about this Discord feature, please take a look at `this official guide <https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks>`_.

By default, each new post will be posted to the webhook by using the Instagram account username as author, and the account profile icon (if present) as Discord profile picture. These settings (and other details) can be customized for each stream.

Instagram post URLs will be posted to Discord, while the submission preview will leverage the native parsing of Instagram content offered by Discord (not available at the time of writing this page, but you can use custom header tags to show more info on each post).

This module will only work on **public accounts**.

.. note::
    The goal of this module is offering a **free alternative** to something that is usually only achieved through the use of paid services. On the other hand, due to limitations that are applied to the Instagram API, this module might suffer from delays (new posts will be checked **every 1~3 hours**, and users' info may take up to 24 hours to be refreshed) and/or miss a few posts in high-traffic accounts (**the module will only catch up to 50 new posts in each check window**).

|bot_prefix|\ instahook
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ instahook (Instagram username) (webhook URL or --channel (channel id/mention/q_name)) [customization params]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Starts a streaming service for the selected Instagram account. If a new submission is found, it will be sent to the specified webhook service.

.. warning::
    Discord webhooks are a very powerful feature, but they (currently) lack 2-way authentication of messages. This means that a malicious user knowing a webhook URL will be able, with some effort, to forge a message containing any kind of content using external tools and send that message to the webhook.
    In order to protect yourself from this (rare) occasion, make sure you run this command in non-public channels.
    
.. note::
    Alternatively, you can replace the webhook URL with the ``--channel (channel id/mention/q_name)`` parameter: a new dedicated webhook will be created and the URL from the new webhook will be automatically used for this feed.
    
    This alternative option requires |bot_name| to have "Manage Webhooks" permissions.

**Customization Params**

``--filter (first word) [second word] [...]``
"""""""""""""""""""""""""""""""""""""""""""""

Adds a **whitelist** filter to the stream. In this example, if the post caption contains ``first word`` and/or (see below) ``second word``, the submission will be sent to the webhook, otherwise it will ignored. You can set one or more words, case-insensitive.

You can also set "composite words" (two or more words as a single filter) by quoting them: ``"foo bar" test`` will count as 2 filter elements: ``foo bar`` and ``test``.

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

These parameters will work together with ``--mode (AND/OR)``, allowing the Instagram connector to filter based on INCLUDING the filter items (e.g., at least one filter item (OR) or all filter items (AND) are included in the submission) or EXCLUDING filter items (e.g., post if all filter items are absent from the submission (AND) or at least one filter item is absent from the submission (OR)).

**Default**: ``--include``

.. note::
    Using both parameters in the same command will give ``--include`` the strict priority and ignore ``--exclude``.

``--header (message)``
""""""""""""""""""""""

Sets a new message template for when submissions are posted. Custom headers can have a maximum of **1024** characters.

Custom headers **can** be formatted as embeds by following a very specific syntax. Do know that both |bot_name| and Discord are very sensitive to this specific syntax, which is easily "broken" by special characters: for this reason, using embeds as header is not suggested, nor directly supported. **Use them at your own risk!** If you are brave enough, I suggest the usage of `this embed generator <https://leovoel.github.io/embed-visualizer/>`_ (click on the **"Enable webhook mode"** button at the bottom of the page).

Custom headers support a few dynamic tags that are replaced with their respective "real" value during run-time. These are:

* **%username%**: This will be replaced with the Instagram account username
* **%fullname%**: This will be replaced with the Instagram account full name, as set by the user
* **%caption%**: This will be replaced with the caption/description of the media being posted
* **%media\_url%**: This will be replaced with the direct URL to the media content (image or video) of the post
* **%display\_url%**: This will be replaced with the direct URL to the media content (image if the post is an image, or static image from the video if the post is a video) of the post
* **%hashtags%**: This will be replaced with the list of hashtags that are included in the post
* **%profile\_url%**: This will be replaced with the direct URL to the profile of the user
* **%profile\_pic%**: This will be replaced with the direct URL to the profile picture of the user
* **%total\_posts%**: This will be replaced with the total number of posts from the user, as shown in the user's profile
* **%followed%**: This will be replaced with the total number of accounts that the user if following, as shown in the user's profile
* **%follower%**: This will be replaced with the total number of followers of the user, as shown in the user's profile
* **%timestamp% or %timestamp\_utc%**: This will be replaced with the post creation UTC time, with format ``YYYY-MM-DD HH:mm:ss (UTC)``.
* **%timestamp\_iso%**: This will be replaced with the post creation UTC time, as ISO8601 string.
* **%timestamp\_pst%**: This will be replaced with the post creation PST time, with format ``YYYY-MM-DD HH:mm:ss (PST)``.
* **%url%**: This will be replaced with the Instagram post direct URL. See below for more info.

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

By default, without an explicit use of ``%url%``, all headers will be followed by the actual Instagram post direct URL on a new line.

If the ``%url%`` parameter is used, the default URL will **not** be appended to the custom header.

.. note::
    Do note that Discord doesn't support the automatic rendering of Instagram URLs (yet). If you want to show the content of the Instagram post in Discord, use the above custom tags or keep the default header: the default header builds an embeds that previews the content of the new Instagram post.

**Default**: ``New post from %author%!`` followed by the post URL and an embed showing the post

``--webhook-name (custom name)``
""""""""""""""""""""""""""""""""

Adds a custom username to the webhook when submissions are posted. Custom usernames can have a maximum of 32 characters.

**Default**: New submissions will be displayed by a webhook with the username of the Instagram account

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

    |bot_prefix|\ instahook cristiano https://discord.com/api/webhooks/123456789098765432/LONG_WEBHOOK_TOKEN
    |bot_prefix|\ instahook lamusicanelsilenzio https://discord.com/api/webhooks/123456789098765432/LONG_WEBHOOK_TOKEN --header A wild post appeared!

....

|bot_prefix|\ instaehook
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ instaehook (Instagram username/stream index) [new customization params]

Command Description
^^^^^^^^^^^^^^^^^^^
**Replaces** all previously set customization params for the selected Instagram stream with a new set of customization params. The stream index is the number shown with |bot_prefix|\ instalhook.

.. warning::
    Editing the webhook will not change the existing params, it will completely replace them. Take note of the existing params first, and use them in the command!

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Webhooks

....

|bot_prefix|\ instarhook
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ instarhook (Instagram username/stream index)

Command Description
^^^^^^^^^^^^^^^^^^^
Stops a previously set Instagram stream and removes its link to the server webhook. The stream index is the number shown with |bot_prefix|\ instalhook.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Webhooks

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ instarhook arianagrande
    |bot_prefix|\ instarhook 2

....

|bot_prefix|\ instalhook
------------------------
    
Command Description
^^^^^^^^^^^^^^^^^^^
Prints a list of all the Instagram streams that are linked to webhooks in the current server.
