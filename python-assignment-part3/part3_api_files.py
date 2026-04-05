#Task 1 — File Read & Write Basics

file_name = "python_notes.txt"

file = open(file_name, "w", encoding="utf-8")

file.write("Topic 1: Variables store data. Python is dynamically typed.\n")
file.write("Topic 2: Lists are ordered and mutable.\n")
file.write("Topic 3: Dictionaries store key-value pairs.\n")
file.write("Topic 4: Loops automate repetitive tasks.\n")
file.write("Topic 5: Exception handling prevents crashes.\n")

file.close()

print("File written successfully.")

file = open(file_name, "a", encoding="utf-8")

file.write("Topic 6: Functions help reuse code.\n")
file.write("Topic 7: Modules help organise code.\n")

file.close()

print("Lines appended.")

print("\nReading file:\n")

file = open(file_name, "r", encoding="utf-8")
lines = file.readlines()
file.close()

count = 1
for line in lines:
    print(str(count) + ". " + line.strip())
    count += 1

print("\nTotal lines:", len(lines))

keyword = input("\nEnter keyword to search: ").lower()

found = False

for line in lines:
    if keyword in line.lower():
        print(line.strip())
        found = True

if found == False:
    print("No matching lines found.")

#Task 2 — API Integration

import requests

base_url = "https://dummyjson.com/products"

response = requests.get(f"{base_url}?limit=20")

if response.status_code == 200:
    data = response.json()
    products = data["products"]

    print("All 20 Products:\n")
    print(f"{'ID':<4} | {'Title':<30} | {'Category':<15} | {'Price':<10} | {'Rating':<6}")
    print("-" * 78)

    for product in products:
        print(
            f"{product['id']:<4} | "
            f"{product['title'][:30]:<30} | "
            f"{product['category']:<15} | "
            f"${product['price']:<9} | "
            f"{product['rating']:<6}"
        )

    filtered_products = []

    for product in products:
        if product["rating"] >= 4.5:
            filtered_products.append(product)

    filtered_products.sort(key=lambda x: x["price"], reverse=True)

    print("\nProducts with rating >= 4.5 sorted by price (highest to lowest):\n")
    print(f"{'ID':<4} | {'Title':<30} | {'Category':<15} | {'Price':<10} | {'Rating':<6}")
    print("-" * 78)

    for product in filtered_products:
        print(
            f"{product['id']:<4} | "
            f"{product['title'][:30]:<30} | "
            f"{product['category']:<15} | "
            f"${product['price']:<9} | "
            f"{product['rating']:<6}"
        )

else:
    print("Failed to fetch products.")


print("\nLaptops Category:\n")

laptop_response = requests.get(f"{base_url}/category/laptops")

if laptop_response.status_code == 200:
    laptop_data = laptop_response.json()
    laptops = laptop_data["products"]

    for laptop in laptops:
        print(f"{laptop['title']} - ${laptop['price']}")
else:
    print("Failed to fetch laptops.")


print("\nPOST Request Result:\n")

new_product = {
    "title": "My Custom Product",
    "price": 999,
    "category": "electronics",
    "description": "A product I created via API"
}

post_response = requests.post(
    f"{base_url}/add",
    json=new_product
)

if post_response.status_code in [200, 201]:
    print(post_response.json())
else:
    print("Failed to add product.")
    print("Status code:", post_response.status_code)

#Task 3 — Exception Handling

import requests


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"


print("Part A")
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))


def read_file_safe(filename):
    try:
        file = open(filename, "r", encoding="utf-8")
        content = file.read()
        file.close()
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        print("File operation attempt complete.")


print("\nPart B")
print(read_file_safe("python_notes.txt"))
print(read_file_safe("ghost_file.txt"))


base_url = "https://dummyjson.com/products"

print("\nPart C")

try:
    response = requests.get(base_url + "?limit=20", timeout=5)

    if response.status_code == 200:
        data = response.json()
        products = data["products"]

        print("\nAll 20 Products:")
        print("ID  | Title                          | Category       | Price      | Rating")
        print("----|--------------------------------|----------------|------------|--------")

        for product in products:
            print(
                f"{product['id']:<3} | "
                f"{product['title'][:30]:<30} | "
                f"{product['category']:<14} | "
                f"${product['price']:<10} | "
                f"{product['rating']}"
            )

        filtered_products = []

        for product in products:
            if product["rating"] >= 4.5:
                filtered_products.append(product)

        filtered_products.sort(key=lambda x: x["price"], reverse=True)

        print("\nFiltered Products:")
        print("ID  | Title                          | Category       | Price      | Rating")
        print("----|--------------------------------|----------------|------------|--------")

        for product in filtered_products:
            print(
                f"{product['id']:<3} | "
                f"{product['title'][:30]:<30} | "
                f"{product['category']:<14} | "
                f"${product['price']:<10} | "
                f"{product['rating']}"
            )

    else:
        print("Could not fetch products.")

except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")
except requests.exceptions.Timeout:
    print("Request timed out. Try again later.")
except Exception as e:
    print("Error:", e)


try:
    laptop_response = requests.get(base_url + "/category/laptops", timeout=5)

    print("\nLaptops:")

    if laptop_response.status_code == 200:
        laptop_data = laptop_response.json()
        laptops = laptop_data["products"]

        for laptop in laptops:
            print(laptop["title"], "-", "$" + str(laptop["price"]))
    else:
        print("Could not fetch laptops.")

except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")
except requests.exceptions.Timeout:
    print("Request timed out. Try again later.")
except Exception as e:
    print("Error:", e)


new_product = {
    "title": "My Custom Product",
    "price": 999,
    "category": "electronics",
    "description": "A product I created via API"
}

try:
    post_response = requests.post(base_url + "/add", json=new_product, timeout=5)

    print("\nPOST Request Result:")

    if post_response.status_code == 200 or post_response.status_code == 201:
        print(post_response.json())
    else:
        print("Could not add product.")

except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")
except requests.exceptions.Timeout:
    print("Request timed out. Try again later.")
except Exception as e:
    print("Error:", e)


print("\nPart D")

while True:
    user_input = input("Enter a product ID to look up (1–100), or 'quit' to exit: ")

    if user_input.lower() == "quit":
        print("Program ended.")
        break

    try:
        product_id = int(user_input)

        if product_id < 1 or product_id > 100:
            print("Please enter a number between 1 and 100.")
            continue

        try:
            product_response = requests.get(base_url + "/" + str(product_id), timeout=5)

            if product_response.status_code == 404:
                print("Product not found.")
            elif product_response.status_code == 200:
                product = product_response.json()
                print("Title:", product["title"])
                print("Price: $" + str(product["price"]))
            else:
                print("Something went wrong.")

        except requests.exceptions.ConnectionError:
            print("Connection failed. Please check your internet.")
        except requests.exceptions.Timeout:
            print("Request timed out. Try again later.")
        except Exception as e:
            print("Error:", e)

    except ValueError:
        print("Invalid input. Please enter a valid number or 'quit'.")

#Task 4 — Logging to File

from datetime import datetime
import requests

log_file = "error_log.txt"

def log_error(function_name, error_type, message):
    file = open(log_file, "a", encoding="utf-8")

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file.write(f"[{time}] ERROR in {function_name}: {error_type} — {message}\n")

    file.close()


try:
    requests.get("https://this-host-does-not-exist-xyz.com/api", timeout=5)
except requests.exceptions.ConnectionError as e:
    print("Connection error triggered.")
    log_error("fetch_products", "ConnectionError", str(e))


try:
    response = requests.get("https://dummyjson.com/products/999", timeout=5)

    if response.status_code != 200:
        print("HTTP error triggered.")
        log_error(
            "lookup_product",
            "HTTPError",
            f"{response.status_code} Not Found for product ID 999"
        )

except Exception as e:
    log_error("lookup_product", "Exception", str(e))


print("\nError Log Contents:\n")

file = open(log_file, "r", encoding="utf-8")
print(file.read())
file.close()