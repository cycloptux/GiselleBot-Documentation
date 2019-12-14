****************
Utility Commands
****************

This module contains generally useful, atomic commands that aren't otherwise categorized into a dedicated module.

These commands might be safe for use by anyone, or locked behind in-Discord permissions.

.. _nsfwjs:

NSFW Images Detection Tools
===========================

|bot_name| implements an (experimental) **NSFW images detection system** using **TensorFlow.js** as its base.

The detection system is based on `Infinite Red's NSFW JS library <https://nsfwjs.com/>`_ and `GantMan's Inception v3 Keras Model for NSFW detection <https://github.com/gantman/nsfw_model/>`_ to classify any image as a composition of **5** categories:

* **Drawings**: Safe for work drawings (including anime).
* **Hentai**: Hentai and pornographic drawings.
* **Neutral**: Safe for work neutral images.
* **Porn**: Pornographic images, sexual acts.
* **Sexy**: Sexually explicit images, not pornography.

The module was furtherly converted into a back-end module and customized with a caching system to enhance its performance.

.. seealso::
    `This interesting article by Infinite Red <https://nsfwjs.com/>`_ explains the reasons behind the creation of the original NSFW JS client-side module.

.. warning::
    This module, by no means, is supposed to reliably recognize all NSFW images. Its main purpose is quickly classifying provided images and supporting humans in better moderating a server.
    
    The module itself will not store or expose any sexually explicit images. The output will not contain a direct link to the original image, and a censored (low resolution, blurred) version of the image will be locally cached and used to refer to the original image.
    
Here's an example of an output of this command, and the corresponding censored image:

.. image:: ../images/util_image_00.png
    :width: 600
    :align: center
    :alt: NSFW Images Detection Output Example
    
.. image:: ../images/util_image_01.jpg
    :align: center
    :alt: NSFW Images Detection Censored Image Example    
    
.. seealso::
    For those of you with a background in image processing - yes, **Lenna** is actually flagged as **NSFW with a confidence score of 81.9%!**
    
    If you don't know what I'm talking about, refer to `this Wikipedia page <https://en.wikipedia.org/wiki/Lenna>`_.

|bot_prefix|\ nsfwcheck
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ nsfwcheck (image URL, or image as a message attachment)
    
Command Description
^^^^^^^^^^^^^^^^^^^

Submits an image against the `GantMan's Inception v3 Keras Model for NSFW detection <https://github.com/gantman/nsfw_model/>`_ (as explained above) and returns a detailed output about the classification.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ nsfwcheck http://www.lenna.org/lena_std.tif
    
....

|bot_prefix|\ nsfwcache
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ nsfwcache (cache ID)
    
Command Description
^^^^^^^^^^^^^^^^^^^

Recalls an image classification output by its cache ID (as given in the footer of the |bot_prefix|\ nsfwcheck command.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ nsfwcache 5d6c4cd78e422b00137d14ce
    
....

.. _nsfwthreshold:

|bot_prefix|\ nsfwthreshold
---------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ nsfwthreshold [new threshold, or "-"]
    
Command Description
^^^^^^^^^^^^^^^^^^^

While the classification scores given to an image cannot be tuned, each server can choose its own NSFW threshold (the sum of NSFW-related scores over which an image is considered NSFW).

The new threshold is an integer within the range ``[0, 100]``, inclusive of ``0`` (treat **all** images as NSFW) and ``100`` (only treat an image as NSFW if the model recognize it as having no-SFW components - which is highly unlikely, hence basically meaning "treat **no** images as NSFW").

Running the command with ``-`` as argument will reset the server threshold to the global, default threshold of **60%**.

Running the command with no arguments will show the current value for the server.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ nsfwthreshold 80
    |bot_prefix|\ nsfwthreshold -
    |bot_prefix|\ nsfwthreshold
    
Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Administrator

....

Server-related Tools
====================

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

Message-related Tools
=====================

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

|bot_prefix|\ pin
-----------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ pin [message ID(s)]

Command Description
^^^^^^^^^^^^^^^^^^^
Pins one or more messages in the current channel. Provide no arguments to pin the latest message in the current channel (before the actual |bot_prefix|\ pin command message).

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Messages
| **Bot**: Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ pin
    |bot_prefix|\ pin 123456789098765432
    |bot_prefix|\ pin 123456789098765432 234567890987654321 345678909876543212

....

|bot_prefix|\ unpin
-------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ unpin [message ID(s)]

Command Description
^^^^^^^^^^^^^^^^^^^
Unpins one or more messages in the current channel. Provide no arguments to unpin the latest message in the current channel (before the actual |bot_prefix|\ unpin command message).

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Messages
| **Bot**: Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ unpin
    |bot_prefix|\ unpin 123456789098765432
    |bot_prefix|\ unpin 123456789098765432 234567890987654321 345678909876543212

....

|bot_prefix|\ toggleembed
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ temb [message ID(s)]

Command Description
^^^^^^^^^^^^^^^^^^^
Hides or unhides an embed in a message. Provide no arguments to hide/unhide the latest message containing an embed in the current channel.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Messages
| **Bot**: Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ temb
    |bot_prefix|\ temb 123456789098765432
    |bot_prefix|\ temb 123456789098765432 234567890987654321 345678909876543212

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

....

Role-related Tools
==================

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

.. _addrole:

|bot_prefix|\ addrole
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ addrole (user id(s)/mention(s)/q_name(s)) (role id(s)/mention(s)/q_name(s))

Command Description
^^^^^^^^^^^^^^^^^^^

Adds any number of roles to any number of users. If ``@everyone`` (or the server ID) is used as one of the parameters, the role(s) will be given to everyone in the server.

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

.. _remrole:

|bot_prefix|\ remrole
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ remrole (user id(s)/mention(s)/q_name(s)) (role id(s)/mention(s)/q_name(s))

Command Description
^^^^^^^^^^^^^^^^^^^
Removes any number of roles from any number of users. If ``@everyone`` (or the server ID) is used as one of the parameters, the role(s) will be removed from everyone in the server.

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

Other Tools
===========

.. _shorturl:

|bot_prefix|\ shorturl
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ shorturl (long URL)

Command Description
^^^^^^^^^^^^^^^^^^^

Converts a long URL into a short URL using the proprietary **gisl.eu** shortening service.

.. note::
    URLs shortened using the gisl.eu service never expire, unless deleted by the person that created the short URL (feature not available yet).

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ shorturl http://www.amazon.com/Kindle-Wireless-Reading-Display-Globally/dp/B003FSUDM4/ref=amb_link_353259562_2?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=center-10&pf_rd_r=11EYKTN682A79T370AM3&pf_rd_t=201&pf_rd_p=1270985982&pf_rd_i=B002Y27P3M 
