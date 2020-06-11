**********
Raid Rooms
**********

This module allows users to create private, temporary text or voice channels for cooperation purposes, such as during cooperative play time on MOBA games, and then delete the voice channel/text channel after an allotted time.

Its best use case is giving a place to small groups of people that need to talk to each other privately for a short amount of time, then disband the group to later re-form another one with different people.

A similar situation can be achieved by setting up a private group DM, with the downsides of:

1. Having to befriend all those that are involved in the group DM (this is only true for the creator of the group DM).
2. Not having access to bots.
3. Not having any kind of moderation or 3rd party control over what happens in the group DM.

In order to preserve the privacy of the group, each raid room will be assigned with a PIN that will only be shared with the room master (whoever created the room). Other users will only be able to enter the room by knowing the PIN code, or being invited by the room master.

Each user can create a maximum of **2** rooms at the same time on a server: **1** text and **1** voice rooms.

Each raid room will expire after a set amount of time, as defined by the user (a soft cap can be set by the mods/admins). When that happens, the channel is automatically deleted. Warning messages will be sent to the room master before that happens.

When a text raid room expires, a chat log is dumped and saved (encrypted). The chat log will be posted into the raid rooms logger channel (see :ref:`first-setup`).

One or more roles can be set as "supervisor" roles. Supervisors will have moderation powers over raid rooms, similar to how moderators have powers over the rest of the server (see :ref:`supervisor-commands`).

.. admonition:: Premium

    Out of the box, each server is limited to having a total of **5 simultaneous Raid Rooms**. If you want to remove this limitation, you can unlock the number of Raid Rooms as a **Premium** feature (see: :ref:`premium-perks`).

....

.. _first-setup:

First Setup
===========

Upon first creation of a room, a "Raid Rooms" channel category will be created. This category will host all of the created raid rooms and the raid rooms logger channel.

This category and the logging channel are hidden to the rest of the server by default. The corresponding permissions will be updated on each command run for the supervisor roles, and both the category and the logger channel will be recreated on the next command run if they are deleted.

You can change the category and channel names, and move the logger channel to another category after it's created.

....

Public Commands
===============

.. _rrcreate:

|bot_prefix|\ rrcreate
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrcreate [text/voice] [--members/--m {room size, including the master (number)}] [--duration/--d {duration timecode}] [--pin/--password/--p {custom PIN}]

Command Description
^^^^^^^^^^^^^^^^^^^
Creates a new raid room. The PIN will be sent to the room master via DM.

All parameters are optional. If omitted, each parameter will be set as the default for the server (see :ref:`rradefaults`). If no default values are assigned for the specific server, the overall default values are:

* **Room Type**: text
* **Members**: 4
* **Duration**: 1 hour

Both parameters have a soft cap that can be set for the server. If these soft cap values aren't assigned for the specific server, the overall default values are:

* **Members**: 8
* **Duration**: 1 day

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **Bot**: Manage Channels, Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrcreate
    |bot_prefix|\ rrcreate voice
    |bot_prefix|\ rrcreate --members 6

....

|bot_prefix|\ rrjoin
--------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrjoin (room id) (room PIN)

Command Description
^^^^^^^^^^^^^^^^^^^
Join a room by knowing its ID and PIN.

The request message will be automatically deleted on success, in order to preserve the secrecy of the PIN.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **Bot**: Manage Channels, Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrjoin abcdef 1234

....

|bot_prefix|\ rrleave
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrleave (room id)

Command Description
^^^^^^^^^^^^^^^^^^^
Leave a specific room.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **Bot**: Manage Channels, Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrleave abcdef

....

|bot_prefix|\ rrstatus
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrstatus (room id)

Command Description
^^^^^^^^^^^^^^^^^^^
Obtain info about a room by knowing its room ID.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **Bot**: Manage Channels, Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrstatus abcdef

....

Room Master Commands
====================

After creating a room through :ref:`rrcreate`, the user that opened the room becomes the "Room Master" and gains access to a set of additional commands used to manage the owned rooms.

|bot_prefix|\ rrinvite
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrinvite (room id) (user id(s)/mention(s)/q_name(s))

Command Description
^^^^^^^^^^^^^^^^^^^
Invite one or more users to your room. They will be automatically added without any interaction from the target user(s). The PIN won't be shared with the target user(s).

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **Bot**: Manage Channels, Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrinvite abcdef @cycloptux#1543

....

|bot_prefix|\ rrclose
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrclose (room id)

Command Description
^^^^^^^^^^^^^^^^^^^
Closes the room, deleting the corresponding channel. If the room type was set as text, a chat log is dumped and saved (encrypted). The chat log will be posted into the raid rooms logger channel (see :ref:`first-setup`).

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **Bot**: Manage Channels, Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrclose abcdef

....

|bot_prefix|\ rrnewpw
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrnewpw (room id)

Command Description
^^^^^^^^^^^^^^^^^^^
Assigns a new PIN to the room, useful if the PIN is somehow leaked. The PIN will be sent to the room master via DM.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **Bot**: Manage Channels, Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrnewpw abcdef

....

|bot_prefix|\ rrkick
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrkick (room id) (user id(s)/mention(s)/q_name(s))

Command Description
^^^^^^^^^^^^^^^^^^^
Kicks one or more users from a room. Kicked users will be able to re-join the room if they know the PIN or are re-invited.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **Bot**: Manage Channels, Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrkick abcdef @cycloptux#1543

....

|bot_prefix|\ rrban
--------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrban (room id) (user id(s)/mention(s)/q_name(s))

Command Description
^^^^^^^^^^^^^^^^^^^
Bans one or more users from a room. Banned users **won't** be able to re-join the room even if they know the PIN or are re-invited.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **Bot**: Manage Channels, Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrban abcdef @cycloptux#1543

....

|bot_prefix|\ rrunban
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrunban (room id) (user id(s)/mention(s)/q_name(s))

Command Description
^^^^^^^^^^^^^^^^^^^
Lifts ban status from one or more users for the specified room. Formerly banned users will now be able to re-join the room if they know the PIN or are re-invited.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **Bot**: Manage Channels, Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrunban abcdef @cycloptux#1543

....

.. _rrextend:

|bot_prefix|\ rrextend
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrextend (room id)

Command Description
^^^^^^^^^^^^^^^^^^^
Extends the duration of a room that is about to expire. This command can only be used when there are **less than 5 minutes left** on the normal expiration of a room.

The room timer will be refreshed, adding the initial duration to the current time (e.g. if the room was supposed to last 24 hours, 24 more hours will be added to that room).

This command can only be used once.

.. note::
    Server managers are able to prohibit the usage of this command through :ref:`rraextend`.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **Bot**: Manage Channels, Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrextend abcdef

....

.. _supervisor-commands:

Supervisor Commands
===================

These commands can only be used by administrators and supervisors. To assign one (or more) role(s) as supervisor roles, see :ref:`rrasetsvrole`.

|bot_prefix|\ rrsls
-------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrsls

Command Description
^^^^^^^^^^^^^^^^^^^
Lists all active raid rooms in the server.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **Bot**: Manage Channels, Manage Messages

....

|bot_prefix|\ rrskick
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrskick (room id) (user id(s)/mention(s)/q_name(s))

Command Description
^^^^^^^^^^^^^^^^^^^
Kicks one or more users from a room. Kicked users will be able to re-join the room if they know the PIN or are re-invited.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **Bot**: Manage Channels, Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrskick abcdef @cycloptux#1543

....

|bot_prefix|\ rrsban
--------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrsban (room id) (user id(s)/mention(s)/q_name(s))

Command Description
^^^^^^^^^^^^^^^^^^^
Bans one or more users from a room. Banned users **won't** be able to re-join the room even if they know the PIN or are re-invited.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **Bot**: Manage Channels, Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrsban abcdef @cycloptux#1543

....

|bot_prefix|\ rrsunban
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrsunban (room id) (user id(s)/mention(s)/q_name(s))

Command Description
^^^^^^^^^^^^^^^^^^^
Lifts ban status from one or more users for the specified room. Formerly banned users will now be able to re-join the room if they know the PIN or are re-invited.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **Bot**: Manage Channels, Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrsunban abcdef @cycloptux#1543

....

|bot_prefix|\ rrsbreak
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrsunban (room id)

Command Description
^^^^^^^^^^^^^^^^^^^
Forcefully closes the room, deleting the corresponding channel, without warning the room master. If the room type was set as text, a chat log is dumped and saved (encrypted). The chat log will be posted into the raid rooms logger channel (see :ref:`first-setup`).

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **Bot**: Manage Channels, Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrsbreak abcdef

....

|bot_prefix|\ rrsforbid
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrsforbid (room id) (user id(s)/mention(s)/q_name(s))

Command Description
^^^^^^^^^^^^^^^^^^^
Prohibits one or more users from creating Raid Rooms. This command won't break any existing room.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **Bot**: Manage Channels, Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrsforbid abcdef @cycloptux#1543

....

|bot_prefix|\ rrsallow
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrsallow (room id) (user id(s)/mention(s)/q_name(s))

Command Description
^^^^^^^^^^^^^^^^^^^
Lifts the prohibition status from one or more users, allowing them to create Raid Rooms.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **Bot**: Manage Channels, Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrsallow abcdef @cycloptux#1543

....

|bot_prefix|\ rrslsforbid
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrslsforbid

Command Description
^^^^^^^^^^^^^^^^^^^
Lists the users that are currently forbidden from creating Raid Rooms in the current server.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **Bot**: Manage Channels, Manage Messages

....

Administrator Commands
======================

Administrators and server managers (users with "Manage Server" permissions) have access to a few configuration commands used to apply server-specific raid room settings.

.. _rrasetsvrole:

|bot_prefix|\ rrasetsvrole
--------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrasetsvrole (role id(s)/mention(s)/q_name(s))

Command Description
^^^^^^^^^^^^^^^^^^^
Toggles one or more role(s) as supervisor role (see :ref:`supervisor-commands`). Use with no params to see the current list of supervisor roles.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Guild
| **Bot**: Manage Channels, Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrasetsvrole @RaidRoomSupervisor
    
....

.. _rradefaults:

|bot_prefix|\ rradefaults
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rradefaults [--type [text/voice]] [--max-members [{number}]] [--members [{number}]] [--max-duration [{timecode}]] [--duration [{timecode}]]

Command Description
^^^^^^^^^^^^^^^^^^^
Sets the raid rooms default values for this server. Use any of the params without an argument to reset the param to the overall default value. Use with no params at all to see the current default settings.

``--type``
""""""""""

Type can be either ``text`` or ``voice``. The overall default is ``text``.

``--members``
"""""""""""""

This param lets administrators and managers configure the default value for the number of members in a raid room if ``--members`` is omitted in :ref:`rrcreate`.

``--max-members``
"""""""""""""""""

This param lets administrators and managers configure the soft cap for the maximum number of members that a user can request by using the ``--members`` param in :ref:`rrcreate`.

The hard cap for the maximum number of members that can join a room is set to 9999.

The hard cap for the minimum number of members that can join a room is set to 2.

``--duration``
""""""""""""""

This param lets administrators and managers configure the default value for the duration of a raid room if ``--duration`` is omitted in :ref:`rrcreate`.

``--max-duration``
""""""""""""""""""

This param lets administrators and managers configure the soft cap for the duration of a raid room that a user can request by using the ``--duration`` param in :ref:`rrcreate`.

The hard cap for the longest duration of a room is set to 1 year.

The hard cap for the shortest duration of a room is set to 10 minutes.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Guild
| **Bot**: Manage Channels, Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rrasetsvrole --type voice --max-members 16 --duration 2h
    |bot_prefix|\ rrasetsvrole --max-duration
    |bot_prefix|\ rrasetsvrole

.. _rraextend:

|bot_prefix|\ rraextend
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ rraextend

Command Description
^^^^^^^^^^^^^^^^^^^
Toggles the ability for Room Masters to use the :ref:`rrextend` command.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Guild
| **Bot**: Manage Channels, Manage Messages
