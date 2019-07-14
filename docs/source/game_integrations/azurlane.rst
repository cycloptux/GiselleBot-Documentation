*********************
Azur Lane Integration
*********************

This module contains a few commands used to get information about **Azur Lane**, a side-scrolling shoot 'em up mobile video game created by Chinese developers Shanghai Manjuu and Xiamen Yongshi, released in 2017 for the iOS and Android operating systems.

The game was released in 4 regions/versions:

* **CN** (Chinese)
* **JP** (Japanese)
* **KR** (Korean)
* **EN** (English/Global)

|bot_prefix|\ azurstatus
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ azurstatus [--region {region code}]
    
Command Description
^^^^^^^^^^^^^^^^^^^

Checks the status of Azur Lane's game servers. Omitting the region code will assume ``--region en`` and show the status of the (4, at the time of writing this page) English servers.

The Chinese region will print 2 embeds: one for the Android servers, one for the iOS servers. Other regions have common servers among the 2 platforms.
    
Examples
^^^^^^^^
.. parsed-literal::
    
    |bot_prefix|\ azurstatus
    |bot_prefix|\ azurstatus --region cn
    