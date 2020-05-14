class Products:
    def __init__(self, price, product_name, category_name):
        self.price = float(price)
        self.product_name = product_name
        self.category_name = category_name
    
    def print_info(self):
        print(f"Price of {self.product_name} is ${self.price}")

    def update_price(self, percent_change, is_increased = True):
        if is_increased is True:
            self.price += self.price * percent_change
            self.price = round(self.price,2)
            return self
        else:
            self.price -= self.price * percent_change
            self.price = round(self.price,2)
            return self

class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.product_list = {}

    def addProduct(self,product, category):
        if category in self.product_list:
            self.product_list[category].append(product)
        else:
            self.product_list[category] = [product]

    def sellProduct(self, product):
        location = (self.product_list[product.category_name].index(product))
        self.product_list[product.category_name].pop(location)

    def availableProducts(self, category = ""):
        if category in self.product_list:
            for product in self.product_list[category]:
                 product.print_info()
        else:
            for category, product_list in self.product_list.items():
                for product in product_list:
                    product.print_info()

    def inflation(self, percent_increase):
        for product_list in self.product_list.values():
            for price in product_list:
                price.update_price(percent_increase)

    def discount(self, category, percent_decrease):
        for product in self.product_list[category]:
            product.update_price(percent_decrease, False)




