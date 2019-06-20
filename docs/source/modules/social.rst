***********************
Social/EXP Leaderboards
***********************

The Social module tracks users' activity in a server (and globally) and rewards a certain number of experience points on each message. A server and a global leaderboards exist, making users aware of how much they are engaging with the community.

.. warning::
    These limitations are applied to avoid users manipulating their EXP:
    
    * EXP is calculated on the amount of messages that are sent by the user. Message length doesn't change the amount of EXP earned on each message.
    * Each message is given a random EXP value, ranging from 10 to 20 EXP.
    * A cooldown is applied after each EXP gain to avoid users spamming messages to power level their profile.

If the level up notifications are enabled on a server, users may be notified by DM or in the current channel as soon as they level up. Global level ups are never notified.

|bot_prefix|\ profile
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ profile [user id/mention]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Shows the server profile (including the EXP status) of a user. By default, it will show the profile of the user that runs the command. Users can check someone else's profile by tagging them or using their ID.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ profile
    |bot_prefix|\ profile @cycloptux#1543
    |bot_prefix|\ profile 123456789098765432

....

|bot_prefix|\ gprofile
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ gprofile [user id/mention]

Command Description
^^^^^^^^^^^^^^^^^^^
Shows the global profile (including the EXP status) of a user. By default, it will show the profile of the user that runs the command. Users can check someone else's profile by tagging them or using their ID.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ gprofile
    |bot_prefix|\ gprofile @cycloptux#1543
    |bot_prefix|\ gprofile 123456789098765432

....

|bot_prefix|\ leaderboard
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ lb [page #] [--days {# of days}]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Prints the server social leaderboard. Use the ``--days`` parameter to look at the leaderboard limited to the latest X days.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ leaderboard
    |bot_prefix|\ leaderboard 2
    |bot_prefix|\ leaderboard --days 30

....

|bot_prefix|\ gleaderboard
--------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ glb [page #] [--days {# of days}]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Prints the global social leaderboard. Use the ``--days`` parameter to look at the leaderboard limited to the latest X days.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ gleaderboard
    |bot_prefix|\ gleaderboard 2
    |bot_prefix|\ gleaderboard --days 30

....

|bot_prefix|\ notifychannel
---------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ notifychannel [channel id(s)/mention(s)/q_name(s)]
    
Command Description
^^^^^^^^^^^^^^^^^^^
If used without any channel identifier, this command will toggle the in-channel notification for level ups in the whole server.

If used with one or more channel identifiers, it will toggle the channel into the blacklist/whitelist of channels that will show the in-channel notification. See below for more details.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Channels

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ notifychannel
    |bot_prefix|\ notifychannel #spam #bot-commands

....

|bot_prefix|\ notifychannelmode
-------------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ notifychannelmode
    
Command Description
^^^^^^^^^^^^^^^^^^^
Toggles the notification channel mode from blacklist (default) to whitelist and viceversa.

**Blacklist** mode will make any channel that is added with the above command **not** to show the level up message, while the rest of the channels will show the in-channel level up message.

**Whitelist** mode will only make the in-channel level up message appear in the selected channels.

....

|bot_prefix|\ notifydm
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ notifydm
    
Command Description
^^^^^^^^^^^^^^^^^^^
Toggles the DM notification for level ups for all server members.

....

|bot_prefix|\ notifystatus
--------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ notifystatus
    
Command Description
^^^^^^^^^^^^^^^^^^^
Shows the current status of the level up notification settings, as set by the above commands.
