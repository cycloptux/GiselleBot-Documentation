# README
GiselleBot is a Discord bot, written by Cyc (cycloptux#1543) for the Reddit Coalition (a Brave Frontier alliance of guilds).
The bot is written in Node.js and requires the [Discord.js](https://discord.js.org/) library.

## Introduction and history
Giselle was born as a "small" project to help the Brave Frontier-based Coalition handle the kind-of-complicated (and fully documented, props to NaviKing) application work-flow.
Her main goal back when she started was pinging guilds in our Discord server every once in a while and reminding them to answer to an application.

The project evolved and became quite big, to a point where she's basically handling the whole application work-flow on her own with minimum user input.

Over time, a lot of side functions were added to help with day-to-day Discord usage, logging, roles management...

## Commands and capabilities
At the time of writing this README, here's a (non-comprehensive) list of what she's capable of:

- Interact via outside users with an auto-responder that will compile an application to the Coalition.
- Format and share said application with the Mods of the Coalition, fill the docs we have on Google, forward the application to the rest of the guild management teams in the Coalition (after some input/validation from us Mods).
- Set up reminders that will bug the guilds to answer via commands.
- According to the output of this survey phase, suggest which guild should get the applicant using an algorithm that takes into account a lot of parameters - fairness checks (this is one of the latest module and it's working great).
- Interact with the original applicant via DMs to let him/her know about the result of that application.
- Surround all these tasks with documental access/updates, administrative functions, etc.
- Manage internal transfers in a similar fashion as the new application work-flow: submission of a transfer request via DM, reminders, documents, etc.
- Parse for user-sent notifications about the Coalition (guild level up/perk upgrade, user joining/leaving a guild, etc.), reading messages and turning those into actions (update docs, change roles, etc.). We're not talking about commands here, just plain text that follows a general, non-strict template.

Plus, there are a few side modules:

- Lookup info about Discord users Giselle knows (profile, last login, etc.).
- Public reminders for contribution resets, plus a few specific internal reminders.
- A reminder engine (reverse engineered from LinBot's) which still uses her non-embedded reminders.
- A custom messages db engine (again, similar to LinBot's ../... module).
- An utility function to print users' reactions to a message in a copy-paste friendly message.
- An additional custom parser - management functions for specific needs (Brave Nexus helper stuff).

All these modules are documented, help files are kept up-to-date, etc. A permission system is embedded in her code that handles which servers and roles/users are enabled to use each one of the above commands.
Behind the scenes, GiselleBot prints logs in her console and backups her databases multiple times a day, just in case something goes wrong.

## Technical "need to know"s
GiselleBot is written in **Node.js** and makes use of very few external libs. The local database uses a light JSON format to avoid external engines to be set up.
Her code is currently hosted in a private Git repository. Sensitive stuff (keys, tokens, Google URLs, ...) are private and are saved locally in my development workspaces and in its final VPS.

### First setup
Work In Progress.
