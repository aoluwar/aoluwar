class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.viewed_products = []
        self.purchased_products = []

    def view_product(self, product):
        self.viewed_products.append(product)

    def purchase_product(self, product):
        self.purchased_products.append(product)

    def __repr__(self):
        return f"User(id={self.user_id}, name='{self.name}')"
