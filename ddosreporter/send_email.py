# -*- coding: cp860 -*- 

import getpass
import smtplib
import settings
import re

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.Utils import formatdate

class Send_Email():
    '''
    Class to send email to Gmail domain
    '''

    def email_validator(self, email):
        '''
        Validates an email using regular expression 

        Args: 
            email (str) - Email

        Returns 1 for valid email and 0 for invalid
        '''

        #Verifica integridade do email
        if re.match('^[_A-Za-z0-9-]+(\\.[_A-Za-z0-9-]+)*@[A-Za-z0-9]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$', 
            email) != None:
            return 1
        return 0

    def send_email(self, email, ips, atk=0):
        '''
        Send an email alert informing DDoS / Dos

        Args:
            email (str) - SYSADM email\n
            ips (str) - List of the ips detected\n
            atk (int) - Type of attack detected (0->DoS, 1->DDoS)
        '''

        #Verifica email do SYSADM
        if not self.email_validator(email):
            print email, '- Email inválido'
        #Verifica email do servidor e se existe um SYSADM cadastrado
        elif len(settings.EMAIL_PASSWORD) == 2 and len(settings.SYSADM) > 0:
            if not self.email_validator(settings.EMAIL_PASSWORD[0]):
                print email, '- Email inválido'
            else:
                #Cabeçalho do email
                msg = MIMEMultipart()
                msg['From'] = settings.EMAIL_PASSWORD[0]
                msg['To'] = email
                msg['Date'] = formatdate(localtime=True)

                #Mensagem do email
                if atk == 0:
                    msg['Subject'] = 'Alerta de DoS'
                    message = []
                    message.append(
                        'Identificamos que seu endereço web está sofrendo um ataque DoS do IP {}.'.format(ips))
                    if settings.BLOQUEAR_ATAQUES:
                        message.append(
                            '\n\nO IP foi bloquado seguindo a regra de iptables \"{}\".'.format(settings.IPTABLES))
                    message.append(
                        '\n\niptables -D INPUT <numero>\tEsta mensagem foi gerada automaticamente pelo sistema, não responda este e-mail.')
                    message = ''.join(message)
                    msg.attach( MIMEText(message) )
                elif atk == 1:
                    msg['Subject'] = 'Alerta de DDoS'
                    message = []
                    message.append(
                        'Identificamos que seu endereço web está sofrendo um ataque DDoS dos IPs:\n')
                    for ip in ips:
                        message.append('\n>> {}'.format(ip))
                    if settings.BLOQUEAR_ATAQUES:
                        message.append(
                            '\n\nOs IPs foram bloquados seguindo a regra de iptables \"{}\".'.format(settings.IPTABLES))
                    message.append(
                        '\n\n\tEsta mensagem foi gerada automaticamente pelo sistema, não responda este e-mail.')
                    message = ''.join(message)
                    msg.attach( MIMEText(message) )

                #Enviando email
                try:
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.ehlo()
                    server.login(settings.EMAIL_PASSWORD[0], settings.EMAIL_PASSWORD[1])
                    server.sendmail(settings.EMAIL_PASSWORD[0], email, msg.as_string())
                    if atk == 0:
                        ipEnviar = ips
                    else:
                        ipEnviar = []
                        for ip in ips:
                            ipEnviar.append(ip)
                        ipEnviar = ', '.join(ipEnviar)
                                            
                    print 'Email enviado para {} sobre o ataque dos IPs: {}'.format(email, ipEnviar)
                except:
                    print 'Falha ao enviar email'
                finally:
                    server.close()
        elif len(settings.EMAIL_PASSWORD) == 0:
            print 'Email para enviar os alertas ainda não foi configurado. Verifique o arquivo settings.py'
        else:
            print 'Falha nas variáveis de email informadas. Verifique o arquivo settings.py.'