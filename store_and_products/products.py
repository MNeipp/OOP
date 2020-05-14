class Products:
    id_counter = 0
    def __init__(self, price, product_name, category_name):
        self.price = float(price)
        self.product_name = product_name
        self.category_name = category_name
        self.id = Products.id_counter
        Products.id_counter += 1


    def print_info(self):
        print(f"Price of {self.product_name} is ${self.price}")
        print(f"the ID of {self.product_name} is {self.id}")

    def update_price(self, percent_change, is_increased = True):
        if is_increased is True:
            self.price += self.price * percent_change
            self.price = round(self.price,2)
            return self
        else:
            self.price -= self.price * percent_change
            self.price = round(self.price,2)
            return self
