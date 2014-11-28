#!/usr/bin/python
# -*- coding: utf-8 -*-
# Desarrollado por William Cabrera
# @willicab
# License GPL2


import time
from subprocess import Popen, PIPE, STDOUT

grupo = 'TL'
ruta = '/home/USUARIO/Documentos/'
documentos = ['const-brasil']

p = Popen(['telegram', '-k', '/home/USUARIO/app/tg/tg-server.pub'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
time.sleep(5)
p.stdin.write('chat_with_peer ' + grupo + '\n')

while 1:
    for i, j in enumerate(documentos):
        txt = ruta + j + '.txt'
        file = open(txt, 'r')
        for line in file:
            l = line.replace('\n', '')
            print line
            p.stdin.write(line+'\n')
            time.sleep(3)

    time.sleep(7)
