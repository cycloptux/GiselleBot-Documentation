Send
====

This module allows authorized users to send messages through the bot,
and/or editing previously sent messages.

msgsend
-------

### Command Syntax

::: {.parsed-literal}
msgsend (channel id/mention) \[message to send\]
:::

### Command Description

Sends a message to a channel in the current server.

You can use embed json from <https://eb.nadeko.bot/> instead of a
regular text, if you want the message to be embedded.

You can attach a file/image to the command to have send the file/image
as attachment on the target message.

### Examples

::: {.parsed-literal}
msgsend \#this-channel Hello world! msgsend \#that-channel {
\"description\": \"Hello world!\" }
:::

------------------------------------------------------------------------

msgedit
-------

### Command Syntax

::: {.parsed-literal}
msgedit (channel id/mention) (message id) (new message content)
:::

### Command Description

Edits a previously sent message.

You can use embed json from <https://eb.nadeko.bot/> instead of a
regular text, if you want the message to be embedded.

You cannot edit a message attachment.

### Examples

::: {.parsed-literal}
msgedit 123456789098765432 Hello world! I\'m alive!
:::

------------------------------------------------------------------------

webhooksend
-----------

### Command Syntax

::: {.parsed-literal}
webhooksend (webhook name) (message to send)
:::

### Command Description

Sends a message to a webhook **in the current channel**. If the webhook
name is made by two or more words, please surround the name with by
double quotes.

This command is meant to test the functionality of a Discord webhook.
For this reason, the feature is limited to sending a message to a
webhook that is set within the channel from where the command is run.

You can use embed json from <https://eb.nadeko.bot/> instead of a
regular text, if you want the message to be embedded.

You can attach a file/image to the command to have send the file/image
as attachment on the target message.

### Permissions Needed

| **User**: Manage Webhooks
| **Bot**: Manage Webhooks

### Examples

::: {.parsed-literal}
webhooksend \"Spidey Bot\" Hello world! webhooksend News {
\"description\": \"Hello world!\" }
:::
