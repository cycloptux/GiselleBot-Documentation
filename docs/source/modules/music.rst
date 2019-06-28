*****
Music
*****

The Music module enables users to listen to YouTube music in a Discord server's dedicated voice channel.

.. admonition:: Patreon

    By default, each server is limited to having a maximum of **3 songs in a queue**, and each song can only be a maximum of **8 minutes long**. You can unlock up to **50 song-queues** and uncap the duration limit (also enabling the streaming of **live channels**) via **Patreon** pledges (see: :ref:`patreon-perks`).
    
    Out of the following commands, |bot_prefix|\ mpause, |bot_prefix|\ mresume, |bot_prefix|\ mvolume and |bot_prefix|\ mlyrics can be unlocked via **Patreon** pledges (see: :ref:`patreon-perks`).

|bot_prefix|\ mplay
-------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ mp (song name or search keyword)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Searches a song with the given keyword and plays the first result automatically.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ mplay Never Gonna Give You Up

....

|bot_prefix|\ msearch
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ msearch (song name or search keyword)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Searches a song with the given keyword and shows a selection of results to play.

....

|bot_prefix|\ mskip
-------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ ms
    
Command Description
^^^^^^^^^^^^^^^^^^^
Skips to the next queued song. If 3 or more people are listening to the same song, a vote will happen.

For a vote skip to take effect, **70%** of the voice channel members must agree.

.. note:
    Let's assume there are 10 users in the music voice channel.
    The threshold for skipping is calculated as 70% of 10 = 7 (numbers will be rounded down if needed).
    For the vote skip to take effect, you would then need 7 positive votes.

.. note:
    Vote skip will not be active until there are 3 or more people in the voice channel (with one person, insta-skip is enabled and with two the threshold for skipping is 1).
    Administrators will bypass the voting system.

....

|bot_prefix|\ mstop
-------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ mstop
    
Command Description
^^^^^^^^^^^^^^^^^^^
Immediately stops the ongoing playlist.

.. note:
    This command is only available if you are alone in the voice channel or if you have "Manage Channels" permissions.

....

|bot_prefix|\ mpause
--------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ mpause
    
Command Description
^^^^^^^^^^^^^^^^^^^
Pauses the currently playing track.

.. note:
    This command is only available if you are alone in the voice channel or if you have "Manage Channels" permissions.

....

|bot_prefix|\ mresume
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ mresume
    
Command Description
^^^^^^^^^^^^^^^^^^^
Resumes paused music.

....

|bot_prefix|\ mrewind
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ mrewind
    
Command Description
^^^^^^^^^^^^^^^^^^^
Rewinds the currently playing track and starts playing it from the beginning.

.. note:
    This command is only available if you are alone in the voice channel or if you have "Manage Channels" permissions.

....

|bot_prefix|\ mvolume
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ mvolume
    
Command Description
^^^^^^^^^^^^^^^^^^^
Checks or changes the current volume.

.. note:
    This command is only available if you are alone in the voice channel or if you have "Manage Channels" permissions.

....

|bot_prefix|\ mnp
-----------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ mnp
    
Command Description
^^^^^^^^^^^^^^^^^^^
Shows what song the bot is currently playing.

....

|bot_prefix|\ mqueue
--------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ mqueue
    
Command Description
^^^^^^^^^^^^^^^^^^^
Shows the music queue.

....

|bot_prefix|\ mlyrics
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ mlyrics [song name or search keyword]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Gets the lyrics of the current playing song **or** looks for lyrics by song name or keyword.

....

|bot_prefix|\ mremove
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ mremove
    
Command Description
^^^^^^^^^^^^^^^^^^^
Removes a certain entry from the queue. 

.. note:
    This command is only available if you are alone in the voice channel or if you have "Manage Channels" permissions.

....

|bot_prefix|\ mskipto
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ mskipto
    
Command Description
^^^^^^^^^^^^^^^^^^^
Skips to a certain position in the queue. If 3 or more people are listening to the same song, a vote will happen.

For a vote skip to take effect, **70%** of the voice channel members must agree.

.. note:
    Let's assume there are 10 users in the music voice channel.
    The threshold for skipping is calculated as 70% of 10 = 7 (numbers will be rounded down if needed).
    For the vote skip to take effect, you would then need 7 positive votes.

.. note:
    Vote skip will not be active until there are 3 or more people in the voice channel (with one person, insta-skip is enabled and with two the threshold for skipping is 1).
    Administrators will bypass the voting system.

....

|bot_prefix|\ mrmdupes
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ mrmdupes
    
Command Description
^^^^^^^^^^^^^^^^^^^
Removes duplicate songs from the queue.

....

|bot_prefix|\ mleavecleanup
---------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ mleavecleanup
    
Command Description
^^^^^^^^^^^^^^^^^^^
Removes absent users' songs from the queue.

....

|bot_prefix|\ mchannel
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ mchannel [channel id, or "-"]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Sets a channel as the authorized music channel for the bot.

Running this command while being in a voice channel will turn the current voice channel into the authorized music channel. You can also use the ID of a voice channel.

Running this command while not in a voice channel and without any extra argument will show the current authorized music channel.

Using "-" as argument will remove the current authorized music channel and disable the music module until a voice channel is authorized.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Administrator

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ mchannel
    |bot_prefix|\ mchannel 123456789098765432
    |bot_prefix|\ mchannel -
