class CategoryManager:
    def __init__(self, db):
        self.db = db
        if "categories" not in db:
            # Initialize a list of categories if it doesn't exist
            db["categories"] = []

    def add_category(self):
        """Adds a new category."""
        print("\n--- ADD CATEGORY ---")
        name = input("Category Name: ")
        description = input("Description (optional): ")

        cid = len(self.db["categories"]) + 1
        self.db["categories"].append({
            "id": cid,
            "name": name,
            "description": description
        })
        print(f"Category '{name}' added with ID: {cid}!")

    def view_categories(self):
        """Displays a list of all categories."""
        print("\n=== CATEGORY LIST ===")
        if not self.db["categories"]:
            print("No categories found.")
            return
            
        for c in self.db["categories"]:
            print(f"[{c['id']}] {c['name']}")
            if c.get('description'):
                print(f"    Description: {c['description']}")
            print("-------------------------------")