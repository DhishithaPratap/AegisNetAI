import random
import string
import json

# Legitimate brands used as seeds for dynamic generation
LEGIT_BRANDS = ["google", "microsoft", "github", "openai", "paypal", "netflix", "amazon", "apple", "facebook", "twitter"]

# TLD pools
NORMAL_TLDS = ["com", "net", "org", "co", "io"]
SUSPICIOUS_TLDS = ["xyz", "ru", "cc", "top", "work", "click", "info", "biz", "live"]

# Keywords commonly found in phishing campaigns
PHISHING_KEYWORDS = ["secure", "login", "update", "verify", "support", "billing", "account", "security", "signin", "portal"]

def generate_normal_domain():
    """Generates a legitimate brand domain (with optional subdomains)."""
    brand = random.choice(LEGIT_BRANDS)
    tld = random.choice(NORMAL_TLDS)
    # 40% chance of having a common legitimate subdomain
    if random.random() < 0.4:
        subdomain = random.choice(["www", "api", "mail", "docs", "blog"])
        return f"{subdomain}.{brand}.{tld}"
    return f"{brand}.{tld}"

def generate_phishing_domain():
    """Generates phishing domains by combining keywords and brands (e.g., paypal-security-verify.xyz)."""
    brand = random.choice(LEGIT_BRANDS)
    kw1 = random.choice(PHISHING_KEYWORDS)
    kw2 = random.choice(PHISHING_KEYWORDS)
    tld = random.choice(SUSPICIOUS_TLDS)
    
    patterns = [
        f"{brand}-{kw1}",
        f"{kw1}-{brand}",
        f"{brand}-{kw1}-{kw2}"
    ]
    return f"{random.choice(patterns)}.{tld}"

def generate_typosquatting_domain():
    """Generates realistic brand typos (omissions, duplications, transpositions, substitutions)."""
    brand = random.choice(LEGIT_BRANDS)
    tld = random.choice(NORMAL_TLDS) # Typo-squatters usually try to get the original TLD
    brand_chars = list(brand)
    
    typo_type = random.choice(["omission", "duplication", "transposition", "substitution"])
    
    if typo_type == "omission" and len(brand_chars) > 3:
        # Remove a random character in the middle
        brand_chars.pop(random.randint(1, len(brand_chars) - 2))
    elif typo_type == "duplication":
        # Double a random character
        idx = random.randint(0, len(brand_chars) - 1)
        brand_chars.insert(idx, brand_chars[idx])
    elif typo_type == "transposition" and len(brand_chars) > 2:
        # Swap two adjacent characters
        idx = random.randint(0, len(brand_chars) - 2)
        brand_chars[idx], brand_chars[idx+1] = brand_chars[idx+1], brand_chars[idx]
    else: # substitution
        # Replace characters with similar lookalikes (e.g., o -> 0, i -> 1, l -> 1)
        lookalikes = {'o': '0', 'i': '1', 'l': '1', 'e': '3', 'a': '4', 's': '5'}
        possible_indices = [i for i, char in enumerate(brand) if char in lookalikes]
        if possible_indices:
            idx = random.choice(possible_indices)
            brand_chars[idx] = lookalikes[brand[idx]]
        else:
            # Fallback: substitute a random character
            idx = random.randint(0, len(brand_chars) - 1)
            brand_chars[idx] = random.choice(string.ascii_lowercase)
            
    return f"{"".join(brand_chars)}.{tld}"

def generate_random_string_domain():
    """Generates completely random strings (DGA style domains)."""
    length = random.randint(8, 16)
    subdomain = "".join(random.choices(string.ascii_lowercase + string.digits, k=length))
    tld = random.choice(SUSPICIOUS_TLDS)
    return f"{subdomain}.{tld}"

def generate_fake_auth_domain():
    """Generates fake SSO / authentication URLs (e.g., login.microsoft-sso-verify.ru)."""
    brand = random.choice(LEGIT_BRANDS)
    auth_keyword = random.choice(["login", "sso", "auth", "mfa", "secure"])
    tld = random.choice(SUSPICIOUS_TLDS)
    
    patterns = [
        f"{brand}.{auth_keyword}-portal-secure.{tld}",
        f"{auth_keyword}.{brand}-verify.{tld}",
        f"sso-{brand}-login.{tld}"
    ]
    return random.choice(patterns)

def generate_simulated_dns_log():
    """Generates a dynamic DNS event matching one of the five domain categories."""
    
    # Categories of domains we want to simulate
    domain_types = [
        ("Normal Domain", generate_normal_domain),
        ("Phishing Domain", generate_phishing_domain),
        ("Typo-Squatting Domain", generate_typosquatting_domain),
        ("Random String (DGA) Domain", generate_random_string_domain),
        ("Fake Authentication URL", generate_fake_auth_domain)
    ]
    
    category, generator_func = random.choice(domain_types)
    
    # 50% chance of a local/private source IP, 50% chance of a public source IP
    if random.random() < 0.5:
        src_ip = f"192.168.1.{random.randint(1, 255)}"
    else:
        src_ip = f"{random.randint(1, 223)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"
        
    return {
        "src_ip": src_ip,
        "query": generator_func(),
        "record_type": random.choice(["A", "AAAA", "CNAME", "MX", "TXT"]),
        "protocol": random.choice(["DNS", "DoH", "DoT"]),
        "category": category
    }
if __name__ == "__main__":
    print("--- Simulating 5 Random Dynamic DNS Events ---")

    with open("data/dns_logs.json", "a") as file:
        for _ in range(5):
            event = generate_simulated_dns_log()

            file.write(json.dumps(event) + "\n")
            print(json.dumps(event, indent=4))
            print("-" * 46)