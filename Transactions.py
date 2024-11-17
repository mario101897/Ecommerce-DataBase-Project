# TRANSACTION LOG AND SNAPSHOTS

import pandas as pd
import random
from datetime import datetime, timedelta

# Load the Orders and Order Details tables 
orders_df = pd.read_csv('/Users/mariocardozo/documents/orders.csv')
order_details_df = pd.read_csv('/Users/mariocardozo/documents/order_details.csv')

# Simulate initial stock levels for products
products = [{'ProductID': i, 'InitialStock': random.randint(50, 300)} for i in range(1, 501)]
inventory = {product['ProductID']: {'StockQuantity': product['InitialStock']} for product in products}

# Initialize lists for transactions and snapshots
transactions = []
snapshots = []

# Join Orders and Order Details to combine the necessary data
merged_data = pd.merge(order_details_df, orders_df[['OrderID', 'OrderDate']], on='OrderID')

# Function to generate the Inventory Transaction Log
def generate_transaction_log(merged_data, inventory):
    for _, row in merged_data.iterrows():
        order_date = datetime.strptime(row['OrderDate'], '%Y-%m-%d')
        product_id = row['ProductID']
        quantity_sold = row['Quantity']
        
        # Check if there's enough stock for the sale
        if inventory[product_id]['StockQuantity'] >= quantity_sold:
            # Reduce stock
            inventory[product_id]['StockQuantity'] -= quantity_sold
            
            # Log the sale as a transaction
            transactions.append({
                'ProductID': product_id,
                'TransactionType': 'Sale',
                'Quantity': -quantity_sold,  # Negative because it's a sale
                'TransactionDate': order_date.strftime('%Y-%m-%d')
            })

# Function to simulate restocking events with rounded quantities
def simulate_restock(inventory, restock_threshold=50, min_restock=80, max_restock=150, round_to=10):
    for product_id, product_data in inventory.items():
        # If stock falls below the threshold, restock with a rounded quantity
        if product_data['StockQuantity'] < restock_threshold:
            restock_quantity = random.randint(min_restock, max_restock)
            
            # Round the restock quantity to the nearest multiple of 'round_to'
            restock_quantity = round(restock_quantity / round_to) * round_to
            
            inventory[product_id]['StockQuantity'] += restock_quantity
            
            # Log the restock as a transaction
            transactions.append({
                'ProductID': product_id,
                'TransactionType': 'Restock',
                'Quantity': restock_quantity,  # Positive because it's a restock
                'TransactionDate': datetime.now().strftime('%Y-%m-%d')
            })

# Function to generate weekly inventory snapshots
def generate_inventory_snapshots(inventory, interval_days=7):
    current_date = datetime.now()
    for i in range(52):  # 52 weeks in a year
        snapshot_date = current_date - timedelta(weeks=i)
        
        # For each product, store the current stock at the snapshot date
        for product_id, product_data in inventory.items():
            snapshots.append({
                'ProductID': product_id,
                'StockQuantity': product_data['StockQuantity'],
                'SnapshotDate': snapshot_date.strftime('%Y-%m-%d')
            })

# Step 1: Generate Transaction Log by processing sales from merged_data
generate_transaction_log(merged_data, inventory)

# Step 2: Simulate Restock Events after processing sales (with rounded restock amounts)
simulate_restock(inventory, restock_threshold=50, min_restock=80, max_restock=150, round_to=10)

# Step 3: Generate Inventory Snapshots weekly
generate_inventory_snapshots(inventory)

# Convert transactions and snapshots to DataFrames for easy export
transactions_df = pd.DataFrame(transactions)
snapshots_df = pd.DataFrame(snapshots)

# Sort transactions by date before saving to ensure sales and restocks are ordered by date
transactions_df['TransactionDate'] = pd.to_datetime(transactions_df['TransactionDate'])
transactions_df = transactions_df.sort_values(by='TransactionDate')

transactions_df.to_csv('/Users/mariocardozo/documents/inventory_transactions.csv', index=False)
snapshots_df.to_csv('/Users/mariocardozo/documents/inventory_snapshots.csv', index=False)