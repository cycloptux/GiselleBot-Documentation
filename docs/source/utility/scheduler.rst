*****************
Command Scheduler
*****************

This module lets users delay the usage of a command to a later date.

When delaying a command, the permission checks for the target command will be checked **both** during the first scheduling request, and then re-checked at run-time. This means that any user willing to schedule an administrator-locked command, will have to have administrator permissions when running the initial scheduler command, and still have administrator permissions by the time the command is scheduled to run. Failing either checks will reject the command run (either by not letting the user schedule the command at all, or failing at run-time). It doesn't matter if a user temporarily loses permissions in between the scheduler command and the actual target command, as long as they have enough permissions when the scheduler is due.

The scheduled command will be ignored if the user is not in the server, or loses "Read Messages" or "Send Messages" permissions in the channel they run the scheduler command into, by the time the command is due to run. Again, it doesn't matter if the user temporarily leaves the server or loses those permissions, as long as they are back up when the scheduler is due.

|bot_name| will notify the channel where the scheduler command was run into as soon as the command is due. The bot **must** still have "Read Messages" and "Send Messages" permissions in that channel to notify the command run before actually running the scheduled command. Failing the notification will also abort the actual command run.

.. warning::
    **Important Note**: While parameters order usually doesn't matter, the command scheduler poses an exception and **require** the ``--command`` parameter to be the **last of the chain**. Any further parameter will be treated as a parameter of the **scheduled command** and not of the command scheduler itself.

.. admonition:: Premium

    By default, each server is limited to scheduling commands within a time interval of no more than **1 hour**. You can unlock higher interval times as a **Premium** feature (see: :ref:`premium-perks`):
    
    * **Tier 1** patron servers will have their cap increased to **12 hours**.
    * **Tier 2** patron servers will have their cap increased to **1 week** (7 days).
    * **Tier 3** patron servers will have their cap increased to **1 month** (31 days).

.. admonition:: Possible Use Cases
    
    This command enables for quite a few interesting use cases. Here are some commands that may get a good boost out of this feature:
    
    * Scheduling announcements, using :ref:`msgsend`
    * Scheduling (massive) addition and/or removal of roles, using :ref:`addrole` and :ref:`remrole`
    * Scheduling repeating message to fire at an exact time and then repeating every X minutes/hours (the default limitation for that use case in the native command is that the repeating message defaults to running every 24 hours) using :ref:`repeat`

....

One-Off Command Scheduler
=========================

|bot_prefix|\ schedule
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ schedule (--interval/--i {time code}) [--channel/--c {channel id/mention}] [--silent] (--command/--cmd {command})

Command Description
^^^^^^^^^^^^^^^^^^^
Runs a command within the current server, after certain amount of time. Check the top of this page for more info.

|bot_name| will treat the command as if it was sent in the current channel, or to a different target channel if the ``--channel`` parameter is used, after the specified amount of time.

When the ``--silent`` parameter is used, the confirmation notification that is sent in the original command channel when the command is triggered will be suppressed.

.. warning::
    Scheduling a command **requires** the ``--command`` parameter to be the **last of the chain**. Any further parameter will be treated as a parameter of the **scheduled command** and not of the command scheduler itself.

Permissions for the target command will be checked when initially scheduling, and at run-time. Although, the actual correct formatting of the command will only be checked at run-time, so be sure to test the commands beforehand if you are not sure about their correctness.

Limitations apply to the maximum interval of time you can set for the scheduler, and can be increased for **Premium**-enabled servers servers. See above.

.. note::
    Up to **5** schedulers can be active at any time for each user within a server.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ schedule --interval 5m --command |bot_prefix|\ ping
    |bot_prefix|\ schedule --i 2d --cmd |bot_prefix|\ msgsend #announcements @everyone A new update is live!
    |bot_prefix|\ schedule --i 14d --cmd |bot_prefix|\ remrole @Moderator_In_Training#1234 "Moderator"

....

|bot_prefix|\ schedulelist
--------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ schedulelist
    
Command Description
^^^^^^^^^^^^^^^^^^^
Lists all schedulers that the user created within the server. Server managers (users with "Manage Server" permissions) will be able to see all schedulers created by anyone within the current server.

It may take up to a few seconds before a newly added scheduler appears in the list.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ schedlist
    |bot_prefix|\ schedls

....

|bot_prefix|\ scheduleremove
----------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ scheduleremove (scheduler index)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Deletes a scheduler on the specified index, as shown by |bot_prefix|\ schedulelist. Users can only remove their own schedulers. Server managers (users with "Manage Server" permissions) can remove any scheduler created by anyone within the current server.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ scheddel 1
    |bot_prefix|\ schedrm 3

....
    
Recurring Command Scheduler
===========================

|bot_prefix|\ schedulerecurring
-------------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ schedulerec (--interval/--i {time code}) [--channel/--c {channel id/mention}] [--silent] (--command/--cmd {command})

Command Description
^^^^^^^^^^^^^^^^^^^
Runs a command, **recurringly**, within the current server, after certain amount of time and then every time the specified interval is over. Check the top of this page for more info.

|bot_name| will treat the command as if it was sent in the current channel, or to a different target channel if the ``--channel`` parameter is used, after the specified amount of time.

When the ``--silent`` parameter is used, the confirmation notification that is sent in the original command channel when the command is triggered will be suppressed.

.. warning::
    Scheduling a command **requires** the ``--command`` parameter to be the **last of the chain**. Any further parameter will be treated as a parameter of the **scheduled command** and not of the command scheduler itself.

Permissions for the target command will be checked when initially scheduling, and at run-time. Although, the actual correct formatting of the command will only be checked at run-time, so be sure to test the commands beforehand if you are not sure about their correctness.

Limitations apply to the maximum interval of time you can set for the scheduler, and can be increased for **Premium**-enabled servers servers. See above.

.. note::
    Up to **5** recurring schedulers can be active at any time within a server.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ schedulerecurring --interval 5m --command |bot_prefix|\ ping
    |bot_prefix|\ schedulerec --i 2d --cmd |bot_prefix|\ msgsend #announcements @everyone A new update is live!

....

|bot_prefix|\ schedulerecurringlist
-----------------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ schedreclist
    
Command Description
^^^^^^^^^^^^^^^^^^^
Lists all recurring schedulers created within the server.

It may take up to a few seconds before a newly added scheduler appears in the list.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ schedreclist
    |bot_prefix|\ schedrecls

....

|bot_prefix|\ schedulerecurringremove
-------------------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ schedrecdel (scheduler index)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Deletes a scheduler on the specified index, as shown by |bot_prefix|\ schedulerecurringlist.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ schedrecdel 1
    |bot_prefix|\ schedrecrm 3

....

|bot_prefix|\ schedulerecurringinvoke
-------------------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ schedrecinv (scheduler index)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Immediately invokes (sends) a scheduler on the specified index, as shown by |bot_prefix|\ schedulerecurringlist.

Invoking a scheduled recurring command also restarts its timer, hence potentially changing the clock time when the next command is going to trigger.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Server

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ schedrecinv 3
