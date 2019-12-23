******************
Social/EXP Ranking
******************

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

|bot_prefix|\ expaddrole
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ expar (level) (role id(s)/mention(s)/q_name(s)) [--persistent] [--volatile]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Adds one (or more) **existing** role(s) as reward for reaching a certain EXP level.

By default, obtained roles are removed if, and when, a reward of higher tier is reached. This behavior can be customized by using the ``--persistent`` or ``--volatile`` tags:

* A **persistent** role is kept "forever", even after obtaining a role given at a higher tier (level).
* A **volatile** role is removed as soon as the user reaches the immediate next level.

"Adding" a role that already exists on a level replaces its settings with the new settings.

.. note::
    Let's make a practical example. User X is currently Lv. 4, and the server currently has these settings:
    
    * "Rookie", obtained at level 5, **volatile**;
    * "Known Member", obtained at level 5, **persistent**;
    * "Junior", obtained at level 7;
    * "Senior", obtained at level 10.
    
    Upon levelling up to Lv. 5, X will obtain **Rookie** and **Known Member**.
    Upon levelling up to Lv. 6, X will lose **Rookie** (volatile).
    Upon levelling up to Lv. 7, X will obtain **Junior**, and keep **Known Member** (persistent).
    Upon levelling up to Lv. 10, X will obtain **Senior**, lose **Junior**, and keep **Known Member** (persistent).

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Roles
| **Bot**: Manage Roles

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ expar 5 @Rookie --volatile
    |bot_prefix|\ expar 5 "Known Member" --persistent
    |bot_prefix|\ expar 7 Junior
    |bot_prefix|\ expar 10 @Senior
    |bot_prefix|\ expar 15 "VIP Member" 123456789098765432 --persistent

....

|bot_prefix|\ expremrole
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ exprr (level) (role id(s)/mention(s)/q_name(s))
    
Command Description
^^^^^^^^^^^^^^^^^^^
Removes one (or more) role(s) as reward for reaching a certain EXP level.

.. note::
    This command will **not** remove any previously aquired role(s) from server members. It will only stop server members from obtaining the role(s) upon levelling up.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Roles
| **Bot**: Manage Roles

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ exprr 5 @Rookie
    |bot_prefix|\ exprr 15 123456789098765432

....

|bot_prefix|\ exproles
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ exproles
    
Command Description
^^^^^^^^^^^^^^^^^^^
Lists all of the EXP roles that are currently set in the current server.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **Bot**: Manage Roles

....

|bot_prefix|\ exprapply
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ exprapply
    
Command Description
^^^^^^^^^^^^^^^^^^^
Recalculates the EXP role(s) each server member is entitled to have, and applies the correct set of roles to each user.

The command will apply the highest EXP tier role(s) and every "persistent" role below the current user level.

.. note::
    This command will **not** remove any previously aquired role(s) from server members, even if the role in question is set as EXP role and no longer available to the user based on the current EXP roles chain.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Roles
| **Bot**: Manage Roles

....

|bot_prefix|\ noexprole
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ noexprole [- {or} role id/mention/q_name]
    
Command Description
^^^^^^^^^^^^^^^^^^^
In order to block certain users from gaining server EXP when messaging (refer to the top of this page), server managers can set one role as "No-Experience Role": users having this role will not gain any experience from their messages.

Running this command with one role identifier as argument will set that role as No-EXP Role.

Running this command with ``-`` as argument will disable this feature (removing the "No-EXP Role" flag from the former role).

Running this command without arguments will show the current No-EXP Role, if any.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ noexprole @Spammer
    |bot_prefix|\ noexprole
    |bot_prefix|\ noexprole -

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
