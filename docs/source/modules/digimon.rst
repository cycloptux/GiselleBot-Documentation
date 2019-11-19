.. _digimon:

*******
Digimon
*******

Lorem ipsum sit dolor amet

(Explanation of the game)

(Explanation of the menus)

This documentation page is still highly work-in-progress. The module is being tested.

|bot_prefix|\ dgparam
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ dgparam
    
Command Description
^^^^^^^^^^^^^^^^^^^
Shows basic parameters about the user and the game itself.

....

|bot_prefix|\ dggacha
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ dggacha
    
Command Description
^^^^^^^^^^^^^^^^^^^
Obtaines a new random Digimon out of the starters pool.

(Add info about rates and trophy units)

....

|bot_prefix|\ dgarchive
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ dgarchive
    
Command Description
^^^^^^^^^^^^^^^^^^^
Shows a summary of all Digimons ever owned by the user.

....

|bot_prefix|\ dginventory
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ dginventory
    
Command Description
^^^^^^^^^^^^^^^^^^^
Shows the current user inventory.

(Add aliases)

....


|bot_prefix|\ dgshop
--------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ dgshop
    
Command Description
^^^^^^^^^^^^^^^^^^^
Opens the items shop. 

....


|bot_prefix|\ dgdex
-------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ dgdex [Digimon -partial- name or number]
    
Command Description
^^^^^^^^^^^^^^^^^^^
Shows all Digimons currently owned by the user. If a name or number is specified, the output will restrict the list to the corresponding Digimons, if any.

Partial names are supported (e.g. "pabu" instead of "Pabumon").

....


|bot_prefix|\ dglookup
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ dglookup (Digimon -partial- name or number)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Shows generic info about a specific Digimon.

Partial names are supported (e.g. "pabu" instead of "Pabumon").

....

|bot_prefix|\ dgechain
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ dgechain (starting Digimon -partial- name or number) (ending Digimon -partial- name or number)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Given two **mandatory** Digimon identifiers (names or numbers), this command shows the Digivolution/Degeneration chain that is needed to go from the first Digimon to the second one, if any.

Partial names are supported (e.g. "pabu" instead of "Pabumon").

....

|bot_prefix|\ dgtrain
---------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ dgtrain (Digimon -partial- name or number)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Sends a Digimon to the Digi-Farm for training. The amount of EXP earned depends on the amount of time that the Digimon will spend in the farm.

During that time, the Digimon will be unavailable for other uses.

(Add aliases & details)

....

|bot_prefix|\ dgretrieve
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ dgretrieve (Digimon -partial- name or number)
    
Command Description
^^^^^^^^^^^^^^^^^^^
Returns a Digimon to the user's Digi-Dex once the Digimon has finished training in the Digi-Farm. The Digimon will wait in an "idle" state within the farm until it's manually retrieved.

(Add aliases & details)

....

|bot_prefix|\ dgdrop
--------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ dgdrop (Digimon -partial- name or number)
    
Command Description
^^^^^^^^^^^^^^^^^^^
(Add aliases & details)

....

|bot_prefix|\ dgevolve
----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ dgevolve (Digimon -partial- name or number)
    
Command Description
^^^^^^^^^^^^^^^^^^^
(Add aliases & details)

....

|bot_prefix|\ dgdegenerate
--------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ dgdegenerate (Digimon -partial- name or number)
    
Command Description
^^^^^^^^^^^^^^^^^^^
(Add aliases & details)

....

|bot_prefix|\ dguseitem
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ dguseitem
    
Command Description
^^^^^^^^^^^^^^^^^^^
(Add aliases & details)

....

|bot_prefix|\ dgdropitem
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ dgdropitem
    
Command Description
^^^^^^^^^^^^^^^^^^^
(Add aliases & details)

....

|bot_prefix|\ dgenhance
-----------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ dgenhance (Digimon -partial- name or number)
    
Command Description
^^^^^^^^^^^^^^^^^^^
(Add aliases & details)
