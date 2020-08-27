.. _verification:

************
Verification
************

The verification module acts as a gate in order to assign (or remove) certain roles to users after making sure they are humans.

Human verification is achieved through text/audio captchas that are randomly generated and sent to the user via DM.

|bot_prefix|\ verify
--------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ verify
    
Command Description
^^^^^^^^^^^^^^^^^^^
Requests a new captcha verification, provided that "verification via command" is enabled through :ref:`verifysetup`.

Users will receive a new randomly generated captcha via text image, and the same captcha as audio file (for visually-impaired users).

Users will have **5 minutes** to complete the captcha request. If the timer expires, or if **3 wrong codes** are submitted, the captcha verification will fail.

Users leaving and re-joining the server **will not** receive a new captcha until the previous one has expired.

Users will be able to submit a code through the |bot_prefix|\ code pseudo-command as a response to the direct message sent by |bot_name|\ .

.. note::
    This command is always available to everyone.

....

.. _verifysetup:

|bot_prefix|\ verifysetup
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ verifyset
    
Command Description
^^^^^^^^^^^^^^^^^^^
Opens an interactive menu to configure the verification module.

Here's an explanation of the available parameters:

* "Toggle captcha verification **on join**" will send a captcha verification message to all users joining the server.
* "Toggle captcha verification **via command**" will send a captcha verification message upon using the |bot_prefix|\ verify command.

These options can be enabled at the same time or only one of them, depending on your desired setup. These options **will not turn on** unless both "Set **main** verification channel" and "Set post-verification role(s)" are correctly set.

* "Set **main** verification channel" will configure the channel as the only channel where the |bot_prefix|\ verify command will work. Users will also be mentioned in here if they can't be reached through DM.
* "Set **fallback** verification channel" will configure the channel as a secondary channel where error message will be sent for verifications triggered by a join event. The |bot_prefix|\ verify command **will not** work in the fallback channel. Verification attempts via command will still send the feedback to the main channel.

* "Set post-verification role(s)" will set one or more role to be assigned (or removed, depending on the following setting) to users when they successfully verify. At least one role is mandatory for the verification feature to be enabled.
* "Toggle post-verification role mode" will configure whether the post-verification role(s) will be assigned or removed upon successfully verifying.

Do note that, if post-verification role mode is set to **Remove**, the user must have the selected role(s) assigned **before the verification starts**. If you are using verification **on join**, you might want to configure the automatic role assignment on join through the :ref:`autoassignrole` feature (verification will natively wait for that role to be assigned before starting the verification on the user).

Using a different bot for the automatic assignment of the role on join might cause the role to be missing when the verification is due to start, hence causing the verification to fail.

* "Set verification log channel(s)" will configure one or more channels as "logging channel", hence receiving a notification upon successful and failed verifications.
* "Set daily stats channel(s)" will configure one or more channels as "stats channel", where the daily :ref:`verifystats` output will be automatically sent each day at midnight, UTC.

* "Automatically kick upon failed verification" will configure whether a user failing the verification (due to their timer expiring or too many errors) will be kicked. If this option is disabled, users will be left untouched in the server and will be able to request a new verification by using the |bot_prefix|\ verify command (if enabled) or by leaving and re-joining the server.

* "Bypass if the user verified at least once **in this server**" will skip verification for those users that successfully verified at least once in the current server.
* "Bypass if the user verified at least once **in any server**" will skip verification for those users that successfully verified at least once in any server.

* "Set a custom message for verifying users" will allow server managers to set an additional short (**500 characters maximum**) message that will be delivered to each user that attempts verifying in that server. This message will be appended to the default instructions message that is sent via DM.

.. admonition:: Premium

    The custom message feature is only available to **Premium**-enabled servers (see: :ref:`premium-perks`).


....

.. _verifystats:

|bot_prefix|\ verifystats
-------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ verifystats
    
Command Description
^^^^^^^^^^^^^^^^^^^
Prints some statistics about the verification module for the current day (referring to UTC midnight). You cannot request stats for previous days.

Here's an explanation of the available stats:

* "Users Sent Captchas" is the total number of sent captchas. It should normally be the sum of the following params, except for some edge cases.
* "Users Passed" is the number of successfully passed captchas.
* "Users Failed (Timer Expired)" and "Users Failed (Too Many Errors)" refer to captchas that were failed **while the user was still in the server**. Depending on the configuration of the module, this number also indicates the number of kicked users, if auto-kick is enabled.
* "Users Leaving While Verifying" refers to users that left the server on their own (while verifying) **before** their verification timeout was over.
* "Users Kicked While Verifying" refers to users that were kicked for reasons unrelated to the verification process (while verifying) **before** their verification timeout was over.
* "Users Kicked By Discord" refers to users that may have been kicked by Discord's automatic system for being flagged as suspicious accounts.
* "Errored Captchas" refers to verifications that resulted in errors due to misconfigurations or other undefined problems (e.g. Discord API errors).
* "Average Time To Verify" only takes into account **Passed** verifications.
* "Average Errors" only takes into account **Passed**, **In Progress**, and **Failed** verifications.

**Users Leaving Before Verifying**, **Users Kicked Before Verifying** and **Users Kicked By Discord** are only populated if **Members Logging** is active in the server (refer to :ref:`log-command`).

In order to properly recognize whether a user left on their own or was kicked, "View Audit Log" permissions must be given to |bot_name|\ .

If **Members Logging** is disabled, the above values will all be added to the **Errored Captchas** statistics.

....

|bot_prefix|\ verifyuser
------------------------

Command Syntax
^^^^^^^^^^^^^^
.. parsed-literal::

    |bot_prefix|\ verifyuser (user id(s)/mention(s)/q_name(s))
    
Command Description
^^^^^^^^^^^^^^^^^^^
Manually verifies one or more users. The corresponding log entry will track the user that run the command.

The user(s) will be notified of the manual verification. The author of the command will not be disclosed in the notification DM.

.. note::

    Manually verified users will not appear in the verification module stats. Also, manually verifying a user will not count as a valid verification in regards to the verification bypass logic.
