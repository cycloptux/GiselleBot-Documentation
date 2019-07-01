************************
Brave Frontier News Feed
************************

Be notified when a new in-game news is published in **Brave Frontier (Global)**, **Brave Frontier 2 (Japan)**, or **Brave Frontier: The Last Summoner**.

The news URL and a preview will be posted in the specified channel, as you see them in-game.

|bot_prefix|\ newsfeed toggle
-----------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ newsfeed toggle [--game {game identifier}] [--force]
    
Command Description
^^^^^^^^^^^^^^^^^^^

Enables or disables one or more News Feed(s) in the current channel.

* For **Brave Frontier** by gumi, the GL news feed is supported. EU news feed support was dropped after the game was discontinued. The game identifier is ``bf1`` or ``bf``.
* For **Brave Frontier 2** by Alim, JP is the only available feed. The game identifier is ``bf2``.
* For **Brave Frontier: The Last Summoner** by gumi, GL is the only available feed. The game identifier is ``bftls``.

The Brave Frontier and Brave Frontier: The Last Summoner feeds also support sending updates whenever a news is updated.

.. note::
    Once enabled, the feed won't post any old news. It will only start posting as soon as new (or updated) news are published.

If you want to enable multiple feeds in one channel, you can either:

* Use a single command, splitting multiple games or languages with ``,`` (comma), no spaces.
* Use multiple commands, one per feed.

If the game is omitted, the **Brave Frontier** feed will be toggled.

.. note::
    There can only be 1 game news feed channel in each server (you can enable different games in different channels, but one game feed cannot be enabled in 2 or more channels). To move an existing feed to another channel, disable it in the first one before enabling it to its new channel. You can also use the ``--force`` parameter in the new channel to automatically move the feed to the new channel while disabling the old one.

.. warning::
    If you move your feed, all those news that were already posted will not carry over to the new channel.
    
Examples
^^^^^^^^
.. parsed-literal::
    
    |bot_prefix|\ newsfeed toggle
    |bot_prefix|\ newsfeed toggle --game bf2
    |bot_prefix|\ newsfeed toggle --game bf1,bftls
    