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
|Airlift|`*JKEYS 1 &B7 &97 &9E &BD &B6 &B6 &150`|y|`*JJOY 1 &150`|y||
| Alien Dropout|`*JKEYS 1 &B7 &97 &9E &BD &A6 &A6 &150`|y|-|-||
|Ballistix|`*JKEYS 1 &DE &AE &9E &BD &EF &EF &880`|n|-|-||
|Blast!|`*JKEYS 1 &B7 &97 &9E &BD &B6 &FF &880`|n|-|-||
|Blitzkrieg|||||set interface address to &FCC0, then say Y when it asks if you have a First Byte interface|
|Bug Blaster|`*JKEYS 1 &B7 &97 &9E &BD &B6 &B6 &150`|n|-|-||
|Caveman Capers|`*JKEYS 1 &B7 &97 &9E &BD &B6 &B6 &150`|n|-|-||
|Centibug|`*JKEYS 1 &B7 &97 &9E &BD &A6 &A6 &150`|y|-|-||
|Chuckie Egg|`*JKEYS 1 &BE &9E &99 &98 &9D &9D &150`|n|-|-||
|Commando|`*JKEYS 1 &B7 &97 &9E &BD &B6 &FF &150`|y|`*JJOY 1 &150`|y|how do you grenade with joysticks?|
|Cops n' Robbers|`*JKEYS 1 &B7 &97 &9E &BD &9D &9D &150`|n|-|-||
|Cosmic Camouflage|`*JKEYS ... &880`|y|-|-|lots of keys! - DIY|
|Crack-out|`*JKEYS 1 &B7 &97 &9E &BD &9D &FF &150`|n|`*JJOY 1 &150`|n|joystick works poorly. Also claims to support joystick via &FCC0, and that doesn't work well either|
|Cybertron|`*JKEYS 1 &8E &9E &99 &98 &9A &9A &150`|n|`*JJOY 1 &150`|n||

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


# Master

## Working

| Game |`*JKEYS`|`X`?|`*JJOY`|`X`?|Notes|
| --- | --- | --- | --- | --- | --- |

## Requires modification

| Game |`*JKEYS`|`X`?|`*JJOY`|`X`?|Notes|
| --- | --- | --- | --- | --- | --- |

## Not compatible

| Game | Reason |
| --- | --- |
| Astro Blaster | Accesses hardware directly |
| Prince of Persia | Uses all the memory |
| White Light | Accesses hardware directly |

## Not working

| Game | Issue |
| --- | --- |
| Plan B2 | https://github.com/tom-seddon/ADJI/issues/30 |
