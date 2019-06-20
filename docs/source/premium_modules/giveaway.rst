******************
Giveaway Campaigns
******************

The Giveaway Campaigns module enables users to start and manage giveaways in a Discord server.

.. seealso::
    Partially inspired by `GiveawayBot <https://giveawaybot.party/>`_.

|bot_prefix|\ gstart
--------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ gstart [--prize {prize name}] [--winners {# of winners (number)}] [--duration {duration timecode}] [--max {# of users after which the bot will stop the giveaway (number)}]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Starts a new giveaway in the current channel. Members can participate by clicking on the reaction that is added by the bot.

All parameters are optional, the default values (on omission) are:

* **Prize Name**: "Sample Prize"
* **Winners**: 1
* **Duration**: 1 day (24 hours)
* **Max**: *None* (Infinite)

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ gstart --prize Free Steam Key --winners 2 --duration 1w
    |bot_prefix|\ gstart --prize Free Steam Key to the fastest 5! --winners 5 --max 5

....

|bot_prefix|\ gend
------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ gend [message id]

Command Description
^^^^^^^^^^^^^^^^^^^
Immediately ends a giveaway and picks a winner among those that participated. The message ID is optional: if omitted, the most recent giveaway in the channel will be ended.

*Side note*: You can abort a campaign by deleting the campaign message that the bot sent.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ gend
    |bot_prefix|\ gend 123456789098765432

....

|bot_prefix|\ greroll
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greroll [message id]

Command Description
^^^^^^^^^^^^^^^^^^^
Picks a new winner from the latest giveaway. The message ID is optional: if omitted, the most recent giveaway in the channel will be rerolled.

This command will only reroll one winner and won't overwrite the existing winners.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greroll
    |bot_prefix|\ greroll 123456789098765432

....

|bot_prefix|\ greaction
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greaction (emoji)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Sets a custom emoji for the giveaway campaign in the current server.

.. warning:
    You **must** use reactions that are either "global" (Discord native emojis) or present in the server. Failing to do so may result in the giveaway reaction not to work.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ greaction 😀
    |bot_prefix|\ greaction :BlobOwO:

