class ShoppingList:
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []

    def add_item(self, item):
        if item not in self.shopping_list:
            self.shopping_list.append(item)

    def remove_item(self, item):
        try:
            self.shopping_list.remove(item)
        except ValueError:
            print("Item not found.")

    def view_list(self):
        print("\nItems in " + self.list_name + ":")
        for item in self.shopping_list:
            print("- " + item)

pet_store_list = ShoppingList("Pet Store Shopping List")

items_to_add = ["dog food", "frisbee", "bowl", "collars", "flea collars"]
for item in items_to_add:
    pet_store_list.add_item(item)

pet_store_list.remove_item("flea collars")
pet_store_list.add_item("frisbee")
pet_store_list.view_list()

