****
Send
****

This module allows authorized users to send messages through the bot, and/or editing previously sent messages.

.. _msgsend:

|bot_prefix|\ msgsend
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ msgsend (channel id/mention) (message to send)

Command Description
^^^^^^^^^^^^^^^^^^^
Send a message to a channel in the current server.

You can use embed json from https://eb.nadeko.bot/ instead of a regular text, if you want the message to be embedded.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ msgsend #this-channel Hello world!
    |bot_prefix|\ msgsend #that-channel { "description": "Hello world!" }

....

|bot_prefix|\ msgedit
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ msgedit (message id) (new message content)

Command Description
^^^^^^^^^^^^^^^^^^^
Edits a previously sent message in the current server.

You can use embed json from https://eb.nadeko.bot/ instead of a regular text, if you want the message to be embedded.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ msgedit 123456789098765432 Hello world! I'm alive!
