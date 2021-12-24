Trivia
======

This module lets users play trivia quiz games on Discord. The module
gets its default questions from the **Open Trivia Database**, which
offers more than 3,000 validated questions in more than 15 categories.

The trivia module is meant to be public and used by anyone for fun.
Users with \"Manage Messages\" & \"Manage Roles\" permissions, hereafter
called \"Elevated Users\", will also have access to extra settings that
will make them able to set trivia quiz games up for use by other users
(typical use cases include events, giveaways, etc.).

Trivia games can be **timed** or **immediate**.

-   **Immediate** trivia games move to the next question as soon as one
    answer is collected.
-   **Timed** trivia games move to the next question as soon as a
    certain time interval passes, and collect answers from anyone during
    that period (limitations may apply, see later).

Depending on the \"type\" of user running the command(s), some
limitations apply to the usage of the trivia module. The following table
shows such limitations.

  ------------------------------------------------------------------------
  User Type                 MQ   MT          RR      TC        AD    SE
  ------------------------- ---- ----------- ------- --------- ----- -----
  Normal (non-\"Elevated\") 10   3 minutes   No      No        No    No

  Elevated                  20   6 hours     Yes\*   Yes\*\*   Yes   Yes

  Elevated (Premium)        30   7 days      Yes\*   Yes\*\*   Yes   Yes
  ------------------------------------------------------------------------

-   **MQ**: Maximum \number of Questions
-   **MT**: Maximum Time Interval
-   **RR**: Can set role restrictions
-   **TC**: Can set a different target channel
-   **AD**: Can configure auto-deletion of messages
-   **SE**: Can configure and/or start someone else\'s trivia

| ~\*:\ Users\ are\ not\ allowed\ to\ set\ a\ role\ restriction\ to\ roles\ higher\ than\ the\ highest\ role\ they\ have.~
| ~\*\*:\ Users\ are\ not\ allowed\ to\ set\ a\ target\ channel\ to\ a\ channel\ they\ don\'t\ have\ R/W\ access\ to\ (Read\ Messages\ and/or\ Send\ Messages).~

The module also includes a set of \"template\" commands. As an
alternative way of starting a trivia (other than initializing a new one
with default settings), users can save a trivia template and load it at
a later time. Trivia templates will be assigned with a new set of IDs
(\"template IDs\") and will not directly be linked to their original
trivia game configuration.

Template commands can be recognized by their `triviat-` prefix.

::: {.admonition}
Premium

As shown in the table, premium-enabled servers will have an increased
cap of 30 questions and can set an interval for timed trivia games up to
1 week (see: `premium-perks`{.interpreted-text role="ref"}).

Additionally, template commands and triviaexport are only available
within Premium-enabled servers.
:::

triviacategories
----------------

### Command Syntax

::: {.parsed-literal}
trcat
:::

### Command Description

Shows all available trivia category names, and the corresponding number
of available questions.

------------------------------------------------------------------------

triviainit
----------

### Command Syntax

::: {.parsed-literal}
trinit
:::

### Command Description

Initializes a trivia in the current channel.

Default settings are:

-   **Name**: None
-   **Description**: None
-   **Channel**: Current
-   **Categories**: Any
-   **Role Restriction**: None
-   **Trivia Mode**: Immediate
-   **Trivia Questions**: 5
-   **Auto-delete Answer**: Yes
-   **Auto-delete Confirmation**: No

See triviasetup to understand the meaning of each parameter.

------------------------------------------------------------------------

triviasetup
-----------

### Command Syntax

::: {.parsed-literal}
trsetup (trivia id)
:::

### Command Description

Opens the trivia game interactive setup menu. Use the menu items to
configure the above settings.

**Name** will show in the title of each embed related to that trivia.
Trivia names cannot be longer than 128 characters.

**Description** will appear on each question, and in the starting and
final embed. Trivia descriptions cannot be longer than 1024 characters.

**Categories** can be left blank (\"any category\") or it can be used to
restrict the questions to **one or more** categories. At the time of
writing this documentation page, the categories available from the Open
Trivia Database are:

1.  Animals
2.  Art
3.  Celebrities
4.  Entertainment: Board Games
5.  Entertainment: Books
6.  Entertainment: Cartoon & Animations
7.  Entertainment: Comics
8.  Entertainment: Film
9.  Entertainment: Japanese Anime & Manga
10. Entertainment: Music
11. Entertainment: Musicals & Theatres
12. Entertainment: Television
13. Entertainment: Video Games
14. General Knowledge
15. Geography
16. History
17. Mythology
18. Politics
19. Science & Nature
20. Science: Computers
21. Science: Gadgets
22. Science: Mathematics
23. Sports
24. Vehicles

The categories selection supports partial names: if you want to select
\"Mythology\" you can just use \"myth\", etc.

::: {.note}
::: {.title}
Note
:::

There will soon be a way to add custom categories and custom questions
to the database.
:::

**Interval** is the amount of time a question will be up in a **timed**
trivia. Disabling this parameter sets the trivia mode to **immediate**.
Go to the top of this page to understand the difference between the two
modes.

**Questions Amount** is the number of questions after which the trivia
game will end. Refer to the limitations table at the top of this page to
know the limits. A trivia game will always end if the actual amount of
available questions is lower than the \"configured\" amount.

**Channel** is the actual channel the trivia will be started into after
the triviastart command. As stated in the limitations table, it can be
set to another channel only if you are an \"Elevated\" user.

::: {.note}
::: {.title}
Note
:::

There can only be **1** running (or paused) trivia game per channel at a
given time.
:::

**Authorized Roles**, as the name suggests, are roles authorized to
submit answers to the selected trivia. If omitted, everyone will be able
to submit an answer. If one or more roles are configured, users will
need to have at least one of these roles to submit an answer.

**Auto-deletion of Answers** toggles whether or not the bot should
delete the answers posted by a user. In order to keep the secrecy of a
user\'s answer (especially in timed trivia games), this configuration is
active by default.

**Auto-deletion of Confirmation Messages** toggles whether or not the
bot should delete its own confirmation message upon registering an
answer. The deletion of confirmation messages happens after 5 seconds.

### Examples

::: {.parsed-literal}
trsetup 0 trset 2
:::

------------------------------------------------------------------------

triviastart
-----------

### Command Syntax

::: {.parsed-literal}
trstart (trivia id)
:::

### Command Description

Starts a trivia game in the configured target channel, using the
corresponding settings.

::: {.note}
::: {.title}
Note
:::

There can only be **1** running (or paused) trivia game per channel at a
given time.
:::

### Examples

::: {.parsed-literal}
trstart 0
:::

------------------------------------------------------------------------

triviaanswer
------------

### Command Syntax

::: {.parsed-literal}
tra (answer number)
:::

### Command Description

Submits an answer to the currently running trivia. Since only 1 running
trivia game can be running in a channel at a given time, you won\'t need
to specify the trivia ID.

### Examples

::: {.parsed-literal}
tra 2 tra 4
:::

------------------------------------------------------------------------

triviaresults
-------------

### Command Syntax

::: {.parsed-literal}
trres (trivia id)
:::

### Command Description

Prints the final results of a trivia game. This is the same embed that
is printed when a trivia game ends, showing the top 5 users and their
corresponding scores.

This command only works on completed trivia games.

### Examples

::: {.parsed-literal}
trres 0
:::

------------------------------------------------------------------------

triviamyresults
---------------

### Command Syntax

::: {.parsed-literal}
trmyres (trivia id)
:::

### Command Description

Shows a detailed list of questions and the corresponding submitted
answers for the user running this command, showing whether the given
answers are correct or not.

This command only works on completed trivia games.

### Examples

::: {.parsed-literal}
trmyres 0 trmres 2
:::

------------------------------------------------------------------------

triviashow
----------

### Command Syntax

::: {.parsed-literal}
trshow \[trivia id\]
:::

### Command Description

Shows the current configuration of a trivia, given its ID.

If the ID is omitted, the command will show the info of the running (or
paused) trivia game in the current channel, if any.

### Examples

::: {.parsed-literal}
trshow trshow 2
:::

------------------------------------------------------------------------

trivialist
----------

### Command Syntax

::: {.parsed-literal}
trlist
:::

### Command Description

Shows the list of all (non-deleted) trivia games in the server: their
ID, name and status.

### Examples

::: {.parsed-literal}
trls
:::

------------------------------------------------------------------------

triviapause
-----------

### Command Syntax

::: {.parsed-literal}
trpause \[trivia id\]
:::

### Command Description

**This command is only available to Elevated Users.**

Pauses a trivia, given its ID. Pausing a trivia will make users unable
to submit answers for that trivia. If the trivia game was set as
**timed**, the timer for the current question will continue to count
down to zero, but the next question will not appear until the game is
unpaused.

If the ID is omitted, the command will attempt to pause the trivia game
in the current channel, if any.

### Permissions Needed

| **User**: Manage Messages, Manage Roles

### Examples

::: {.parsed-literal}
trpause trpause 2
:::

------------------------------------------------------------------------

triviaresume
------------

### Command Syntax

::: {.parsed-literal}
trresume \[trivia id\]
:::

### Command Description

**This command is only available to Elevated Users.**

Resumes a previously paused trivia, given its ID. Resuming a trivia will
make users able to submit answers for that trivia again.

If the ID is omitted, the command will attempt to resume the paused
trivia game in the current channel, if any.

### Permissions Needed

| **User**: Manage Messages, Manage Roles

### Examples

::: {.parsed-literal}
trresume trresume 2
:::

------------------------------------------------------------------------

triviadelete
------------

### Command Syntax

::: {.parsed-literal}
trdelete \[trivia id\]
:::

### Command Description

**This command is only available to Elevated Users.**

**This command only works on paused or completed trivia games.**

Stops (if paused) and deletes a trivia game from the server, also hiding
its ID from trivialist.

If the ID is omitted, the command will attempt to delete the paused
trivia game in the current channel, if any.

### Permissions Needed

| **User**: Manage Messages, Manage Roles

### Examples

::: {.parsed-literal}
trdelete trdelete 2
:::

------------------------------------------------------------------------

triviaexport
------------

### Command Syntax

::: {.parsed-literal}
trexp \[trivia id\]
:::

### Command Description

**This command is only available to Elevated Users in Premium-enabled
servers.**

**This command only works on completed trivia games.**

Exports the detailed info about a completed trivia into a `.csv` file.
The file will contain the complete list of users who answered to the
trivia game and the corresponding correctness (or incorrectness) for
each question in the trivia.

*This is the only way of having a full list of users. The top 5 users
are shown in the trivia final results embed.*

### Permissions Needed

| **User**: Manage Messages, Manage Roles

### Examples

::: {.parsed-literal}
trexp 2
:::

------------------------------------------------------------------------

triviatsave
-----------

### Command Syntax

::: {.parsed-literal}
trtsave \[trivia id\]
:::

### Command Description

**This command is only available to Elevated Users in Premium-enabled
servers.**

Saves the current configuration for the selected trivia into a
\"template\" which can then be re-used with trtload. Each run of this
command will generate a new **template ID**.

Once saved, a template becomes independent from the corresponding
original trivia game: changing the settings for the originating trivia
game will **not** update the corresponding template.

### Permissions Needed

| **User**: Manage Messages, Manage Roles

### Examples

::: {.parsed-literal}
trtsave 3
:::

------------------------------------------------------------------------

triviatload
-----------

### Command Syntax

::: {.parsed-literal}
trtload \[template id\]
:::

### Command Description

**This command is only available in Premium-enabled servers.**

Loads a previously saved configuration from a template, creating a new
trivia game with a new trivia ID.

The new trivia game will be set in a \"Initialized\" status, and can be
immediately started with trstart or furtherly configured with trset.

### Examples

::: {.parsed-literal}
trtload 1
:::

------------------------------------------------------------------------

triviatdelete
-------------

### Command Syntax

::: {.parsed-literal}
trtdelete \[template id\]
:::

### Command Description

**This command is only available to Elevated Users in Premium-enabled
servers.**

Deletes a previously saved configuration template (it will not delete
the originating trivia game).

### Permissions Needed

| **User**: Manage Messages, Manage Roles

### Examples

::: {.parsed-literal}
trtdelete 1
:::

------------------------------------------------------------------------

triviatshow
-----------

### Command Syntax

::: {.parsed-literal}
trtshow \[template id\]
:::

### Command Description

**This command is only available in Premium-enabled servers.**

Shows the current configuration of a trivia template, given its ID.

### Examples

::: {.parsed-literal}
trtshow 1
:::

------------------------------------------------------------------------

triviatlist
-----------

### Command Syntax

::: {.parsed-literal}
trtlist
:::

### Command Description

**This command is only available in Premium-enabled servers.**

Shows the list of all (non-deleted) trivia templates in the server:
their ID, name and basic info.

### Examples

::: {.parsed-literal}
trtls
:::
