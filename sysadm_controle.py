#!/usr/bin/python
# -*- coding: cp860 -*- 

import re
from django import forms

def email_validator(email):
	'''
    Valida um e-mail

    Args: email (str) - email a ser validado
    '''

	f = forms.EmailField()
	try:
		f.clean(email)
		return 1
	except:
		print 'Forneça um e-mail válido'
		return 0

def cadastrar_sysadm():
	'''
    Adiciona um cadastro em sysadm.txt
    '''

	texto = open('sysadm.txt','r').read()
	duplicado = False
	email = raw_input('Digite o e-mail do SYSADM: ') 
	while not email_validator(email):
		email = raw_input('Digite o e-mail do SYSADM: ')
	with open('sysadm.txt','a') as f:
		if len(texto):
			for linha in texto.split('\n'):
				if email.lower() in linha:
					duplicado = True
		if not duplicado:
			f.write('{}\n'.format(email.lower()))
		else:
			print 'E-mail já cadastrado'

def remover_sysadm():
	'''
    Remove um cadastro em sysadm.txt
    '''

	texto = open('sysadm.txt','r').read()
	achou_email = False
	if len(texto):
		email = raw_input('Digite o e-mail do SYSADM que deseja remover: ') 
		while not email_validator(email):
			email = raw_input('Digite o e-mail do SYSADM que deseja remover: ')
		novo = []
		for linha in texto.split('\n'):
			if email.lower() not in linha:
				novo.append(linha)
			else:
				achou_email = True
		if achou_email:
			novo = '\n'.join(novo)
			with open('sysadm.txt','w') as f:
				f.write(novo)
		else:
			print 'E-mail não encontrado'
	else:
		print 'Nenhum SYSADM cadastrado'


