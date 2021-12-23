Permissions System 
==================

As soon as you invite the bot to your server, a few modules will be
immediately available to all of your members. The restricted modules, on
the other hand, will only be available to **server managers** (users
with \"Manage Server\" permissions).

This module lets server managers authorize server members to use any of
the bot\'s modules, on a module basis.

Each module can be enabled for a list of roles and/or individual users,
so that authorized members will immediately have access to all of the
commands contained in said module. Discord permissions checks (e.g.
\"Manage Messages\") will still apply and take precedence, where
applicable. The list of Discord permissions needed to run each command
is written below each command within this documentation.

Modules can also be **completely disabled** within a server, which means
not even server managers will be able to use them unless the module is
re-enabled (see `permtogglemod`{.interpreted-text role="ref"}).

**Before** role permissions are checked, another layer of permissions
are checked **for non-manager members**: channel overrides. Each module
can be locked to be only run **within** a specified set of channels
(**whitelist** mode) or **outside** a specified set of channels
(**blacklist** mode). See `channel-overrides`{.interpreted-text
role="ref"}.

::: {.note}
::: {.title}
Note
:::

A small subset of commands ignores these limitations and can **always**
be run by everyone in the server, as long as the whole module isn\'t
disabled. These commands have a dedicated way of setting their
permissions, which is usually specified in the dedicated module page.
This particular set contains the following commands:
`verbose`{.interpreted-text role="ref"}, `emojisubmit`{.interpreted-text
role="ref"}, `bid`{.interpreted-text role="ref"},
`listrules`{.interpreted-text role="ref"}, `submit`{.interpreted-text
role="ref"}, `lsar`{.interpreted-text role="ref"},
`iam`{.interpreted-text role="ref"} and `iamnot`{.interpreted-text
role="ref"}.
:::

------------------------------------------------------------------------

Default Module Permissions
--------------------------

Here\'s the list of modules that are automatically enabled for everyone
as soon as the bot joins a server and those that are locked to server
managers only. Internal module permissions and in-Discord permissions
checks (e.g. \"Manage Messages\") still apply.

### Available to everyone

-   alarm
-   azurlane
-   currency
-   digimon
-   games
-   help
-   mahjongsoul
-   miscellaneous
-   music
-   raidroom
-   reactions
-   scheduler
-   social
-   trivia
-   twitch
-   util
-   youtube

------------------------------------------------------------------------

Permissions Debugging
---------------------

### verbose

#### Command Syntax

::: {.parsed-literal}
verbose
:::

#### Command Description

Toggles **verbose mode** for the **current user** in the **current
server**.

Users in verbose mode will have send a Direct Message to them whenever
one of their commands is rejected silently for a permissions issue.

In addition, users incorrectly typing a command may receive a DM with a
suggestion of a correct command they actually have access to (e.g.
typing bang as moderator will suggest ban, while typing the same
incorrect command as normal user will suggest urban).

The output of verbose mode is **always sent via DM**, hence it can be
activated on a user\'s basis on each specific server without messing
with the server\'s activities.

::: {.note}
::: {.title}
Note
:::

This command is always available to everyone.
:::

------------------------------------------------------------------------

Roles and Users Permissions
---------------------------

### permshow

#### Command Syntax

::: {.parsed-literal}
pes
:::

#### Command Description

Shows a summary of all the modules that are available within the current
Discord server, and the corresponding permissions.

------------------------------------------------------------------------

### permshowmod

#### Command Syntax

::: {.parsed-literal}
pesm (module name)
:::

#### Command Description

Shows a detailed view of the permissions (users, roles, channel
overrides) for a single module.

#### Examples

::: {.parsed-literal}
pesm moderation
:::

------------------------------------------------------------------------

### permenablemod

#### Command Syntax

::: {.parsed-literal}
peem (module name) (role and/or user id(s)/mention(s)/q\_name(s))
:::

#### Command Description

Enable the selected module for the specified users and/or groups. The
bot will seamlessly understand if the entity you are using is a user or
a role.

#### Examples

::: {.parsed-literal}
peem moderation \"Discord Moderators\" peem administration \@Staff
:::

------------------------------------------------------------------------

### permdisablemod

#### Command Syntax

::: {.parsed-literal}
pedm (module name) (role and/or user id(s)/mention(s)/q\_name(s))
:::

#### Command Description

Disable the selected module for the specified users and/or groups. The
bot will seamlessly understand if the entity you are using is a user or
a role.

#### Examples

::: {.parsed-literal}
pedm moderation \"Not Discord Moderators\" pedm administration \@Lil
Staff
:::

------------------------------------------------------------------------

### permtogglemod

#### Command Syntax

::: {.parsed-literal}
petm (module name)
:::

#### Command Description

Toggles the whole module within the current server.

Completely disabling a module will render it unusable by anyone,
including administrators and managers. The module will virtually
disappear from the server until re-enabled.

#### Examples

::: {.parsed-literal}
petm alarm
:::

------------------------------------------------------------------------

Channel Overrides
-----------------

### chanpermtoggle

#### Command Syntax

::: {.parsed-literal}
cpt (module name) (channel id(s)/mention(s)/q\_name(s))
:::

#### Command Description

Toggles the presence of one or more channels on the override list for
the selected module. See below for more details.

**Blacklist** mode will make any channel that is added with the above
command **not** to show the level up message, while the rest of the
channels will show the in-channel level up message.

**Whitelist** mode will only make the in-channel level up message appear
in the selected channels.

#### Examples

::: {.parsed-literal}
cpt games \#spam \#games
:::

------------------------------------------------------------------------

### chanpermtogglemode

#### Command Syntax

::: {.parsed-literal}
cptm (module name)
:::

#### Command Description

Toggles override list mode for the selected module:

**Blacklist** mode will make any command that is run in a channel on the
override list **not** to work. This is the default mode, hence enabling
the module on all channels if no overrides are specified.

**Whitelist** mode will only make the command work in the selected
channels.

#### Examples

::: {.parsed-literal}
cptm games
:::
