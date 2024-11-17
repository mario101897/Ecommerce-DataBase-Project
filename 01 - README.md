E-Commerce Dataset Journey: Thoughts, Challenges, and Insights

---------------------------------------------------------------------------------------------------------

What This Is About

This project started as a way to showcase my SQL and Python skills but quickly grew into something much more complex. The idea was simple: create a simulated dataset reflecting a year of operations for an e-commerce business. But once I got into the details, I realized just how much thought goes into making data look real. Here’s my journey of building this dataset—complete with the hurdles I faced and what I learned along the way.

---------------------------------------------------------------------------------------------------------

The Dataset in a Nutshell

Imagine an online store selling Electronics, Clothing, Home & Kitchen goods, Books, and Sports equipment. To make this come to life, I created eight tables:
Products
Suppliers
Customers
Orders
Order Details
Inventory
Inventory Transactions
Inventory Snapshots

Each table connects to the others like puzzle pieces, creating a realistic simulation of e-commerce activity.

---------------------------------------------------------------------------------------------------------

How the Tables Came Together

Products: Naming the Unnamable
I started with 500 unique products divided into five categories. Coming up with realistic names was harder than I thought. Random combinations gave me some hilariously bad results, like "Smart Yoga Mat" and "Luxury Screwdriver." Eventually, I built separate lists of adjectives and nouns for each category, which made the names sound much better.
Another challenge was pricing. Electronics needed higher price ranges, while Books and Sports equipment were on the cheaper side. Balancing this across 500 items took some trial and error.

Suppliers: Adding Character
I gave each product a supplier and made sure suppliers specialized in specific categories. This made the data feel more natural, like a real business with distinct partnerships. To add depth, I included payment terms like "Net 30" or "Cash on Delivery." These small details made a surprising difference in how “real” the dataset felt.

Customers: Matching Names and Emails
Generating 2,500 customer profiles taught me one thing: details matter. At first, the emails didn’t match the names, which looked weird. Fixing this and standardizing phone numbers felt tedious, but in the end, it gave the data the polish it needed.

Orders: Making Data Dynamic
Orders were my way of showing customer activity over the year. I quickly realized that a static number of orders per customer wouldn’t work. Instead, I introduced repeat customers—some ordering regularly, others just once. This uneven distribution brought the dataset to life.

Order Details: Tying It All Together
Each order included 1 to 5 products, with quantities pulled from the Products table to ensure consistency. Linking prices dynamically from the Products table felt like a small victory—it ensured everything stayed accurate, even if I updated the product data.

Inventory: The Hard Part
This table turned out to be the most challenging. Stock levels had to reflect both sales and restocking events, which meant I couldn’t just plug in random numbers. I had to think through thresholds, delays for restocking, and realistic starting quantities. Some products even had zero initial stock, which added complexity.

Inventory Transactions: Tracking Every Move
Logging every sale and restock brought its own headaches. I wanted restocking delays to feel real, so I added variation—restocks would arrive 2 to 10 days after stock dipped too low. Adding randomness to restocking quantities (rounded to the nearest 10) made it feel even more organic.

Inventory Snapshots: Telling the Story
Weekly snapshots showed how stock levels changed over time. My first attempt failed because I didn’t properly link sales and restocking to the snapshots. Once I fixed this, the snapshots became a powerful tool for analyzing trends.

---------------------------------------------------------------------------------------------------------

Lessons Along the Way

Realism is Hard: It’s easy to generate random numbers, but making them believable takes thought. Details like matching customer emails to names or ensuring price ranges fit categories are worth the effort.

Relational Integrity is Key: Linking data across tables without introducing errors is challenging but essential. Dynamic relationships (like pulling prices from the Products table) made the dataset feel cohesive.
Iterate, Iterate, Iterate: My first versions of almost everything failed—bad names, nonsensical stock levels, you name it. Each iteration made the data stronger.

---------------------------------------------------------------------------------------------------------

What I’d Do Next

Add Complexity: Include promotional events, regional differences, or supplier lead times for more nuanced analysis.

Automate with AI: Use machine learning to simulate customer behavior, restocking trends, or even product popularity.

Expand the Scope: Add more product categories or extend the timeframe to two or three years.

---------------------------------------------------------------------------------------------------------

Wrapping Up

This project was a deep dive into the art of dataset creation. It taught me how to think critically about data structure, maintain relational integrity, and simulate real-world scenarios. What started as a technical exercise turned into an exploration of what makes data feel authentic—and how small details can make all the difference.
