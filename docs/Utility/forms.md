Forms Builder
=============

The Forms Builder module enables users to create Q/A forms that are
presented to end-users by sending a Direct Message to the bot. The Q/As
can be set up to be a sequence of multi-choice or open questions, with
the final output (submission) being sent into a server channel by the
bot itself for further validation, priority assignment and optional
integration with external services.

(Optional features) Upon accepting a submission, a submission summary
can be forwarded as a read-only post to a different channel and can be
automatically given an \"upvote\" and \"downvote\" reaction for people
to show their support (or lack thereof) to the specific submission.

Currently, each form submission can be configured to remain within the
Discord realm, or uploaded to [Trello](https://trello.com/) (a powerful
web-based, list-making application) as a \"Trello card\" (\"share
mode\").

Trello integration also includes the 2-way synchronization of
upvotes/downvotes and comments number from and to Discord and Trello
(showing the number of upvotes and downvotes on the Trello card, as well
as showing the current number of Trello comments and votes on the
Discord message), and Discord DM notifications to the author of the
submission upon Trello card activities (new comments, title changes,
card archival, etc.).

::: {.warning}
::: {.title}
Warning
:::

For the **Trello** integration to work, some limitations currently
apply:

1.  You must **invite** to your Trello team and give it permissions to
    edit the board in order for the bot to monitor, post and update
    cards. You can invite to your Trello team using this email address:
    .
2.  You must **pair** the Discord server with the Trello team by using
    the trellopair command. Each Discord server can only be paired with
    1 Trello team.
3.  Form settings will be fixed once a user sends a submission. Any
    change to a form will not apply to submissions that are already in
    the approval queue. This also means that the Trello board must be
    set (thus, exist) before a submission is sent.
:::

::: {.note}
::: {.title}
Note
:::

Users that are enabled to use the module using the
`permissions`{.interpreted-text role="ref"} will always be authorized to
accept or reject any submission coming from any form. In order to enable
more roles to accept/reject specific forms, you can set one or more
roles as \"authorized roles\" on each form both during the initial setup
of the form and through the formsetup command.
:::

::: {.admonition}
Premium

Out of the box, each server is limited to having a total of **3
available forms**. If you want to remove this limitation and have up to
**20** forms, you can unlock the number of forms as a **Premium**
feature (see: `premium-perks`{.interpreted-text role="ref"}).
:::

::: {.hint}
::: {.title}
Hint
:::

In order to ease the creation of the complex strings you need to add
questions to a form, you can use this [Forms Builder
Helper](https://gisl.eu/formbuilder) to create pre-made strings to be
used in those phases. Just create a copy of that sheet and customize it
to your needs.
:::

trellopair
----------

### Command Syntax

::: {.parsed-literal}
trellopair \[team name/URL, or \"-\"\]
:::

### Command Description

Pairs a Discord server with a Trello team. No restrictions are applied
to the number of Discord servers that can pair a Trello team, although
**each server must pass the verification step individually** (see
below).

In order to pair with a team, you can use the team name or the URL
containing the team name (see the note below).

Using the command without any argument will show the current paired
Trello team.

Using `-` as the only argument will unpair the current server from the
paired Trello team.

::: {.note}
::: {.title}
Note
:::

The team name is the one you find inside the Trello URL within the team
page, which usually has this form: `https://trello.com/TEAM_NAME/home`
:::

**As a security measure, the Trello team pairing process is composed of
2 steps.** Running this command will issue a verification request to the
target Trello team, giving the user who run the command a 6-digits
unique code (that is generated randomly when the command is run). You
must then verify that you have enough permissions to create cards on at
least one Team board before the pairing is effective.

will start querying the Trello team boards in order to find a card with
the 6-digits code set as title. You must head to one of the Team boards
and **create a card (in any list) with the provided 6-digits code as
title**.

If no card is found with the correct title within **5 minutes** from
running the command, the pairing will fail. If the card is found, the
pairing will complete and the team boards will be available for use in
the Forms module.

Once the card is found the pairing will complete, actvating the
integration. The verification card will be deleted, and you will be
notified (with a mention) in the current channel.

### Permissions Needed

| **User**: Manage Server

------------------------------------------------------------------------

submit
------

### Command Syntax

::: {.parsed-literal}
submit
:::

### Command Description

Shows the available forms for the servers a user is currently in, giving
the option to start filling a submission.

::: {.note}
::: {.title}
Note
:::

This command can be used in a **Direct Message channel** with . In that
case, will start the submission by showing a list of servers the user
can select.

If used within an actual server, it will make send a DM to the user
running the command, showing the available forms for the specific server
the command was run into.

When the command is used in \'s DMs, the list of available servers is
taken from \'s current cache. If the server you are looking for does not
appear, use the submit command from within that server.

This command **is not subject to any permissions** other than a specific
blacklist check (see formblacklist).

The actual form submission must always happen though \'s DMs.
:::

------------------------------------------------------------------------

submitreact
-----------

### Command Syntax

::: {.parsed-literal}
submitreact \[\--m {message id}\]
:::

### Command Description

Other than sending the `submit`{.interpreted-text role="ref"} command to
via DM, or using it in a server to quickly start the DM workflow,
authorized people can enable a specific reaction on a message of choice
(or a message created by for that purpose) to have send the initial form
submission DM to the user clicking on the reaction.

This command starts a simple interactive process to build this \"submit
reaction message\". will guide you through the process of creating this
reaction, just follow the in-Discord instructions.

If a valid message ID is specified through the dedicated parameter, the
submit reaction will be created on the target message.

### Examples

::: {.parsed-literal}
submitreact submitreact \--m 123456789098765432
:::

------------------------------------------------------------------------

submitreactremove
-----------------

### Command Syntax

::: {.parsed-literal}
submitreactremove \[message id\]
:::

### Command Description

Removes the submit reaction behavior from an existing message. The
message itself won\'t be deleted, nor the existing reactions will be
removed, but will now not do anything with the reaction on that message.

If the message ID is omitted (or is invalid), will attempt to pick the
latest submit reaction message in the current channel.

### Examples

::: {.parsed-literal}
submitreactremove 123456789098765432
:::

------------------------------------------------------------------------

adsubmit
--------

### Command Description

Toggles the automatic deletion of the \"confirmation\" message that is
sent upon using the submit command into a server, and of the command
itself.

The user-sent message will be deleted immediately. The confirmation
message will be deleted after 5 seconds.

### Permissions Needed

| **User**: Manage Messages
| **Bot**: Manage Messages

------------------------------------------------------------------------

forminit
--------

### Command Syntax

::: {.parsed-literal}
foinit
:::

### Command Description

Initializes a new form builder. The bot will guide the user into setting
up the basic configurations and first question.

Forms questions will expire after:

-   5 minutes, for reaction questions;
-   15 minutes, for open questions.

The format to set a form question is:

::: {.parsed-literal}
(message/reaction)(list of reactions)/\[validation words\]\[Trello
mapping\]
:::

Each question has to be set using 5 fields, separated by one `|`
character.

-   First field: `message` will require the question to be answered with
    a plain text message. `reaction` will require the user to select one
    answer by clicking on a reaction that will be added to the question
    by the bot.
-   Second field: The actual question.
-   Third field:
    -   If `reaction` is selected in the first field, this field will
        list all of the possible answers, using `;` to separate these
        answers. If this is the case, this field is **mandatory**.
    -   If `message` is selected in the first field, this field will
        include a list of validation words: any answer given by the
        target user will be ignored unless the message contains at least
        one of the chosen words/sentences (case insensitive). Again, you
        can separate words/sentences with `;`. If this is the case, this
        field is optional.

::: {.note}
::: {.title}
Note
:::

Due to Discord limitations, there can only be a maximum of 20 answers in
a reaction question. Answers from the 21st onward will be ignored.
:::

-   Fourth field: The question \"alias\". This is the title that will
    replace the full question when the feedback is posted in the server
    channel. This field is optional, but it\'s higly suggested that you
    set an alias.
-   Fifth field: This will map the question into one of the entities of
    the Trello board. While `private` and `attachment` have a meaning in
    in-Discord share mode (see formsetup), the rest is only useful if
    you are interested in Trello integration; you can choose whether or
    not including Trello integration later:
    -   `title` will use the answer as the title of a card.
    -   `list` will use the answer as the title of a list.
    -   `label` will add the answer as a card label.
    -   `attachment` will add the answer as a card attachment. If the
        \"attachments highlighting\" option is active, fields flagged as
        `attachment` will also appear in the public in-Discord summary
        message.
    -   `description` will add the answer as part of the description
        text, with the format: `{Alias}: {Text}`.
    -   `private` will show the answer into the \"in-Discord\" embed
        during the authorization process but won\'t upload the field to
        Trello (or show it in the public in-Discord summary message)
        whatsoever.

::: {.warning}
::: {.title}
Warning
:::

A field being \"optional\" means that its content can be left blank, but
the field itself has to exist; e.g.
`message|Heads or Tails?||The user picked...|`
:::

::: {.hint}
::: {.title}
Hint
:::

In order to ease the creation of these complex strings, you can use this
[Forms Builder Helper](https://gisl.eu/formbuilder) to create a pre-made
string to be used in this phase. Just create a copy of that sheet and
customize it to your needs.
:::

------------------------------------------------------------------------

formsetup
---------

### Command Syntax

::: {.parsed-literal}
foset (form id)
:::

### Command Description

Opens the forms builder interactive configuration menu. Use the menu
items to configure the available settings.

![Forms Builder Interactive Configuration Menu](../images/forms_image_00.png){.align-center
width="400px"}

Options 1. and 2. are used to save the settings you applied through the
menu (the settings will not apply until you save them), or discard said
changes.

3.  \"Set title\" sets the title of the form, as it appears when listed
    by .
4.  \"Set color\" sets the form embeds color.
5.  \"Set authorization channel\" sets the channel where form
    submissions are sent to for the initial validation by the authorized
    users. This option is mandatory.
6.  \"Set forwarding channel(s)\" sets the additional forwarding
    channels where, if set, the public in-Discord summary message will
    be sent to. This is optional.
7.  \"Set authorized role(s)\" sets the list of roles that will be both
    authorized to accept and reject submissions to the current form, and
    mentioned (optional, see option 18) within the authorization channel
    when a submission is received.
8.  \"Toggle share mode\" sets the final target of a validated
    submission to either Trello, or just Discord.
9.  \"Toggle publish status\" works as an alias of formpublish and
    formwithhold to make a form available or unavailable for server
    members through \'s DMs.
10. \"Toggle upvoting\" enables or disables the upvote tracking feature
    (and upvote arrow application for new submissions) on a specific
    form.
11. \"Toggle downvoting\" enables or disables the downvote tracking
    feature (and downvote arrow application for new submissions) on a
    specific form.

::: {.note}
::: {.title}
Note
:::

-   **Disabling** a voting arrow will **not** remove the `:arrow_up:`
    and/or `:arrow_down:` reaction from existing submissions, but it
    will stop those submissions\' votes from being tracked in Trello (if
    you are using the Trello share mode). New submissions will **not**
    have the corresponding arrow reaction applied.
-   **Enabling** a previously disabled voting arrow will **not** reapply
    the arrow to existing submissions. It **will** track the votes as
    long as **any user** adds the `:arrow_up:` and/or `:arrow_down:`
    reaction to the public submission message (as long as it\'s the
    native Discord reaction and not a custom one).
:::

12. \"Toggle highlighting of attachments\" enables or disables the
    public embed from having an additional field where all of the
    \"attachment\"-flagged fields are linked, using their `gisl.eu`
    short link (using the same engine behind
    `shorturl`{.interpreted-text role="ref"}).
13. \"Set mentioned role(s)\" sets the list of roles that will be
    mentioned in the public in-Discord summary message(s) when a
    submission is accepted.
14. (Only useful in \"Trello share mode\") \"Set target board\" lists
    the available boards within the paired Trello team (refer to
    `trellopair`{.interpreted-text role="ref"}) and sets the linked
    Trello board for the current form. Renaming a board in Trello will
    not affect this link.
15. (Only useful in \"Trello share mode\") \"Toggle extended embed\"
    enables or disabled the public in-Discord summary message extended
    mode: by default, a submission that has Trello set as \"share mode\"
    will only show a short summary of the submission, while the actual
    full post will be found in the linked Trello card. By enabling the
    \"extended embed\", the whole submission will be kept within
    Discord, while still having a link to the corresponding Trello card.
16. (Only useful in \"Discord share mode\" or \"Trello share mode\" with
    \"extended embed\" active) \"Anonymize public submissions\"
    completely hides the submitter info from the public in-Discord
    summary message, keeping the user\'s anonymity intact (as long as
    \"private\"-flagged fields are used for other kinds of recognizable
    data within the form).
17. \"Anonymize rejection messages\" enables or disables whether the
    name of the user that rejected a submission will appear in the
    rejection message on a specific form.
18. \"Mention the authorized role(s) on new submissions\" toggles
    whether the authorized role(s) will be mentioned when a new
    submission is received.
19. \"Toggle priority reactions\" toggles whether the priority reactions
    are applied to the validation message. When this option is off, the
    only options will be \"Pass (No Priority)\" and \"Drop\".

Here\'s an example of a public in-Discord summary message with Trello
share mode, extended embed, attachments highlighting and anonymizer on.

![Forms Builder Submission Example](../images/forms_image_01.png){.align-center
width="600px"}

------------------------------------------------------------------------

formaddqst
----------

### Command Syntax

::: {.parsed-literal}
foaq (form id)
:::

### Command Description

Adds a question to an existing form. Follow the instructions given by
the bot to configure the question. Refer to the previous paragraph for
more details.

### Examples

::: {.parsed-literal}
foaq 1
:::

------------------------------------------------------------------------

formeditqst
-----------

### Command Syntax

::: {.parsed-literal}
foeq (form id) (question id)
:::

### Command Description

Replaces the selected question from an existing form with a new one.
Refer to the previous paragraphs for more details.

### Examples

::: {.parsed-literal}
foeq 1 5
:::

------------------------------------------------------------------------

formremqst
----------

### Command Syntax

::: {.parsed-literal}
forq (form id) (question id)
:::

### Command Description

Deletes a specific question from an existing form.

### Examples

::: {.parsed-literal}
forq 1 5
:::

------------------------------------------------------------------------

formsortqst
-----------

### Command Syntax

::: {.parsed-literal}
fosq (form id) (question\_ids)
:::

### Command Description

Sorts the questions of an existing workflow into the specified order.

### Examples

::: {.parsed-literal}
fosq 1 4 5 1 2 3
:::

------------------------------------------------------------------------

formpublish
-----------

### Command Syntax

::: {.parsed-literal}
fopub (form id)
:::

### Command Description

Publishes an existing form, making it available to server members
through the dedicated section of the bot Direct Messages behavior (see
`submit`{.interpreted-text role="ref"}).

------------------------------------------------------------------------

formwithhold
------------

### Command Syntax

::: {.parsed-literal}
fowh (form id)
:::

### Command Description

Witholds a previously published form, making it unavailable for server
members. This is particularly useful, or even required, for forms that
need to be edited/deleted.

------------------------------------------------------------------------

formdelete
----------

### Command Syntax

::: {.parsed-literal}
fod (form id)
:::

### Command Description

Completely deletes a server form.

------------------------------------------------------------------------

formpreview
-----------

### Command Syntax

::: {.parsed-literal}
fop
:::

### Command Description

Prints the list of available forms for the current server. For each
form, a preview of each question (and the corresponding question ID) is
shown.

------------------------------------------------------------------------

formblacklist
-------------

### Command Syntax

::: {.parsed-literal}
fobl (user id(s)/mention(s)/q\_name(s))
:::

### Command Description

Toggles one (or more) user\'s presence on the forms blacklist.
Blacklisted users won\'t be able to see any available form for the
current server.

### Examples

::: {.parsed-literal}
fobl cycloptux\#1543
:::

------------------------------------------------------------------------

formsexport
-----------

### Command Syntax

::: {.parsed-literal}
foexp
:::

### Command Description

Exports the current forms submission statistics and contents for the
current server.

### Permissions Needed

| **User**: Bot Owner
