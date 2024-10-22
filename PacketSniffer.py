from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime
def packet_handler (packet): 
    timestamp = datetime.now()
    if packet.haslayer(IP):
        ip_layer= packet.getlayer(IP)
        print(f"{timestamp}        IP        {ip_layer.src}        {ip_layer.dst}")

    if packet.haslayer(TCP):
        tcp_layer = packet.getlayer(TCP)
        print(f"{timestamp}        TCP             {tcp_layer.sport}                    {tcp_layer.dport}")

    if packet.haslayer(UDP):
        udp_layer = packet.getlayer(UDP)
        print(f"{timestamp}        UDP             {udp_layer.sport}                    {udp_layer.dport}")


print(f"          Date/Time                Protocol                     Source            Destination")

sniff(filter="ip" , prn=packet_handler, store=0)
sniff(filter="tcp" , prn=packet_handler, store=0)
sniff(filter="udp" , prn=packet_handler, store=0)
