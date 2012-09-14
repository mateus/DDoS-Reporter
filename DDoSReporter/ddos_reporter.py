#!/usr/bin/python
# -*- coding: utf-8 -*- 

# import sysadm_controle# sysadm_controle.cadastrar_sysadm() # sysadm_controle.remover_sysadm()
import send_email
import time
import re
import settings
import os

class Ddos_reporter():

    def start_monitoring(self):
        print '\nMonitorando...'
        #Capturando tamanho do arquivo para ler a partir do próximo bloco de bytes
        fileBytePos = os.path.getsize(settings.ARQUIVO_DE_LOG)

        #Objeto que enviará emails caso haja um ataque
        email_sender = send_email.Send_Email()

        while True:
            with open(settings.ARQUIVO_DE_LOG, 'r') as _file:
                #Posicionando para ler a partir do byte anterior
                _file.seek(fileBytePos) 

                #Lendo novos registros do log, separando por '\n'
                data = _file.read()
                # data = data.split('\n')

                #Capturando somente o(s) IP(s) de cada cliente
                access_list = re.findall(r'(.+?) .+?\n', data)
               
                #Verifica se house um estouro no limite de requisições possíveis por segundo
                if len(access_list) > settings.LIMITE_REQUISICOES_TOTAL:
                    ips = []
                    for ip in set(access_list):
                        ips.append(ip)
                    ips = ', '.join(ips)
                    print 'Estouro do limite de {} requisições por segundo (Ataque DDoS)\nIPs:'.format(
                        settings.LIMITE_REQUISICOES_TOTAL), ips

                #Contando numero de requisições para cada IP
                ipcounter = []
                for ip in set(access_list):
                    total = access_list.count(ip)
                    if total > settings.LIMITE_REQUISICOES_POR_IP:
                        print 'IP:', ip, 'TOTAL:', access_list.count(ip), 'ALERTA DE ATAQUE'
                        ipcounter.append(ip)
                    else:
                        print 'IP:', ip, 'TOTAL:', access_list.count(ip)
                
                #Define tipo de ataque
                if len(ipcounter) > 0 and len(access_list) < settings.LIMITE_REQUISICOES_TOTAL:
                    if len(ipcounter) > 1:
                        ips = []
                        for ip in set(ipcounter):
                            ips.append(ip)
                        ips = ', '.join(ips)
                        print 'Ataque DDoS - IPs:', ips
                        print 'Enviando email para o(s) SYSADM(s)...'
                        if len(settings.SYSADM) == 0:
                            print 'Nenhum email de SYSADM cadastrado'
                        else:
                            for email in settings.SYSADM:
                                email_sender.send_email(email, ipcounter, 1)
                    else:
                        print 'Ataque DoS - IP', ipcounter[0]
                        print 'Enviando email para o(s) SYSADM(s)...'
                        if len(settings.SYSADM) == 0:
                            print 'Nenhum email de SYSADM cadastrado'
                        else:
                            for email in settings.SYSADM:
                                email_sender.send_email(email, ipcounter[0], 0)

                #Saltar uma linha
                if data != '':
                    print ''

                #Tamanho atual do arquivo
                fileBytePos = _file.tell()
                
                #Delay de 1 segundo até a próxima leitura
                try:
                    time.sleep(1)
                except:
                    print '\nMonitoramento finalizado'
                    exit()
            
    def print_settings(self):
        print 'Arquivo de log:',settings.ARQUIVO_DE_LOG
        sysadms = []
        for email in settings.SYSADM:
            sysadms.append(email)
        sysadms = ', '.join(sysadms)
        print 'SYSADMs:', sysadms
        print 'Limite de requisições para um único IP:', settings.LIMITE_REQUISICOES_POR_IP
        print 'Limite de requisições distintas para o servidor:', settings.LIMITE_REQUISICOES_TOTAL
        print 'Iptables:', settings.BLOQUEAR_ATAQUES
        if settings.BLOQUEAR_ATAQUES:
            print 'Regra iptables:', settings.IPTABLES

if __name__== "__main__":
    monitor = Ddos_reporter()
    monitor.print_settings()
    monitor.start_monitoring()