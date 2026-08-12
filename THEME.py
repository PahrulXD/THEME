# -*- coding: utf-8 -*-
import os, sys, time
os.system('clear')

logo = ('''\033[1;96m
████████╗██╗  ██╗███████╗███╗   ███╗███████╗
╚══██╔══╝██║  ██║██╔════╝████╗ ████║██╔════╝
   ██║   ███████║█████╗  ██╔████╔██║█████╗  
   ██║   ██╔══██║██╔══╝  ██║╚██╔╝██║██╔══╝  
   ██║   ██║  ██║███████╗██║ ╚═╝ ██║███████╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝

\033[1;97m- Coding By : Pahrul Aguspriana XF.

\033[1;97m[\033[1;96m1\033[1;97m] ubah tampilan termux
\033[1;97m[\033[1;96m2\033[1;97m] hapus tampilan termux
\033[1;97m[\033[1;96m3\033[1;97m] ubah tombol termux
\033[1;97m[\033[1;96m0\033[1;97m] exit
''')


def animasi():
    for x in range(20):
        sys.stdout.write('\rtunggu sebentar |')
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\rtunggu sebentar /')
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\rtunggu sebentar -')
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\rtunggu sebentar \\')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.flush()
    
def main():
    print logo
    tanya = raw_input('\033[1;97m- pilih : ')
    if tanya == '1':
        os.system('clear')
        ubah()
    elif tanya == '2':
        os.system('clear')
        delet()
    elif tanya == '3':
        os.system('clear')
        setup()
    elif tanya == '0':
        exit()
    else:
        exit()

def ubah():
    os.system('clear')
    prompt = str(raw_input('\033[1;97m- masukan nama kamu ( bebas ) : '))
    ugex = open('bash.bashrc', 'w')
    ugex.write('clear')
    ugex.write("\necho '\x1b[1;97m                    .:::!~!!!!!:.'")
    ugex.write("\necho '                 .xUHWH!! !!?M88WHX:.'")
    ugex.write("\necho '               .X*#M@&!!  !X!M&&&&&&WWx:.'")
    ugex.write("\necho '              :!!!!!!?H! :!&!&&&&&&&&&&8X:'")
    ugex.write("\necho '             !!~  ~:~!! :~!&!#&&&&&&&&&&8X:'")
    ugex.write("\necho '            :!~::!H!<   ~.U&X!?R&&&&&&&&MM!'")
    ugex.write("\necho '            ~!~!!!!~~ .:XW&&&U!!?&&&&&&RMM!'")
    ugex.write("\necho '              !:~~~ .:!MST#&&&&WX??#MRRMMM!'")
    ugex.write("\necho '              ~?WuxiW*`   `\xe2\x88\x9a#&&&&8!!!!??!!!'")
    ugex.write("\necho '            :X- M&&&&       `rT#&T~!8&WUXU~'")
    ugex.write("\necho '           :%`  ~#&&&m:    \x1b[1;91m\xe2\x9c\xaa   \x1b[1;97m~!~ ?&&&&&&'")
    ugex.write("\necho '         :!`.-   ~T&&&&8xx.  .xWW- ~x&&&&&'")
    ugex.write("\necho '.....   -~~:<` !    ~?T#&&@@W@*?&&   \x1b[1;91m\xe2\x9c\xaa  \x1b[1;97m/`'")
    ugex.write("\necho 'W&@@M!!! .!~~ !!     .:XUW&W!~ `&~:    :'")
    ugex.write("\necho '#&~~`.:x%`!!  !H:   !WM&&&&Ti.: .!WUn+!`'")
    ugex.write("\necho ':::~:!!`:X~ .: ?H.!u \xc2\xb0&&&B&&&!W:U!T&&M~'")
    ugex.write("\necho '.~~   :X@!.-~   ?@WTWo(`*&&&W&TH&! `'")
    ugex.write("\necho 'Wi.~!X$?!-~    / ?&&&B&Wu(`**&RM!'")
    ugex.write("\necho '.....         /   ~&&&&&B&&en:``'")
    ugex.write("\necho '\x1b[1;791m                  ~`##*&&&&M~'")
    ugex.write('\necho')
    ugex.write('\necho')
    ugex.write("\n\nPS1='\x1b[1;34m\\]\xe2\x95\xad\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\\[\x1b[1;31m\\][\\[\x1b[1;33m\\]" + prompt + '\\[\x1b[1;34m\\]\\[\x1b[1;31m\\]]\\[\x1b[1;31m\\]\\[\x1b[1;34m\\]\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\\[\x1b[1;31m\\][\\[\x1b[1;30m\\]\\w\\[\x1b[1;31m\\]] ')
    ugex.write("\n\\[\x1b[1;34m\\]\xe2\x95\xb0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\\[\x1b[1;31m\\]\xe2\x9f\xa9\xe2\x9f\xa9\xe2\x9f\xa9\\[\x1b[1;32m\\] '")
    ugex.close()
    os.system('rm $HOME/../usr/etc/bash.bashrc')
    os.system('cp -f bash.bashrc $HOME/../usr/etc')
    os.system("clear")
    animasi()
    os.system('termux-reload-settings')
    os.system('login')


def delet():
    os.chdir('delet')
    os.system('rm $HOME/../usr/etc/bash.bashrc')
    os.system('cp -f bash.bashrc $HOME/../usr/etc')
    os.system('clear')
    animasi()
    os.system('termux-reload-settings')
    os.system('login')


def setup():
    try:
        os.mkdir('/data/data/com.termux/files/home/.termux')
    except:
        pass

    key = "extra-keys = [['CTRL','END','HOME','UP','cd /sdcard ','pkg install ',' pip install '],['python ','python2 ','LEFT','DOWN','RIGHT','/','pip2 install ']]"
    open('/data/data/com.termux/files/home/.termux/termux.properties', 'w').write(key)
    os.system("clear")
    animasi()
    os.system('termux-reload-settings')
    os.system('login')
    
    

main()