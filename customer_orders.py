# ===============================
# PART 1: STORE CUSTOMER ORDERS
# ===============================

# List of customer names
customer_names = ["Amro", "John", "David", "Sandra", "Sophia"]

# Main category per customer (as requested)
customer_main_category = {
    "Amro": "Electronics",
    "John": "Media",
    "David": "Furniture",
    "Sandra": "Beauty",
    "Sophia": "Toys"
}

# Orders stored as tuples:
# (customer_name, product, price, category)
orders = [
    ("Amro", "Laptop", 85, "Electronics"),
    ("Amro", "Headphones", 30, "Electronics"),
    ("Amro", "T-Shirt", 25, "Clothing"),

    ("John", "Book", 15, "Media"),
    ("John", "Streaming Subscription", 20, "Media"),
    ("John", "Smartwatch", 60, "Electronics"),

    ("David", "Office Chair", 75, "Furniture"),
    ("David", "Desk Lamp", 35, "Furniture"),

    ("Sandra", "Skincare Set", 55, "Beauty"),
    ("Sandra", "Perfume", 70, "Beauty"),

    ("Sophia", "Lego Set", 45, "Toys"),
    ("Sophia", "Doll", 25, "Toys")
]

# Dictionary: customer -> list of ordered products
customer_products = {name: [] for name in customer_names}

for cust, product, price, category in orders:
    customer_products[cust].append(product)

print(customer_products)

# ===================================
# PART 2: CLASSIFY PRODUCTS BY CATEGORY
# ===================================

# Product -> Category mapping
product_to_category = {}

for cust, product, price, category in orders:
    product_to_category[product] = category

# Unique product categories using set
unique_categories = set(product_to_category.values())

print("Available Categories:")
for cat in unique_categories:
    print(cat)

# ===================================
# PART 3: ANALYZE CUSTOMER ORDERS
# ===================================

# Calculate total spending per customer
customer_total_spend = {name: 0 for name in customer_names}

for cust, product, price, category in orders:
    customer_total_spend[cust] += price

# Classification logic
def classify_customer(total):
    if total > 100:
        return "High-value buyer"
    elif 50 <= total <= 100:
        return "Moderate buyer"
    else:
        return "Low-value buyer"

# Store classification
customer_classification = {}

for name in customer_names:
    customer_classification[name] = classify_customer(customer_total_spend[name])

print(customer_total_spend)
print(customer_classification)

# ===================================
# PART 4: GENERATE BUSINESS INSIGHTS
# ===================================

# Total revenue per category
category_revenue = {}

for cust, product, price, category in orders:
    category_revenue[category] = category_revenue.get(category, 0) + price

print("Revenue by Category:")
print(category_revenue)

# Unique products using set
unique_products = {product for cust, product, price, category in orders}

print("Unique Products:")
print(unique_products)

# List comprehension:
# Customers who purchased Electronics
electronics_customers = list({
    cust for cust, product, price, category in orders
    if category == "Electronics"
})

print("Customers who bought Electronics:")
print(electronics_customers)

# Top 3 highest-spending customers
top_customers = sorted(
    customer_total_spend.items(),
    key=lambda x: x[1],
    reverse=True
)[:3]

print("Top 3 Customers:")
print(top_customers)

# ===================================
# PART 5: ORGANIZE AND DISPLAY DATA
# ===================================

# Summary of spending + classification
print("\nCustomer Summary")
for name in customer_names:
    print(name,
          "| Total:", customer_total_spend[name],
          "|", customer_classification[name])

# Build customer -> categories dictionary
customer_categories = {name: set() for name in customer_names}

for cust, product, price, category in orders:
    customer_categories[cust].add(category)

# Customers who purchased multiple categories
multi_category_customers = [
    cust for cust in customer_names
    if len(customer_categories[cust]) > 1
]

print("\nCustomers with multiple categories:")
print(multi_category_customers)

# Customers who bought BOTH electronics and clothing
electronics_set = {
    cust for cust in customer_names
    if "Electronics" in customer_categories[cust]
}

clothing_set = {
    cust for cust in customer_names
    if "Clothing" in customer_categories[cust]
}

common_customers = electronics_set.intersection(clothing_set)

print("\nCustomers who bought Electronics and Clothing:")
print(common_customers)
