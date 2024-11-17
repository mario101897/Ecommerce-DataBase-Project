# PRODUCTS TABLE

# To bring variety to the business, I decided to focus on five different product categories. 
# My goal was to create 500 unique product names, which would be quite time-consuming to generate individually. 
# To simplify the process, I selected 10 nouns and 10 adjectives for each category, 
# then combined them in various ways. This approach allowed me to generate 100 unique product names per category efficiently.

import csv
import random

# Define the categories and how many products to generate per category
category_distribution = {
    "Electronics": 100,
    "Clothing": 100,
    "Home & Kitchen": 100,
    "Books": 100,
    "Sports": 100
}

# Define product names and adjectives for each category
adjectives = {
    "Electronics": ["Innovative", "High-Performance", "Advanced", "Compact", "Durable", "Sleek", "Multifunctional", "Energy-Efficient", "User-Friendly", "Reliable"],
    "Clothing": ["Comfortable", "Stylish", "Casual", "Elegant", "Versatile", "Trendy", "Lightweight", "Breathable", "Durable", "Cozy"],
    "Home & Kitchen": ["Efficient", "Space-Saving", "Durable", "Easy-to-Clean", "Modern", "Compact", "High-Quality", "Versatile", "Stylish", "Reliable"],
    "Books": ["Engaging", "Inspiring", "Informative", "Captivating", "Thought-Provoking", "Educational", "Entertaining", "Best-Selling", "Award-Winning", "Classic"],
    "Sports": ["High-Performance", "Durable", "Lightweight", "Professional", "Versatile", "Reliable", "Comfortable", "Quality", "Adjustable", "Sturdy"]
}

nouns = {
    "Electronics": ["Laptop", "Tablet", "Headphones", "Smartwatch", "Digital Camera", "Bluetooth Speaker", "Gaming Console", "Wireless Router", "E-reader", "Portable Charger"],
    "Clothing": ["T-shirt", "Jeans", "Jacket", "Dress", "Sweater", "Skirt", "Shorts", "Blouse", "Hoodie", "Socks"],
    "Home & Kitchen": ["Blender", "Coffee Maker", "Vacuum Cleaner", "Toaster", "Microwave Oven", "Dish Rack", "Cutting Board", "Cookware Set", "Electric Kettle", "Food Processor"],
    "Books": ["Novel", "Cookbook", "Biography", "Textbook", "Travel Guide", "Children's Book", "Poetry Collection", "Graphic Novel", "Mystery Thriller", "Science Fiction Book"],
    "Sports": ["Basketball", "Soccer Ball", "Tennis Racket", "Golf Clubs", "Yoga Mat", "Running Shoes", "Dumbbells", "Skateboard", "Bicycle Helmet", "Football"]
}

# Supplier and pricing parameters
num_suppliers = 50
supplier_ids = range(1, num_suppliers + 1)
supplier_categories = {}  # To store each supplier's category

price_ranges = {
    "Electronics": (100, 1000),
    "Clothing": (20, 200),
    "Home & Kitchen": (50, 500),
    "Books": (10, 50),
    "Sports": (15, 150)
}

unique_product_names = set()  # Track unique names

# Step 1: Assign a single category to each supplier
categories = list(category_distribution.keys())
for supplier_id in supplier_ids:
    supplier_categories[supplier_id] = random.choice(categories)  # Each supplier gets one category

# Step 2: Assign weights to suppliers to determine how many products they supply
supplier_weights = {supplier_id: random.uniform(0.5, 2.0) for supplier_id in supplier_ids}  # Larger suppliers get more weight
total_weight = sum(supplier_weights.values())

# Step 3: Calculate the number of products each supplier will provide
def assign_products_to_suppliers(total_products):
    supplier_product_count = {supplier_id: max(1, int(supplier_weights[supplier_id] / total_weight * total_products)) for supplier_id in supplier_ids}
    
    # Ensure that the total number of products is correct
    assigned_products = sum(supplier_product_count.values())
    
    # If there are unassigned products due to rounding, distribute them
    while assigned_products < total_products:
        supplier_id = random.choice(supplier_ids)
        supplier_product_count[supplier_id] += 1
        assigned_products += 1
    
    # In case we over-assign due to rounding, remove products randomly from suppliers
    while assigned_products > total_products:
        supplier_id = random.choice(supplier_ids)
        if supplier_product_count[supplier_id] > 1:  # Ensure each supplier still provides at least one product
            supplier_product_count[supplier_id] -= 1
            assigned_products -= 1

    return supplier_product_count

# Function to generate unique product names and assign them to suppliers
def generate_unique_product_names(total_products):
    products = []
    product_id = 1
    products_per_category = {category: 0 for category in category_distribution}

    # Precompute all possible product name combinations for each category
    all_product_names = {
        category: [f"{adj} {noun}" for adj in adjectives[category] for noun in nouns[category]]
        for category in category_distribution
    }

    # Assign the number of products for each supplier
    supplier_product_count = assign_products_to_suppliers(total_products)

    # Generate products while ensuring each category gets exactly its assigned limit
    for supplier_id in supplier_ids:
        category = supplier_categories[supplier_id]  # Get the supplier's category
        num_products_for_supplier = supplier_product_count[supplier_id]  # Get the specific number for this supplier

        for _ in range(num_products_for_supplier):
            # Find a category that still has capacity
            available_categories = [cat for cat, count in products_per_category.items() if count < category_distribution[cat]]
            if not available_categories:
                break  # Stop if all categories are filled

            # Pick a random category from those still available
            category = random.choice(available_categories)

            if not all_product_names[category]:
                raise ValueError(f"Ran out of unique product names for category: {category}")

            # Randomly select and remove a product name to guarantee uniqueness
            product_name = random.choice(all_product_names[category])
            all_product_names[category].remove(product_name)

            # Generate product details
            price = round(random.uniform(*price_ranges[category]), 2)
            stock_quantity = random.randint(20, 300)

            # Append the product details to the list
            products.append({
                'ProductID': product_id,
                'ProductName': product_name,
                'Category': category,
                'Price': price,
                'StockQuantity': stock_quantity,
                'SupplierID': supplier_id
            })

            # Increment the count for the category
            products_per_category[category] += 1
            product_id += 1

    return products

# Step 4: Generate 500 unique products
products = generate_unique_product_names(500)

# Step 5: Write the products data to a CSV file
with open('/users/mariocardozo/documents/products.csv', 'w', newline='') as csvfile:
    fieldnames = ['ProductID', 'ProductName', 'Category', 'Price', 'StockQuantity', 'SupplierID']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for product in products:
        writer.writerow(product)