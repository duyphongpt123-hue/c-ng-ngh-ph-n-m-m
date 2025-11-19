class StaffManager:
    def __init__(self, db):
        self.db = db

    def staff_menu(self, order_manager, product_manager):
        print("\n--- STAFF MENU ---")
        while True:
            print("1. View orders")
            print("2. Update stock")
            print("0. Exit")
            c = input("Choose: ")

            if c == "1":
                for o in self.db["orders"]:
                    print(o)
            elif c == "2":
                pid = int(input("Product ID: "))
                qty = int(input("New stock: "))
                for p in self.db["products"]:
                    if p["id"] == pid:
                        p["stock"] = qty
                        print("Stock updated.")
            elif c == "0":
                break
