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

    |bot_prefix|\ msgsend (channel id/mention) [message to send]

Command Description
^^^^^^^^^^^^^^^^^^^
Sends a message to a channel in the current server.

You can use embed json from https://eb.nadeko.bot/ instead of a regular text, if you want the message to be embedded.

You can attach a file/image to the command to have |bot_name| send the file/image as attachment on the target message.

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

    |bot_prefix|\ msgedit (channel id/mention) (message id) (new message content)

Command Description
^^^^^^^^^^^^^^^^^^^
Edits a previously sent message.

You can use embed json from https://eb.nadeko.bot/ instead of a regular text, if you want the message to be embedded.

You cannot edit a message attachment.

.. note::
    To remove the content (plain text) of a message, pass ``{"content":""}`` as new message content.
    To remove all embeds of a message, pass ``{"embeds":[]}`` as new message content.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ msgedit #that-channel 123456789098765432 Hello world! I'm alive!

....

|bot_prefix|\ webhooksend
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ webhooksend (webhook name) (message to send)

Command Description
^^^^^^^^^^^^^^^^^^^
Sends a message to a webhook **in the current channel**. If the webhook name is made by two or more words, please surround the name with by double quotes.

This command is meant to test the functionality of a Discord webhook. For this reason, the feature is limited to sending a message to a webhook that is set within the channel from where the command is run.

You can use embed json from https://eb.nadeko.bot/ instead of a regular text, if you want the message to be embedded.

You can attach a file/image to the command to have |bot_name| send the file/image as attachment on the target message.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Webhooks
| **Bot**: Manage Webhooks

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ webhooksend "Spidey Bot" Hello world!
    |bot_prefix|\ webhooksend News { "description": "Hello world!" }
