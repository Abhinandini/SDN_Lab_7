import subprocess
import shlex
import time


output = subprocess.check_output(shlex.split("""sudo tshark -f "(host 192.168.56.101 and tcp port 59454)" -i enp0s8 -d tcp.port==6653,openflow -O openflow_v4 -Y "((openflow_v4.type == 10))" -c 100"""))
print ("\nThreshold Reached")
subprocess.call(shlex.split("""sudo iptables -A INPUT -s 192.168.56.101 -d 192.168.56.102 -p tcp --sport 59454 --dport 6653 -j REJECT"""))
subprocess.call(shlex.split("""sudo iptables -L INPUT"""))
#time.sleep(10)
#subprocess.call(shlex.split("""sudo iptables -D INPUT -s 192.168.56.101 -d 192.168.56.102 -p tcp --dport 59454 -j REJECT"""))
#subprocess.call(shlex.split("""sudo iptables -L INPUT"""))
