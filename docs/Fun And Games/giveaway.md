Giveaway Campaigns
==================

The Giveaway Campaigns module enables users to start and manage
giveaways in a Discord server.

{{bot.prefix}}gcstart
-------

### Command Syntax
!!!example ""

        {{bot.prefix}}gcstart [--channel {channel id/mention/q_name}] [--prize {prize name}] [--winners {number of winners}] [--duration {duration timecode}] [--roles {role(s) id/mention/q_name}] [--max {number of users after which the bot will stop the giveaway}]


### Command Description

Starts a new giveaway in a channel (the current channel, if the
`--channel` parameter is omitted). Members can participate by clicking
on the reaction that is added by the bot.

If the `--roles` parameter is used, the giveaway will only select
winners among those participants that have **at least one of the
selected roles** at the time of closure of the giveaway. The `--roles`
parameter cannot be used in conjunction with the `--max` parameter,
using both will ignore the `--max` parameter.

All parameters are optional, the default values (on omission) are:

-   **Channel**: Current channel
-   **Prize Name**: "Sample Prize"
-   **Winners**: 1
-   **Duration**: 1 day (24 hours)
-   **Roles Restriction**: *None* (All participants will be considered)
-   **Max**: *None* (Infinite)

!!!abstract "Note"

        Users must still be members of the server at the time of the giveaway
        campaign end for them to be rolled as winners. Users that are not in the
        server when the campaign ends will not be considered. Bots reacting to
        the giveaway campaign will always be ignored.


### Examples
!!!example ""

        {{bot.prefix}}gcstart --prize Free Steam Key --winners 2 --duration 1w
        {{bot.prefix}}gcstart --prize Blue Hat --winners 5 --roles @BluePeople @WearingHats
        {{bot.prefix}}gcstart --channel #giveaways --prize Free Steam Key to the fastest 5! --winners 5 --max 5


------------------------------------------------------------------------

{{bot.prefix}}gcedit
------

### Command Syntax
!!!example ""

        gcedit [message id]


### Command Description

Opens an editing menu for an existing giveaway in the current channel.
The message ID is optional: if omitted, the most recent giveaway in the
channel will be considered.

You cannot edit a giveaway duration, channel, list of restricted roles
(if applicable) or maximum amount of users (if applicable, refer to the
`--max` parameter).

### Examples
!!!example ""

        {{bot.prefix}}gcedit --prize 2 Free Steam Keys
        {{bot.prefix}}gcedit 123456789098765432 --winners 5


------------------------------------------------------------------------

{{bot.prefix}}gcend
-----

### Command Syntax
!!!example ""

        {{bot.prefix}}gcend [message id]


### Command Description

Immediately ends a giveaway and picks a winner (or more winners) among
those that participated. The message ID is optional: if omitted, the
most recent giveaway in the channel will be considered.

!!!tip "Tip"

        You can completely abort a campaign by deleting the campaign message that the bot sent.

### Examples
!!!example ""

        {{bot.prefix}}gcend
        {{bot.prefix}}gcend 123456789098765432


------------------------------------------------------------------------

{{bot.prefix}}gcreroll
--------

### Command Syntax
!!!example ""

        {{bot.prefix}}gcreroll [message id] [--winners {number of winners}]


### Command Description

Picks one (or more, if the `--winners` parameter is used) new winner(s)
for an already ended giveaway. The message ID is optional: if omitted,
the most recent (ended) giveaway in the channel will be considered.

You can only reroll up to 10 winners per command run.

This command will not overwrite the existing winners in the original
message. It will also keep track of former winners and previous rerolls
to make sure that the new winners weren't already picked in a previous
iteration of the command.

!!!abstract "Note"

        Users must still be members of the server at the time of the giveaway
        campaign reroll for them to be rolled as winners. Users that are not in
        the server when the campaign is rerolled will not be considered. Bots
        reacting to the giveaway campaign will always be ignored.


### Examples
!!!example ""

        {{bot.prefix}}gcreroll
        {{bot.prefix}}gcreroll 123456789098765432 --winners 5


------------------------------------------------------------------------

{{bot.prefix}}gclist
------

### Command Syntax
!!!example ""

        {{bot.prefix}}gclist


### Command Description

Lists all ongoing giveaways in the current server.

------------------------------------------------------------------------

{{bot.prefix}}gcreaction
----------

### Command Syntax
!!!example ""

        {{bot.prefix}}gcreaction [emoji]


### Command Description

Sets a custom emoji for the giveaway campaign in the current server.

This change only applies to new giveaways: giveaway campaigns that are
already running will keep their former reaction setting.

Use with no parameters (no emoji) to show the current giveaway reaction
emoji. Use with `-` as parameter to restore the default emoji: :tickets:

!!!warning "Warning"

        You **must** use reactions that are either "global" (Discord native emojis) or present in the server.


### Permissions Needed

**User**: Manage Server

### Examples
!!!example ""

        gcreaction 😀
        gcreaction :GiselleDrink:
        gcreaction -
        gcreaction

