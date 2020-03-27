************************
Brave Frontier News Feed
************************

Be notified when a new in-game news is published in **Brave Frontier (Global)** by gumi and **Brave Frontier 2 (Japan)** by Alim.

The news URL and a preview will be posted in the specified channel, as you see them in-game.

|bot_prefix|\ bf1news
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ bf1news [channel id/mention/q_name] [--stop]
    
Command Description
^^^^^^^^^^^^^^^^^^^

Enables (or disables, if used with the ``--stop`` parameter) the Brave Frontier (Global) news feed in the selected channel.

If the channel is omitted, the current configuration will be shown.

Examples
^^^^^^^^
.. parsed-literal::
    
    |bot_prefix|\ bf1news
    |bot_prefix|\ bf1news #bfgl-news
    |bot_prefix|\ bf1news --stop
    
....

|bot_prefix|\ bf2news
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ bf2news [channel id/mention/q_name] [--stop]
    
Command Description
^^^^^^^^^^^^^^^^^^^

Enables (or disables, if used with the ``--stop`` parameter) the Brave Frontier 2 (Japan) news feed in the selected channel.

If the channel is omitted, the current configuration will be shown.

Examples
^^^^^^^^
.. parsed-literal::
    
    |bot_prefix|\ bf2news
    |bot_prefix|\ bf2news #bf2jp-news
    |bot_prefix|\ bf2news --stop
