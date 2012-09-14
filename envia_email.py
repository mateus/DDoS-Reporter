#!/usr/bin/python
# -*- coding: cp860 -*- 

import getpass
import smtplib

def envia_email(atk=0):
    '''
    Envia um e-mail informando um alerta de DDoS/Dos

    Args: atk (int) - Tipo do ataque detectado (0->DoS, 1->DDoS)
    '''

    fromaddr = 'ddosreporter@gmail.com'
    password = 'ifet2012'
    toaddrs = 'mtsferreirasilva@gmail.com'

    if atk == 0:
    	subject = 'Alerta de DoS'
    	message = '''Seu endereço web está sobrendo um ataque DoS... {mais detalhes a seguir}

    	Esta mensagem foi gerada automaticamente pelo sistema, não responda este e-mail.'''
    elif atk == 1:
    	subject = 'Alerta de DDoS'
    	message = '''Seu endereço web está sobrendo um ataque DDoS... {mais detalhes a seguir}

    	Esta mensagem foi gerada automaticamente pelo sistema, não responda este e-mail.'''

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    server.sendmail(
    	fromaddr, 
    	toaddrs, 
    	'To: {0}\nFrom: {1}\nSubject: {2}\n\n{3}\n\n'.format(
    		toaddrs, 
    		fromaddr, 
    		subject,
            message)
    	)
    server.close()

if __name__ == '__main__':
    envia_email(1)