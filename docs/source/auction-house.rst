*************
Auction House
*************

The Auction House module lets server members bid for items within a certain span of time.

|bot_prefix|\ ahnew
-------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ ahnew [--item {item name}] [--starting {starting bid price (number)}] [--currency {currency name (singular,plural)}] [--duration {duration timecode}] [--roles {role id(s)/mention(s)/q_name(s)}] [--forward {user id(s)/mention(s)/q_name(s)}]

Command Description
^^^^^^^^^^^^^^^^^^^
Starts a new auction in the current channel. The currency parameter will define which currency names will be used in the message, separate singular and plural with a simple comma ``,``. Please note that no currency is actually used. The roles parameter will restrict the ability to vote to users that have (at least one of) the defined role(s). The forward parameter will define more users that will receive the auction closure notification via DM (the author of the auction will always be notified). The final notification will also include a .csv containing the full bid history, for auditing purposes.

All parameters are optional, the default values (on omission) are:

* **Item Name**: "Sample Item"
* **Starting Bid Price**: 0
* **Currency**: *None*
* **Duration**: 1 day (24 hours)
* **Roles**: *None* (everyone)
* **Forward**: *None* (author only)

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ ahnew --item Steam Key --starting 100 --currency buck,bucks --duration 5d --roles "Auction Enabled" @Gamers --forward cycloptux#1543

....

|bot_prefix|\ ahstop
--------------------

Command Description
^^^^^^^^^^^^^^^^^^^
Stops the auction (in the current channel) that was started by the command author, as if the timer had expired (e.g. the author will be notified with the winner, etc.).

....

|bot_prefix|\ bid
-----------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ bid (amount)

Command Description
^^^^^^^^^^^^^^^^^^^
Lets a user bid a certain amount for the current auction. Validation rules are in place to make sure that the bid is valid before it's registered. Invalid bids will still be registered in the detailed .csv that is sent to the author, but those will not interfere with the actual auction.

Please note that this command will always be available to everyone, ignoring the permissions set for the module.

Examples
^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ bid 110
