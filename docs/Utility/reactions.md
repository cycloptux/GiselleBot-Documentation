Reactions Parsing
=================

This module enables users to gather stats about the reactions sent into
a channel.

reprint
-------

### Command Syntax

::: {.parsed-literal}
reprint (message id) \[\--sort username/discriminator/nickname\]
\[\--show username/nickname\] \[\--emoji {default or custom emoji}\]
:::

### Command Description

Prints the list of users that reacted to the specified message in a
readable way.

Setting the `--sort` parameter will sort the output using the specified
setting. Defaults to showing the reactions with the order Discord
outputs them.

Setting the `--show` parameter will show the output using the specified
setting. Defaults to showing the users by their username.

Setting the `--emoji` parameter will filter the output to the specified
emoji.

### Examples

::: {.parsed-literal}
reprint 123456789098765432 reprint 123456789098765432 \--sort nickname
\--show nickname reprint 123456789098765432 \--emoji :pikathink:
:::

------------------------------------------------------------------------

resummary
---------

### Command Syntax

::: {.parsed-literal}
resummary \[\# of messages\] \[\--csv\] \[\--silent\]
:::

### Command Description

Prints a list of messages with reactions within the last `# of messages`
in the current channel, showing the list of reactions and number of uses
per each reaction.

Using the `--csv` parameter instructs the bot to send a `.csv` file
containing the details of the summary to the command author.

Using the `--silent` parameter suppresses the in-channel embed output
(this only works if used with `--csv`).

If the number of messages is omitted, the bot will scan the latest 10
messages.

The maximum number of messages the bot will scan is **250**.

### Permissions Needed

| **User**: Manage Messages

### Examples

::: {.parsed-literal}
resummary resummary 20 \--csv \--silent resummary \--csv
:::

------------------------------------------------------------------------

reunique
--------

### Command Syntax

::: {.parsed-literal}
reunique \[\# of messages\] \[\--csv\] \[\--silent\]
:::

### Command Description

Prints a list of **unique users** that reacted to at least one message
within the last `number-of-messages` in the current channel.

Using the `--csv` parameter instructs the bot to send a `.csv` file
containing the details of the output to the command author. The `.csv`
file also shows the nickname of the user(s) and the number of times each
user reacted to each reaction.

Using the `--silent` parameter suppresses the in-channel embed output
(this only works if used with `--csv`).

If the number of messages is omitted, the bot will scan the latest 10
messages.

The maximum number of messages the bot will scan is **250**.

### Permissions Needed

| **User**: Manage Messages

### Examples

::: {.parsed-literal}
reunique reunique 20 \--csv \--silent reunique \--csv
:::

------------------------------------------------------------------------

recontest
---------

### Command Syntax

::: {.parsed-literal}
recontest \[\# of messages\] \[\--age (time code)\] \[\--joined (time
code)\] \[\--members (number)\]
:::

### Command Description

This function is specifically built with reaction contests in mind. Its
output is focused on highlighting reactions that are added by Discord
accounts that have been recently created, in order to perform a better
analysis of potential \"fraudulent votes\": duplicate reactions added by
newly created accounts just for the sake of increasing one\'s message\'s
reactions.

The `--age` and `--joined` parameters will define how to recognize a
suspect user:

-   `--age` defines the minimum age of the Discord account to avoid
    being flagged.
-   `--joined` defines the minimum amount of time the user needs to be
    on the server to avoid being flagged.

The `--members` parameter, on the other hand, defines the minimum number
of members needed to pass **both** checks for a message to be flagged as
having fraudulent reaction votes.

As a practical example:

::: {.parsed-literal}
recontest 50 \--age 1w \--joined 3d \--members 5
:::

would flag any messages, within the last 50 messages in the current
channel, with more than **5** (unique) members that have reacted to the
message with a Discord account that is **less than 1 week old** and that
joined the server **less than 3 days ago**.

If the number of messages is omitted, the bot will scan the latest 10
messages.

Omitting `--age` and/or `--joined` parameters will disable the
corresponding check from being relevant in recognizing fraudulent votes
(e.g. omitting `--age` will mark any account as suspect, regardless of
its actual Discord age).

Omitting the `--members` parameter will set its default value of 0,
making every message with at least 1 suspect member being flagged as
fraudulent.

Using the `--csv` parameter instructs to send 2 `.csv` files to the
command author:

1.  A .csv with the same output of resummary, showing the list of
    messages with reactions within the last `# of messages` in the
    current channel, including the list of reactions and number of uses
    per each reaction. This is further enhanced with a \"Fraudulent
    Flag\" and a \"Fraudulent Votes\" extra column.
2.  A 2nd .csv with the list of users that meet that \"Fraudulent
    Votes\" criteria, with a separate record for each message they
    reacted to (including how they reacted to the message).

Using the `--silent` parameter suppresses the in-channel embed output
(this only works if used with `--csv`).

The maximum number of messages the bot will scan is **250**.

### Permissions Needed

| **User**: Manage Messages

### Examples

::: {.parsed-literal}
recontest \--age 5d \--joined 1d recontest recontest 50 \--age 2w
\--joined 1w \--members 10 \--csv \--silent
:::
