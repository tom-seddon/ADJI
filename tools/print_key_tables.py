#!/usr/bin/python3
import os,os.path,sys,collections

# Build keys table.
#
# This is doable with 64tass, but (a) it's a bit annoying, and (b) it
# makes a huge mess in the listing file.

##########################################################################
##########################################################################

Key=collections.namedtuple('Key','name value_str')

# Common keys.
keys=[
    Key('A','key_a'),
    Key('B','key_b'),
    Key('C','key_c'),
    Key('D','key_d'),
    Key('E','key_e'),
    Key('F','key_f'),
    Key('G','key_g'),
    Key('H','key_h'),
    Key('I','key_i'),
    Key('J','key_j'),
    Key('K','key_k'),
    Key('L','key_l'),
    Key('M','key_m'),
    Key('N','key_n'),
    Key('O','key_o'),
    Key('P','key_p'),
    Key('Q','key_q'),
    Key('R','key_r'),
    Key('S','key_s'),
    Key('T','key_t'),
    Key('U','key_u'),
    Key('V','key_v'),
    Key('W','key_w'),
    Key('X','key_x'),
    Key('Y','key_y'),
    Key('Z','key_z'),
    Key('0','key_0'),
    Key('1','key_1'),
    Key('2','key_2'),
    Key('3','key_3'),
    Key('4','key_4'),
    Key('5','key_5'),
    Key('6','key_6'),
    Key('7','key_7'),
    Key('8','key_8'),
    Key('9','key_9'),
    Key('-','key_minus'),
    Key(';','key_semicolon'),
    Key(':','key_colon'),
    Key(',','key_comma'),
    Key('.','key_stop'),
    Key('/','key_slash'),
    Key("SPACE",'key_space'),
    Key("ESCAPE",'key_escape'),
    Key("DELETE",'key_delete'),
    Key("RETURN",'key_return'),
    Key("CURSOR UP",'key_up'),
    Key("CURSOR DOWN",'key_down'),
    Key("CURSOR LEFT",'key_left'),
    Key("CURSOR RIGHT",'key_right'),
    Key("COPY",'key_copy'),
    Key("SHIFT",'key_shift'),
    Key("CTRL",'key_ctrl'),
    Key("CAPS LOCK",'key_caps_lock'),
]
num_electron_keys=len(keys)

# BBC B keys
keys+=[
    Key('@','key_at'),
    Key('[','key_left_square_bracket'),
    Key('\\\\','key_backslash'),
    Key(']','key_right_square_bracket'),
    Key('^','key_caret'),
    Key('_','key_underline'),
    Key("TAB",'key_tab'),
    Key("SHIFT LOCK",'key_shift_lock'),
    Key("f0",'key_f0'),
    Key("f1",'key_f1'),
    Key("f2",'key_f2'),
    Key("f3",'key_f3'),
    Key("f4",'key_f4'),
    Key("f5",'key_f5'),
    Key("f6",'key_f6'),
    Key("f7",'key_f7'),
    Key("f8",'key_f8'),
    Key("f9",'key_f9'),
]
num_bbc_keys=len(keys)

# Master 128 keys
keys+=[
    Key('NUM 0','key_numpad_0'),
    Key('NUM 1','key_numpad_1'),
    Key('NUM 2','key_numpad_2'),
    Key('NUM 3','key_numpad_3'),
    Key('NUM 4','key_numpad_4'),
    Key('NUM 5','key_numpad_5'),
    Key('NUM 6','key_numpad_6'),
    Key('NUM 7','key_numpad_7'),
    Key('NUM 8','key_numpad_8'),
    Key('NUM 9','key_numpad_9'),
    Key('NUM +','key_numpad_plus'),
    Key('NUM -','key_numpad_minus'),
    Key('NUM /','key_numpad_divide'),
    Key('NUM #','key_numpad_hash'),
    Key('NUM *','key_numpad_multiply'),
    Key('NUM ,','key_numpad_comma'),
    Key('NUM RETURN','key_numpad_return'),
    Key('NUM DELETE','key_numpad_delete'),
    Key('NUM .','key_numpad_stop'),
]
num_master_keys=len(keys)

##########################################################################
##########################################################################

def needs_string_table_entry(x):
    assert len(x)>0
    if len(x)==1: return False
    if x=='\\\\': return False
    return True

def main(argv):
    key_offsets=[]
    next_offset=0
    for k in keys:
        if needs_string_table_entry(k.name):
            key_offsets.append(next_offset)
            next_offset+=len(k.name)
        else: key_offsets.append(None)

    if len(keys)>128:
        print('FATAL: too many keys',file=sys.stderr)
        sys.exit(1)

    print('num_bbc_keys=%d'%num_bbc_keys)
    print('num_master_keys=%d'%num_master_keys)
    print('num_electron_keys=%d'%num_electron_keys)

    # INKEY value in bits 0-6 (must set bit 7 before use).
    #
    # Bit 7 indicates how to interpret the corresponding entry in
    # key_names_table:
    #
    # Clear: 1-char key name
    #
    # Set: offset into key_strings_table
    print('key_inkey_numbers_table:')
    for i,k in enumerate(keys):
        print("    .cerror (%s&$7f)!=%s,'oops'"%(k.value_str,k.value_str))
        inkey_str='%s^$7f'%(k.value_str)
        if key_offsets[i] is not None: inkey_str+='|$80'
        print('    .byte %s ; %d'%(inkey_str,i))

    print('key_names_table:')
    for i,k in enumerate(keys):
        s='    '
        if needs_string_table_entry(k.name):
            s+='.byte %d'%(key_offsets[i])
        else: s+='.text "%s"'%(k.name)
        s+=' ; %d'%i
        print(s)

    print('key_strings_table:')
    for i,k in enumerate(keys):
        if needs_string_table_entry(k.name):
            print('    .shiftl "%s" ; %d'%(k.name,i))

##########################################################################
##########################################################################

if __name__=='__main__': main(sys.argv[1:])
