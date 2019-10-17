******************
Alarms & Reminders
******************

This module includes tools to set timed reminders.

|bot_prefix|\ remind
--------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ remind (recipient) (time code) (message)

Command Description
^^^^^^^^^^^^^^^^^^^
Sends a message to you (via DM) or a channel within the current server, after certain amount of time.

The recipient parameter can be either ``me``, ``here``, or a channel mention or name.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ remind #party-chat 2h It's party time!

....

|bot_prefix|\ remindlist
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ remindlist
    
Command Description
^^^^^^^^^^^^^^^^^^^
Lists all reminders you created within the server.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ remindls

....

|bot_prefix|\ reminddel
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ reminddel (reminder index)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Deletes a reminder on the specified index, as shown by |bot_prefix|\ remindlist.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ reminddel 1
    |bot_prefix|\ remindrm 3

....

|bot_prefix|\ remindtemplate
----------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ remindtemplate (reminder message)
    
Command Description
^^^^^^^^^^^^^^^^^^^
**This command is currently not active.**

Sets message template for when a reminder is triggered. 

You can use one (or more) of these placeholders in your response message:

* **%message%**: The message specified in the remind command. This placeholder is **mandatory**.
* **%target%**: The target channel of the remind command.
* **%botname%**: The name of the bot.
* **%user%**: This will be replaced with a mention of the user who ran the command.
* **%server%**: This will be replaced with the server name.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Bot Owner

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ remindtemplate Hello %user%~! %botname% here to tell you %message%!

....

.. _repeat:

|bot_prefix|\ repeat
--------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ repeat (time in minutes) (message)
    |bot_prefix|\ repeat (time of day, HH:mm, UTC timezone) (message)
    |bot_prefix|\ repeat (--message/--m {message to repeat}) [--no-redundant/--n] [--interval/--i {time code}] [--channel/--c {channel id/mention/q_name}]

Command Description
^^^^^^^^^^^^^^^^^^^
Repeat a message periodically in a channel.

This command has a quick syntax (with 2 variations) and a full syntax. It is advised to use the full syntax if you want take advantage of the advanced settings. Some advanced parameters will still work with the quick syntaxes, but using that mix is not officially supported.

.. admonition:: Premium

    Each server can have a maximum of 5 repeating messages. If you need more repeating messages, you can unlock more via **Patreon** pledges (see: :ref:`patreon-perks`).

The default interval time is set to 1 day, and the first message will begin being sent after the first time interval has passed.

The ``--no-redundant`` parameter will instruct the bot to skip sending a repeating message if the latest message in the channel is still the last repeating message.

.. note::
    Using the 2nd syntax (the one that specifies the time of the day) will automatically set the interval to 1 day, and repeat the message everyday around the same clock time.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ repeat 120 2 hours have passed since my last message.
    |bot_prefix|\ repeat 8:00 Everyone, wake up!
    |bot_prefix|\ repeat --m This is not a spam channel, please behave correctly. --c #serious-chat --i 6h --no-redundant

....

|bot_prefix|\ repeatlist
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ repeatlist
    
Command Description
^^^^^^^^^^^^^^^^^^^
Lists all repeating messages within the server.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ repls

....

|bot_prefix|\ repeatremove
--------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ repeatremove (repeating message index)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Deletes a repeating message on the specified index, as shown by |bot_prefix|\ repeatlist.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ reprm 3

....

|bot_prefix|\ repeatinvoke
--------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ repeatinvoke (repeating message index)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Immediately invokes (sends) a repeating message on the specified index, as shown by |bot_prefix|\ remindlist.

Invoking a message also restarts its timer, hence potentially changing the clock time when the next reminders are going to show.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Messages

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ repinv 3
