import json
import random
import time
from datetime import datetime
from faker import Faker

fake = Faker()

# Sample log sources
sources = ["firewall", "ids", "application"]
events = {
    "firewall": ["Blocked IP: {ip}", "Port scan detected from {ip}"],
    "ids": ["Intrusion attempt: {ip} on port {port}", "Malware signature match"],
    "application": ["Failed login for user {user}", "SQL injection attempt"]
}

def generate_log(source):
    event = random.choice(events[source])
    log = {
        "timestamp": datetime.utcnow().isoformat(),
        "source": source,
        "event": event.format(
            ip=fake.ipv4(),
            port=random.randint(1, 65535),
            user=fake.user_name()
        ),
        "severity": random.choice(["low", "medium", "high"]),
        "ip": fake.ipv4()
    }
    return log

def main():
    log_file = "logs/security_logs.log"
    with open(log_file, "a") as f:
        for _ in range(100):  # Generate 100 sample logs
            source = random.choice(sources)
            log = generate_log(source)
            f.write(json.dumps(log) + "\n")
            time.sleep(0.1)  # Simulate real-time generation
    print(f"Generated logs in {log_file}")

if __name__ == "__main__":
    main()
