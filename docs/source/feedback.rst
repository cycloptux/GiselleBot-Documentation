******************
Feedback Workflows
******************

The Feedback Workflows module enables users to set up Q/A workflows that are presented to those that send a Direct Message to the bot. The Q/As can be set up to be a sequence of multi-choice or open questions, with the final output being sent into a server channel by the bot itself.


|bot_prefix|\ workflowpreview
-----------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ wfp
    
Command Description
^^^^^^^^^^^^^^^^^^^
Prints the list of available workflows for the current server. For each workflow, a preview of each question (and the corresponding question ID) is shown.

....

|bot_prefix|\ workflowinit
--------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ wfinit

Command Description
^^^^^^^^^^^^^^^^^^^
Initializes a new workflow setup. The bot will guide the user into setting up the basic configurations and first question.
Workflow questions will expire after:

* 2 minutes, for reaction questions;
* 15 minutes, for open questions.

The format to set a workflow question is:

.. parsed-literal::

    (message/reaction)|(text of the question)|(list of reactions)/[validation words]|[alias]
    
Each question has to be set using 4 fields, separated by one ``|`` character.

* First field: ``message`` will require the question to be answered with a plain text message. ``reaction`` will require the user to select one answer by clicking on a reaction that will be added to the question by the bot.
* Second field: The actual question.
* Third field:

  * If ``reaction`` is selected in the first field, this field will list all of the possible answers, using ``;`` to separate these answers. If this is the case, this field is **mandatory**. Please note that, due to Discord limitations, there can only be a maximum of 20 answers. Answers from the 21st onward will be ignored.
  * If ``message`` is selected in the first field, this field will include a list of validation words: any anwer given by the target user will be ignored unless the message contains at least one of the chosen words/sentences (case insensitive). Again, you can separate words/sentences with ``;``. If this is the case, this field is optional.

* Fourth field: The question "alias". This is the title that will replace the full question when the feedback is posted in the server channel. This field is optional.

Please note that a field being "optional" means that its content can be left blank, but the field itself has to exist; e.g. ``message|Heads or Tails?||The user picked...``

....

|bot_prefix|\ workflowaddqst
----------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ wfaq (workflow_id)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Adds a question to an existing workflow. Follow the instructions given by the bot to configure the question. Refer to the previous paragraph for more details.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ wfaq 1

....

|bot_prefix|\ workflowremqst
----------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ wfrq (workflow_id) (question_id)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Deletes a specific question from an existing workflow.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ wfrq 1 5

....

|bot_prefix|\ workflowsortqst
-----------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ wfsq (workflow_id) (question_ids)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Sorts the questions of an existing workflow into the specified order.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ wfsq 1 4 5 1 2 3

....

|bot_prefix|\ workflowpublish
-----------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ wfpub (workflow_id)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Publishes an existing workflow, making it available through the dedicated section of the bot Direct Messages behavior.

....

|bot_prefix|\ workflowwithhold
------------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ wfwh (workflow_id)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Witholds a previously published workflow, making it unavailable for the target users. This is particularly useful for workflows that need to be edited.

....

|bot_prefix|\ workflowblacklist
-------------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ wfbl (user id(s)/mention(s)/q_name(s))
    
Command Description
^^^^^^^^^^^^^^^^^^^
Toggles one (or more) user's presence on the workflows blacklist. Blacklisted users won't be able to see any available workflow for the current server.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ wfbl cycloptux#1543
