#!/usr/bin/python
# -*- coding: utf-8 -*- 

import time
import random
import settings

from datetime import datetime

class Create_test_file():

    def create_empty_file(self):
        open(settings.ARQUIVO_DE_LOG, 'w')

    def create_access_list(self):
        #Data e Hora atuais
        today = datetime.now()
        dh = '{}/{}/{}:{}:{}:{}'.format(today.day,
        today.month,today.year,today.hour,today.minute,today.second)

        #Criando lista
        access_list = [
        '''10.0.0.1 - - [{} -0300] "GET /pagina.htm HTTP/1.1" 200 7079 "http://www.teste.com.br/" "Mozilla/5.0 (Windows; U; Windows NT 6.1; pt-BR; rv:1.9.1.10) Gecko/20100504 Firefox/3.5.10"\n'''.format(dh),
        '''10.0.0.10 - - [{} -0300] "GET /pagina.htm HTTP/1.1" 200 7079 "http://www.teste.com.br/" "Mozilla/5.0 (Windows; U; Windows NT 6.1; pt-BR; rv:1.9.1.10) Gecko/20100504 Firefox/3.5.10"\n'''.format(dh),
        '''10.0.0.15 - - [{} -0300] "GET /pagina.htm HTTP/1.1" 200 7079 "http://www.teste.com.br/" "Mozilla/5.0 (Windows; U; Windows NT 6.1; pt-BR; rv:1.9.1.10) Gecko/20100504 Firefox/3.5.10"\n'''.format(dh),
        '''10.0.0.20 - - [{} -0300] "GET /pagina.htm HTTP/1.1" 200 7079 "http://www.teste.com.br/" "Mozilla/5.0 (Windows; U; Windows NT 6.1; pt-BR; rv:1.9.1.10) Gecko/20100504 Firefox/3.5.10"\n'''.format(dh),
        '''10.0.0.25 - - [{} -0300] "GET /pagina.htm HTTP/1.1" 200 7079 "http://www.teste.com.br/" "Mozilla/5.0 (Windows; U; Windows NT 6.1; pt-BR; rv:1.9.1.10) Gecko/20100504 Firefox/3.5.10"\n'''.format(dh),
        '''10.0.0.30 - - [{} -0300] "GET /pagina.htm HTTP/1.1" 200 7079 "http://www.teste.com.br/" "Mozilla/5.0 (Windows; U; Windows NT 6.1; pt-BR; rv:1.9.1.10) Gecko/20100504 Firefox/3.5.10"\n'''.format(dh),
        '''10.0.0.35 - - [{} -0300] "GET /pagina.htm HTTP/1.1" 200 7079 "http://www.teste.com.br/" "Mozilla/5.0 (Windows; U; Windows NT 6.1; pt-BR; rv:1.9.1.10) Gecko/20100504 Firefox/3.5.10"\n'''.format(dh)
        ]
        return access_list

    def create_file(self):
        #Criando arquivo de teste vazio
        self.create_empty_file()
        
        while True:
            text = ''
            access_list = self.create_access_list() 

            #Lendo arquivo e salvando seu conteudo
            with open(settings.ARQUIVO_DE_LOG, 'r') as _file:
                text = _file.read()
            
            #Salvando novos registros
            with open(settings.ARQUIVO_DE_LOG, 'w') as _file:
                l = []
                #Gerando quantidade aleatória de X a Y requisições por segundo
                for _ in xrange(random.randint(3,20)):
                    #Escolhendo aleatoriamente um registro da lista de acesso
                    line = '{}'.format(access_list[random.randint(0, 6)])
                    l.append(line)
                    print line
                
                print '\n'
                l = ''.join(l)
                #Adicionando novo contéudo ao arquivo de teste
                _file.write('{}{}'.format(text, l))
            
            #Delay de 1 segundo até o próximo incremento
            try:
                time.sleep(1)
            except:
                print '\nCriação interrompida'
                exit()

if __name__== "__main__":
    file_test = Create_test_file()
    file_test.create_file()