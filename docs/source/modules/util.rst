****************
Utility Commands
****************

This module contains generally useful, atomic commands that aren't otherwise categorized into a dedicated module.

These commands might be safe for use by anyone, or locked behind in-Discord permissions.

|bot_prefix|\ searchuser
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ searchuser (user id/mention/name, or a substring of the user's name or discriminator)

Command Description
^^^^^^^^^^^^^^^^^^^
Searches for a user and returns the known info about that user.

You can use the exact username, or look for users by using a substring of their name (this will only scan the bot cache).

.. note::
    Generally speaking, the bot will look into its cache to find the Discord user(s). If you want to look for uncached users, you **must** use their ID.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ searchuser cyclopt
    |bot_prefix|\ searchuser 1543
    |bot_prefix|\ searchuser cycloptux#1543
    |bot_prefix|\ searchuser 123456789098765432
    
....

|bot_prefix|\ embed
-------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ embed (text build with Nadeko's embed builder, or using embed enhancer tags)

Command Description
^^^^^^^^^^^^^^^^^^^
Answers to the author's message with an embedded message.

In order to customize your embed, you can either use:

* `NadekoBot's Embed Builder <https://eb.nadeko.bot/>`_
* The available embed enhancer tags

Embed enhancer tags are words in the form ``{tag}`` that are used to set a few fields of an embed. Currently, these tags are supported:

* ``{title}`` sets the title for the embed.
* ``{url}`` sets an URL for the embed, which means clicking on the title will bring users to the specified URL.
* ``{footer}`` sets the footer for the embed (the small text at the bottom of the embed).
* ``{color}`` sets the color for the embed. You need to use an hex code to select a color.
* ``{image}`` and ``{thumbnail}`` will set the bottom image and top-right thumbnail within the embed.

.. seealso::
    Do you need ideas for your embed color? Try these links:
    `Random Hex Color Code Generator <https://www.random.org/colors/hex>`_
    `HTML Color Picker <https://www.w3schools.com/colors/colors_picker.asp>`_
    `BrandColors <https://brandcolors.net/>`_

.. note::
    A few things to know when building your embed with the enhancer tags:

    * Tags have to start on a new line, surrounded by ``{ }`` parenthesis.
    * URLs have to be complete and correct, including the http*:// prefix.
    * Supported image formats are \*.png, \*.jpg, \*.jpeg.
    * If you need to add something that looks like an enhancer tag in your recruitment message, you can "escape" by prepending it with ``\``
    
.. warning:: 
    `Discord's native limits <https://discordapp.com/developers/docs/resources/channel#embed-limits>`_ for embeds still apply.

Examples
^^^^^^^^
.. parsed-literal::
    
    |bot_prefix|\ embed { "description": "Hello world!" }
    |bot_prefix|\ embed {title} Hey I'm recruiting! This is my title, it can hold up to 256 characters!
        {color} #ffffff
        {footer} This is your fancy footer text.
        {url} https://discord.gg/bravenetwork
        {image} https://b.thumbs.redditmedia.com/t5OGyddII6m8aBeYlSDXUkvJeOVYP4DpH594oqgnn7U.png
        {thumbnail} https://i.imgur.com/HoBQiSI.png
    
....

|bot_prefix|\ serverinfo
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ sinfo

Command Description
^^^^^^^^^^^^^^^^^^^
Prints a bunch of info about the current server.

....

|bot_prefix|\ serveremojis
--------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ semoji

Command Description
^^^^^^^^^^^^^^^^^^^
Shows all of the emojis from the current server into an embed.

....

|bot_prefix|\ emojify
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ emojify (any number of emoji names, without the : :)

Command Description
^^^^^^^^^^^^^^^^^^^

Converts a sequence of words into a sequence of emojis, provided the bot has access to the emojis.

Emoji names are case-sensitive.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ emojify BlobOwO BlobPats

....

|bot_prefix|\ savechat
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ savechat [# of messages]

Command Description
^^^^^^^^^^^^^^^^^^^

Dumps a certain number of messages from the channel in which the command is run. The saved messages are compiled into a ``.csv`` file.

The file will be sent to the author of the command via Direct Message. Instead of receiving the actual file as Discord attachment, the author will receive:

* An URL to an **encrypted** ``.zip`` file containing the actual ``.csv``.
* The password to decrypt the archive.

.. note::
    The archive password is unknown to anyone but the author of the command, not even the bot developer!
    The archive will only be available for 30 days, after which it will be deleted.

If the number of messages isn't specified, the default value of **150** messages will be used.

.. warning::
    This command might be very slow, or even fail, if you are trying to dump a high amount of messages. Please be patient.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ savechat 500

....

.. _roleid:

|bot_prefix|\ roleid
--------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rid (role name, or a substring of the role name)

Command Description
^^^^^^^^^^^^^^^^^^^

While offering easy ways of obtaining the IDs of a certain number of entities, Discord doesn't offer an easy way to get the ID of a role, which is often needed for bot commands (see :ref:`discord-ids`).

This commands shows a list of roles and the corresponding IDs found, starting from the name (or substring thereof) of the role. The lookup string is case-insensitive.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ roleid Discord Moderator
    |bot_prefix|\ rid moder
    
.... 

|bot_prefix|\ inrole
--------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ inrole (role id/mention/name)

Command Description
^^^^^^^^^^^^^^^^^^^

Prints the list of users that currently have the specified role.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ inrole Discord Moderator
    |bot_prefix|\ inrole 123456789098765432 
    
....

|bot_prefix|\ addrole
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ addrole (user id(s)/mention(s)/q_name(s)) (role id(s)/mention(s)/q_name(s))

Command Description
^^^^^^^^^^^^^^^^^^^

Adds any number of roles to any number of users.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Roles
| **Bot**: Manage Roles

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ addrole "Discord Moderator" @cycloptux#1543 NaviKing#3820
    |bot_prefix|\ addrole cycloptux#1543 Staff "Network Developer"
    
....

|bot_prefix|\ remrole
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ remrole (user id(s)/mention(s)/q_name(s)) (role id(s)/mention(s)/q_name(s))

Command Description
^^^^^^^^^^^^^^^^^^^
Removes any number of roles from any number of users.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Roles
| **Bot**: Manage Roles

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ remrole "Discord Moderator" @cycloptux#1543 NaviKing#3820
    |bot_prefix|\ remrole cycloptux#1543 Staff "Network Developer"

....

.. _deletedm:

|bot_prefix|\ deletedm
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ deletedm (message id)
    
Command Description
^^^^^^^^^^^^^^^^^^^
.. note::
    This command is only available in a Direct Message channel with the bot. It will **not** work in actual servers, and it's not subject to any permissions.

Deletes a direct message sent by the bot. This can be particularly useful as a privacy/security feature to delete previously sent passwords to encrypted archives, in order to make them completely unrecoverable.

.. seealso::
    Refer to :ref:`discord-ids` if you don't know how to obtain a message ID.

.. note::
    Non-sensitive direct messages (e.g. moderation actions) might still be logged into the owner-restricted bot console.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ deletedm 123456789098765432
