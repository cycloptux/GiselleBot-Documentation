*************************
Modules Documentation 101
*************************

Throughout the whole documentation website, you'll find different ways of explaining commands and a few keywords to indicate particular ways of writing a parameter.

Server/Guild, Channel, Message, Role, User IDs
==============================================

Each entity in Discord is mapped with a unique ID. Knowing what an ID is, and how to get the ID of a said entity is crucial to knowing how a bot works. Obtaining an ID also requires that you have Discord's Developer Mode active.

There are a lot of guides and tutorials about how to activate Developer Mode and how to get an ID for an entity in Discord. `This link <https://support.discordapp.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID->`_ will bring you to the official Discord support page about this topic.

Obtaining a role ID may be trivial: you can obtain the role ID by prepending a role mention with ``\``, but that message will still mention the role.

In order to make your life easier, the bot offers a |bot_prefix|\ roleid command. More details **here** (link currently not working).

Parenthesis
===========

Parenthesis are used into command syntax snippets. The type of parenthesis indicates whether that parameter or string is mandatory, optional or just a simple description (hence, not an actual part of the command).

+----------+-------------+
| Type     | Meaning     |
+==========+=============+
| ``()``   | Mandatory   |
+----------+-------------+
| ``[]``   | Optional    |
+----------+-------------+
| ``{}``   | Description |
+----------+-------------+

Names and Double Quotes
=======================

Within the documentation, you may find the tag ``q_name`` in command syntax snippets. That's a short name for "name surrounded by double quotes", and is generally used for Discord user, channel or role **plain** names:

.. parsed-literal::

    "cycloptux Development#1543"
    "Role With Spaces"
    
.. _timecode:

Time Format Code
================

Time durations are indicated through the use of a standard time format, which consists of 5 (or 6) time bits:

+----------+-----------+
| Time Bit | Meaning   |
+==========+===========+
| ``mo``   | month(s)  |
+----------+-----------+
| ``w``    | week(s)   |
+----------+-----------+
| ``d``    | day(s)    |
+----------+-----------+
| ``h``    | hour(s)   |
+----------+-----------+
| ``m``    | minute(s) |
+----------+-----------+

If specified, the time code may allow an extra bit, ``s`` for second(s). Each time bit has to be prepended with an actual (positive, integer) number, or omitted if the corresponding time bit would be set to 0.

.. warning:
    **Important Note**: While some flexibility is allowed in time codes, be sure to write the time bits in the correct order: ``mo > w > d > h > m > s``

That said, a typical time code would be like this:

.. parsed-literal::

    2mo6h40m = 2 months, 6 hours, 40 minutes
    
