# SUPPLIERS TABLE

import re
from faker import Faker
import random
import csv

num_suppliers = 50

fake = Faker()

# I added the "Payment Term" column to simulate real-world supplier relationships, as businesses typically
# have varying payment agreements. This allows for a more robust analysis of cash flow, supplier payment patterns, 
# and potential discount benefits. The distribution reflects common industry practices 

payment_terms_distribution = {
    "Net 30": 18,
    "Net 60": 8,
    "Net 90": 3,
    "Payment in Advance (PIA)": 5,
    "Cash on Delivery (COD)": 5,
    "2/10 Net 30": 3, 
    "1/15 Net 60": 2,
    "Net 10": 2, 
    "Net 15": 5,
    "Mixed/Custom Terms": 3
}

def generate_phone_number():
    # Generate a raw phone number using Faker
    phone_number = fake.phone_number()
    
    # Remove any non-numeric characters
    cleaned = re.sub(r'[^\d]', '', phone_number)
    
    # Ensure the phone number is exactly 10 digits long
    if len(cleaned) < 10:
        cleaned = cleaned.zfill(10)  # Pad with zeros if it's too short
    elif len(cleaned) > 10:
        cleaned = cleaned[-10:]  # Keep the last 10 digits if it's too long
    
    # Format the phone number in the US standard format with a leading +1
    formatted = f"+1-{cleaned[0:3]}-{cleaned[3:6]}-{cleaned[6:]}"
    
    return formatted

# Create a list with the correct number of each payment term
payment_terms_list = []
for term, count in payment_terms_distribution.items():
    payment_terms_list.extend([term] * count)

# Shuffle the list to randomly assign payment terms
random.shuffle(payment_terms_list)

# Track unique supplier contact information
unique_contact_info = set()

# Creating suppliers data
with open('/users/mariocardozo/documents/suppliers.csv', 'w', newline='') as csvfile:
    fieldnames = ['SupplierID', 'SupplierName', 'ContactInfo', 'PaymentTerm']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for i in range(1, num_suppliers + 1):
        contact_info = generate_phone_number()  # Reusing the function to ensure consistent phone numbers
        
        # Ensure the contact info is unique
        while contact_info in unique_contact_info:
            contact_info = generate_phone_number()  # Regenerate if there's a duplicate
        
        unique_contact_info.add(contact_info)
        
        # Assign payment term from the shuffled list
        payment_term = payment_terms_list.pop()  # Get a payment term from the list
        
        writer.writerow({
            'SupplierID': i,
            'SupplierName': fake.company(),
            'ContactInfo': contact_info,  # Use the generated phone number
            'PaymentTerm': payment_term # Use the created list
        })