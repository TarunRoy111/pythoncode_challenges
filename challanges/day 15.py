#calculator
class Calculator:
    def solve(self,exp):
        print(eval(exp))

A=input("enter expression to solve: ")
O=Calculator()
O.solve(A)


#shopping cart

class Cart:
    def __init__(self):
        self.items = []
    def Add_item(self,*args):
        for item in args:
            self.items.append(item)
        print(self.items)
    def Remove_item(self,*args):
        for item in args:
            self.items.remove(item)
        print(self.items)
    def total_bill(self):
        total=0
        for item in self.items:
            if item == "phone": total+=100
            elif item == "laptop": total+=150
            else: total+=50
        print(f"total bill is {total}")
Flipkart=Cart()
Flipkart.Add_item("phone","laptop","buds","phone")
Flipkart.Remove_item("buds")
Flipkart.total_bill()