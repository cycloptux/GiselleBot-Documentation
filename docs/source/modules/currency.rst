.. _currency-system:

***************
Currency System
***************

Each user known to the bot has a currency wallet. Currency is earned in a few ways:

* Each message sent in a channel the bot has access to will give a small amount of currency to the user (a cooldown is applied to avoid plain spamming just to earn currency).
* Once a day, using the :ref:`timely` command.
* Every once in a while, reacting to events on the main bot support server.
* Playing with :ref:`games`.

Currently, the main goal of currency is playing with games. More uses are planned, but still not implemented.

|bot_prefix|\ $
---------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ $ [user id/mention/q_name]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Shows the current amount of currency of a user. By default, it will show the currency wallet info of the user that runs the command. Users can check someone else's wallet by tagging them or using their ID/name.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ $
    |bot_prefix|\ $ @cycloptux#1543
    |bot_prefix|\ $ 123456789098765432
    
....

.. _timely:

|bot_prefix|\ timely
--------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ timely
    
Command Description
^^^^^^^^^^^^^^^^^^^
Once a day (by default, but the cooldown can be configured by the bot owner) users can earn a specified amount of currency by running this command. The default amount of currency earned is 10 per command run.

.... 

.. _dblnotify:

|bot_prefix|\ dblnotify
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ dblnotify
    
Command Description
^^^^^^^^^^^^^^^^^^^
As an additional source of income for bot currency, and as a way to show your appreciation to |bot_name|\ , you can vote for |bot_name| on `Discord Bot List <https://discordbots.org/bot/356831787445387285>`_ (click on the website name to be sent to the bot page).

Any Discord user can vote for each bot once every 12 hours. Each vote for |bot_name| will award you with 125 currency coins.

To help give |bot_name| a better chance to fight for the top spots, votes will count double on the weekend (Fridays, Saturdays and Sundays). This also means **double the amount of coins**!

By enabling the notification service using the |bot_prefix|\ dblnotify command in any server, you will also be notified when your Discord Bots List vote is available, thus being able to actively collect your daily coins efficiently. Each run of the command will toggle its previous state.

Users will only be notified once per vote reset.

....

.. _bfdnotify:

|bot_prefix|\ bfdnotify
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ bfdnotify
    
Command Description
^^^^^^^^^^^^^^^^^^^
As an additional source of income for bot currency, and as a way to show your appreciation to |bot_name|\ , you can vote for |bot_name| on `Bots for Discord <https://botsfordiscord.com/bot/356831787445387285>`_ (click on the website name to be sent to the bot page).

Any Discord user can vote for each bot once per day. The window opens at midnight, UTC. Each vote for |bot_name| will award you with 250 currency coins.

Even though the website doesn't award double points during weekends (see: :ref:`dblnotify`), |bot_name| will still award **double the amount of coins** on **Fridays, Saturdays and Sundays**!

By enabling the notification service using the |bot_prefix|\ bfdnotify command in any server, you will also be notified when your Bots for Discord vote is available, thus being able to actively collect your daily coins efficiently. Each run of the command will toggle its previous state.

Users will only be notified once per vote reset.

....

|bot_prefix|\ cleaderboard
--------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ clb [page #]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Prints the **global** currency leaderboard.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ clb
    |bot_prefix|\ clb 3

....

|bot_prefix|\ currencyemoji
---------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ currencyemoji [emoji]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Sets a custom emoji as currency in the current server. Using the command without the extra emoji argument will reset the currency emoji to the default one.

.. warning::
    You **must** use reactions that are either "global" (Discord native emojis) or present in the server. Failing to do so may result in the currency emoji not to work.
    
Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ currencyemoji 😀
    |bot_prefix|\ currencyemoji :BlobOwO:
    
....

|bot_prefix|\ timelyreset
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ timelyreset
    
Command Description
^^^^^^^^^^^^^^^^^^^
Resets the |bot_prefix|\ timely countdown for everyone.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Bot Owner

....

|bot_prefix|\ timelyset
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ timelyset [timecode] [# of currency coins]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Sets the **global** amount of currency and/or cooldown for the |bot_prefix|\ timely command. Modified cooldown applies to everyone immediately, but doesn't reset users' cooldown.

Running the command with no arguments will show the current settings.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Bot Owner

....

|bot_prefix|\ award
-------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ award (user and/or role id(s)/mention(s)/q_name(s)) (amount of currency)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Awards the selected amount of currency to the specified user(s) and/or role(s).

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Bot Owner

....

|bot_prefix|\ take
------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ take (user and/or role id(s)/mention(s)/q_name(s)) (amount of currency, or "all")
    
Command Description
^^^^^^^^^^^^^^^^^^^
Takes the selected amount of currency from the specified user(s) and/or role(s). You can use ``all`` instead of the currency amount to remove all currency from the target user(s).

.. warning::
    The currency is permanently lost. It's **not** transferred to the owner.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Bot Owner

.... 

|bot_prefix|\ eventstart
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ eventstart [--amount/--a {amount of currency to gift to each reacting user}] [--pot-size/--p {maximum amount of currency that can be gifted}] [--duration/--d {event duration timecode}]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Starts an event reaction in the current channel.

Each reacting user will be gifted with the selected amount of currency. You can define the amount of received currency with the ``--amount`` parameter.

By default, each user will be rewarded with the specified amount of currency. You can set a maximum amount of currency for the event "bucket" by using the ``--pot-size`` parameter (e.g. if ``--amount 50 --p 100`` is used, only the first 2 users will actually receive 50 currency each). You can also set a custom duration for the event.

.. note::
    Checks are in place to ensure that users will only receive their gift the first time they react. Reacting more than once will **not** assign any extra currency.

Here are the default values for the command parameters, on omission:

* **Amount**: 100
* **Pot Size**: 0 (= no limit)
* **Duration**: 1 day

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Bot Owner
