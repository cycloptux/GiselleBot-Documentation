.. _guide-administration:

*********************************************
Step 1: Configuring the Administration Module
*********************************************

**Author**: NaviKing#3820

....

The Administration module is the first module you should use when managing a Discord server. It will let you configure all of the following options:

* Bot prefix
* Activity Logging
* Greeter
* Automatic role assignment/removal
* Self assignable roles

This guide will serve as a brief introduction for how, why, and when you should use these commands. It is not meant as a replacement to the documentation for each command. For more details, please consult the :ref:`administration` full documentation page.

.. warning::
    This guide assumes you have all the necessary permissions to run each command. The easiest way to make sure all commands work is to have the Administrator permission on one of your roles, and to make sure the bot has Administrator on one of its roles. For specifics on the permissions needed for each command, see :ref:`administration`.

Bot Prefix
----------

The bot prefix is the symbol you type before the bot command name in order to have the bot recognize that you're talking to it. By default, the bot's prefix is |bot_prefix_name| (|bot_prefix|\ ). However, you can use the :ref:`prefix` command to set a new prefix. For example, if you are already using a bot with |bot_prefix_name| as the command prefix, you could run the following command to change the bot's prefix to a question mark.

.. parsed-literal::

    |bot_prefix|\ prefix ?

After you set the bot prefix (if you need to) you can start setting up the rest of the modules. Unless otherwise specified, this introduction will assume you have a dedicated, private channel, such as #bot-console, for running bot commands. You don't need to have such a channel setup, but it's often useful to separate bot commands from other messages and it keep them private.

Server Activity Logging
-----------------------

Logging server activity is important to supplement Discord's server Audit Log and to capture activity that it does not, such as deleted messages and attachments. Discord's Audit Log also clears out old activity, while messages in a channel will remain forever. 

The logging module also includes the ability to selectively ignore specific users and channels meaning that you are still able to control the information that is logged on your server. This is important if your logs are visible to a group of people that not all channels are visible to.

Logging Example
^^^^^^^^^^^^^^^

Here is one way to set up the logging for your server.

1. Create the following channels

  a. #log-members
  b. #log-users
  c. #log-messages
  d. #log-mod
  e. #log-warn
  f. #log-roles (If you are a patron of the bot developer)
  g. #log-channels (If you are a patron of the bot developer)
  h. #log-voice (If you are a patron of the bot developer)
  i. #log-server (If you are a patron of the bot developer)

2. Run the following commands in each channel

  a. |bot_prefix|\ log members
  b. |bot_prefix|\ log users
  c. |bot_prefix|\ log messages
  d. |bot_prefix|\ log mod
  e. |bot_prefix|\ log warn
  f. |bot_prefix|\ log roles (if you are a patron)
  g. |bot_prefix|\ log channels (if you are a patron)
  h. |bot_prefix|\ log voice (if you are a patron)
  i. |bot_prefix|\ log server (if you are a patron)

3. If your Discord name is @NaviKing#3820 and you have an #admin-channel that isn't visible to Moderators, you could have the bot ignore you and all the messages in that channel using the following commands
  
  a. |bot_prefix|\ logignore channels #admin-channel
  b. |bot_prefix|\ logignore members @NaviKing#3820

.. note::
    While the moderation module will log some external moderation actions, it is primarily intended to be used with the warning log in conjunction with the bot's moderation module. This module will be discussed in another guide.
    

Greeter
-------

When new members join your Discord server, it is often nice to welcome them to the server and give them some guidance on what to do next. The bot includes two types of greeters: one that sends a direct message to a user when they join the server, and another that sends a message in a specific channel. Some administrators prefer to have slightly different messages in each, while others prefer to use only one. You can also configure the greeter to delete itself after a certain amount of time.

Greeter Example
^^^^^^^^^^^^^^^

You could set up a greeter as follows

1. Create a #greeter channel
2. Run |bot_prefix|\ greet in the #greeter channel
3. Run |bot_prefix|\ greetmsg Welcome to the server, %user%!
4. Run |bot_prefix|\ greetdel 60
5. If NaviKing#3820 joins your server, the bot will send the message "Welcome to the server, @NaviKing#3820!" in the #greeter channel, and then delete it after 60 seconds.

Similarly, if you used |bot_prefix|\ greetdm and |bot_prefix|\ greetdmmsg instead of |bot_prefix|\ greet and |bot_prefix|\ greetmsg, it would send a message to that user as a direct message (the direct message would not be autodeleted though). If you use |bot_prefix|\ greetdm, it doesn't matter what channel you run the command in. Remember that some users have direct messages disabled by default though, so it might not always work.

Remember, if you enable one or both greeters with |bot_prefix|\ greetdm or |bot_prefix|\ greet but don't set a message, nothing will happen when users join the server!

Automated Role Assignment/Removal
---------------------------------

Oftentimes, it's useful to grant a role to a user as soon as they join the server. Sometimes this is used to bar new users from viewing certain channels, to give all users a different color from the default Discord color, or just to recognize the users as new! This is a common feature in Discord bots, but this bot also features the ability to automatically remove one or more roles after a certain amount of time.

The bot also allows you to specify a role that users receive when they join a voice channel. This is often used to allow users access to a corresponding text channel.

.. note::
    All roles used in commands should exist prior to running the command. The bot will not create roles that don't already exist.

Role Assignment/Removal Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. If you want to give a Newcomer role to members that join the server, you can run the following command
  
  * |bot_prefix|\ aar Newcomer

2. You could then have the bot remove this role after 3 days

  * |bot_prefix|\ arr 3d Newcomer

3. Join the General voice channel and run the following command

  * |bot_prefix|\ vcrole "General Voice"

    * This will give the General Voice role to users that join the General voice channel. Note the quotation marks around the role name. These are necessary if the role name is two or more words.

You can undo these commands in the following fashion

1. |bot_prefix|\ aar Newcomer
  
  * will stop the role from being autoassigned if it is currently being autoassigned

2. |bot_prefix|\ arr Newcomer
  
  * exclude the time code, the bot will stop removing the role
  
3. Join the voice channel that has an associated role and just type |bot_prefix|\ vcrole

  * Provide no role names, the bot will stop assigning a role

.. note::
    The time code format uses mo/w/d/h/m for months/weeks/days/hours/minutes. Any command that uses a timecode in any module follows this format. For example, if you use 1d3h2m as the time code, that lets the bot know that it should be 1 day, 3 hours, and 2 minutes. More info in :ref:`timecode`.

Self Assignable Roles
---------------------

One of the most complex modules of the bot, this allows you to configure roles that users can assign to themselves via the bot. It is strongly recommended to read the full documentation on self assignable roles. This section will cover only the basics.

Self assignable roles are used for many reasons.

* Users may want to opt in or opt out of specific channels. By allowing specific roles access (or excluding them) via channel permissions, users have control over which channels they can or can't see.
* Users may want to change their Discord name color. By creating roles with a variety of colors, users can self assign a color of their choice
* Users may want to volunteer for certain duties. For example, creating a taggable @Helper role and making it self assignable allows people to volunteer to be tagged if they need help.
* Users may want to opt in for notifications. For example, instead of using @everyone for server updates, you can create a taggable @Server Updates role. Users can then opt in to this role and be tagged if there are updates about the Discord server

Setting up Self Assignable Roles - Basics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this bot, you can assign any number of roles to a group of self assignable roles like so

.. parsed-literal::

    |bot_prefix|\ asar 1 Role1 "Role 2" "Role 3" Role4

Will add the following roles to group 1

* Role1
* Role 2
* Role 3
* Role4

You can remove roles from a group with |bot_prefix|\ rsar in the same fashion (e.g., |bot_prefix|\ rsar 1 Role1 will remove Role1 from group 1). You can list all the self assignable roles on the server with |bot_prefix|\ lsar. It will display them by group.

You can use the |bot_prefix|\ sargs command and a role ID to configure advanced options for self assignable roles. For example

.. parsed-literal::

    |bot_prefix|\ sargs 1

will let you configure additional options for group 1. These are explained in the resulting command menu and also on the dedicated documentation page (see :ref:`self-assignable-roles`), and will not be covered here.

Using Self Assignable Roles
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Users can then assign themselves these roles using a role menu (explained later) or via |bot_prefix|\ iam and remove these roles via |bot_prefix|\ iamnot. For example

.. parsed-literal::

    |bot_prefix|\ iam Role1

will add Role1 to the user that runs the command and

.. parsed-literal::

    |bot_prefix|\ iamnot Role1

will remove the role

Role Menus
^^^^^^^^^^

Some users find it difficult to use |bot_prefix|\ iam and |bot_prefix|\ iamnot because it requires the command and role name to be typed exactly correct. Many users find it simpler to use role menus, which allow users to assign and remove roles from a single group by reacting to a message. Continuing the previous example, you can use the following command to create a role menu for group 1

.. parsed-literal::

    |bot_prefix|\ rmcreate 1

The bot will create a message to use as the role menu and prompt you to provide a reaction for each role. The bot will build the role menu as you react and let users know which reactions correspond to which roles. You can also create your own role menu by using ``--m`` and providing a valid message ID. To get a message ID, make sure developer mode is enabled (User Settings -> Appearance -> Developer Mode) and then right click on a message and choose Copy ID. For example

.. parsed-literal::

    |bot_prefix|\ rmcreate 1 --m 591116046606270464

will create a role menu using the message with the ID 591116046606270464 in the current channel.

You may also find that you want to add additional roles to a role group. In that case, you can run the following command to have the bot add reactions for the new roles in the most recent role group in the channel, or use ``--m`` and a valid message ID to update the role menu on that channel

.. parsed-literal::

    |bot_prefix|\ rmupdate

Similarly, if you want to remove a role menu, you can use the following command to remove the most recent role menu in the channel, or use ``--m`` and a valid message ID to remove the role menu from that message. It will not delete the reactions, just prevent them from being used as a role menu.

.. parsed-literal::

    |bot_prefix|\ rmremove

It is often useful to have a separate channel for self assignable roles and have multiple role menus in that channel, so using the ``--m`` parameter to specify a particular message is extremely useful. Be sure that when you are configuring the role menus that you are using emoji from Discord or from your own server, as the bot cannot use emotes it does not have access to.

Summary
-------

The administrative module greatly enhances the functionality of your server. From the basics of setting a custom command prefix, you can enable logging of various items on your server, greet people as they join, automatically give and remove roles from them, and even allow people to pick their own roles! These functions are the foundation of a flexible server structure and allow for greater customization, tracking, and organization.
