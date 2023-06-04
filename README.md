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

## `*JSETUP` - set up the joystick

**WIP instructions**

You'll be prompted for the following:

`Joystick no (1/2/3/4)?` - enter the joystick number.

`Joystick/Keys (J/K)?` - press `J` to have the joystick behave as an
analogue joystick, or `K` to have it translated into keypresses for
games.

If behaving as an analogue joystick, it behaves as if it's the first
analogue joystick, and its state can be read with `ADVAL` or OSBYTE
&80:

- `ADVAL(0)` reports the digital fire button
- `ADVAL(1)` reports the digital left/right axis
- `ADVAL(2)` reports the digital up/down axis

If behaving as keys, it hooks into the processing of `INKEY` and
OSBYTE &81 - the goal being to support its use with games. The
joystick can't be used for ordinary text input.

`Press UP:`, `Press DOWN:`, `Press LEFT:`, `Press RIGHT:`, `Press
FIRE:` - if you opted for keys mode, you'll be prompted for the key that each joystick action should correspond to.

`Xvector/Overlay (X/O)?` - pick the method the ROM uses to hook into
the keyboard and joystick processing.

`Xvector` uses the extended vectors, which would be the Acorn-approved
method, but many games overwrite the relevant OS workspace and so you
may experience crashes or hangs. 

`Overlay` installs a short (max 20 bytes) routine somewhere in RAM to
handle the hooking. There's no best place for this, so you'll be
prompted for an address! The default of &150, which will be used if
you just press Return when prompted, should be good for many games.

If providing an address in hex, precede with `&`, as per BASIC.

Once the questions are over, `*JSETUP` will install the hooks and
finish. Last thing it does is print a `*JKEYS` or `*JJOY` command
line, that you can note down and use later to set up the same settings
non-interactively (e.g., from `!BOOT` or a loader program).

## `*JOFF` - switch digital joystick support off

No parameters required.

## `*JJOY` - use the digital joystick as an analogue joystick

`*JJOY` takes 2 parameters:

1. Joystick number, 1-4, as per `*JTEST`
2. Overlay address (precede with `&` if in hex), or `X` to use
   extended vectors

## `*JKEYS` - use the digital joystick as keys

`*JKEYS` takes 7 parameters, with all keys specified as negative INKEY
values:

1. Joystick number, 1-4, as above
2. Key for up
3. Key for down
4. Key for left
5. Key for right
6. Key for fire
7. Overlay address or `X', as above

Easiest thing to do is use `*JSETUP`, which will prompt you for the
keys and print a command line you can use again.

Negative INKEY values are as follows. Keys common to all systems:

| Key | Dec | Hex || Key | Dec | Hex || Key | Dec | Hex |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | -66 | &BE || S | -82 | &AE || - | -24 | &E8 |
| B | -101 | &9B || T | -36 | &DC || ; | -88 | &A8 |
| C | -83 | &AD || U | -54 | &CA || : | -73 | &B7 |
| D | -51 | &CD || V | -100 | &9C || , | -103 | &99 |
| E | -35 | &DD || W | -34 | &DE || . | -104 | &98 |
| F | -68 | &BC || X | -67 | &BD || / | -105 | &97 |
| G | -84 | &AC || Y | -69 | &BB || SPACE | -99 | &9D |
| H | -85 | &AB || Z | -98 | &9E || ESCAPE | -113 | &8F |
| I | -38 | &DA || 0 | -40 | &D8 || DELETE | -90 | &A6 |
| J | -70 | &BA || 1 | -49 | &CF || RETURN | -74 | &B6 |
| K | -71 | &B9 || 2 | -50 | &CE || CURSOR UP | -58 | &C6 |
| L | -87 | &A9 || 3 | -18 | &EE || CURSOR DOWN | -42 | &D6 |
| M | -102 | &9A || 4 | -19 | &ED || CURSOR LEFT | -26 | &E6 |
| N | -86 | &AA || 5 | -20 | &EC || CURSOR RIGHT | -122 | &86 |
| O | -55 | &C9 || 6 | -53 | &CB || COPY | -106 | &96 |
| P | -56 | &C8 || 7 | -37 | &DB || SHIFT | -1 | &FF |
| Q | -17 | &EF || 8 | -22 | &EA || CTRL | -2 | &FE |
| R | -52 | &CC || 9 | -39 | &D9 || CAPS LOCK | -65 | &BF |

Keys specific to B/Master:

| Key | Dec | Hex || Key | Dec | Hex |
| --- | --- | --- | --- | --- | --- | --- |
| @ | -72 | &B8 || NUM 0 | -107 | &95 |
| [ | -57 | &C7 || NUM 1 | -108 | &94 |
| \ | -121 | &87 || NUM 2 | -125 | &83 |
| ] | -89 | &A7 || NUM 3 | -109 | &93 |
| ^ | -25 | &E7 || NUM 4 | -123 | &85 |
| _ | -41 | &D7 || NUM 5 | -124 | &84 |
| TAB | -97 | &9F || NUM 6 | -27 | &E5 |
| SHIFT LOCK | -81 | &AF || NUM 7 | -28 | &E4 |
| f0 | -33 | &DF || NUM 8 | -43 | &D5 |
| f1 | -114 | &8E || NUM 9 | -44 | &D4 |
| f2 | -115 | &8D || NUM + | -59 | &C5 |
| f3 | -116 | &8C || NUM - | -60 | &C4 |
| f4 | -21 | &EB || NUM / | -75 | &B5 |
| f5 | -117 | &8B || NUM # | -91 | &A5 |
| f6 | -118 | &8A || NUM * | -92 | &A4 |
| f7 | -23 | &E9 || NUM , | -93 | &A3 |
| f8 | -119 | &89 || NUM RETURN | -61 | &C3 |
| f9 | -120 | &88 || NUM DELETE | -76 | &B4 |
||||| NUM . | -77 | &B3 |

# Limitations/bugs

- Joystick keys don't affect OSRDCH, so you can't use them to press
  keys at the BASIC prompt, or when using `INPUT`, etc.
  
- `*JJOY` effectively disables both analogue joysticks, even though it
  could pass through to one of them and it wouldn't interfere

# Technical info

## Master 128

The ROM uses 1 page of HAZEL to store its data.

# Compatibility notes

In most cases, you'll find things work using an overlay address of
&150. This list notes the exceptions I've found.

## Frak (Superior re-release) (Master 128)

Works with overlay address of &120.

## Zalaga (Superior re-release) (Master 128)

Hooks are simply ignored. Perhaps it resets the vectors. To be
investigated.
