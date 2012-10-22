Project
=======

Final work for the course Python for Linux Administrators provided by Instituto Federal de Educação, Ciência e Tecnologia do Sudeste de Minas, Campus Barbacena. Developed by Mateus Ferreira Silva this project had as theme implement a DoS/DDoS monitor for the web server Apache.


Main topics (basics functionalities):
-------------------------------------

- Implement a real time DoS/DDoS monitor for the web server Apache. The program should periodically read the access logs of the web server, and in case of anomalies (mass access), detect the IP or IPs involved in the attack.
- When an attack is detected, it should sent an email to the network administrator (given in the configuration file) warning that a DoS or DDoS attack is ongoing and the IPs involved.
- In the configuration file should be possible to determine, in addition to information such as email, if the IP(s) that is(are) conducting the attack is(are) going to be blocked by a *DROP* rule of *iptables*.