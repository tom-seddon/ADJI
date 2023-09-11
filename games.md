A list of games that have been tested with the ADJI ROM.

`*JKEYS` is the suggested command line for the game, probably using
the overlay routine. `X?` indicates whether the game will also work
with `*JKEYS ... X`.

`*JJOY` is the suggested command line for the game, assuming the game
supports joysticks. Again, `X?` indicates whether the game will also
work with `*JJOY ... X`.

# Electron

Working:

| Game |`*JKEYS`|`X`?|`*JJOY`|`X`?|Notes|
| --- | --- | --- | --- | --- | --- |
|Airlift|`*JKEYS 1 &B7 &97 &9E &BD &B6 &B6 &150`|y|`*JJOY 1 &150`|y||
| Alien Dropout|`*JKEYS 1 &B7 &97 &9E &BD &A6 &A6 &150`|y|-|-||
|Alphatron|`*JKEYS 1 &B7 &97 &9E &BD &B6 &B6 &150`|y|-|-|needs hack|
|Ballistix|`*JKEYS 1 &DE &AE &9E &BD &EF &EF &880`|n|-|-||
|Blast!|`*JKEYS 1 &B7 &97 &9E &BD &B6 &FF &880`|n|-|-||
|Bug Blaster|`*JKEYS 1 &B7 &97 &9E &BD &B6 &B6 &150`|n|-|-||
|Caveman Capers|`*JKEYS 1 &B7 &97 &9E &BD &B6 &B6 &150`|n|-|-||
|Centibug|`*JKEYS 1 &B7 &97 &9E &BD &A6 &A6 &150`|y|-|-||
|Chuckie Egg|`*JKEYS 1 &BE &9E &99 &98 &9D &9D &150`|n|-|-||
|Commando|`*JKEYS 1 &B7 &97 &9E &BD &B6 &FF &150`|y|`*JJOY 1 &150`|y|how do you grenade with joysticks?|
|Cops n' Robbers|`*JKEYS 1 &B7 &97 &9E &BD &9D &9D &150`|n|-|-||
|Cosmic Camouflage|`*JKEYS ... &880`|y|-|-|lots of keys! - DIY|

Not working:

| Game |`*JKEYS`|`X`?|`*JJOY`|`X`?|Notes|
| --- | --- | --- | --- | --- | --- |
|Boffins 2|`*JKEYS 1 &A8 &98 &9E &BD &B6 &B6 &150`|y|-|-|slow movement - need to debug this|
|Bonecruncher|n|n|-|-|need to debug|
|Camelot|`*JKEYS 1 &B7 &97 &9E &BD &B6 &9D &880`|?|-|-|ignored! need to debug|
|Citadel||||no room for overlay :(|

# Master
