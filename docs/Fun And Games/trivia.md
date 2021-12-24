Trivia
======

This module lets users play trivia quiz games on Discord. The module
gets its default questions from the **Open Trivia Database**, which
offers more than 3,000 validated questions in more than 15 categories.

The trivia module is meant to be public and used by anyone for fun.
Users with "Manage Messages" & "Manage Roles" permissions, hereafter
called "Elevated Users", will also have access to extra settings that
will make them able to set trivia quiz games up for use by other users
(typical use cases include events, giveaways, etc.).

Trivia games can be **timed** or **immediate**.

-   **Immediate** trivia games move to the next question as soon as one
    answer is collected.
-   **Timed** trivia games move to the next question as soon as a
    certain time interval passes, and collect answers from anyone during
    that period (limitations may apply, see later).

Depending on the "type" of user running the command(s), some
limitations apply to the usage of the trivia module. The following table
shows such limitations.

| User Type               | MQ   | MT      | RR    | TC     | AD   | SE   |
|:------------------------|:-----|:--------|:------|:-------|:-----|:-----|
| Normal                  | 10   | 3 mins  | No    | No     | No   | No   |
| Elevated                | 20   | 6 hours | Yes*  | Yes**  | Yes  | Yes  |
| Premium                 | 30   | 7 days  | Yes*  | Yes**  | Yes  | Yes  |

-   **MQ**: Maximum number of Questions
-   **MT**: Maximum Time Interval
-   **RR**: Can set role restrictions
-   **TC**: Can set a different target channel
-   **AD**: Can configure auto-deletion of messages
-   **SE**: Can configure and/or start someone else's trivia

~*~~Users~ ~are~ ~not~ ~allowed~ ~to~ ~set~ ~a~ ~role~ ~restriction~ ~to~ ~roles~ ~higher~ ~than~ ~the~ ~highest~ ~role~ ~they~ ~have.~

~**~~Users~ ~are~ ~not~ ~allowed~ ~to~ ~set~ ~a~ ~target~ ~channel~ ~to~ ~a~ ~channel~ ~they~ ~don't~ ~have~ ~R/W~ ~access~ ~to~ ~(Read~ ~Messages~ ~and/or~ ~Send~ ~Messages).~

The module also includes a set of "template" commands. As an
alternative way of starting a trivia (other than initializing a new one
with default settings), users can save a trivia template and load it at
a later time. Trivia templates will be assigned with a new set of IDs
("template IDs") and will not directly be linked to their original
trivia game configuration.

Template commands can be recognized by their `triviat-` prefix.

!!!tip "Premium Perks"

        As shown in the table, [Premium-enabled](../Contents/premium-perks.md) servers will have an increased
        cap of 30 questions and can set an interval for timed trivia games up to
        1 week (see: [Premium Perks](../Contents/premium-perks.md)).

        Additionally, template commands and triviaexport are only available
        within [Premium-enabled](../Contents/premium-perks.md)) servers.


{{bot.prefix}}triviacategories
----------------

### Command Syntax
!!!example ""

        {{bot.prefix}}trcat


### Command Description

Shows all available trivia category names, and the corresponding number
of available questions.

------------------------------------------------------------------------

{{bot.prefix}}triviainit
----------

### Command Syntax
!!!example ""

        {{bot.prefix}}trinit


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

See [`{{bot.prefix}}triviasetup`](/GiselleBot-Documentation/Fun And Games/trivia#triviasetup) to understand the meaning of each parameter.

------------------------------------------------------------------------

{{bot.prefix}}triviasetup
-----------

### Command Syntax
!!!example ""

        {{bot.prefix}}trsetup (trivia id)


### Command Description

Opens the trivia game interactive setup menu. Use the menu items to
configure the above settings.

**Name** will show in the title of each embed related to that trivia.
Trivia names cannot be longer than 128 characters.

**Description** will appear on each question, and in the starting and
final embed. Trivia descriptions cannot be longer than 1024 characters.

**Categories** can be left blank ("any category") or it can be used to
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

!!!tip "Tip"

        The categories' selection supports partial names: if you want to select
        "Mythology" you can just use "myth", etc.

!!!abstract "Note"

        There will soon be a way to add custom categories and custom questions
        to the database.


**Interval** is the amount of time a question will be up in a **timed**
trivia. Disabling this parameter sets the trivia mode to **immediate**.
Go to the top of this page to understand the difference between the two
modes.

**Questions Amount** is the number of questions after which the trivia
game will end. Refer to the limitations' table at the top of this page to
know the limits. A trivia game will always end if the actual amount of
available questions is lower than the "configured" amount.

**Channel** is the actual channel the trivia will be started into after
the triviastart command. As stated in the limitations table, it can be
set to another channel only if you are an "Elevated" user.

!!!info "Note"

        There can only be **1** running (or paused) trivia game per channel at a
        given time.


**Authorized Roles**, as the name suggests, are roles authorized to
submit answers to the selected trivia. If omitted, everyone will be able
to submit an answer. If one or more roles are configured, users will
need to have at least one of these roles to submit an answer.

**Auto-deletion of Answers** toggles whether the bot should
delete the answers posted by a user. In order to keep the secrecy of a
user's answer (especially in timed trivia games), this configuration is
active by default.

**Auto-deletion of Confirmation Messages** toggles whether the
bot should delete its own confirmation message upon registering an
answer. The deletion of confirmation messages happens after 5 seconds.

### Examples
!!!example ""

        {{bot.prefix}}trsetup 0 
        {{bot.prefix}}trset 2


------------------------------------------------------------------------

{{bot.prefix}}triviastart
-----------

### Command Syntax
!!!example ""

        {{bot.prefix}}trstart (trivia id)


### Command Description

Starts a trivia game in the configured target channel, using the
corresponding settings.

!!!info "Note"

        There can only be **1** running (or paused) trivia game per channel at a
        given time.


### Example
!!!example ""

        {{bot.prefix}}trstart 0


------------------------------------------------------------------------


{{bot.prefix}}triviaanswer
------------

### Command Syntax
!!!example ""

        {{bot.prefix}}tra (answer number)


### Command Description

Submits an answer to the currently running trivia. Since only 1 running
trivia game can be running in a channel at a given time, you won\'t need
to specify the trivia ID.

### Examples
!!!example ""

        {{bot.prefix}}tra 2
        {{bot.prefix}}tra 4


------------------------------------------------------------------------

{{bot.prefix}}triviaresults
-------------

### Command Syntax
!!!example ""

        {{bot.prefix}}trres (trivia id)


### Command Description

Prints the final results of a trivia game. This is the same embed that
is printed when a trivia game ends, showing the top 5 users and their
corresponding scores.

This command only works on completed trivia games.

### Example
!!!example ""

        {{bot.prefix}}trres 0


------------------------------------------------------------------------

{{bot.prefix}}triviamyresults
---------------

### Command Syntax
!!!example ""

        {{bot.prefix}}trmyres (trivia id)


### Command Description

Shows a detailed list of questions and the corresponding submitted
answers for the user running this command, showing whether the given
answers are correct or not.

This command only works on completed trivia games.

### Examples
!!!example ""

        {{bot.prefix}}trmyres 0
        {{bot.prefix}}trmres 2


------------------------------------------------------------------------

{{bot.prefix}}triviashow
----------

### Command Syntax
!!!example ""

        {{bot.prefix}}trshow [trivia id]


### Command Description

Shows the current configuration of a trivia, given its ID.

If the ID is omitted, the command will show the info of the running (or
paused) trivia game in the current channel, if any.

### Examples
!!!example ""

        {{bot.prefix}}trshow
        {{bot.prefix}}trshow 2


------------------------------------------------------------------------

{{bot.prefix}}trivialist
----------

### Command Syntax
!!!example ""

        {{bot.prefix}}trlist


### Command Description

Shows the list of all (non-deleted) trivia games in the server: their
ID, name and status.

### Example
!!!example ""

        {{bot.prefix}}trls


------------------------------------------------------------------------

{{bot.prefix}}triviapause
-----------

### Command Syntax
!!!example ""

        {{bot.prefix}}trpause [trivia id]


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

**User**: Manage Messages, Manage Roles

### Examples
!!!example ""

        {{bot.prefix}}trpause
        {{bot.prefix}}trpause 2

------------------------------------------------------------------------

{{bot.prefix}}triviaresume
------------

### Command Syntax
!!!example ""

        {{bot.prefix}}trresume [trivia id]


### Command Description

**This command is only available to Elevated Users.**

Resumes a previously paused trivia, given its ID. Resuming a trivia will
make users able to submit answers for that trivia again.

If the ID is omitted, the command will attempt to resume the paused
trivia game in the current channel, if any.

### Permissions Needed

**User**: Manage Messages, Manage Roles

### Examples
!!!example ""

        {{bot.prefix}}trresume
        {{bot.prefix}}trresume 2

------------------------------------------------------------------------

{{bot.prefix}}triviadelete
------------

### Command Syntax
!!!example ""       


        {{bot.prefix}}trdelete [trivia id]


### Command Description

**This command is only available to Elevated Users.**

**This command only works on paused or completed trivia games.**

Stops (if paused) and deletes a trivia game from the server, also hiding
its ID from trivialist.

If the ID is omitted, the command will attempt to delete the paused
trivia game in the current channel, if any.

### Permissions Needed

**User**: Manage Messages, Manage Roles

### Examples
!!!example ""

        {{bot.prefix}}trdelete
        {{bot.prefix}}trdelete 2


------------------------------------------------------------------------

{{bot.prefix}}triviaexport
------------

### Command Syntax
!!!example ""

        {{bot.prefix}}trexp [trivia id]


### Command Description

**This command is only available to Elevated Users in [Premium-enabled](../Contents/premium-perks.md)
servers.**

**This command only works on completed trivia games.**

Exports the detailed info about a completed trivia into a `.csv` file.
The file will contain the complete list of users who answered to the
trivia game and the corresponding correctness (or incorrectness) for
each question in the trivia.

*This is the only way of having a full list of users. The top 5 users
are shown in the trivia final results embed.*

### Permissions Needed

**User**: Manage Messages, Manage Roles

### Example
!!!example ""

        {{bot.prefix}}trexp 2


------------------------------------------------------------------------

{{bot.prefix}}triviatsave
-----------

### Command Syntax
!!!example ""

        {{bot.prefix}}trtsave [trivia id]


### Command Description

**This command is only available to Elevated Users in [Premium-enabled](../Contents/premium-perks.md)
servers.**

Saves the current configuration for the selected trivia into a
"template" which can then be re-used with trtload. Each run of this
command will generate a new **template ID**.

Once saved, a template becomes independent of the corresponding
original trivia game: changing the settings for the originating trivia
game will **not** update the corresponding template.

### Permissions Needed

**User**: Manage Messages, Manage Roles

### Example
!!!example ""

        {{bot.prefix}}trtsave 3


------------------------------------------------------------------------

{{bot.prefix}}triviatload
-----------

### Command Syntax
!!!example ""

        {{bot.prefix}}trtload [template id]


### Command Description

**This command is only available in [Premium-enabled](../Contents/premium-perks.md) servers.**

Loads a previously saved configuration from a template, creating a new
trivia game with a new trivia ID.

The new trivia game will be set in an "Initialized" status, and can be
immediately started with trstart or furtherly configured with trset.

### Example
!!!example ""

        {{bot.prefix}}trtload 1


------------------------------------------------------------------------

{{bot.prefix}}triviatdelete
-------------

### Command Syntax
!!!example ""

        {{bot.prefix}}trtdelete [template id]


### Command Description

**This command is only available to Elevated Users in [Premium-enabled](../Contents/premium-perks.md)
servers.**

Deletes a previously saved configuration template (it will not delete
the originating trivia game).

### Permissions Needed

**User**: Manage Messages, Manage Roles

### Example
!!!example ""

        {{bot.prefix}}trtdelete 1


------------------------------------------------------------------------

{{bot.prefix}}triviatshow
-----------

### Command Syntax
!!!example ""

        {{bot.prefix}}trtshow [template id]


### Command Description

**This command is only available in [Premium-enabled](../Contents/premium-perks.md) servers.**

Shows the current configuration of a trivia template, given its ID.

### Example
!!!example ""

        {{bot.prefix}}trtshow 1


------------------------------------------------------------------------

{{bot.prefix}}triviatlist
-----------

### Command Syntax
!!!example ""

        {{bot.prefix}}trtlist


### Command Description

**This command is only available in [Premium-enabled](../Contents/premium-perks.md) servers.**

Shows the list of all (non-deleted) trivia templates in the server:
their ID, name and basic info.

### Example
!!!example ""

        {{bot.prefix}}trtls

