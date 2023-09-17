# Advanced Digital Joystick Interface ROM

Support ROM for Retro Hardware's Advanced Digital Joystick Interface
cartridge for the Acorn Electron/BBC Master 128.

Based in part on the Slogger Electron Expansion 2.02 ROM:
https://github.com/tom-seddon/SloggerElectronExpansion

# Using the ADJI

Requires Electron or Master 128.

Connect the joystick interface to one of the cartridge slots, and plug
a 9-pin joystick into the 9-pin plug.

The ROM can run from any bank, including sideways RAM.

## Slogger interface compatibility

There is a special version of the ROM for use with the original
Slogger Switched Joystick Interface cartridge. This doesn't support a
2nd fire button, but is otherwise fully-featured!

This ROM reports itself as `(1F)` in the `*HELP` output.

Note that `*JKEYS` still requires a valid number to be specified for
the second fire button, even though the value is ignored. `*JSETUP`
will suggest `0`.

## `*JTEST` - test the joystick

To test it out, use `*JTEST`. This takes one parameter: the joystick
number, 1-4, corresponding to the DIP switch settings on the cartridge
(D = Down, U = Up).

| Number | Switches |
| --- | --- |
| 1 | D D |
| 2 | U D |
| 3 | D U |
| 4 | U U |

The joystick test screen reads the joystick, and shows on screen which
directions and/or buttons are being pressed.

The ADJI supports 2 independent fire buttons if the joystick has them.

## `*JSETUP` - set up the joystick

You'll be prompted for the following. Press Escape at any time to
cancel.

`Joystick no (1/2/3/4)?` - enter the joystick number.

`Joystick/Keys (J/K)?` - press `J` to have the joystick behave as an
analogue joystick, or `K` to have it translated into keypresses for
games.

If behaving as an analogue joystick, it behaves as if it's the first
analogue joystick, and its state can be read with `ADVAL` or OSBYTE
&80:

- `ADVAL(0)` reports the fire button - both are treated the same
- `ADVAL(1)` reports the digital left/right axis
- `ADVAL(2)` reports the digital up/down axis

If behaving as keys, it hooks into the processing of `INKEY` and
OSBYTE &81 - the goal being to support its use with games. The
joystick can't be used for ordinary text input.

`Press UP:`, `Press DOWN:`, `Press LEFT:`, `Press RIGHT:`, `Press
FIRE1:`, `Press FIRE2:` - if you opted for keys mode, you'll be
prompted for the key that each joystick action should correspond to.

(If you press Escape here, it'll cancel the setup. If you want to bind
a joystick action to Escape, you'll need to use the `*JKEYS` command,
described below.)

`Xvector/Overlay (X/O)?` - pick the method the ROM uses to hook into
the keyboard and joystick processing.

`Xvector` uses the extended vectors, which would be the Acorn-approved
method, but many games overwrite the relevant OS workspace and so you
may experience crashes or hangs. 

`Overlay` installs a short routine somewhere in RAM to handle the
hooking. (The routine is 15 bytes on the Master, and 18 bytes on the
Electron.) There's no best place for this to go, so you'll be prompted
for an address!

The default of &150, which will be used if you just press Return when
prompted, should be good for many games. If you still experience
problems, unfortunately some experimentation may be necessary. These
other options are all worth trying:

- &100-&140 inclusive - also in the stack area
- &880-&8A0 inclusive - the printer buffer
- &380-&3C0 inclusive (disk only) - OS tape workspace

If using the printer buffer, you must then avoid using the printer,
and if using the OS tape workspace, you must then avoid using tapes!

When providing an address in hex, precede with `&`, as per BASIC.

Once the questions are over, `*JSETUP` will install the hooks and
finish. Last thing it does is print a `*JKEYS` (see below) or `*JJOY`
(see below) command line, that you can note down and use later to set
up the same settings non-interactively (e.g., from `!BOOT` or a loader
program).

The `*JSETUP` settings will persist across a SHIFT+BREAK or BREAK if
you do it straight away after `*JSETUP`. Note that after running a
game, they might not survive a subsequent BREAK, even if the joystick
was working fine in game.

`*HELP ADJI` will print `(active)` or `(inactive)` to indicate the
ADJI joystick status.

## `*JOFF` - switch digital joystick support off

No parameters required.

## `*JJOY` - use the digital joystick as an analogue joystick

`*JJOY` takes 2 parameters:

1. Joystick number, 1-4, as per `*JTEST`
2. Overlay address (precede with `&` if in hex), or `X` to use
   extended vectors

The settings will persist across a soft BREAK as per `*JSETUP`.

## `*JKEYS` - use the digital joystick as keys

`*JKEYS` takes 7 parameters, with all keys specified as negative INKEY
values:

1. Joystick number, 1-4, as above
2. Key for up
3. Key for down
4. Key for left
5. Key for right
6. Key for fire button 1
7. Key for fire button 2 (ignored if using the `1F` ROM)
8. Overlay address or `X', as above

Easiest thing to do is use `*JSETUP`, which will prompt you for the
keys and print a command line you can use again.

The settings will persist across a soft BREAK as per `*JSETUP`.

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

# Using the ADJI from code

The joystick appears as a single byte in page &FC, location depending
on the DIP switch settings. The relationship between joystick number
(as per `*JSETUP`, etc.), DIP switches and address is as follows:

| Number | Address | Switches |
| --- | --- | --- |
| 1 | &FCC0 | D D |
| 2 | &FCD0 | U D |
| 3 | &FCE0 | D U |
| 4 | &FCF0 | U U |

The value read is a 6-bit quantity, bits as follows. Each used bit is
set if the corresponding button is pressed, or the joystick is moved
in that direction.

(You `Raw value` shown in the `*JTEST` output will show the exact
value read.)

| Bit | What |
| --- | --- |
| 7   | Unused (ignore) |
| 6   | Unused (ignore) |
| 5   | Fire 2 |
| 4   | Fire 1 |
| 3   | Right |
| 2   | Left |
| 1   | Down |
| 0   | Up |

On the Electron, you can read the value directly. `A%=?&FCC0` from
BASIC, for example, to read the joystick state into `A%`. Or something
like `lda &FCC0` from assembly language.

On the Master, page &FC needs to be redirected to the cartridge first,
by setting bit 5 of ACCCON (&FE34): `?&FE34=?&FE34 OR &20`, or `lda
#&20:tsb &FE34`. This may interfere with any devices connected to the
1 MHz bus, so you might want to save the old value of ACCCON and
restore it afterwards.

# Technical info

There isn't tons of spare memory, so the ROM's state has to be
squeezed in. Here's where it lives.

## Master 128

The ROM stores its state in a dummy filing system entry in HAZEL. This
buys it a few bytes that are fairly unlikely to get overwritten.

It's impossible to select the filing system it pretends to be.

To handle persistence across a BREAK, the following areas are also
used:

- &287-&289 (BREAK intercept routine) - xvector/overlay settings info

## Electron

The ROM sneaks its data into 7 otherwise-unused bytes of OS workspace.
One byte is used for flags:

- &0290 - unused by Electron OS

The remaining 6 are used when the joystick behaves as keys, to store
the key assignments:

- &02A8 (ROM flags for the keyboard's other ROM bank)
- &02A9 (ROM flags for the keyboard's ROM bank)
- &02AA (ROM flags for the BASIC ROM's other ROM bank)
- &02F5 (unused by Electron OS)
- &02F6 (unused by Electron OS)
- &027E (unused by Electron OS)

To handle persistence across a BREAK, the following areas are also
used:

- &39F-&3A6 (unused by Electron OS) - copy of the ROM state above
- &287-&289 (BREAK intercept routine) - xvector/overlay settings info

# Compatibility notes

See https://github.com/tom-seddon/ADJI/blob/main/games.md
