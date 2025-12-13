import csv
import random
from datetime import datetime, timedelta

event_types = ["login", "view_product", "add_to_cart", "purchase", "logout"]

event_id = 1

with open("event.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["event_id", "customer_id", "event_type", "timestamp"])
    
    for _ in range(1000):
        customer_id = random.randint(1, 201)
        event_type = random.choice(event_types)
        days_ago = random.randint(0, 730)
        timestamp = datetime.now() - timedelta(days=days_ago)
        
        writer.writerow([event_id, customer_id, event_type, timestamp])
        event_id += 1