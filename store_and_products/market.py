from products import Products
from store import Store

BuyLow = Store("BuyLow")
MasonMart = Store("MasonMart")

cereal = Products(2.50, "cereal", "breakfast" )
pastries = Products(3.50, "pastries", "breakfast")
steak = Products(2.25, "steak", "meat")
chicken = Products(2.00, "chicken", "meat")
ham = Products(1.25, "ham", "meat")
apple = Products(.50, "apple", "produce")
banana = Products(.35, "banana", "produce")
milk = Products(2.88, "milk", "dairy")
cheese = Products(3.00, "cheese", "dairy")

BuyLow.addProduct(cheese, "dairy")
BuyLow.addProduct(milk, "dairy")
BuyLow.addProduct(banana, "produce")
BuyLow.addProduct(apple, "produce")
BuyLow.addProduct(ham, "meat")
BuyLow.addProduct(chicken, "meat")
BuyLow.addProduct(steak, "meat")
BuyLow.addProduct(pastries,"breakfast")
BuyLow.addProduct(cereal,"breakfast")

BuyLow.availableProducts("dairy")

BuyLow.availableProducts("dairy")

