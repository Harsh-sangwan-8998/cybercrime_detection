from scapy.all import sniff, IP, TCP

def packet_callback(packet):
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        print(f"Packet: {ip_layer.src} -> {ip_layer.dst}")
        return {"src": ip_layer.src, "dst": ip_layer.dst}

    if packet.haslayer(TCP):
        tcp_layer = packet[TCP]
        print(f"TCP Packet: {tcp_layer.sport} -> {tcp_layer.dport}")
        return {"src_port": tcp_layer.sport, "dst_port": tcp_layer.dport}

def start_sniffing(count=10):
    sniffed_data = sniff(prn=packet_callback, count=count)
    return [{"src": p[IP].src, "dst": p[IP].dst} for p in sniffed_data if p.haslayer(IP)]
