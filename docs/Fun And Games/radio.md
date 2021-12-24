Radio
=====

The Radio module enables users to listen to web radio stations in a
Discord server\'s dedicated voice channel.

The Radio module must be first enabled by a server manager (someone with
**Manage Server** permissions) by setting a web radio channel with the
rchannel command.

{{bot.prefix}}rchannel
--------

### Command Syntax
!!!example ""

        {{bot.prefix}}rchannel [channel id, or "-"]


### Command Description

Sets a channel as the authorized web radio channel for the bot.

Running this command while being in a voice channel will turn the
current voice channel into the authorized web radio channel. You can
also use the ID of a voice channel.

Running this command while not in a voice channel and without any extra
argument will show the current authorized web radio channel.

Using "-" as argument will remove the current authorized web radio
channel and disable the radio module until a voice channel is
authorized.

### Permissions Needed

**User**: Manage Server

### Examples
!!!example ""

        {{bot.prefix}}rchannel 
        {{bot.prefix}}rchannel 123456789098765432 
        {{bot.prefix}}rchannel -


------------------------------------------------------------------------

{{bot.prefix}}rplay
-----

### Command Syntax
!!!example ""

        {{bot.prefix}}rp


### Command Description

Shows the list of available web radio stations.

------------------------------------------------------------------------

{{bot.prefix}}rstop
-----

### Command Syntax
!!!example ""

        {{bot.prefix}}rstop


### Command Description

Immediately stops the web radio stream. If 3 or more people are
listening in the same web radio voice channel, a vote will happen.

For a "vote stop" to take effect, **70%** of the voice channel members
must agree.

!!!note "Note"

        Let's assume there are 10 users in the web radio voice channel. The
        threshold for skipping is calculated as 70% of 10 = 7 (numbers will be
        rounded down if needed). For the "vote stop" to take effect, you would
        then need 7 positive votes.


!!!info "Note"

        "Vote stop" will not be active until there are 3 or more people in the
        voice channel (with one person, insta-skip is enabled and with two the
        threshold for skipping is 1). Server managers (users with "Manage
        Server" permissions) will bypass the voting system.


------------------------------------------------------------------------

{{bot.prefix}}rnowplaying
-----------

### Command Syntax
!!!example ""

        {{bot.prefix}}rnp


### Command Description

Shows info about the currently playing radio station.
