# ORDERS

import random
import csv
from datetime import datetime, timedelta
import pandas as pd

# Adjusted parameters for seasonality and base randomness
num_customers = 2500  
num_orders = 2500
base_orders_per_day = 3  # Average number of base orders per day
peak_orders_per_day = 15  # Higher number of orders during peak periods

products = pd.read_csv('products.csv') # take the information from the Products table created by ProductsTable.py

# Define specific "peak" periods like holiday shopping seasons
peak_periods = [
    {"start": datetime(2024, 11, 25), "end": datetime(2024, 12, 26)},  # Black Friday to Christmas
    {"start": datetime(2024, 7, 1), "end": datetime(2024, 7, 10)},     # Summer sales week
    {"start": datetime(2024, 3, 1), "end": datetime(2024, 3, 7)}       # End-of-winter clearance
]

# Function to check if a date falls within any peak period
def is_peak_period(order_date):
    for peak in peak_periods:
        if peak["start"] <= order_date <= peak["end"]:
            return True
    return False

# Generate random orders, with more orders during peak periods
def generate_orders():
    orders = []
    current_date = datetime.now() - timedelta(days=365)  # Start from a year ago
    for _ in range(num_orders):
        # Generate a random order date within the last year
        order_date = current_date + timedelta(days=random.randint(0, 364))
        
        # Adjust the number of orders based on whether it's a peak period or not
        if is_peak_period(order_date):
            orders_per_day = random.randint(base_orders_per_day, peak_orders_per_day)
        else:
            orders_per_day = random.randint(1, base_orders_per_day)
        
        # Generate customer and order data for each day
        for _ in range(orders_per_day):
            customer_id = random.choice(range(1, num_customers + 1))
            total_amount = round(random.uniform(20, 1000), 2)  # Random total order amount
            orders.append({
                'OrderID': len(orders) + 1,
                'CustomerID': customer_id,
                'OrderDate': order_date.strftime('%Y-%m-%d'),
                'TotalAmount': total_amount
            })
    
    return orders

# Generate the OrderDetails table (same as before, using product prices from the product list)
def generate_order_details(orders, products):
    order_details = []
    for order in orders:
        order_id = order['OrderID']
        num_products_in_order = random.randint(1, 5)  # Each order will have 1 to 5 products
        
        for _ in range(num_products_in_order):
            product = random.choice(products)  # Select a random product
            product_id = product['ProductID']
            price = product['Price']  # Fetch the price from the product object
            quantity = random.randint(1, 5)  # Generate a random quantity of the product
            
            # Add the order details
            order_details.append({
                'OrderID': order_id,
                'ProductID': product_id,
                'Quantity': quantity,
                'Price': price  # Use the price from the product object
            })
    
    return order_details

# Now we can generate the orders with more realistic seasonal trends
orders = generate_orders()

# Generate OrderDetails using the orders and products lists
order_details = generate_order_details(orders, products)

# (Write the orders and order_details to CSV or display, same as before)

# Step 3: Write the Orders data to a CSV file
with open('/users/mariocardozo/documents/orders.csv', 'w', newline='') as csvfile:
    fieldnames = ['OrderID', 'CustomerID', 'OrderDate', 'TotalAmount']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for order in orders:
        writer.writerow(order)

# Step 4: Write the OrderDetails data to a CSV file
with open('/users/mariocardozo/documents/order_details.csv', 'w', newline='') as csvfile:
    fieldnames = ['OrderID', 'ProductID', 'Quantity', 'Price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for detail in order_details:
        writer.writerow(detail)
