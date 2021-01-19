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

    |bot_prefix|\ lb [page #] [--days {# of days}] [--roles (role id(s)/mention(s))] [--min {minimum score}]

Command Description
^^^^^^^^^^^^^^^^^^^
Prints the server social leaderboard. Use the ``--days`` parameter to look at the leaderboard limited to the latest X days.

Using the ``--roles`` parameter will filter the leaderboard to those having at least one of the selected roles.

Using the ``--min`` parameter will filter the leaderboard to those users whose gained EXP is greater than or equal to the selected value.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ leaderboard
    |bot_prefix|\ leaderboard 2
    |bot_prefix|\ leaderboard --days 30 --roles @Players

....

|bot_prefix|\ gleaderboard
--------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ glb [page #] [--days {# of days}] [--min {minimum score}]

Command Description
^^^^^^^^^^^^^^^^^^^
Prints the global social leaderboard. Use the ``--days`` parameter to look at the leaderboard limited to the latest X days.

Using the ``--min`` parameter will filter the leaderboard to those users whose gained EXP is greater than or equal to the selected value.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ gleaderboard
    |bot_prefix|\ gleaderboard 2
    |bot_prefix|\ gleaderboard --days 30 --min 10000

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

|bot_prefix|\ expboost
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ expboost [boost percentage value]

Command Description
^^^^^^^^^^^^^^^^^^^
Sets a custom Experience Boost Multiplier for the current server. This multiplier will be applied to the default rates of gaining EXP in order to increase or decrease the amount of gained server EXP when messaging (refer to the top of this page).

* The **lower** hard limit for Experience Boosting is **-50%**, which corresponds to **0.5x** EXP gained per message (vs. the default value).
* The **upper** hard limit for Experience Boosting is **100%**, which corresponds to **2x** EXP gained per message (vs. the default value).
* The **default** multiplier for Experience Boosting is **0%**, which sets the EXP rate back to the default **1x**.

Running this command without arguments will show the current EXP Boost Multiplier. Running it with a percentage value (without the ``%`` sign) between -50 and 200 will set a new EXP Boost on the current server.

The new multiplier will be **rounded down to the nearest ten**, and must be within the aforementioned limits.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ expboost -30
    |bot_prefix|\ expboost 150
    |bot_prefix|\ expboost

....

|bot_prefix|\ expedit
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ expedit (EXP amount) (user id/mention)

Command Description
^^^^^^^^^^^^^^^^^^^
Adds or removes a certain amount of server EXP to a member of the server. You can increase or decrease someone's EXP of **up to 10,000 EXP** with this command. In order to increase or decrease someone's EXP of more than that, you must run the command multiple times.

Use positive values to increase EXP. Use negative values to decrease EXP.

Editing someone's EXP will not trigger EXP role assignments for any level in between the start level and end level.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ expedit -2000 @cycloptux#1543
    |bot_prefix|\ expedit 5000 123456789098765432

....

|bot_prefix|\ expreset
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ expreset (user id/mention)

Command Description
^^^^^^^^^^^^^^^^^^^
Resets the server EXP and level of a member of the server.

Any EXP role that the user had when running the command will be preserved and may need to be removed manually.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ expreset @cycloptux#1543
    |bot_prefix|\ expreset 123456789098765432

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

.. _noexpchannels:

|bot_prefix|\ noexpchannels
---------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ noexpchannels [- {or} channel(s) id/mention/q_name]

Command Description
^^^^^^^^^^^^^^^^^^^
In order to block certain channels (usually, spam channels) from being a source to gain server EXP when messaging (refer to the top of this page), server managers can set one or more channels as "No-Experience Channels": users chatting in these channels will not gain any experience from their messages.

Running this command with one or more channel identifier(s) as argument will set those channels as No-EXP Channels. This command will always override the former list of channels.

Running this command with ``-`` as argument will disable this feature (removing the "No-EXP Channel" flag from any former channel).

Running this command without arguments will show the current No-EXP Channels, if any.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ noexpchannels #spam
    |bot_prefix|\ noexpchannels #spam #bot-commands
    |bot_prefix|\ noexpchannels
    |bot_prefix|\ noexpchannels -

....

|bot_prefix|\ explvupsetup
--------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ explvupsetup
    
Command Description
^^^^^^^^^^^^^^^^^^^
Opens an interactive menu to configure the EXP level-up notifications settings. Use the menu items to configure the available settings.

Options 1. and 2. are used to save the settings you applied through the menu (the settings will not apply until you save them), or discard said changes.

3. "Toggle in-server level-up notifications" toggles whether users are notified when they gain a level, into a server channel. You can enable option 3, or 4, or both at the same time. Default: **Disabled**
4. "Toggle DM level-up notifications" toggles whether users are notified when they gain a level, with a DM sent by |bot_name|\ . You can enable option 3, or 4, or both at the same time. Default: **Disabled**
5. "Select in-server level-up notifications location" lets you select one channel to be used as centralized level-up notifications channel. If this option is enabled, all level-up notifications will be posted in this channel. Otherwise, level-up notifications will be sent to the same channel where the message triggering the level-up was posted. Default: **Same Channel**
6. "Set a custom in-server level-up message" lets you set a custom message to be posted as level-up message for in-server notifications. See below for more customizations info.
7. "Set a custom DM level-up message" lets you set a custom message to be posted as level-up message for DM notifications. See below for more customizations info.
8. "Add channels to the level-up notifications blacklist/whitelist" lets you select one or more channels that will be added to the blacklist (or whitelist, depending on the list mode). **Blacklist mode** will make any channel that is on the list **not to trigger** the level-up message, while the rest of the channels will trigger the in-server level-up messages. **Whitelist mode** will only make the in-server level-up message appear when a level is gained in one of the selected channels.
9. "Toggle mode for the level-up notifications list" toggles between **blacklist mode** and **whitelist mode**.

.. note::
    List modes will only change whether or not messaging in the selected channel will trigger the level-up **message**: if you want to stop users from getting EXP **at all** in a certain channel, use the :ref:`noexpchannels` command.

The custom messages support the following dynamic placeholders:

* **%level%**: This will be replaced with the level that the user just achieved.
* **%user%**: This will be replaced with a mention of the user.
* **%username%**: This will be replaced with the username of the user, without the discriminator (e.g. cycloptux).
* **%discriminator%**: This will be replaced with the discriminator of the user, without the ``#`` character (e.g. 1543).
* **%fullusername%**: This will be replaced with the username of the user, including the discriminator (e.g. cycloptux#1543).
* **%user\_avatar\_url%**: This will be replaced with the current user avatar URL (in WebP or GIF format).
* **%bot%**: This will be replaced with a mention of the bot.
* **%botname%**: This will be replaced with the username of the bot, without the discriminator.
* **%botdiscriminator%**: This will be replaced with the discriminator of the bot, without the ``#`` character.
* **%fullbotname%**: This will be replaced with the username of the bot, including the discriminator.
* **%bot\_avatar\_url%**: This will be replaced with the current bot avatar URL (in WebP or GIF format).
* **%server%**: This will be replaced with the server name.
* **%now%**: This will be replaced with the current time, with format ``YYYY-MM-DD HH:mm:ss (UTC)``.
* **%now\_iso%**: This will be replaced with the current time, as ISO8601 string.
* **%server\_time%**: This will be replaced with the current time, with format ``HH:mm UTC``.
* **%server\_icon\_url%**: This will be replaced with the current server icon URL (in WebP or GIF format).
* **%server\_banner\_url%**: This will be replaced with the current server icon URL (in WebP format).
* **%server\_splash\_url%**: This will be replaced with the current server icon URL (in WebP format).
* **%server\_member\_count%**: This will be replaced with the current amount of members in the server.
* **%boost\_level%**: This will be replaced with the current Nitro Server Boost level for the server.
* **%boost\_number%**: This will be replaced with the current number of Nitro Server Boosts that the server received.

You can use embed json from https://eb.nadeko.bot/ instead of a regular text, if you want the message to be embedded.

Custom messages cannot exceed **1024 characters**.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Channels

....

|bot_prefix|\ expnotifyoptout
-----------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ expnotifyoptout

Command Description
^^^^^^^^^^^^^^^^^^^
Provides a way for individual users to disable the DM notification upon leveling up, even if the server-wide notifications are active.

Run the command again to re-enable the DM notifications.
