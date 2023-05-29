#!/usr/bin/python3
import os,os.path,sys,argparse

def main2(options):
    with open(options.input_path,'rb') as f: data=f.read()
    i=data.index(b'AA\xc1BB')
    while data[i]!=0:
        ascii=data[i]
        i+=1

        name=''
        while (data[i]&0x80)==0:
            name+=chr(data[i])
            i+=1

        inkey=(data[i]&0x7f^0xff)-256
        i+=1

        

        print('| %s | %d | &%X |'%(name,inkey,inkey&0xff))

def main(argv):
    p=argparse.ArgumentParser()

    p.add_argument('input_path',metavar='FILE',help='''read ROM from %(metavar)s''')
    main2(p.parse_args(argv))

if __name__=='__main__': main(sys.argv[1:])
