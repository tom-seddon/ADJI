# Advanced Digital Joystick Interface ROM

Support ROM for Retro Hardware's Advanced Digital Joystick Interface
cartridge for the Acorn Electron/BBC Master 128.

Based in part on the Slogger Electron Expansion 2.02 ROM:
https://github.com/tom-seddon/SloggerElectronExpansion

**Extremely WIP**

**Only actually supports Master 128 at the moment**

# Using the ADJI

Requires Electron or Master 128.

Connect the joystick interface to one of the cartridge slots, and plug
a 9-pin joystick into the 9-pin plug.

Load the ROM into sideways RAM. In theory it should run from the
socket on the ADJI cartridge! It doesn't matter which bank it's in.

## `*JTEST` - test the joystick

To test it out, use `*JTEST`. This takes one parameter: the joystick
number, 1-4, corresponding to the DIP switches on the device.

| Number | Address |
| --- | --- |
| 1 | &FCC0 |
| 2 | &FCD0 |
| 3 | &FCE0 |
| 4 | &FCF0 |

The joystick test screen reads the joystick, and shows on screen which
directions are being pressed.

## `*JJOY` - use the digital joystick as an analogue joystick

`*JJOY` hooks into the analogue joystick processing, so the digital
joystick appears to be an analogue joystick. Use this to play games
with existing joystick support.

It takes two parameters:

1. Joystick number, 1-4, as above
2. Overlay address, or `X` to use extended vectors

The Acorn-approved way for the joystick ROM to operate is to hook into
things using the extended vectors. Many games overwrite the extended
vectors, however, so this method may result in crashes or hangs.

As an alternative, the joystick ROM can hook into things using a
20-byte overlay routine stored in main RAM. The recommended standard
address is &150, an area of the CPU stack that is typically unused,
but (with caution) any address from 0 to &7FE0 can be used.

If specifying an address in hex, precede with `&`, same as BASIC.

Once `*JJOY` is active, `ADVAL`/OSBYTE &80 will start to return
digital joystick info:

- `ADVAL(0)` reports the digital fire button
- `ADVAL(1)` reports the digital left/right axis
- `ADVAL(2)` reports the digital up/down axis

## `*JOFF` - switch digital joystick support off

No parameters required.

## `*JKSETUP` - use the digital joystick as keys

`*JKSETUP` hooks into the keyboard processing, so the digital joystick
appears to be particular keys on the keyboard. Use this to play games
that don't support joysticks.

`*JKSETUP` takes two parameters, same as `*JJOY`.

Press a key when prompted - each key is the one corresponding to that
axis or button.

Once `*JKSETUP` is active, the joystick will affect the following
calls:

- OSBYTE &79/KEYV
- OSBYTE &7A
- `INKEY`/OSBYTE &81

## `*JKEYS` - use the digital joystick as keys

If you know the negative INKEY values of the keys, you can use
`*JKEYS` to configure the joystick without requiring any input.

`*JKEYS` takes 7 parameters, with all keys specified as negative INKEY
values:

1. Joystick number, 1-4, as above
2. Key for up
3. Key for down
4. Key for left
5. Key for right
6. Key for fire
7. Overlay address or `X', as above

`*JKSETUP` will print out a suitable `*JKEYS` command line, which you
can later use to set up the same keys again.

Negative INKEY values are as follows:

| Key | Dec | Hex | Key | Dec | Hex | Key | Dec | Hex |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | -66 | &BE | @ | -72 | &B8 | NUM 0 | -107 | &95 |
| B | -101 | &9B | [ | -57 | &C7 | NUM 1 | -108 | &94 |
| C | -83 | &AD | \ | -121 | &87 | NUM 2 | -125 | &83 |
| D | -51 | &CD | ] | -89 | &A7 | NUM 3 | -109 | &93 |
| E | -35 | &DD | ^ | -25 | &E7 | NUM 4 | -123 | &85 |
| F | -68 | &BC | _ | -41 | &D7 | NUM 5 | -124 | &84 |
| G | -84 | &AC | TAB | -97 | &9F | NUM 6 | -27 | &E5 |
| H | -85 | &AB | SHIFT LOCK | -81 | &AF | NUM 7 | -28 | &E4 |
| I | -38 | &DA | f0 | -33 | &DF | NUM 8 | -43 | &D5 |
| J | -70 | &BA | f1 | -114 | &8E | NUM 9 | -44 | &D4 |
| K | -71 | &B9 | f2 | -115 | &8D | NUM + | -59 | &C5 |
| L | -87 | &A9 | f3 | -116 | &8C | NUM - | -60 | &C4 |
| M | -102 | &9A | f4 | -21 | &EB | NUM / | -75 | &B5 |
| N | -86 | &AA | f5 | -117 | &8B | NUM # | -91 | &A5 |
| O | -55 | &C9 | f6 | -118 | &8A | NUM * | -92 | &A4 |
| P | -56 | &C8 | f7 | -23 | &E9 | NUM , | -93 | &A3 |
| Q | -17 | &EF | f8 | -119 | &89 | NUM RETURN | -61 | &C3 |
| R | -52 | &CC | f9 | -120 | &88 | NUM DELETE | -76 | &B4 |
| S | -82 | &AE |||| NUM . | -77 | &B3 |
| T | -36 | &DC |
| U | -54 | &CA |
| V | -100 | &9C |
| W | -34 | &DE |
| X | -67 | &BD |
| Y | -69 | &BB |
| Z | -98 | &9E |
| 0 | -40 | &D8 |
| 1 | -49 | &CF |
| 2 | -50 | &CE |
| 3 | -18 | &EE |
| 4 | -19 | &ED |
| 5 | -20 | &EC |
| 6 | -53 | &CB |
| 7 | -37 | &DB |
| 8 | -22 | &EA |
| 9 | -39 | &D9 |
| - | -24 | &E8 |
| ; | -88 | &A8 |
| : | -73 | &B7 |
| , | -103 | &99 |
| . | -104 | &98 |
| / | -105 | &97 |
| SPACE | -99 | &9D |
| ESCAPE | -113 | &8F |
| DELETE | -90 | &A6 |
| RETURN | -74 | &B6 |
| CURSOR UP | -58 | &C6 |
| CURSOR DOWN | -42 | &D6 |
| CURSOR LEFT | -26 | &E6 |
| CURSOR RIGHT | -122 | &86 |
| COPY | -106 | &96 |
| SHIFT | -1 | &FF |
| CTRL | -2 | &FE |
| CAPS LOCK | -65 | &BF |

# Limitations/bugs

- `*JKSETUP` doesn't examine the address/overlay parameter until after
  you've pressed the keys. So if you enter something invalid, you
  won't get the error immediately
  
- Joystick keys don't affect OSRDCH, so you can use them to press keys
  at the BASIC prompt, or when using `INPUT`, etc.
  
- `*JJOY` effectively disables both analogue joysticks, even though it
  could pass through to one of them and it wouldn't interfere

# Technical info

## Master 128

The ROM uses 1 page of HAZEL to store its data.

