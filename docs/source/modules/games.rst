.. _games:

*****
Games
*****

As a way of betting, spending and/or earning currency (see :ref:`currency-system`), a few game are available.

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

Bets a certain amount of currency and rolls a dice. Possible outputs are 0-100.

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
