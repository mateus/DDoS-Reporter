# -*- coding: utf-8 -*- 

#True para enviar emails, False para não enviar
SEND_EMAIL = True

#Email(gmail) e senha do email que enviará o alerta de ataques (servidor)
EMAIL_PASSWORD = ('email@gmail.com', 'senha')

#Lista de emails de SYSADMs 
SYSADM = ('ddosreporter@gmail.com', )

#Limite de requisições para um único IP 
LIMITE_REQUISICOES_POR_IP = 200

#Limite de requisições distintas que o servidor por aguentar
LIMITE_REQUISICOES_TOTAL = 180

#Arquivo de log do apache (Default -> /var/log/apache2/access.log)
ARQUIVO_DE_LOG = '/var/log/apache2/access.log'

#Bloquear IPs para que não mais receber requisições
BLOQUEAR_ATAQUES = True 

#Regra de iptables para bloquear IPs 
#(Default -> iptables -D INPUT -s <ip> -j DROP)
IPTABLES = 'iptables -I INPUT -s <ip> -j DROP'

# Lista de IPs bloqueados:
# iptables -L INPUT -n --line-numbers
# Liberar IPs usando número de identificação da lista:
# iptables -D INPUT <numero>
