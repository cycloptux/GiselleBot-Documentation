******
Trivia
******

.. warning::
    This module is currently on a **Closed Beta Test (CBT)** phase. The module design is reaching its stable phase and isn't currently final. This documentation page will be updated as the module reaches its Release Candidate (RC) phase.
    
This module lets users play trivia quiz games on Discord. The module gets its default questions from the **Open Trivia Database**, which offers more than 3,000 validated questions in more than 15 categories.

The trivia module is meant to be public and used by anyone for fun. Users with "Manage Messages" & "Manage Roles" permissions, hereafter called "Elevated Users", will also have access to extra settings that will make them able to set trivia quiz games up for use by other users (typical use cases include events, giveaways, etc.).

Trivia games can be **timed** or **immediate**.

* **Immediate** trivia games move to the next question as soon as one answer is collected.
* **Timed** trivia games move to the next question as soon as a certain time interval passes, and collect answers from anyone during that period (limitations may apply, see later).

Depending on the "type" of user running the command(s), some limitations apply to the usage of the trivia module. The following table shows such limitations.

+-------------------------+----+-----------+-------+---------+-----+-----+
| User Type               | MQ | MT        | RR    | TC      | AD  | SE  |
+=========================+====+===========+=======+=========+=====+=====+
| Normal (non-"Elevated") | 10 | 3 minutes | No    | No      | No  | No  |
+-------------------------+----+-----------+-------+---------+-----+-----+
| Elevated                | 20 | 6 hours   | Yes\* | Yes\*\* | Yes | Yes |
+-------------------------+----+-----------+-------+---------+-----+-----+
| Elevated (Premium)      | 30 | 7 days    | Yes\* | Yes\*\* | Yes | Yes |
+-------------------------+----+-----------+-------+---------+-----+-----+

* **MQ**: Maximum # of Questions
* **MT**: Maximum Time Interval
* **RR**: Can set role restrictions
* **TC**: Can set a different target channel
* **AD**: Can configure auto-deletion of messages
* **SE**: Can configure and/or start someone else's trivia

| :sub:`\*: Users are not allowed to set a role restriction to roles higher than the highest role they have.`
| :sub:`\*\*: Users are not allowed to set a target channel to a channel they don't have R/W access to (Read Messages and/or Send Messages).`

.. admonition:: Premium

    As shown in the table, premium-enabled servers will have an increased cap of 30 questions and can set an interval for timed trivia games up to 1 week.

|bot_prefix|\ triviacategories
------------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ trcat
    
Command Description
^^^^^^^^^^^^^^^^^^^
Shows all available trivia category names, and the corresponding number of available questions.

....

|bot_prefix|\ triviainit
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ trinit
    
Command Description
^^^^^^^^^^^^^^^^^^^
Initializes a trivia in the current channel.

Default settings are:

* **Name**: None
* **Description**: None
* **Channel**: Current
* **Categories**: Any
* **Role Restriction**: None
* **Trivia Mode**: Immediate
* **Trivia Questions**: 5
* **Auto-delete Answer**: Yes
* **Auto-delete Confirmation**: No

See |bot_prefix|\ triviasetup to understand the meaning of each parameter.

....

|bot_prefix|\ triviasetup
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ trsetup (trivia id)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Opens the trivia game interactive setup menu. Use the menu items to configure the above settings.

**Name** will show in the title of each embed related to that trivia. Trivia names cannot be longer than 128 characters.

**Description** will appear on each question, and in the starting and final embed. Trivia descriptions cannot be longer than 1024 characters.

**Categories** can be left blank ("any category") or it can be used to restrict the questions to **one or more** categories. At the time of writing this documentation page, the categories available from the Open Trivia Database are:

1. Animals
2. Art
3. Celebrities
#. Entertainment: Board Games
#. Entertainment: Books
#. Entertainment: Cartoon & Animations
#. Entertainment: Comics
#. Entertainment: Film
#. Entertainment: Japanese Anime & Manga
#. Entertainment: Music
#. Entertainment: Musicals & Theatres
#. Entertainment: Television
#. Entertainment: Video Games
#. General Knowledge
#. Geography
#. History
#. Mythology
#. Politics
#. Science & Nature
#. Science: Computers
#. Science: Gadgets
#. Science: Mathematics
#. Sports
#. Vehicles

The categories selection supports partial names: if you want to select "Mythology" you can just use "myth", etc.

.. note::
    There will soon be a way to add custom categories and custom questions to the database.

**Interval** is the amount of time a question will be up in a **timed** trivia. Disabling this parameter sets the trivia mode to **immediate**. Go to the top of this page to understand the difference between the two modes.

**Questions Amount** is the number of questions after which the trivia game will end. Refer to the limitations table at the top of this page to know the limits. A trivia game will always end if the actual amount of available questions is lower than the "configured" amount.

**Channel** is the actual channel the trivia will be started into after the |bot_prefix|\ triviastart command. As stated in the limitations table, it can be set to another channel only if you are an "Elevated" user.

.. note::
    There can only be **1** running (or paused) trivia game per channel at a given time.
    
**Authorized Roles**, as the name suggests, are roles authorized to submit answers to the selected trivia. If omitted, everyone will be able to submit an answer. If one or more roles are configured, users will need to have at least one of these roles to submit an answer.

**Auto-deletion of Answers** toggles whether or not the bot should delete the answers posted by a user. In order to keep the secrecy of a user's answer (especially in timed trivia games), this configuration is active by default.

**Auto-deletion of Confirmation Messages** toggles whether or not the bot should delete its own confirmation message upon registering an answer. The deletion of confirmation messages happens after 5 seconds.
    
Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ trsetup 0
    |bot_prefix|\ trset 2
    
....

|bot_prefix|\ triviastart
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ trstart (trivia id)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Starts a trivia game in the configured target channel, using the corresponding settings.

.. note::
    There can only be **1** running (or paused) trivia game per channel at a given time.
    
Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ trstart 0
    
....

|bot_prefix|\ triviaanswer
--------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ tra (answer number)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Submits an answer to the currently running trivia. Since only 1 running trivia game can be running in a channel at a given time, you won't need to specify the trivia ID.
    
Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ tra 2
    |bot_prefix|\ tra 4
    
....

|bot_prefix|\ triviaresults
---------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ trres (trivia id)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Prints the final results of a trivia game. This is the same embed that is printed when a trivia game ends, showing the top 5 users and their corresponding scores.
    
Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ trres 0
    
....

|bot_prefix|\ triviamyresults
-----------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ trmyres (trivia id)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Shows a detailed list of questions and the corresponding submitted answers for the user running this command, showing whether the given answers are correct or not.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ trmyres 0
    |bot_prefix|\ trmres 2
    
....

|bot_prefix|\ triviashow
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ trshow [trivia id]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Shows the current configuration of a trivia, given its ID.

If the ID is omitted, the command will show the info of the running (or paused) trivia game in the current channel, if any.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ trshow
    |bot_prefix|\ trshow 2
    
....

|bot_prefix|\ trivialist
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ trlist
    
Command Description
^^^^^^^^^^^^^^^^^^^
Shows the list of all (non-deleted) trivias in the server: their ID, name and status.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ trls
    
....

|bot_prefix|\ triviapause
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ trpause [trivia id]
    
Command Description
^^^^^^^^^^^^^^^^^^^
**This command is only available to Elevated Users.**

Pauses a trivia, given its ID. Pausing a trivia will make users unable to submit answers for that trivia. If the trivia game was set as **timed**, the timer for the currently running question will keep clocking, but will then freeze without moving to the next question.

If the ID is omitted, the command will attempt to pause the trivia game in the current channel, if any.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Messages, Manage Roles

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ trpause
    |bot_prefix|\ trpause 2
    
....

|bot_prefix|\ triviaresume
--------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ trresume [trivia id]
    
Command Description
^^^^^^^^^^^^^^^^^^^
**This command is only available to Elevated Users.**

Resumes a previously paused trivia, given its ID. Resuming a trivia will make users able to submit answers for that trivia again.

If the ID is omitted, the command will attempt to resume the paused trivia game in the current channel, if any.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Messages, Manage Roles

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ trresume
    |bot_prefix|\ trresume 2
    
....

|bot_prefix|\ triviadelete
--------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ trdelete [trivia id]
    
Command Description
^^^^^^^^^^^^^^^^^^^
**This command is only available to Elevated Users.**

**This command only works on paused or completed trivia games.**

Stops (if paused) and deletes a trivia game from the server, also hiding its ID from |bot_prefix|\ trivialist.

If the ID is omitted, the command will attempt to delete the paused trivia game in the current channel, if any.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Manage Messages, Manage Roles

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ trdelete
    |bot_prefix|\ trdelete 2
    