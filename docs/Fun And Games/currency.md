Currency System
===============

Each user known to the bot has a currency wallet. Currency is earned in
a few ways:

-   Each message sent in a channel the bot has access to will give a
    small amount of currency to the user (a cooldown is applied to avoid
    plain spamming just to earn currency).
-   Once a day, using the `timely`{.interpreted-text role="ref"}
    command.
-   Every once in a while, reacting to events on the main bot support
    server.
-   Playing with `games`{.interpreted-text role="ref"}.

Currently, the main goal of currency is playing with games. More uses
are planned, but still not implemented.

\$
--

### Command Syntax

::: {.parsed-literal}
\$ \[user id/mention/q\_name\]
:::

### Command Description

Shows the current amount of currency of a user. By default, it will show
the currency wallet info of the user that runs the command. Users can
check someone else\'s wallet by tagging them or using their ID/name.

### Examples

::: {.parsed-literal}
\$ balance \@cycloptux\#1543 bal 123456789098765432
:::

------------------------------------------------------------------------

currencytransfer
----------------

### Command Syntax

::: {.parsed-literal}
currencytransfer (currency amount) (user id/mention)
:::

### Command Description

Transfers a certain amount of currency from the user running the command
to the target/receiving user. You can use `all` instead of the currency
amount to transfer all your currency to the target/receiving user.

### Examples

::: {.parsed-literal}
ctransfer 5000 \@cycloptux\#1543 cpay all 123456789098765432
:::

------------------------------------------------------------------------

timely
------

### Command Syntax

::: {.parsed-literal}
timely
:::

### Command Description

Once a day (by default, but the cooldown can be configured by the bot
owner) users can earn a specified amount of currency by running this
command. The default amount of currency earned is 10 per command run.

------------------------------------------------------------------------

topggnotify
-----------

### Command Syntax

::: {.parsed-literal}
topggnotify
:::

### Command Description

As an additional source of income for bot currency, and as a way to show
your appreciation to , you can vote for on
[Top.gg](https://top.gg/bot/356831787445387285) (click on the website
name to be sent to the bot page).

Any Discord user can vote for each bot once every 12 hours. Each vote
for will award you with **250 currency coins**.

To help give a better chance to fight for the top spots, votes will
count double on the weekend (Fridays, Saturdays and Sundays). This also
means **double the amount of coins**!

By enabling the notification service using the topggnotify command in
any server, you will also be notified when your Discord Bots List vote
is available, thus being able to actively collect your daily coins
efficiently. Each run of the command will toggle its previous state.

Users will only be notified once per vote reset.

------------------------------------------------------------------------

bodvalidate
-----------

### Command Syntax

::: {.parsed-literal}
bodvalidate
:::

### Command Description

As an additional source of income for bot currency, and as a way to show
your appreciation to , you can leave a review for on [Bots on
Discord](https://bots.ondiscord.xyz/bots/356831787445387285) (click on
the website name to be sent to the bot page).

This command will **anonymously** validate your review within the bot.
will check for the existence of a review on your name, and will award
**25,000 currency coins** if found.

will not know which specific review was submitted, nor its positive or
negative state.

**This reward can only be obtained once!**

------------------------------------------------------------------------

cleaderboard
------------

### Command Syntax

::: {.parsed-literal}
clb \[page \#\]
:::

### Command Description

Prints the **global** currency leaderboard.

### Examples

::: {.parsed-literal}
clb clb 3
:::

------------------------------------------------------------------------

currencyemoji
-------------

### Command Syntax

::: {.parsed-literal}
currencyemoji \[emoji\]
:::

### Command Description

Sets a custom emoji as currency in the current server. Using the command
without the extra emoji argument will reset the currency emoji to the
default one.

::: {.warning}
::: {.title}
Warning
:::

You **must** use reactions that are either \"global\" (Discord native
emojis) or present in the server. Failing to do so may result in the
currency emoji not to work.
:::

### Permissions Needed

| **User**: Manage Server

### Examples

::: {.parsed-literal}
currencyemoji 😀 currencyemoji :BlobOwO:
:::

------------------------------------------------------------------------

#### Stonk Market: Buying and Selling Broccoli

The **Stonk Market** allows users to buy and sell 🥦 broccoli at
fluctuating prices, just like real stock markets.

🥦 broccoli can be purchased **every Sunday morning before 12 PM UTC**.
Their price fluctuates over time: **the purchase price will be different
every week, and in every server**. During the week, users can sell 🥦
broccoli at different prices to make a profit. These prices will differ
each morning and afternoon, and again, for each server.

The pricing algorithm is the same that powers Animal Crossing: New
Horizons\'s Stalk Market. You can read more about it
[here](https://docs.google.com/document/d/1bSVNpOnH_dKxkAGr718-iqh8s8Z0qQ54L-0mD-lbrXo/edit#)
.

Buying prices vary between 90 and 110 currency per head of 🥦 broccoli.
There\'s no limit on how many you can buy or sell.

🥦 broccoli must be sold within a week. Otherwise, **they will rot by the
following Sunday morning and lose their monetary value**. will dispose
of them for you when they are no longer good.

broccoliprice
-------------

### Command Syntax

::: {.parsed-literal}
brcprice
:::

### Command Description

Checks the current 🥦 broccoli buying or selling price.

🥦 broccoli can be purchased every Sunday morning before 12 PM UTC, and
sold during the week (Monday to Saturday). The selling price changes
every 12 hours (at 12 AM and 12 PM UTC). All markets are closed on
Sunday afternoon.

------------------------------------------------------------------------

broccolibuy
-----------

### Command Syntax

::: {.parsed-literal}
brcbuy (amount to buy)
:::

### Command Description

Buys the specified amount of 🥦 broccoli at the current buying price for
the server.

🥦 broccoli can be purchased every Sunday morning before 12 PM UTC.
Prices vary between servers.

### Examples

::: {.parsed-literal}
brcbuy 50
:::

------------------------------------------------------------------------

broccolisell
------------

### Command Syntax

::: {.parsed-literal}
brcsell (amount to sell)
:::

### Command Description

Sells the specified amount of 🥦 broccoli at the current selling price
for the server.

🥦 broccoli can be sold during the week, from Monday to Saturday. Prices
vary between servers, and every 12 hours (at 12 AM and 12 PM).

### Examples

::: {.parsed-literal}
brcsell 30
:::

------------------------------------------------------------------------

broccolibag
-----------

### Command Syntax

::: {.parsed-literal}
brcbag
:::

### Command Description

Shows the current amount of 🥦 broccoli a user has.

------------------------------------------------------------------------

broccolianalysis
----------------

### Command Syntax

::: {.parsed-literal}
brcanalysis
:::

### Command Description

Shows the current highest and lowest buying/selling price for 🥦
broccoli.

This will act as a benchmark to evaluate if the price you found in a
server is good or not, or if there\'s any better price to be hunted!

::: {.note}
::: {.title}
Note
:::

This command is **only** available in **GiselleBot Support Center**. You
can join the Discord server using this invite:
:::

------------------------------------------------------------------------

#### Bot Owner Reserved Commands

timelyreset
-----------

### Command Syntax

::: {.parsed-literal}
timelyreset
:::

### Command Description

Resets the timely countdown for everyone.

### Permissions Needed

| **User**: Bot Owner

------------------------------------------------------------------------

timelyset
---------

### Command Syntax

::: {.parsed-literal}
timelyset \[timecode\] \[\# of currency coins\]
:::

### Command Description

Sets the **global** amount of currency and/or cooldown for the timely
command. Modified cooldown applies to everyone immediately, but doesn\'t
reset users\' cooldown.

Running the command with no arguments will show the current settings.

### Permissions Needed

| **User**: Bot Owner

------------------------------------------------------------------------

currencyaward
-------------

### Command Syntax

::: {.parsed-literal}
currencyaward (user and/or role id(s)/mention(s)/q\_name(s)) (amount of
currency)
:::

### Command Description

Awards the selected amount of currency to the specified user(s) and/or
role(s).

### Permissions Needed

| **User**: Bot Owner

------------------------------------------------------------------------

currencytake
------------

### Command Syntax

::: {.parsed-literal}
currencytake (user and/or role id(s)/mention(s)/q\_name(s)) (amount of
currency, or \"all\")
:::

### Command Description

Takes the selected amount of currency from the specified user(s) and/or
role(s). You can use `all` instead of the currency amount to remove all
currency from the target user(s).

::: {.warning}
::: {.title}
Warning
:::

The currency is permanently lost. It\'s **not** transferred to the
owner.
:::

### Permissions Needed

| **User**: Bot Owner

------------------------------------------------------------------------

currencyeventstart
------------------

### Command Syntax

::: {.parsed-literal}
currencyeventstart \[\--amount/\--a {amount of currency to gift to each
reacting user}\] \[\--pot-size/\--p {maximum amount of currency that can
be gifted}\] \[\--duration/\--d {event duration timecode}\]
:::

### Command Description

Starts an event reaction in the current channel.

Each reacting user will be gifted with the selected amount of currency.
You can define the amount of received currency with the `--amount`
parameter.

By default, each user will be rewarded with the specified amount of
currency. You can set a maximum amount of currency for the event
\"bucket\" by using the `--pot-size` parameter (e.g. if
`--amount 50 --p 100` is used, only the first 2 users will actually
receive 50 currency each). You can also set a custom duration for the
event.

::: {.note}
::: {.title}
Note
:::

Checks are in place to ensure that users will only receive their gift
the first time they react. Reacting more than once will **not** assign
any extra currency.
:::

Here are the default values for the command parameters, on omission:

-   **Amount**: 100
-   **Pot Size**: 0 (= no limit)
-   **Duration**: 1 day

### Permissions Needed

| **User**: Bot Owner
