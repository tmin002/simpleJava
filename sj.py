#!/usr/bin/env python3
import glob, os, sys 

RUN_AFTER = False

## Functions
def sjexit(msg=None):
    if msg:
        sjprint(msg)
        exit(1)
    exit(0)

def sjprint(text):
    print('sj: ' + text)

def sjhelp(badcmd=False):
    if badcmd:
        sjprint('Invalid command.')
    print('usage: sj [options]')
    print('options: ')
    print('  --run/-r     Run after compile')
    print('  --clean/-c   Remove \'out\' directory')
    print('  --help/-h/?  Show help')
    print('important: src/ and manifest.mf required.')
    sjexit()

def shell(args):
    print('> ' + args)
    if (os.system(args) != 0):
        sjexit('error detected, terminating.')

#0. Chceck requisities and args

if len(sys.argv) >= 3:
    sjhelp(True)
if len(sys.argv) == 2:
    if sys.argv[1].lower() == '-h' or sys.argv[1] == '--help' or sys.argv[1] == '?':
        sjhelp()
    elif sys.argv[1].lower() == '-r' or sys.argv[1] == '--run':
        RUN_AFTER = True
    elif sys.argv[1].lower() == '-c' or sys.argv[1] == '--clean':
        os.system('rm -rf out')
        sjexit()
    else:
        sjhelp(True)

if not os.path.exists('src'):
    sjexit('src directory not found')
if not os.path.exists('manifest.mf'):
    sjexit('manifest.mf not found')
if not os.path.exists('out'):
    os.mkdir('out')

#1. Get file list
flist = []

sjprint('Seeking files..')
for file in glob.iglob('src/**/*.java', recursive=True):
    if not os.path.isdir(file):
        print(' ' + file)
        flist.append(file)

#2. Compile everything in list
sjprint('Generating bytecodes..')
for file in flist:
    shell('javac -classpath src ' + file + ' -d out/')

#3. Create jar
sjprint('Creating jar..')
shell('cd out; jar cmf ../manifest.mf ../output.jar *')

#4. Run or exit
if RUN_AFTER:
    sjprint('Executing..')
    print('\033[0;32m[Program started]\033[0;0m')
    result = os.system('java -jar output.jar')
    print('\033[0;%dm[Program terminated]\033[0;0m' % (32 if result == 0 else 31))
sjexit()
