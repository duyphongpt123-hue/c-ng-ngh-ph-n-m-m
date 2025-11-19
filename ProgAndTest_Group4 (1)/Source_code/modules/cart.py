class CartManager:
    def __init__(self, db):
        self.db = db
        if "cart" not in db:
            db["cart"] = {}

    def add_to_cart(self, user):
        pid = int(input("Product ID: "))
        quantity = int(input("Quantity: "))

        if user["email"] not in self.db["cart"]:
            self.db["cart"][user["email"]] = []

        self.db["cart"][user["email"]].append({
            "product_id": pid,
            "qty": quantity
        })
        print("Added to cart!")

    def view_cart(self, user):
        print("\n--- YOUR CART ---")
        cart = self.db["cart"].get(user["email"], [])
        for item in cart:
            print(f"Product {item['product_id']} - Qty: {item['qty']}")
