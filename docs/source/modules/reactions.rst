*****************
Reactions Parsing
*****************

This module enables users to gather stats about the reactions sent into a channel.

|bot_prefix|\ reprint
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ reprint (message id) [--sort username/discriminator/nickname] [--show username/nickname] [--emoji {default or custom emoji}]

Command Description
^^^^^^^^^^^^^^^^^^^
Prints the list of users that reacted to the specified message in a readable way.

Setting the ``--sort`` parameter will sort the output using the specified setting. Defaults to showing the reactions with the order Discord outputs them.

Setting the ``--show`` parameter will show the output using the specified setting. Defaults to showing the users by their username.

Setting the ``--emoji`` parameter will filter the output to the specified emoji.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ reprint 123456789098765432
    |bot_prefix|\ reprint 123456789098765432 --sort nickname --show nickname
    |bot_prefix|\ reprint 123456789098765432 --emoji :pikathink:

....

|bot_prefix|\ resummary
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ resummary [# of messages] [--csv] [--silent]

Command Description
^^^^^^^^^^^^^^^^^^^
Prints a list of messages with reactions within the last ``# of messages`` in the current channel, showing the list of reactions and number of uses per each reaction.

Using the ``--csv`` parameter instructs the bot to send a ``.csv`` file containing the details of the summary to the command author.

Using the ``--silent`` parameter suppresses the in-channel embed output (this only works if used with ``--csv``).

If the number of messages is omitted, the bot will scan the latest 10 messages.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ resummary 
    |bot_prefix|\ resummary 20 --csv --silent
    |bot_prefix|\ resummary --csv

....

|bot_prefix|\ reunique
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ reunique [# of messages] [--csv] [--silent]

Command Description
^^^^^^^^^^^^^^^^^^^
Prints a list of **unique users** that reacted to at least one message within the last ``number-of-messages`` in the current channel.

Using the ``--csv`` parameter instructs the bot to send a ``.csv`` file containing the details of the output to the command author. The ``.csv`` file also shows the nickname of the user(s) and the number of times each user reacted to each reaction.

Using the ``--silent`` parameter suppresses the in-channel embed output (this only works if used with ``--csv``).

If the number of messages is omitted, the bot will scan the latest 10 messages.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ reunique 
    |bot_prefix|\ reunique 20 --csv --silent
    |bot_prefix|\ reunique --csv
