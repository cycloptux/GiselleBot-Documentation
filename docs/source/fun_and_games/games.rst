.. _games:

*****
Games
*****

As a way of betting, spending and/or earning currency (see :ref:`currency-system`), a few simple games are available.

....

Wheel of Fortune
================

Bets a certain amount of currency on the wheel of fortune. The wheel can stop on one of many different multipliers. Won amount is rounded down to the nearest whole number.

|bot_prefix|\ wheeloffortune
----------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ wheel (bet amount)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Plays a round of wheel of fortune.

....

Bet Roll
========

Bets a certain amount of currency and rolls a die. Possible outputs are 0-100.

* Rolling over 66 yields x2 of the bet currency
* Rolling over 90 yields x4 of the bet currency
* Rolling a 100 yields x10 of the bet currency

|bot_prefix|\ betroll
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ br (bet amount)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Plays a round of bet roll.

....

Minesweeper
===========

Contrary to other games, this game does not involve any currency or bet, and can be played by any number of users on the same "board".

Game rules and information about the current board will be shown upon running the command.

|bot_prefix|\ minesweeper
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ mswp [--easy/--normal/--hard/--extreme]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Generates a random minesweeper board. Any user can play locally by unhiding the spoiler tags on the board. No other kind of interaction is implemented, just have fun and play fair!

Use one of the optional tags to create a new board of the selected difficulty. "Normal" is the default mode, if the difficulty tag is omitted.

.. warning::
    Due to a long running bug in the Discord desktop and web client, the "Hard" and "Extreme" difficulty boards will not correctly show up. The mobile clients do seem to show the boards correctly. Here's the related Discord bug report: https://bugs.discord.com/T812
    