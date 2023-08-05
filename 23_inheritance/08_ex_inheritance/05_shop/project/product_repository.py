from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for el in self.products:
            if el.name == product_name:
                return el

    def remove(self, product_name):
        searched_product = self.find(product_name)
        if searched_product is not None:
            self.products.remove(searched_product)

    def __repr__(self):
        result = ''
        for el in self.products:
            result += f"{el.name}: {el.quantity}\n"
        return result.strip()

