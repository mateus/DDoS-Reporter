# -*- coding: utf-8 -*- 

#Email(gmail) e senha do email que enviará o alerta de ataques (servidor)
EMAIL_PASSWORD = ['servidor@gmail.com', 'senha']

#Lista de emails de SYSADMs 
SYSADM = ['ddosreporter@gmail.com', ]

#Limite de requisições para um único IP 
LIMITE_REQUISICOES_POR_IP = 4

#Limite de requisições distintas que o servidor por aguentar
LIMITE_REQUISICOES_TOTAL = 18

#Arquivo de log do apache (Default -> /var/log/apache2/access.log)
ARQUIVO_DE_LOG = 'arquivo'

#Bloquear IPs para que não mais receber requisições
BLOQUEAR_ATAQUES = True 

#Regra de iptables para bloquear IPs 
#(Default -> iptables -D INPUT -s <ip> -j DROP)
IPTABLES = 'iptables -D INPUT -s <ip> -j DROP'