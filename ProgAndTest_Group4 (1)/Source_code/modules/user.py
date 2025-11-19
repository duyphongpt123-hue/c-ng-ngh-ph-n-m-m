class UserManager:
    def __init__(self, db):
        self.db = db

    def register(self):
        print("\n--- Register Account ---")
        name = input("Full Name: ")
        email = input("Email: ")
        password = input("Password: ")
        role = "customer"

        self.db["users"].append({
            "name": name,
            "email": email,
            "password": password,
            "role": role
        })
        print("Registration successful!")

    def login(self):
        print("\n--- Login ---")
        email = input("Email: ")
        password = input("Password: ")

        for u in self.db["users"]:
            if u["email"] == email and u["password"] == password:
                print("Login successful!")
                return u
        print("Login failed.")
        return None

    def customer_menu(self, product_manager, cart_manager, order_manager):
        print("\n--- CUSTOMER MENU ---")
        print("1. Register")
        print("2. Login")
        c = input("Choose: ")

        if c == "1":
            self.register()
        elif c == "2":
            user = self.login()
            if user:
                while True:
                    print("\n1. View products")
                    print("2. Search product")
                    print("3. Add to cart")
                    print("4. View cart")
                    print("5. Checkout")
                    print("6. Order history")
                    print("0. Logout")
                    ch = input("Choose: ")

                    if ch == "1":
                        product_manager.view_products()
                    elif ch == "2":
                        product_manager.search_product()
                    elif ch == "3":
                        cart_manager.add_to_cart(user)
                    elif ch == "4":
                        cart_manager.view_cart(user)
                    elif ch == "5":
                        order_manager.checkout(user, cart_manager)
                    elif ch == "6":
                        order_manager.view_order_history(user)
                    elif ch == "0":
                        break
