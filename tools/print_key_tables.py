#!/usr/bin/python3
import os,os.path,sys,collections

# Build keys table.
#
# This is doable with 64tass, but (a) it's a bit annoying, and (b) it
# makes a huge mess in the listing file.

##########################################################################
##########################################################################

ElectronKey=collections.namedtuple('Key','name value_str electron_key')
Key=collections.namedtuple('Key','name value_str')

key_names={
    'key_space':0x62,
    'key_comma':0x66,
    'key_minus':0x17,
    'key_stop':0x67,
    'key_slash':0x68,
    'key_0':0x27,
    'key_1':0x30,
    'key_2':0x31,
    'key_3':0x11,
    'key_4':0x12,
    'key_5':0x13,
    'key_6':0x34,
    'key_7':0x24,
    'key_8':0x15,
    'key_9':0x26,
    'key_colon':0x48,
    'key_semicolon':0x57,
    'key_at':0x47,
    'key_a':0x41,
    'key_b':0x64,
    'key_c':0x52,
    'key_d':0x32,
    'key_e':0x22,
    'key_f':0x43,
    'key_g':0x53,
    'key_h':0x54,
    'key_i':0x25,
    'key_j':0x45,
    'key_k':0x46,
    'key_l':0x56,
    'key_m':0x65,
    'key_n':0x55,
    'key_o':0x36,
    'key_p':0x37,
    'key_q':0x10,
    'key_r':0x33,
    'key_s':0x51,
    'key_t':0x23,
    'key_u':0x35,
    'key_v':0x63,
    'key_w':0x21,
    'key_x':0x42,
    'key_y':0x44,
    'key_z':0x61,
    'key_left_square_bracket':0x38,
    'key_backslash':0x78,
    'key_right_square_bracket':0x58,
    'key_caret':0x18,
    'key_underline':0x28,
    'key_escape':0x70,
    'key_tab':0x60,
    'key_caps_lock':0x40,
    'key_ctrl':0x1,
    'key_shift_lock':0x50,
    'key_shift':0x0,
    'key_delete':0x59,
    'key_copy':0x69,
    'key_return':0x49,
    'key_up':0x39,
    'key_down':0x29,
    'key_left':0x19,
    'key_right':0x79,
    'key_f0':0x20,
    'key_f1':0x71,
    'key_f2':0x72,
    'key_f3':0x73,
    'key_f4':0x14,
    'key_f5':0x74,
    'key_f6':0x75,
    'key_f7':0x16,
    'key_f8':0x76,
    'key_f9':0x77,
    'key_numpad_0':0x6a,
    'key_numpad_1':0x6b,
    'key_numpad_2':0x7c,
    'key_numpad_3':0x6c,
    'key_numpad_4':0x7a,
    'key_numpad_5':0x7b,
    'key_numpad_6':0x1a,
    'key_numpad_7':0x1b,
    'key_numpad_8':0x2a,
    'key_numpad_9':0x2b,
    'key_numpad_plus':0x3a,
    'key_numpad_minus':0x3b,
    'key_numpad_divide':0x4a,
    'key_numpad_hash':0x5a,
    'key_numpad_multiply':0x5b,
    'key_numpad_comma':0x5c,
    'key_numpad_return':0x3c,
    'key_numpad_delete':0x4b,
    'key_numpad_stop':0x4c,
}

# Common keys.
keys=[
    ElectronKey('A','key_a',0x32),
    ElectronKey('B','key_b',0x23),
    ElectronKey('C','key_c',0x2b),
    ElectronKey('D','key_d',0x2a),
    ElectronKey('E','key_e',0x29),
    ElectronKey('F','key_f',0x26),
    ElectronKey('G','key_g',0x22),
    ElectronKey('H','key_h',0x1e),
    ElectronKey('I','key_i',0x15),
    ElectronKey('J','key_j',0x1a),
    ElectronKey('K','key_k',0x16),
    ElectronKey('L','key_l',0x12),
    ElectronKey('M','key_m',0x1b),
    ElectronKey('N','key_n',0x1f),
    ElectronKey('O','key_o',0x11),
    ElectronKey('P','key_p',0x0d),
    ElectronKey('Q','key_q',0x31),
    ElectronKey('R','key_r',0x25),
    ElectronKey('S','key_s',0x2e),
    ElectronKey('T','key_t',0x21),
    ElectronKey('U','key_u',0x19),
    ElectronKey('V','key_v',0x27),
    ElectronKey('W','key_w',0x2d),
    ElectronKey('X','key_x',0x2f),
    ElectronKey('Y','key_y',0x1d),
    ElectronKey('Z','key_z',0x33),
    ElectronKey('0','key_0',0x0c),
    ElectronKey('1','key_1',0x30),
    ElectronKey('2','key_2',0x2c),
    ElectronKey('3','key_3',0x28),
    ElectronKey('4','key_4',0x24),
    ElectronKey('5','key_5',0x20),
    ElectronKey('6','key_6',0x1c),
    ElectronKey('7','key_7',0x18),
    ElectronKey('8','key_8',0x14),
    ElectronKey('9','key_9',0x10),
    ElectronKey('-','key_minus',0x08),
    ElectronKey(';','key_semicolon',0x0e),
    ElectronKey(':','key_colon',0x0a),
    ElectronKey(',','key_comma',0x17),
    ElectronKey('.','key_stop',0x13),
    ElectronKey('/','key_slash',0x0f),
    ElectronKey("SPACE",'key_space',0x03),
    ElectronKey("ESCAPE",'key_escape',0x34),
    ElectronKey("DELETE",'key_delete',0x07),
    ElectronKey("RETURN",'key_return',0x06),
    ElectronKey("CUR UP",'key_up',0x09),
    ElectronKey("CUR DOWN",'key_down',0x05),
    ElectronKey("CUR LEFT",'key_left',0x04),
    ElectronKey("CUR RIGHT",'key_right',0x00),
    ElectronKey("COPY",'key_copy',0x01),
    ElectronKey("SHIFT",'key_shift',0x37),
    ElectronKey("CTRL",'key_ctrl',0x36),
    ElectronKey("CAPS LOCK",'key_caps_lock',0x35),
]
num_electron_keys=len(keys)

temp=set()
for k in keys:
    assert k.electron_key not in temp,hex(k.electron_key)
    temp.add(k.electron_key)

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
    Key('N0','key_numpad_0'),
    Key('N1','key_numpad_1'),
    Key('N2','key_numpad_2'),
    Key('N3','key_numpad_3'),
    Key('N4','key_numpad_4'),
    Key('N5','key_numpad_5'),
    Key('N6','key_numpad_6'),
    Key('N7','key_numpad_7'),
    Key('N8','key_numpad_8'),
    Key('N9','key_numpad_9'),
    Key('N+','key_numpad_plus'),
    Key('N-','key_numpad_minus'),
    Key('N/','key_numpad_divide'),
    Key('N#','key_numpad_hash'),
    Key('N*','key_numpad_multiply'),
    Key('N,','key_numpad_comma'),
    Key('NRETURN','key_numpad_return'),
    Key('NDELETE','key_numpad_delete'),
    Key('N.','key_numpad_stop'),
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
        value=key_names[k.value_str]
        assert (value&0x7f)==value,"not 7-bit"
        # print("    .cerror (%s&$7f)!=%s,'oops'"%(k.value_str,k.value_str))
        # inkey_str='%s^$7f'%(k.value_str)

        topbit=''
        if key_offsets[i] is not None: topbit='|$80'
        print('    .byte $%x%s ; %d %s'%(value^0x7f,topbit,i,k.value_str))

    print('key_names_table:')
    for i,k in enumerate(keys):
        s='    '
        if needs_string_table_entry(k.name):
            s+='.byte %d'%(key_offsets[i])
        else: s+='.text "%s"'%(k.name)
        s+=' ; %d'%i
        print(s)

    print('key_strings_table:')
    offset=0
    for i,k in enumerate(keys):
        if needs_string_table_entry(k.name):
            print('    .shiftl "%s" ; %d +%d'%(k.name,i,offset))
            offset+=len(k.name)

    # print('electron_keys_table:')
    # electron_keys=128*[None]
    # for i in range(num_electron_keys):
    #     assert keys[i].value_str in key_names
    #     internal=key_names[keys[i].value_str]
    #     assert electron_keys[internal] is None
    #     electron_keys[internal]=(keys[i].electron_key,keys[i].value_str)

    # for ek in electron_keys:
    #     if ek is None: print('    .byte $ff')
    #     else: print('    .byte $%02x ; %s'%(ek[0],ek[1]))
        
##########################################################################
##########################################################################

if __name__=='__main__': main(sys.argv[1:])
