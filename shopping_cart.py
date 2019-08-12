class ShoppingCart:
    # write your code here
    def __init__(self, employee_discount=None):
        self.prices = []
        self.total = sum(self.prices)
        self.employee_discount = employee_discount
        self.items = []

    def add_item(self, name, price, quantity=1):
        i = 0
        while i < quantity:
            self.items.append(name)
            self.prices.append(price)
            self.total = sum(self.prices) 
            i += 1
        return self.prices, self.items, self.total
    
    def median_item_price(self):
        prices_list = self.prices
        prices_list.sort()
        if len(prices_list)%2 == 1:
            midpoint = int((len(prices_list)-1)/2)
            median = prices_list[midpoint]
            return print(median)
        else:
            midpoint2 = int(len(prices_list)/2)
            midpoint1 = int((len(prices_list)/2)-1)
            median = (prices_list[midpoint2]+prices_list[midpoint1])/2
            return print(median)
    
    def mean_item_price(self):
        return print(self.total/len(self.prices))
     
    def apply_discount(self):
        if self.employee_discount == None:
            message = "Sorry, there is no discount to apply to your cart :("
            return message
        else:
            return self.total*((100-self.employee_discount)/100)

    def void_last_item(self):
        prices_list2 = self.prices
        items_list2 = self.items
        if len(prices_list2) == 0:
            return print("There are no items in your cart!")
        else:
            del prices_list2[-1]
            self.prices = prices_list2
            del items_list2[-1]
            self.items = items_list2
            self.total = sum(self.prices)
            return self.prices, self.items, self.total
            