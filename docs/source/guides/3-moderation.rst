.. _guide-moderation:

*****************************
#3: |bot_name| and Moderation
*****************************

**Author**: NaviKing#3820

....

|bot_name| features a robust moderation system that allows you to track misbehavior and notes for your server's users with an incredible amount of detail and nuance using a points-based moderation system. This guide will serve as a brief introduction on how to set up and use the moderation moderation module. However, it is not meant as a replacement to the documentation for each command, and not all commands are covered in this guide. For more details, please consult the :ref:`moderation-module` full documentation page or use |bot_name|\ 's |bot_prefix|\ help command to learn more about each individual command.

Enabling the moderation module
------------------------------

To ensure that the moderation module works properly, you should use |bot_name|\ 's |bot_prefix|\ log command to enable both the moderation and warning logs somewhere on your server. To do this, you can run each command below

.. parsed-literal::

    |bot_prefix|\ log warning
    |bot_prefix|\ log moderation

After this, you will need to define the roles that should be allowed to use the moderation module. You can add and remove roles using the |bot_prefix|\ modrole command like so

.. parsed-literal::

    |bot_prefix|\ modrole add Moderators

Where "Moderators" is any number of roles that designate your mod team.

Rules and Points
----------------

You may also want to add the rules of your server to |bot_name| and configure how many points they are worth. Rules are assigned point values to denote how severe a violation is by default, and can be adjusted by a moderator on a per-violation basis (more on that later). For example, a user that is breaking a nickname rule is likely committing a less severe violation than a user posting NSFW content on the server. The points system allows you to quantify this difference and appropriately discipline users based on both the frequency and severity of their actions.

You can see the default set of rules that |bot_name| has by using the |bot_prefix|\ listrules command and disable any rules you don't want to use with the |bot_prefix|\ toggleglobalrule command. You also have the ability to add your own rules including the rule name, description, alias, and point value via the |bot_prefix|\ addrule command. Global rules will always be represented by a number, while custom rules will be represented with ``s_`` before the rule number (e.g., ``s_1``).

The system was designed such that rules are expected to be an even number between 2 and 10 points, with 6 points representing an "average" warning. However, you are welcome to use any number you want, or even set the point value of a rule to 0.

Also by default, |bot_name| will half the points associated with the first infraction of each rule that a user commits. This results in users being able to commit two different violations of three different rules before being banned. However, additional types of logic also exist when it comes to halving the points of warnings. These can be configured using the |bot_prefix|\ halflogic command. For example

.. parsed-literal::
    
    |bot_prefix|\ halflogic none

Will prevent |bot_name| from halving the points for any warnings a user received. This can be useful if you want your server to be more strict.

|bot_name|\ 's moderation system will automatically suggest that a user be muted when they have acquired 18 points and banned when they hit 27 points. Warnings expire to 1 point after 90 days, and these two thresholds apply only to unexpired points. However, users that acquire 54 points total, regardless of expiration, will also cause |bot_name| to suggest banning the user, which is referred to as an absolute ban. None of these thresholds are automatically enforced by |bot_name| though, so you are welcome to ignore them if you want.

Types of Punishments
--------------------

|bot_name| features a variety of moderation actions that you can take against a user. By default, all of these actions will log a case associated with that user and send them a direct message to inform them of the violation. This message includes the name of the moderator that sent the warning by default, but this can be anonymized using the |bot_prefix|\ modanonymization command.

|bot_name| also supports a variety of punishment types include warning, muting, banning, kicking, channel banning (preventing a user from accessing a channel), channel muting (preventing a user from speaking in a channel), image banning (preventing a user from uploading images or embedding links), and channel image banning (preventing a user from uploading images or links in a specific channel).

All moderation commands expect the following parameters

* A user mention, name, or ID
* ``--rule``: the name, ID, or alias of the rule broken
* ``--reason``: a text explanation of how the rule was broken
* ``--attachments``: one or more links (or text) related to proof of a user's infraction. You can skip this parameter if you upload one or more images when sending the command.

You can also use the ``--padj`` parameter to adjust the point value of a warning and the ``--just`` parameter to include a justification of the point adjustment. Additionally, you may use the ``--skip-dm`` parameter to prevent |bot_name| from sending a direct message to the user when they are warned, or the ``--skip-case`` parameter to avoid logging the warning entirely and only execute the moderation action.

After running a moderation command, |bot_name| will inform whoever runs the command if they are missing any necessary parameters when the command is used and will alert the user how to fix the case with the |bot_prefix|\ edit command. You can also turn off these alerts using the |bot_prefix|\ modnotification command. A few example moderation commands are provided below. However, it is encouraged to read the full documentation on the moderation commands as well

.. parsed-literal::

    |bot_prefix|\ warn @user --rule 1 --reason being a jerk --attachments imgur.com/a/youralbum
    |bot_prefix|\ mute 1d 356831787445387285 --rule NSFW --reason Posting NSFW content in the #general channel --attachments imgur.com/a/yourscreenshot
    |bot_prefix|\ ban 356831787445387285  --rule Spam --reason Posting a phishing link in chat --padj 27 --just As phishing links are dangerous to the community, this merits an instant ban

Reviewing, Modifying, and Deleting Cases
----------------------------------------

After logging an action against a user, it may be necessary to review their warning history, edit, or remove warnings against them.

The |bot_prefix|\ warnhistory command can be used to look up a user's warning history with their ID, name, or mention. If you wish to review any cases in detail, using |bot_prefix|\ case combined with the case ID will show you that case. Similarly, cases can also be deleted using the |bot_prefix|\ delete command and the case ID. **Moderators are allowed to delete automoderator cases created by the bot (e.g. in case of auto-moderation actions), but cannot delete cases created by other mods, including themselves.** Only users with Administrator or Manage Server permissions are allowed to delete cases by other moderators.

The |bot_prefix|\ edit command lets you edit an existing case by overwriting existing values with new values. You do not have to edit every parameter for a warning at once. For example, if you only need to edit the reason of a case, you can use

.. parsed-literal::

    |bot_prefix|\ edit 1 --reason New reason

To update the reason. You can include as many or as few parameters as you want according to your needs.

Bonus: Using Zero Point Rules
-----------------------------

Although this covers the basics of using |bot_name|\ 's warning system, there is one more thing to discuss which is the application of "0 point rules". Rules that are worth zero points, by definition, do not advance someone any closer to a ban in |bot_name|\ 's warning system. This gives you a couple of options.

One option is to make a dummy rule worth 0 points to be used to make silent notes on someone's account. For example, something like

.. parsed-literal::
    
    |bot_prefix|\ addrule --name None --description This is an informational message and does not count towards being banned from the server --alias None --points 0

Can be used in a "warning" like this

.. parsed-literal::
    
    |bot_prefix|\ warn @user --rule None --reason This user was acting weird in someone's DMs. Give them an official warning if you hear about it happening again --attachments proof here --skip-dm

Using ``--skip-dm`` in that warning means it will get logged to the user's warning history without them being aware that it's been logged, but moderators can still double check that person's warning history in the future and know the appropriate action to take if something like that happens again.

Furthermore, if you wish to use your own moderation system related to number of warnings instead of points, you may want to make all of your warnings worth zero points so that you don't have to worry about the points system confusing any of your moderators. In this way, you can still use |bot_name| as a normal moderation bot.

Summary
-------

The moderation module includes a lot of moving parts. You need to ensure that it is set up properly so that it starts working, verify that the rules your moderators have access to are appropriate for your server, and then you can start using it to apply a variety of punishments to members of your server that break the rules. Beyond that, you even have extra flexibility to leave notes on someone's account or even avoid the points system entirely.

Hopefully after reading this article you better understand how to use |bot_name|\ 's moderation system to help your server, but as always you can find more information in the module's documentation (see :ref:`moderation-module`). If you're still having trouble, feel free to join |bot_name|\ 's Support Server (|bot_support|\ ) and ask your questions there!
