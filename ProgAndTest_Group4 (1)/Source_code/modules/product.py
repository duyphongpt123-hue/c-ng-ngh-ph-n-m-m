class ProductManager:
    def __init__(self, db):
        self.db = db

    def view_products(self):
      print("\n=== PRODUCT LIST ===")
      for p in self.db["products"]:
        print(f"[{p['id']}] {p['name']}")
        print(f"    Price: {p['price']} VND")
        print(f"    Stock: {p['stock']}")
        if 'description' in p:
            print(f"    Description: {p['description']}")
        print("-----------------------------------")



    def search_product(self):
        key = input("Search keyword: ").lower()
        results = [p for p in self.db["products"] if key in p["name"].lower()]
        for p in results:
            print(f"{p['id']} - {p['name']} - ${p['price']}")

    def add_product(self):
      print("\n--- ADD PRODUCT ---")
      name = input("Product Name: ")
      price = float(input("Price: "))
      stock = int(input("Stock: "))
      description = input("Description: ")
      pid = len(self.db["products"]) + 1

      self.db["products"].append({
        "id": pid,
        "name": name,
        "price": price,
        "stock": stock,
        "description": description
    })

    print("Product added successfully!")


    def update_product(self):
        pid = int(input("Product ID to update: "))
        for p in self.db["products"]:
            if p["id"] == pid:
                p["name"] = input("New name: ")
                p["price"] = float(input("New price: "))
                p["stock"] = int(input("New stock: "))
                print("Product updated.")
                return
        print("Product not found.")
