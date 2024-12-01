A list of games that have been tested with the ADJI ROM.

`*JKEYS` is the suggested command line for the game, probably using
the overlay routine. `X?` indicates whether the game will also work
with `*JKEYS ... X`.

`*JJOY` is the suggested command line for the game, assuming the game
supports joysticks. Again, `X?` indicates whether the game will also
work with `*JJOY ... X`.

For games that only need left/right or up/down, but not both, I've
assigned dummy keys to the unused axis.

# Electron

## Working

Compatible with one or both of `*JKEYS` and `*JJOY`.

| Game |`*JKEYS`|`X`?|`*JJOY`|`X`?|Notes|
| --- | --- | --- | --- | --- | --- |
| Alien Dropout|`*JKEYS 1 &B7 &97 &9E &BD &A6 &A6 &150`|y|-|-||
|3D Dotty|`*JKEYS 1 &B7 &97 &9E &BD &B6 &B6 &150`|
|Airlift|`*JKEYS 1 &B7 &97 &9E &BD &B6 &B6 &150`|y|`*JJOY 1 &150`|y||
|Alien Dropout |`*JKEYS 1 &B6 &B6 &9E &BD &A6 &A6 &150`
|Anarchy Zone |`*JKEYS 1 &B6 &B6 &9E &BD &A6 &A6 &150`
|Arcadians |`*JKEYS 1 &96 &96 &FE &BE &B6 &B6 &150`
|Astro Plumber |`*JKEYS 1 &B7 &97 &9E &BD &FF &B6 &150`
|Ballistix|`*JKEYS 1 &DE &AE &9E &BD &EF &EF &880`|n|-|-||
|Baloon Buster |`*JKEYS 1 &96 &96 &9E &BE &B6 &B6 &150`
|Blast!|`*JKEYS 1 &B7 &97 &9E &BD &B6 &FF &880`|n|-|-||
|Blitzkrieg|||||set interface address to &FCC0, then say Y when it asks if you have a First Byte interface|
|Boffins 2 |`*JKEYS 1 &EF &EF &9E &BD &B6 &B6 &150`||||https://github.com/tom-seddon/ADJI/issues/25|
|Boxer |`*JKEYS 1 &B7 &97 &9E &BD &B6 &FF &150`
|Breakthrough |`*JKEYS 1 &EF &EF &9E &BD &B6 &FF &150`
|Bug Blaster|`*JKEYS 1 &B7 &97 &9E &BD &B6 &B6 &150`|n|-|-||
|BugBlaster |`*JKEYS 1 &B7 &97 &9E &BD &B6 &B6 &150`
|Bumble Bee |`*JKEYS 1 &B7 &97 &9E &BD &B6 &9D &150`
|Caveman Capers|`*JKEYS 1 &B7 &97 &9E &BD &B6 &B6 &150`|n|-|-||
|Centibug|`*JKEYS 1 &B7 &97 &9E &BD &A6 &A6 &150`|y|-|-||
|Chuckie Egg|`*JKEYS 1 &BE &9E &99 &98 &9D &9D &150`|n|-|-||
|Commando|`*JKEYS 1 &B7 &97 &9E &BD &B6 &FF &150`|y|`*JJOY 1 &150`|y|how do you grenade with joysticks?|
|Cops n' Robbers|`*JKEYS 1 &B7 &97 &9E &BD &9D &9D &150`|n|-|-||
|Cosmic Camouflage|`*JKEYS ... &880`|y|-|-|lots of keys! - DIY|
|Crack-out|`*JKEYS 1 &B7 &97 &9E &BD &9D &FF &150`|n|`*JJOY 1 &150`|n|joystick works poorly. Also claims to support joystick via &FCC0, and that doesn't work well either|
|Cybertron|`*JKEYS 1 &BE &9E &99 &98 &9A &9A &150`|n|`*JJOY 1 &150`|n||
|Cyclon Attack |`*JKEYS 1 &BE &9E &99 &98 &9D &9D &150`|||| Choose 3 to select Joystick from menu and it runs ok
|Danger UXB |`*JKEYS 1 &B7 &97 &9E &BD &AE &CD &150`
|Electron Invaders |`*JKEYS 1 &EF &EF &9E &BD &FF &FF &150`|y
|Frak|Interface position 1||||Interface position 1 then Choose Y when prompted for First Byte joystick
|Firebug |`*JKEYS 1 &B7 &97 &9E &BD &FF &FF &150`
|Frenzy |`*JKEYS 1 &B7 &97 &9E &BD &B6 &9D &150`
|GalaForce |`*JKEYS 1 &B7 &97 &9E &BD &B6 &B6 &150`
|Hard Hat Harry |`*JKEYS 1 &B7 &97 &9E &BD &B6 &B6 &150`
|Hobgoblin |`*JKEYS 1 &EF &EF &9E &BD &FF &9D &150`
|Hobgoblin 2 |`*JKEYS 1 &EF &EF &9E &BD &FF &9D &150`
|Hopper |`*JKEYS 1 &B7 &97 &9E &BD &EF &EF &150`||||https://github.com/tom-seddon/ADJI/issues/48
|Jungle Journey |`*JKEYS 1 &B7 &97 &9E &BD &B6 &B6 &150`
|Killer Gorilla |`*JKEYS 1 &B7 &97 &9E &BD &B6 &B6 &150`
|Magic Mushrooms |`*JKEYS 1 &B7 &97 &9E &BD &B6 &B6 &150`
|Meteors |`*JKEYS 1 &FF &FF &9E &BD &B6 &9D &150`
|Monsters |`*JKEYS 1 &B7 &97 &9E &BD &BC &CD &150`
|Repton |`*JKEYS 1 &B7 &97 &9E &BD &B6 &B6 &150`
|Repton 2 |`*JKEYS 1 &B7 &97 &9E &BD &B6 &B6 &150`
|Repton 3 |`*JKEYS 1 &B7 &97 &9E &BD &B6 &B6 &150`
|Smash and Grab |`*JKEYS 1 &B7 &97 &9E &BD &B6 &B6 &150`
|Snapper |`*JKEYS 1 &B7 &97 &9E &BD &B6 &B6 &150`||`*JJOY 1 &150`
|Space Alien meets Bugeyes |`*JKEYS 1 &B7 &97 &9E &BD &B6 &B6 &150`
|Spectapede||| `*JJOY 1 &150`
|Stock Car |`*JKEYS 1 &EF &EF &9E &BD &FF &FF &150`
|Swoop |`*JKEYS 1 &B7 &97 &9E &BD &FF &FF &150`
|Tetris |`*JKEYS 1 &9D &BE &99 &98 &BD &9E &150`
|The Mine |`*JKEYS 1 &B7 &97 &9E &BD &B6 &B6 &150` 
|Mr.Wiz |`*JKEYS 1 &B7 &97 &9E &BD &9D &9D &150`
|Percy Penguin |`*JKEYS 1 &B7 &97 &9E &BD &B6 &B6 &150`

## Requires modification

Can be modified to be compatible with one or both of `*JKEYS` and
`*JJOY`.

| Game |`*JKEYS`|`X`?|`*JJOY`|`X`?|Notes|
| --- | --- | --- | --- | --- | --- |
|Alphatron|`*JKEYS 1 &B7 &97 &9E &BD &B6 &B6 &150`|y|-|-|Remove `FORX=672 TO 687:?X=0:NEXT` from `ALPHA-3`|

## Not compatible

Not compatible with either `*JKEYS` or `*JJOY`.

| Game | Explanation |
| --- | --- |

## Not working

Doesn't behave properly, but for reasons unknown. Might not be
compatible, might just need modification.

| Game | Issue |
| --- | --- |
| Boffins 2| https://github.com/tom-seddon/ADJI/issues/25|
| Bonecruncher| https://github.com/tom-seddon/ADJI/issues/26|
| Camelot| https://github.com/tom-seddon/ADJI/issues/27|
| Citadel| https://github.com/tom-seddon/ADJI/issues/28|
| Croaker| https://github.com/tom-seddon/ADJI/issues/29|
| Cyborg Warriors|https://github.com/tom-seddon/ADJI/issues/34|
| Firetrack|https://github.com/tom-seddon/ADJI/issues/46|
| Galaforce 2|https://github.com/tom-seddon/ADJI/issues/47|

# Master

## Working

| Game |`*JKEYS`|`X`?|`*JJOY`|`X`?|Notes|
| --- | --- | --- | --- | --- | --- |
| Tenebra | *JKEYS 1 &EF &BE &C9 &C8 &9D &B6 X | Y | N/A | N | No native joystick option |
| YieArKungFu | *JKEYS 1 &B7 &97 &9E &BD &B6 &FF X | Y | N/A | N/A | No native joystick option, the game itself is not fully compatible with the Master |
| YieArKungFu II | *JKEYS 1 &B7 &97 &9E &BD &B6 &FF &0150 | N | N/A | N/A | No native joystick option, the game itself is not fully compatible with the Master |
| Felix in the Factory | *JKEYS 1 &B7 &97 &9E &BD &B6 &9F &0150 | N | N/A | N/A | No native joystick option, the game itself is not fully compatible with the Master |
| Nubium | *JKEYS 1 &B7 &97 &9E &BD &B6 &9D X | Y | N/A | N/A | No native joystick option |
| Nubium II | *JKEYS 1 &B7 &97 &9E &BD &B6 &9D X | Y | N/A | N/A | No native joystick option |
| Repton 3 Redux | N/A | N/A | *JJOY 1 X | Y |  |
| Repton The Lost Realms | N/A | N/A | *JJOY 1 X | Y |  |
| BubbleBobble | *JKEYS 1 &B7 &97 &DE &DD &9F &FE X | Y | N/A | N/A | No native joystick option |
| ChuckieEgg Professional Edition | N/A | N/A | *JJOY 1 &0880 | N | Has native joystick but needs overlay at &880 |
| Hobgobblin | *JKEYS 1 &B7 &97 &9E &BD &9D &0880 | N | N/A | N/A | No native joystick option |
| Hobgobblin II | *JKEYS  1 &B7 &97 &9E &BD &9D &0880 | N | N/A | N/A | No native joystick option |
| Swoop | N/A | N/A | *JJOY 1 &150 | N | |
| Cybertron Mission | N/A | N/A | *JJOY 1 &150 | N | |
| Overdrive | *JKEYS 1 ? ? ? ? &150 | N | N/A | N/A | Use standard keys for game | 
| Repton | *JKEYS 1 ? ? ? ? &150 | N | N/A | N/A | Use standard keys for game | 
| Repton 2 | *JKEYS 1 ? ? ? ? &150 | N | N/A | N/A | Use standard keys for game | 
| Repton 3 | N/A | N/A | *JJOY 1 X | Y | |
| Galaforce | N/A | N/A | *JJOY 1 &150 | N | |
| Vindaloo | *JKEYS 1 ? ? ? ? &380 | N | N/A | N/A | Use standard keys for game | 
| Imogen | *JKEYS 1 ? ? ? ? &150 | N | N/A | N/A | Use standard keys for game | 
| Starquake | N/A | N/A | *JJOY 1 &880 | N | Select Joytstick option | 
| 3D Dotty | N/A | N/A | *JJOY 1 &150 | N | | 
| Arkanoid | *JKEYS 1 ? ? ? ? &380 | N | N/A | N/A | Use standard keys for game | 
| E-Type | N/A | N/A | *JJOY 1 X | Y | |
| Virtigo | N/A | N/A | *JJOY 1 X | Y | |
| Nevyron | *JKEYS 1 ? ? ? ? ? ? X | Y | N/A | N/A | Use standard keys for game |
| Morriss Minor | *JKEYS 1 ? ? ? ? ? ? X | Y | N/A | N/A | Use standard keys for game |
| Manic Mansion | *JKEYS 1 ? ? ? ? ? ? X | Y | N/A | N/A | Use standard keys for game |
| Python | *JKEYS 1 ? ? ? ? ? ? X | Y | N/A | N/A | Use standard keys for game |
| Starport | N/A | N/A | *JJOY 1 &380 | N | Select Joytstick option | 
| Killer Gorilla 2 | N/A | N/A | *JJOY 1 &150 | N | | 
| Hunchback | N/A | N/A | *JJOY 1 &150 | N | | 
| Killer Gorilla | N/A | N/A | *JJOY 1 &150 | N | | 
| Prince of Persia | ? | ? | ? | ? | Does work, but don't have a record of the command line - see https://github.com/tom-seddon/ADJI/issues/45 |

## Requires modification

| Game |`*JKEYS`|`X`?|`*JJOY`|`X`?|Notes|
| --- | --- | --- | --- | --- | --- |

## Not compatible

| Game | Reason |
| --- | --- |
| Astro Blaster | Accesses hardware directly |
| White Light | Accesses hardware directly |

## Not working

| Game | Issue | Notes |
| --- | --- | --- |
| Plan B2 | https://github.com/tom-seddon/ADJI/issues/30 |
| Electrobots | |
| Mr EE | | This game has glitches on master anyway, but JKEYS and JJOY only have partial success |
| Strykers Run | | Hangs on menu screen |
| Electrobots Going Underground | | Accesses hardware directly? |
| Soko-ban | | | 
| Night Ninja | | | 
| Quak NULA Version | | |
| Nightshade | | |
| Thrust | | |
| Kixx | | Responded to fire button but nothinge else |
| Airwork | | Varying results but never fully |
| Uridium | | Could not get off title page |
| Spellbinder | | |
| OmegaOrb | | |
| Firetrack | | Though seems to have some hidden hooks for other joysticks, worth looking into, search for 'DEVICE' http://www.level7.org.uk/miscellany/firetrack-disassembly.txt |
| Pipeline | | |
| Infinity | | |
| Xen | | |
| SpaceInvaders (TrickySoft) | | |
| Pacman (TrickySoft) | | |
| Ballot | | |
| Pitfall | | |
| New Manic Minor | | |
| Defender | | |
| Intertia | | |
