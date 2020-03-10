.. _custreact:

****************
Custom Reactions
****************

The Custom Reactions module enables users to set up custom bot reactions and build pseudo-commands in a server.

|bot_prefix|\ togglecustreact
-----------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ tcr

Command Description
^^^^^^^^^^^^^^^^^^^
Toggles the custom reactions module on the whole Discord server.

....

|bot_prefix|\ addcustreact
--------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ acr (--in {trigger text}) (--out {response text}) [--anywhere] [--dm] [--delete] [--global]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Adds a new custom reaction for the current server.

Optional Parameters:

* ``anywhere``: Triggers the reaction based on a text that appears anywhere in a message, instead of starting with the trigger text. Default: off.
* ``dm``: Sends the response text via DM instead of using the current channel. Default: off.
* ``delete``: Deletes the original message after a reaction is triggered. Default: off.
* ``global``: **Bot Owner**. Makes the custom reaction global, hence triggering in any server the bot is. Default: off.

You can use one (or more) of these placeholders in your response message:

* **%user%**: This will be replaced with a mention of the user.
* **%username%**: This will be replaced with the username of the user, without the discriminator (e.g. cycloptux).
* **%fullusername%**: This will be replaced with the username of the user, including the discriminator (e.g. cycloptux#1543).
* **%bot%**: This will be replaced with a mention of the bot.
* **%botname%**: This will be replaced with the username of the bot, without the discriminator.
* **%fullbotname%**: This will be replaced with the username of the bot, including the discriminator.
* **%server%**: This will be replaced with the server name.
* **%channel%**: This will be replaced with the channel name.
* **%now%**: This will be replaced with the current time, with format ``YYYY-MM-DD HH:mm:ss (UTC)``.
* **%server\_time%**: This will be replaced with the current time, with format ``HH:mm UTC``.
* **%prefix%**: This will be replaced with the current prefix for the server.
* **%globalprefix%**: This will be replaced with the default, global prefix.
* **%boost\_level%**: This will be replaced with the current Nitro Server Boost level for the server.
* **%boost\_number%**: This will be replaced with the current number of Nitro Server Boosts that the server received.
* **%target%**: This will be replaced with anything the user wrote after the trigger.

You can use embed json from https://eb.nadeko.bot/ instead of a regular text in the response parameter, if you want the message to be embedded.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ acr --in what time is it --out Hello %user%! The current time is %now%. --anywhere

....

|bot_prefix|\ editcustreact
---------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ ecr (reaction id) [--in {trigger text}] [--out {response text}] [--anywhere] [--dm] [--delete] [--global]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Edits an existing custom reaction for the current server. Global custom reactions can only be edited by the bot owner.

.. You cannot edit the trigger text of a custom reaction: if you want to change the trigger text of a reaction, delete the existing one and add a new custom reaction. <-- Not true anymore

The presence of an optional parameter will **toggle** the option to the opposite of what it was before the edit. ``--global``, on the other hand, will need to be added or removed accordingly, depending on the scope of the reaction.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ ecr 1 --out Hello %user%! The current time is %server\_time%.  --delete

....

|bot_prefix|\ showcustreact
---------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ scr (reaction id)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Prints the current configuration for a specific custom reaction. It will also preview how the reaction is printed when triggered in a server (placeholders will **not** be replaced in this preview).

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ scr 3

....

|bot_prefix|\ listcustreact
---------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ lcr [--global] [--in {text}]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Lists all available custom reactions in the current server. Using the ``--global`` argument will show the list of global reactions.

Using the ``--in`` parameter will filter on reactions that are triggered by the text used within that argument.

....

|bot_prefix|\ delcustreact
--------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ dcr (reaction id)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Deletes a specific custom reaction. Global custom reactions can only be deleted by the bot owner.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ dcr 3

....

|bot_prefix|\ restcustreact
---------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rcr (reaction id) [role id(s)/mention(s)/q_name(s)] [--exclude] [--and]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Restricts an existing custom reaction to a specified set of roles, or exludes a set of roles from using a reaction.

If used without any argument, the command will apply the default setting: **allowing** all users in a server.

By using the command with one or more role identifiers, the command will restrict the custom reaction to all users that have at least one of those roles.

By adding the ``--exclude`` parameter to the command, the logic will switch from whitelisting the specified roles to **blacklisting** them: users with at least one the specified roles will **not** be able to use the custom reaction.

By adding the ``--and`` parameter to the command, the logic will switch from an **OR** logic to and **AND** logic, allowing or restricting a custom reaction to users that have (or lack) all of the configured roles.

Use the above parameters to configure each custom reaction with the desided configuration. Each usage of this command will overwrite the previously set logic.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rcr 4 Moderators "Authorized People"
    |bot_prefix|\ rcr 3 "Authorized People" "Sensitive Data" --and
    |bot_prefix|\ rcr 12 @Restricted --exclude
    |bot_prefix|\ rcr 27 "Unauthorized A" "Unauthorized B" --and --exclude

....

|bot_prefix|\ crclear
---------------------
    
Command Description
^^^^^^^^^^^^^^^^^^^
Deletes all server specific custom reactions. Global custom reactions can only be deleted by the bot owner.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server