Custom Reactions
================

The Custom Reactions module enables users to set up custom bot reactions and build pseudo-commands in a server.

!togglecustreact
----------------

Command Syntax
^^^^^^^^^^^^^^
.. code-block:: none

    !tcr

Command Description
^^^^^^^^^^^^^^^^^^^
Toggles the custom reactions module on the whole Discord server.

....

!addcustreact
-------------

Command Syntax
^^^^^^^^^^^^^^
.. code-block:: none

    !acr (--in {trigger text}) (--out {response text}) [--anywhere] [--dm] [--delete] [--global]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Adds a new custom reaction for the current server.

Optional Parameters:
* ``anywhere``: Triggers the reaction based on a text that appears anywhere in a message, instead of starting with the trigger text. Default: off.
* ``dm``: Sends the response text via DM instead of using the current channel. Default: off.
* ``delete``: Deletes the original message after a reaction is triggered. Default: off.
* ``global``: **Bot owner only**. Makes the custom reaction global, hence triggering in any server the bot is. Default: off.

You can use one (or more) of these placeholders in your response message:
* **%user%**: This will be replaced with a mention of the user.
* **%server%**: This will be replaced with the server name.
* **%now%**: This will be replaced with the current time, with format ``YYYY-MM-DD HH:mm:ss (UTC)``.
* **%server\_time%**: This will be replaced with the current time, with format ``HH:mm UTC``.

You can use embed json from https://embedbuilder.nadekobot.me/ instead of a regular text in the response parameter, if you want the message to be embedded.

Examples
^^^^^^^^
.. code-block:: none

    !acr --in what time is it --out Hello %user%! The current time is %now%. --anywhere

....

!editcustreact
--------------

Command Syntax
^^^^^^^^^^^^^^
.. code-block:: none

    !ecr (reaction_id) [--out {response text}] [--anywhere] [--dm] [--delete] [--global]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Edits an existing custom reaction for the current server. Global custom reactions can only be edited by the bot owner.

You cannot edit the trigger text of a custom reaction: if you want to change the trigger text of a reaction, delete the existing one and add a new custom reaction.

The presence of an optional parameter will **toggle** the option to the opposite of what it was before the edit. ``--global``, on the other hand, will need to be added or removed accordingly, depending on the scope of the reaction.

Examples
^^^^^^^^
.. code-block:: none

    !ecr 1 --out Hello %user%! The current time is %server\_time%.  --delete

....

!showcustreact
--------------

Command Syntax
^^^^^^^^^^^^^^
.. code-block:: none

    !scr (reaction_id)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Prints the current configuration for a specific custom reaction.

Examples
^^^^^^^^
.. code-block:: none

    !scr 3

....

!listcustreact
--------------

Command Syntax
^^^^^^^^^^^^^^
.. code-block:: none

    !lcr
    
Command Description
^^^^^^^^^^^^^^^^^^^
Lists all available custom reactions in the current server (including global reactions).

....

!delcustreact
-------------

Command Syntax
^^^^^^^^^^^^^^
.. code-block:: none

    !dcr (reaction_id)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Deletes a specific custom reaction. Global custom reactions can only be deleted by the bot owner.

Examples
^^^^^^^^
.. code-block:: none

    !dcr 3

....

!crclear
--------
    
Command Description
^^^^^^^^^^^^^^^^^^^
Deletes all server specific custom reactions. Global custom reactions can only be deleted by the bot owner.
