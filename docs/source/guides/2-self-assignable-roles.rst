.. _guide-self-assignable-roles:

********************************************
#2: Reaction Roles and Self Assignable Roles
********************************************

**Author**: NaviKing#3820

.. seealso::
    Different use cases of the same topic are described in :ref:`guide-administration`

....

One popular bot feature is the ability to have self-assignable roles and reaction (button) roles. Self assignable roles are roles that user's are able to freely add to and remove from themselves via a bot, while reaction (button) roles refer to a method of assigning these roles by clicking on a button on a specific message.

|bot_name| has both of these features, and this article will give you a brief overview of how you can set up your very own self-assignable roles and reaction roles. If you want to learn more about how self-assignable roles work, you can take a look at the documentation here: :ref:`self-assignable-roles`

Step 1: Create a Role Group
---------------------------

The very first thing you need to do to create a self-assignable role is to add an existing role to a Role Group. A Role Group is simply any set of roles grouped together via |bot_name|\ 's |bot_prefix|\ asar command. For example:

.. parsed-literal::

    |bot_prefix|\ asar 1 "Role 1" @Role 2

will add both Role 1 and Role 2 to group 1 of your self assignable roles. You can confirm this by using the |bot_prefix|\ lsar command to see the list of current self-assignable roles. Don't worry, you can add more roles later and even remove roles using the |bot_prefix|\ rsar command.

Users can immediately assign and remove roles to themselves using the |bot_prefix|\ iam and |bot_prefix|\ iamnot commands once they have been assigned to a Role Group, but you can also configure your Role Group settings further and even set up a reaction role menu for ease of use.

Step 2: Configure your Role Group
---------------------------------

The next step is to make sure you configure your Role Group settings properly. Although this step is optional, it's worth becoming familiar with the default settings and being aware of the potential options.

You can configure a self-assignable Role Group by using the |bot_prefix|\ sargs command with the ID of the group you want to configure (e.g., |bot_prefix|\ sargs 1). A detailed explanation of each option can be found on the documentation page (see :ref:`self-assignable-roles`), but a few use cases are described below.

* Let server boosters choose a color for themselves by creating a Role Group of different colored roles. Set up the Nitro Booster role as a required role and enable the prerequisites check feature.
* Have people choose their favorite faction in a game by creating a Role Group with a role for each faction. Set the mode to Single and enable removing the existing role when assigning another role in the group. Alternatively, set the mode to Multiple and have people choose up to 2 or 3 of their favorite factions!
* Have people assign a role to themselves to acknowledge they have read your server rules. Add your verification role to its own Role Group, enable single mode, and then enable requiring one role in the group at all times after the initial assignment. This way people will be able to assign the role to themselves, but not remove it. **Note:** Don't forget you need to set up your server role and channel permissions for a verification role to have any effect, which has nothing to do with |bot_name|\ ! You can read more about this `here <https://discord.com/moderation/1500000177981-301:-Implementing-Verification-Gates>`_.

Step 3: Create a reaction role menu
-----------------------------------

The last step is to set up your reaction role menu using |bot_prefix|\ rmcreate. This is as easy as just using the command with the group ID of the self-assignable role group you want to turn into a menu.

.. parsed-literal::

    |bot_prefix|\ rmcreate 1

|bot_name| will then send an embed instructing people to press a button to assign a role. Each button will be named after the role it's for. If you want the buttons to be named something else, you can simply rename your roles to what you want the buttons to say, create the role menu, and then change the name of the roles back to normal. This is great for making a self-assignable verification role menu to have the button say "I agree to the server rules" while keeping the role itself named "Member" long term.

If you want to edit the default message, you can use the |bot_prefix|\ msgedit command to do so. If you want to make an embed, I suggest using a website like https://embedbuilder.nadekobot.me/ to generate the embed text. More information about the |bot_prefix|\ msgedit command is available on its documentation page.

If you modify the roles that are in your role group, you can update your reaction role menu using the |bot_prefix|\ rmupdate command. Do note that if you used the trick mentioned earlier to manipulate the names of the buttons such that they are different from the roles, you will need to temporarily update your role names again to match what the buttons say or running this command will also rename your existing buttons to your current role names.

Summary
-------

After you create a self-assignable role group, you can then customize it and turn it into a reaction role menu. Although customizing the default behavior of a role group is optional, remember that you can't create a reaction role menu without a self-assignable role group.

Remember, this guide doesn't cover all of the self-assignable role commands. Be sure to check out the full documentation (:ref:`self-assignable-roles`) if you get stuck, and feel free to ask additional questions on the |bot_name|\ 's Support Server (|bot_support|\ ) if you're still having problems after looking at the documentation!