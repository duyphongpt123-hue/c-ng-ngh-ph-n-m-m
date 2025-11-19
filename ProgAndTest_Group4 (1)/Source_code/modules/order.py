class OrderManager:
    def __init__(self, db):
        self.db = db

    def checkout(self, user, cart_manager):
        print("\n--- CHECKOUT ---")
        cart = self.db["cart"].get(user["email"], [])
        if not cart:
            print("Cart is empty!")
            return

        total = 0
        for item in cart:
            for p in self.db["products"]:
                if p["id"] == item["product_id"]:
                    total += p["price"] * item["qty"]

        oid = len(self.db["orders"]) + 1
        self.db["orders"].append({
            "id": oid,
            "user": user["email"],
            "items": cart,
            "total": total
        })
        self.db["cart"][user["email"]] = []

        print(f"Order created! Total = ${total}")

    def view_order_history(self, user):
        print("\n--- ORDER HISTORY ---")
        for o in self.db["orders"]:
            if o["user"] == user["email"]:
                print(f"Order {o['id']} - Total: ${o['total']}")

from modules.order_detail import OrderDetail

class OrderManager:
    def __init__(self, db):
        self.db = db

    def checkout(self, user, cart_manager):
        print("\n--- CHECKOUT ---")
        email = user["email"]

        cart = self.db["cart"].get(email, [])
        if not cart:
            print("Cart is empty!")
            return

        order_id = len(self.db["orders"]) + 1
        order_items = []
        total = 0

        for item in cart:
            pid = item["product_id"]
            qty = item["qty"]

            for p in self.db["products"]:
                if p["id"] == pid:
                    unit_price = p["price"]
                    subtotal = qty * unit_price

                    od = OrderDetail(
                        order_id=order_id,
                        product_id=pid,
                        quantity=qty,
                        unit_price=unit_price
                    )
                    order_items.append(od.to_dict())
                    total += subtotal

                    p["stock"] -= qty

        order = {
            "order_id": order_id,
            "user": email,
            "items": order_items,
            "total": total
        }

        self.db["orders"].append(order)
        self.db["cart"][email] = []

        print(f"Order created successfully! Total = {total} VND")
