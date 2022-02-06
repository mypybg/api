from sys import stdout
import subprocess as sp
import os, sys, time, random, base64, marshal, getpass, re, zlib
from uncompyle6.main import decompile



def clr():
    os.system('clear')


m = '\x1b[1;91m'
u = '\x1b[1;95m'
h = '\x1b[1;92m'
p = '\x1b[1;37m'
k = '\x1b[1;33m'
b = '\x1b[1;34m'
bm = '\x1b[96m'



def jalan(z, t):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(t)



def running(s):
	try:
		for c in s + '\n':
        	    sys.stdout.write(c)
	            sys.stdout.flush()
	            time.sleep(0.001)
	except (KeyboardInterrupt,EOFError):
		run('Nonaktif!!!')


#
def logo():
    Kai = '''
   {}  ____    _____    ____   _  _   ____  
    |  _ \  | ____|  / ___| | || | |  _ \ 
    | | | | |  _|   | |     | || |_| |_) |
    | |_| | | |___  | |___  |__   _|  __/ 
    |____/  |_____|  \____|    |_| |_|    
- - - - - - - - - - - - - - - - - - - - - - - - 
                                          '''.format(u)
    running(Kai) 



def run(x):
    pt = '\x1b[1;37m'
    rd = '\x1b[1;37m\x1b[1;31m'
    rg = '\x1b[6;32m'
    try:
        num = 0
        while num < 1:
            for i, char in enumerate(x):
                if i == 0:
                    print '\r%s%s%s%s' % (rg, char.lower(), rd, x[1:]),
                    sys.stdout.flush()
                else:
                    if i == 1:
                        roy = x[0].lower()
                        print '\r%s%s%s%s%s%s' % (rd, roy, pt, char.lower(), rg, x[2:]),
                        sys.stdout.flush()
                    elif i == i:
                        roy = x[0:i].lower()
                        print '\r%s%s%s%s%s%s' % (rd, roy, pt, char.lower(), rg, x[i + 1:]),
                        sys.stdout.flush()
                    time.sleep(0.07)

            num += 1

    except:
        exit()



def menu():
    logo()
    running('{}[{}03{}]{} Encrypt Base64'.format(m,p,m,k))
    running('{}[{}07{}]{} Encrypt Marshal Zlib Base64'.format(m,p,m,k))
    running('{}[{}03{}]{} Compile py > pyc'.format(m,p,m,k))
    running('{}[{}04{}]{} Encrypt Hex'.format(m,p,m,k))
    try:
        inp = raw_input('{}[{}??{}]{} Choose {}>>{} '.format(m,p,m,k,h,p))
    except (KeyboardInterrupt,EOFError):
        run ('Nonaktif!!')
        menu()
    if inp == '1' or inp == '01':
        clr()
        Tiga()
    elif inp == '2' or inp == '02':
        clr()
        emzb()
    elif inp == '3' or inp == '03':
        clr()
        pyc()
    elif inp == '4' or inp == '04':
        clr()
        Empat()
    elif inp == '':
        run ('Pilih Nomornya Woe!!!')
        time.sleep(2)
        menu()
    elif inp == '0' or inp == '00':
        exit()
    else:
        run ('This Script Only KAI.. ')
        time.sleep(2)
        menu()

def Tiga():
        logo()
        try:
            f = raw_input(' - Enter Filenames : ')
        except:
            exit()

        try:
            bk = open(f, 'r').read()
        except:
            run('file %s Can,t Find This Fille' % f)
            exit()

        en = base64.b64encode(bk)
        ff = f + 'c'
        open(ff, 'w').write('import base64\nexec(base64.b64decode("' + en + '"))')
        nm = ('').join(f.split('.')[:1]) + '-enc.py'
        os.rename(ff, nm)
        run('file berhasil di encrypt menjadi %s ' % nm)




def emzb():
	clr()
	logo()
	
	try:
            file = raw_input(' - Enter Name File: ')
            fileopen = open(file).read()
	    no = compile(fileopen,'aso','exec')
	    b = marshal.dumps(no)
            c = zlib.compress(b)
            d = base64.b64encode(c)
            e = ('import marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b64decode("' + d + '"))))')
            f = file.replace('.py', '-enc.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            run('file berhasil di encrypt menjadi %s ' % f)
            raw_input('Tekan Enter Untuk Kembali Ke Menu')
	    menu()
        except IOError:
	    run('file tidak ditemukan ')
	    raw_input('Tekan Enter Untuk Kembali Ke Menu')
            emzb()
            
            
            
            
def pyc():
    logo()
    print m + '[' + p + '#' + m + ']' + p + ' For Example : /sdcard/kai/xxx.py'
    f = raw_input(m + '[' + p + '?' + m + ']' + p + ' Enter Your File : ')
    from py_compile import compile
    compile(f)
    print(m + '[' + p + '#' + m + ']' + p + ' Running compile PLS Wait.. ')
    jalan('\n' + m + '[' + p + '#' + m + ']' + p + ' file successfully compiled', 0.01)
    print '\n' + m + '[' + p + '#' + m + ']' + p + (' File Saved: {}c').format(f)
    ask = raw_input(m + '[' + p + '?' + m + ']' + p + ' Compile Again? y/t >> ')
    if ask == 'y' or ask == 'Y':
        menu()
    elif ask == 't' or ask == 'T':
        sys.exit()
    else:
        print m + '[' + m + '!' + m + ']' + p + ' Choose the right one ' + m + '!!!'
        raw_input(m + '[' + p + '^' + m + ']' + p + ' Press Enter to Return to the menu ')
        os.system('clear')
        menu()



def Empat():
        clr()
        logo()
        try:
            f = raw_input('Filenames: ')
        except:
            exit()

        try:
            bk = open(f, 'r').read()
        except:
            run('file %s tidak ditemukan ' % f)
            exit()

        en = bk.encode('hex')
        ff = f + 'c'
        open(ff, 'w').write('exec("' + en + '").decode("hex")')
        nm = ('').join(f.split('.')[:1]) + '-enc.py'
        os.rename(ff, nm)
        run('file berhasil di encrypt menjadi %s ' % nm)


menu()
