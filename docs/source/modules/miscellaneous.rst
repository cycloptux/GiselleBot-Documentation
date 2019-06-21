*************
Miscellaneous
*************

This module contains generally safe, atomic commands that aren't otherwise categorized into a dedicated module.

....

Bot Information
===============

|bot_prefix|\ invite
--------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ invite

Command Description
^^^^^^^^^^^^^^^^^^^
Creates and shows an invite to get the bot into a Discord server you manage.

....

|bot_prefix|\ stats
-------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ stats

Command Description
^^^^^^^^^^^^^^^^^^^
Shows technical info about the bot and the infrastructure it's running on.

....

|bot_prefix|\ ping
------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ ping

Command Description
^^^^^^^^^^^^^^^^^^^
Tests the bot ping response.

Calculates ping between sending a message and editing it, giving a nice round-trip latency.

The second ping is an average latency between the bot and the websocket server (one-way, not round-trip).

....

Internet Lookups
================

|bot_prefix|\ urban
-------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ urban (search string) [--more]

Command Description
^^^^^^^^^^^^^^^^^^^
Urban Dictionary text lookup. The output will be the highest ranked result. The embed title will hyperlink to the corresponding online page.

Using ``--more`` will show up to 5 results, if available.

.. note::
    By default, given the nature of the website, the output of any Urban Dictionary lookup will be checked against a list of "not safe for work" words and "censored" accordingly. This check will be skipped if the channel where the command is run is set as **NSFW**.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ urban guinea tee
    
....

|bot_prefix|\ ytsearch
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ vsearch (search string)

Command Description
^^^^^^^^^^^^^^^^^^^
Looks for YouTube videos based on the selected lookup string. The top result will be available to be played in Discord.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ ytsearch veritasium
