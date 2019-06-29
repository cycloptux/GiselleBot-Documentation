*************
Forms Builder
*************

The Forms Builder module enables users to create Q/A forms that are presented to end-users by sending a Direct Message to the bot. The Q/As can be set up to be a sequence of multi-choice or open questions, with the final output (submission) being sent into a server channel by the bot itself for further validation, priority assignment and optional integration with external services.

(Optional feature) Upon accepting a submission, a submission summary will appear in a different channel and will be automatically given an "upvote" and "downvote" reaction for people to show their support (or lack of) to the specific submission.

Currently, each form submission can be configured to remain within the Discord realm, or uploaded to `Trello <https://trello.com/>`_ (a powerful web-based, list-making application) as a "Trello card".

Trello integration also includes the 2-way synchronization of upvotes/downvotes and comments number from and to Discord and Trello (showing the number of upvotes and downvotes on the Trello card, as well as showing the current number of Trello comments and votes on the Discord message), and Discord DM notifications to the author of the submission upon Trello card activities (new comments, title changes, card archival, etc.).

.. warning::
    For the **Trello** integration to work, some limitations currently apply:
    
    1. Each form will be sent to one board, you cannot have 2 forms posting to the same board (this will be fixed in the near future).
    2. The Trello board must exist before a card is uploaded, its name must be exactly what the bot will tell you to be after creating a form, and must be adjusted if you change your server name or form name (more details later) (this will be fixed in the near future).
    3. You must **invite** the bot to your Trello team and give it permissions to edit the board in order for the bot to monitor, post and update cards.
    4. You must **pair** the Discord server with the Trello team by using the |bot_prefix|\ trellopair command. Each Discord server can only be paired with 1 Trello team.

.. note::
    A **web dashboard (BETA)** will soon be available to create, edit and and maintain forms.
    
.. admonition:: Patreon

    Out of the box, each server is limited to having a total of **1 available form**. If you want to remove this limitation and have up to **20** forms, you can unlock the number of forms via **Patreon** pledges (see: :ref:`patreon-perks`).

|bot_prefix|\ trellopair
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ trellopair [team name]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Pairs a Discord server with a Trello team. Using the command without the team name will unpair the server from the Trello team.

.. note::
    The team name is the one you find inside the Trello URL within the team page, which usually has this form: ``https://trello.com/TEAM_NAME/home``

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Administrator

....

.. _submit:

|bot_prefix|\ submit
--------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ submit
    
Command Description
^^^^^^^^^^^^^^^^^^^
.. note::
    This command is only available in a Direct Message channel with the bot. It will **not** work in actual servers, and it's not subject to any permissions other than a blacklist check (see |bot_prefix|\ formblacklist).

Shows the available forms for the servers a user is currently in, giving the option to start filling a submission.

....

|bot_prefix|\ forminit
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ foinit

Command Description
^^^^^^^^^^^^^^^^^^^
Initializes a new form builder. The bot will guide the user into setting up the basic configurations and first question.

Forms questions will expire after:

* 5 minutes, for reaction questions;
* 15 minutes, for open questions.

The format to set a form question is:

.. parsed-literal::

    (message/reaction)|(text of the question)|(list of reactions)/[validation words]|[alias]|[Trello mapping]
    
Each question has to be set using 5 fields, separated by one ``|`` character.

* First field: ``message`` will require the question to be answered with a plain text message. ``reaction`` will require the user to select one answer by clicking on a reaction that will be added to the question by the bot.
* Second field: The actual question.
* Third field:

  * If ``reaction`` is selected in the first field, this field will list all of the possible answers, using ``;`` to separate these answers. If this is the case, this field is **mandatory**.
  * If ``message`` is selected in the first field, this field will include a list of validation words: any answer given by the target user will be ignored unless the message contains at least one of the chosen words/sentences (case insensitive). Again, you can separate words/sentences with ``;``. If this is the case, this field is optional.

.. note:
    Due to Discord limitations, there can only be a maximum of 20 answers in a reaction question. Answers from the 21st onward will be ignored.

* Fourth field: The question "alias". This is the title that will replace the full question when the feedback is posted in the server channel. This field is optional, but it's higly suggested that you set an alias.
* Fifth field: This will map the question into one of the entities of the Trello board (only useful if you are interested in Trello integration, you can choose whether or not including Trello integration later):

  * ``title`` will use the answer as the title of a card. 
  * ``list`` will use the answer as the title of a list.
  * ``label`` will add the answer as a card label. 
  * ``attachment`` will add the answer as a card attachment.
  * ``description`` will add the answer as part of the description text, with the format: ``{Alias}: {Text}``.
  * ``private`` will show the answer into the "in-Discord" embed but won't upload the field to Trello whatsoever.

.. warning::
    A field being "optional" means that its content can be left blank, but the field itself has to exist; e.g. ``message|Heads or Tails?||The user picked...|``
    
.. hint::
    In order to ease the creation of these complex strings, you can use this `Forms Builder Helper <https://docs.google.com/spreadsheets/d/1rn6CY2PVD2Nn0cda1gfF_E3OysBcBN63ma-BG602NyI/edit?usp=sharing>`_ to create a pre-made string to be used in this phase. Just create a copy of that sheet and customize it to your needs.
    
When setting the authorization channel, "authorized users" will be those that are enabled to use the module using the :ref:`permissions`, not those that are mentioned in when a new feedback is posted.

....

|bot_prefix|\ formaddqst
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ foaq (form id)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Adds a question to an existing form. Follow the instructions given by the bot to configure the question. Refer to the previous paragraph for more details.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ foaq 1
    
....

|bot_prefix|\ formeditqst
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ foeq (form id) (question id)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Replaces the selected question from an existing form with a new one. Refer to the previous paragraphs for more details.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ foeq 1 5

....

|bot_prefix|\ formremqst
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ forq (form id) (question id)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Deletes a specific question from an existing form.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ forq 1 5

....

|bot_prefix|\ formsortqst
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ wfsq (form id) (question_ids)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Sorts the questions of an existing workflow into the specified order.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ wfsq 1 4 5 1 2 3

....

|bot_prefix|\ formpublish
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ fopub (form id)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Publishes an existing form, making it available to server members through the dedicated section of the bot Direct Messages behavior (see :ref:`submit`).

....

|bot_prefix|\ formwithhold
--------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ fowh (form id)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Witholds a previously published form, making it unavailable for server members. This is particularly useful, or even required, for forms that need to be edited/deleted.

....

|bot_prefix|\ formdelete
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ fod (form id)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Completely deletes a server form.

....

|bot_prefix|\ formedit
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ foe (form id) [--channel {channel id(s)/mention(s)/q_name(s)}] [--role {role id(s)/mention(s)/q_name(s)}] [--title {new title}] [--color {new color hex code}] [--trello/--discord]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Edits a form settings after its initial creation.

``--channel (authorization channel id/mention/q_name) [forwarding channel id(s)/mention(s)/q_name(s)]``
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Sets a new authorization channel (where authorized people will be able to validate or reject submissions) and, if more than one channel is specified, forwarding channels as well.

.. note::
    You have to re-set both the authorization channel and forwarding channels when you use this parameter. Skipping the forwarding channels in this command will disable the forwarding channels completely.

``--role [role id(s)/mention(s)/q_name(s)]``
""""""""""""""""""""""""""""""""""""""""""""

Sets new role mentions. Using this parameter with no role identifiers will disable mentioning of roles.

``--title (new title)``
"""""""""""""""""""""""

Sets a new title for the form.

.. warning::
    Changing the title of a form will require a change in the Trello board name, if Trello integration is active.

``--color (new color hex code)``
""""""""""""""""""""""""""""""""

Sets a new color for the form embeds.

``--trello`` or ``--discord``
"""""""""""""""""""""""""""""

Sets the type of output for the form. These parameters are mutually exclusive in nature, but ``--trello`` will take precedence over ``--discord`` if both are used.

....

|bot_prefix|\ formpreview
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ fop
    
Command Description
^^^^^^^^^^^^^^^^^^^
Prints the list of available forms for the current server. For each form, a preview of each question (and the corresponding question ID) is shown.

....

|bot_prefix|\ formblacklist
---------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ fobl (user id(s)/mention(s)/q_name(s))
    
Command Description
^^^^^^^^^^^^^^^^^^^
Toggles one (or more) user's presence on the forms blacklist. Blacklisted users won't be able to see any available form for the current server.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ fobl cycloptux#1543

....

|bot_prefix|\ formsexport
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ foexp
    
Command Description
^^^^^^^^^^^^^^^^^^^
Exports the current forms submission stats for the current server.

Permissions Needed
^^^^^^^^^^^^^^^^^^
| **User**: Bot Owner
