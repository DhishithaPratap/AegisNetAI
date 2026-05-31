import random
import json

# Simulated source and destination IPs

def generate_random_ip():
   
    # Generating 4 octets, each between 0 and 255
    # (Avoiding 0 or 255 as the first octet for standard unicast addresses, but standard 1-254 is commonly used)
    return f"{random.randint(1, 254)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"

# Common TCP ports
ports = [80, 443, 22, 53]

# TCP flags
flags = ["SYN", "ACK", "FIN"]

# Generate simulated packet
packet = {
    "src_ip": generate_random_ip(),
    "dst_ip": generate_random_ip(),
    "port": random.choice(ports),
    "protocol": "TCP",
    "flag": random.choice(flags)
}

# Print packet nicely
#print(json.dumps(packet, indent=4))
with open("data/tcp_logs.json", "a") as file:
    file.write(json.dumps(packet) + "\n")

print(json.dumps(packet, indent=4))
