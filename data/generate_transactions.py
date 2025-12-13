import csv
import random
from datetime import datetime, timedelta

transaction_id = 1

with open("transactions.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["transaction_id", "customer_id", "product_id", "amount", "timestamp"])
    
    for customer_id in range (1, 201):
        num_tx = random.randint(1, 5)
        
        for _ in range(num_tx):
            product_id = random.randint(100, 120)
            amount = round(random.uniform(10, 300), 2)
            days_ago = random.randint(0, 730)
            timestamp = datetime.now() - timedelta(days=days_ago)
            
            writer.writerow([transaction_id, customer_id, product_id, amount, timestamp])
            transaction_id += 1