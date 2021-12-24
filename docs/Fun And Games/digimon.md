Digimon
=======

**Digimon** (デジモン Dejimon, branded as **Digimon: Digital Monsters**,
stylized as **DIGIMON**), short for "Digital Monsters"
(デジタルモンスター Dejitaru Monsutā), is a Japanese media franchise
encompassing virtual pet toys, anime, manga, video games, films and a
trading card game. The franchise focuses on Digimon creatures, which are
monsters living in a "Digital World", a parallel universe that
originated from Earth\'s various communication networks. (Source:
[Wikipedia](https://en.wikipedia.org/wiki/Digimon))

This module allows users to obtain, collect and train their own
Digimons. The set of available Digimons is the same one that you can
find in the video game **Digimon Story: Cyber Sleuth** and its sequel,
**Digimon Story: Cyber Sleuth -- Hacker's Memory**.

!!!abstract "See also"

        I'd like to thank **Chia** (:fontawesome-brands-discord: Chia#8045) for her work in
        gathering the full list of Digimons and their respective stats into the
        [Digimon Cyber Sleuth Hacker's Memory Competitive Database (DigiDB)](http://digidb.io/).
        This module would not exist if it wasn't for her huge indirect help.

        Her: [:fontawesome-brands-discord:](https://discord.gg/ynWMccz) & [:fontawesome-brands-patreon:](https://www.patreon.com/digidb)


The current version of the game lets users:

-   Obtain one of the first 5 "Baby" (starter) Digimons with a gacha mechanism
-   Exercising your Digimons to make them gain EXP
-   Digivolving and De-Digivolving your Digimons in order to give them a new form
-   Enhancing the stats of your Digimons through specific boost items
-   Buy items (evolution items, stat boosters, inventory expansions)
    through an interactive shop menu

The following documentation will further explain some of these concepts.

~Digimon~ ~names,~ ~images,~ ~and~ ~related~ ~information~ ~are~ ~property~ ~of~ ~Akiyoshi~ ~Hongo,~ ~Bandai~ ~and~ ~Toei~ ~Animation.~

{{bot.prefix}}dgparam
-------

### Command Syntax
!!!example ""

        {{bot.prefix}}dgparam


### Command Description

Shows basic parameters about the user and the game itself.

------------------------------------------------------------------------

{{bot.prefix}}dggacha
-------

### Command Syntax
!!!example ""

        {{bot.prefix}}dggacha


### Command Description

Obtains a new random Digimon out of the starters pool. One gacha run
costs 1,000 currency.

Currently, 5 **Baby** Digimons are available in the starters pool:

-   Kuramon
-   Pabumon
-   Punimon
-   Botamon
-   Poyomon

Each one of these Digimons have a 19.8% chance of being obtained, for a
total of 99%. The last 1% is evenly split (0.2% each) on the following 5
**trophy units**:

-   Alphamon NX
-   Crusadermon NX
-   Leopardmon NX
-   Omnimon NX
-   Gallantmon NX

The NX units cannot be evolved, or obtained through evolution.

------------------------------------------------------------------------

{{bot.prefix}}dgarchive
---------

### Command Syntax
!!!example ""

        {{bot.prefix}}dgarchive


### Command Description

Shows a summary of all Digimons ever owned by the user.

------------------------------------------------------------------------

{{bot.prefix}}dginventory
-----------

### Command Syntax
!!!example ""

        {{bot.prefix}}dginv


### Command Description

Shows the current user inventory.

------------------------------------------------------------------------

{{bot.prefix}}dgshop
------

### Command Syntax
!!!example ""

        {{bot.prefix}}dgshop


### Command Description

Opens the items shop.

------------------------------------------------------------------------

{{bot.prefix}}dgdex
-----

### Command Syntax
!!!example ""

        {{bot.prefix}}dgdex [Digimon -partial- name]


### Command Description

Shows all Digimons currently owned by the user. If a name is specified,
the output will restrict the list to the corresponding Digimon(s), if
any.

Partial names are supported (e.g. "pabu" instead of "Pabumon").

------------------------------------------------------------------------

{{bot.prefix}}dglookup
--------

### Command Syntax
!!!example ""

        {{bot.prefix}}dglookup (Digimon -partial- name)


### Command Description

Shows generic info about a specific Digimon.

Partial names are supported (e.g. "pabu" instead of "Pabumon").

------------------------------------------------------------------------

{{bot.prefix}}dgechain
--------

### Command Syntax
!!!example ""

        {{bot.prefix}}dgechain (starting Digimon -partial- name) (ending Digimon -partial- name)


### Command Description

Given two **mandatory** Digimon names, this command shows the
Digivolution/Degeneration chain that is needed to go from the first
Digimon to the second one, if any.

Partial names are supported (e.g. "pabu" instead of "Pabumon").

------------------------------------------------------------------------

{{bot.prefix}}dgexercise
----------

### Command Syntax
!!!example ""

        {{bot.prefix}}dgexer (Digimon -partial- name)


### Command Description

Sends a Digimon to the Digi-Farm for an exercise session. The amount of
EXP earned depends on the amount of time that the Digimon will spend in
the farm. One exercise session costs 250 currency.

During that time, the Digimon will be unavailable for other uses.

The Digimon will receive the EXP immediately: eventual info about a
level up event will show up immediately, but you still won't be able to
"use" the Digimon until it's done exercising.

You will not receive a warning when the exercise session is done, but
you can check the time left in the Digi-Dex page for that Digimon or
using dgfarm.

You must manually retrieve a Digimon from the Digi-Farm once it's done
exercising. You must also have at least one free slot in your Digi-Dex
when you do so (sending a Digimon to the Digi-Farm temporarily frees up
one slot in your Digi-Dex).

!!!info "Note"

        The exercise session curve is based on the following criterias:
        
        - Shorter times yield more EXP per hour (2,500 EXP in 15 minutes =
            10,000 EXP per hour) but cost more currency (2,500 EXP per 250 coins
            = 10 EXP per coin).
        - Longer times yield less EXP per hour (10,500 EXP in 8 hours =
            1,312.5 EXP per hour) but cost less currency (10,500 EXP per 250
            coins = 42 EXP per coin).


------------------------------------------------------------------------

{{bot.prefix}}dgretrieve
----------

### Command Syntax
!!!example ""

        {{bot.prefix}}dgreturn (Digimon -partial- name) dgret (Digimon -partial- name)


### Command Description

Returns a Digimon to the user's Digi-Dex once it has finished
exercising in the Digi-Farm. The Digimon will wait in an "idle" state
within the farm until it's manually retrieved.

------------------------------------------------------------------------

{{bot.prefix}}dgfarm
------

### Command Syntax
!!!example ""

        {{bot.prefix}}dgfarm


### Command Description

Shows info and parameters about the user's Digi-Farm.

------------------------------------------------------------------------

{{bot.prefix}}dgdrop
------

### Command Syntax
!!!example ""

        {{bot.prefix}}dgdrop (Digimon -partial- name)


### Command Description

Sets a Digimon free, dropping it from your Digi-Dex. This action cannot
be undone.

------------------------------------------------------------------------

{{bot.prefix}}dgevolve
--------

### Command Syntax
!!!example ""

        {{bot.prefix}}dgevolve (Digimon -partial- name)


### Command Description

Digivolves a Digimon into one of its possible new forms. A Digivolution
will always require one or more evolution items, will usually have a
level requirement and may have an additional stats' requirement.

There are 2 evolution items:

-   Digivolution-Chips: these are used for "standard" evolutions.
-   Digi-Eggs: these are used to evolve a Digimon to its "Armor" form.
    Currently, there are only 3 Armor Digimons: Flamedramon, Magnamon
    and Rapidmon (Armor). Digi-Eggs cannot be bought and are only
    obtained through specific giveaways or events.

The stats requirements can be satisfied by raising the Digimon level
until its stats are compliant with the evolution requirements, or by
using Booster items (bought from the shop). Stat boosts are kept during
Digivolution/Degenerations.

The only exception to this is the **ABI** parameter. ABI is only
obtained by De-Digivolutions: upon degenerating a Digimon, you will gain
1 point of ABI per 9,900 EXP points that the Digimon has gained in that
specific form. ABI is kept during Digivolution/Degenerations.

!!!note "Example"

        Wizardmon needs 10 ABI to Digivolve into Myotismon. You can exercise
        Wizardmon (or a lower form that still has a further lower form) until it
        has gained 99,000 EXP (Lv. 63\~64), then Degenerate it to Keramon (which
        will now have 10 ABI), Digivolve it again to Wizardmon, then up to Myotismon.


------------------------------------------------------------------------

{{bot.prefix}}dgdegenerate
------------

### Command Syntax
!!!example ""

        {{bot.prefix}}dgdegen (Digimon -partial- name)


### Command Description

The opposite of Digivolutions, this command brings back a Digimon to a
lower form. The only requirement of doing so is that the lower form you
are Degenerating to must be one you have already obtained in the past.

You can check the list of Digimons you have seen in the past with
[{{bot.prefix}}dgarchive](/GiselleBot-Documentation/Fun And Games/digimon/#dgarchive).

------------------------------------------------------------------------

{{bot.prefix}}dguseitem
---------

### Command Syntax
!!!example ""

        {{bot.prefix}}dguseitem


### Command Description

Uses an item. You can select the specific item and the quantity to use
through an interactive menu.

------------------------------------------------------------------------

{{bot.prefix}}dgdropitem
----------

### Command Syntax
!!!example ""

        {{bot.prefix}}dgdropitem


### Command Description

Drops an item. You can select the specific item and the quantity to drop
through an interactive menu. This action cannot be undone.

------------------------------------------------------------------------

{{bot.prefix}}dgenhance
---------

### Command Syntax
!!!example ""

        {{bot.prefix}}dgenhance (Digimon -partial- name)


### Command Description

Uses an item (e.g. a stat booster item) on a Digimon. You can select the
specific item and the quantity to use through an interactive menu.
