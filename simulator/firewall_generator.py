import random
import json

def generate_random_internal_ip():
    """Generates a random private (internal) IPv4 address."""
    # Choose between the three standard private IP ranges
    net_type = random.choice(["10", "172", "192"])
    
    if net_type == "10":
        # Range: 10.0.0.0 - 10.255.255.255
        return f"10.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"
    elif net_type == "172":
        # Range: 172.16.0.0 - 172.31.255.255
        return f"172.{random.randint(16, 31)}.{random.randint(0, 255)}.{random.randint(1, 254)}"
    else:
        # Range: 192.168.0.0 - 192.168.255.255
        return f"192.168.{random.randint(0, 255)}.{random.randint(1, 254)}"

def generate_random_destination_ip():
    """Generates a random public IPv4 address, avoiding private ranges."""
    while True:
        first_octet = random.randint(1, 223)
        # Avoid loopback (127.x.x.x) and private class A (10.x.x.x)
        if first_octet in (10, 127):
            continue
        
        second_octet = random.randint(0, 255)
        # Avoid private class B (172.16.x.x - 172.31.x.x)
        if first_octet == 172 and 16 <= second_octet <= 31:
            continue
        # Avoid private class C (192.168.x.x)
        if first_octet == 192 and second_octet == 168:
            continue
        # Avoid Link-local (169.254.x.x)
        if first_octet == 169 and second_octet == 254:
            continue
            
        third_octet = random.randint(0, 255)
        fourth_octet = random.randint(1, 254)
        
        return f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"

# Common ports
ports = [22, 80, 443, 3389]

# Firewall actions
actions = ["ALLOW", "DENY"]

# Generate simulated firewall event
firewall_log = {
    "src_ip": generate_random_internal_ip(),
    "dst_ip": generate_random_destination_ip(),
    "port": random.choice(ports),
    "protocol": "TCP",
    "action": random.choice(actions)
}

# Print formatted firewall log
if __name__ == "__main__":
    print(json.dumps(firewall_log, indent=4))

import random
import json

def generate_random_internal_ip():
    """Generates a random private (internal) IPv4 address."""
    # Choose between the three standard private IP ranges
    net_type = random.choice(["10", "172", "192"])
    
    if net_type == "10":
        # Range: 10.0.0.0 - 10.255.255.255
        return f"10.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"
    elif net_type == "172":
        # Range: 172.16.0.0 - 172.31.255.255
        return f"172.{random.randint(16, 31)}.{random.randint(0, 255)}.{random.randint(1, 254)}"
    else:
        # Range: 192.168.0.0 - 192.168.255.255
        return f"192.168.{random.randint(0, 255)}.{random.randint(1, 254)}"

def generate_random_destination_ip():
    """Generates a random public IPv4 address, avoiding private ranges."""
    while True:
        first_octet = random.randint(1, 223)
        # Avoid loopback (127.x.x.x) and private class A (10.x.x.x)
        if first_octet in (10, 127):
            continue
        
        second_octet = random.randint(0, 255)
        # Avoid private class B (172.16.x.x - 172.31.x.x)
        if first_octet == 172 and 16 <= second_octet <= 31:
            continue
        # Avoid private class C (192.168.x.x)
        if first_octet == 192 and second_octet == 168:
            continue
        # Avoid Link-local (169.254.x.x)
        if first_octet == 169 and second_octet == 254:
            continue
            
        third_octet = random.randint(0, 255)
        fourth_octet = random.randint(1, 254)
        
        return f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"

# Common ports
ports = [22, 80, 443, 3389]

# Firewall actions
actions = ["ALLOW", "DENY"]

# Generate simulated firewall event
firewall_log = {
    "src_ip": generate_random_internal_ip(),
    "dst_ip": generate_random_destination_ip(),
    "port": random.choice(ports),
    "protocol": "TCP",
    "action": random.choice(actions)
}

# Print formatted firewall log
if __name__ == "__main__":
   # print(json.dumps(firewall_log, indent=4))
   with open("data/firewall_logs.json", "a") as file:
    file.write(json.dumps(firewall_log) + "\n")

print(json.dumps(firewall_log, indent=4))

