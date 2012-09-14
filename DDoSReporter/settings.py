# -*- coding: utf-8 -*- 

#Lista de emails de SYSADMs 
SYSADM = ['ddosreporter@gmail.com', ]

#Limite de requisições para um único IP 
LIMITE_REQUISICOES_POR_IP = 2

#Limite de requisições distintas que o servidor por aguentar
LIMITE_REQUISICOES_TOTAL = 15

#Arquivo de log do apache (Default -> /var/log/apache2/access.log)
ARQUIVO_DE_LOG = 'arquivo'

#Bloquear IPs para que não mais entrem na rede
BLOQUEAR_ATAQUES_FORWARD = True 

#Bloquear IPs para que não mais sejam destinados ao IP do Firewall
BLOQUEAR_ATAQUES_INPUT = True 

#Regra de iptables para bloquear IPs para que não mais entrem na rede
#(Default -> iptables -A FORWARD -s <ip> -j DROP)
IPTABLES_FORWARD = 'iptables -A FORWARD -s <ip> -j DROP'

#Regra de iptables para bloquear IPs para que não mais sejam destinados ao IP do Firewall
#(Default -> iptables -D INPUT -s <ip> -j DROP)
IPTABLES_INPUT = 'iptables -D INPUT -s <ip> -j DROP'

# REJECT/DROP << Testar