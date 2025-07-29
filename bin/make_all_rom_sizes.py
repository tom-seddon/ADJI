#!/usr/bin/python3
import argparse,sys,os,os.path,math

##########################################################################
##########################################################################

def fatal(msg):
    sys.stderr.write('FATAL: %s\n'%msg)
    sys.stderr.flush()
    sys.exit(1)

##########################################################################
##########################################################################

g_verbose=False

def pv(msg):
    if g_verbose:
        sys.stdout.write(msg)
        sys.stdout.flush()

##########################################################################
##########################################################################

def main2(options):
    global g_verbose;g_verbose=options.verbose
    
    with open(options.input_path,'rb') as f: data=f.read()
    if len(data)>65536:
        fatal('file is %d bytes, but max permissible is 65536: %s'%(len(data),options.input_path))

    log2=math.log2(len(data))
    if log2!=int(log2):
        next_size_up=1<<int(log2)+1
        data+=bytes(next_size_up-len(data))

    output_name,output_ext=os.path.splitext(os.path.split(options.input_path)[1])
    if options.output_path is None: save=False
    else:
        save=True
        output_name=os.path.join(options.output_path,output_name)
        
    pv('padded size: %d\n'%len(data))
    while len(data)<=65536:
        assert len(data)%1024==0
        output_path='%s.%dK%s'%(output_name,len(data)//1024,output_ext)
        pv('%s...\n'%output_path)
        if save:
            with open(output_path,'wb') as f: f.write(data)
        data+=data

##########################################################################
##########################################################################

def main(argv):
    p=argparse.ArgumentParser()
    p.add_argument('-v','--verbose',action='store_true',help='''be extra verbose''')
    p.add_argument('-o',metavar='FOLDER',dest='output_path',help='''write output file(s) to %(metavar)s''')
    p.add_argument('input_path',metavar='FILE',help='''read ROM from %(metevar)s''')
    main2(p.parse_args(argv))

##########################################################################
##########################################################################
    
if __name__=='__main__': main(sys.argv[1:])
