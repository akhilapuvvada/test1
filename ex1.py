class Produce:
    def __init__(self):
        self.Producediscount=10
class Fruits(Produce):
    def __init__(self):
        super().__init__()
        self.Fruitsdiscount=18
class Apple(Fruits):
    def __init__(self):
        super().__init__()
        self.Applecost=50
    def cost1(self,no_of_kgs):
        app_discount_kgs=no_of_kgs//4
        app_kgs=no_of_kgs-app_discount_kgs
        app_cost=app_kgs*self.Applecost
        app_actualcost=no_of_kgs*self.Applecost
        return app_cost,app_actualcost
class Orange(Fruits):
    def __init__(self):
        super().__init__()
        self.Orangediscount=20
        self.Orangecost=80
    def cost2(self,no_of_kgs):
        ora_maxdiscount=max(self.Producediscount,self.Fruitsdiscount,self.Orangediscount)
        ora_actualcost=no_of_kgs*self.Orangecost
        ora_discount=ora_maxdiscount*ora_actualcost*0.01
        ora_cost=ora_actualcost-ora_discount
        return ora_cost,ora_actualcost
class Veg(Produce):
    def __init__(self):
        super().__init__()
        self.Vegdiscount=5
class Potato(Veg):
    def __init__(self):
        super().__init__()
        self.Potatocost=30
    def cost3(self,no_of_kgs):
        pot_discount_kgs=no_of_kgs//3
        pot_kgs=no_of_kgs-pot_discount_kgs
        pot_cost=pot_kgs*self.Potatocost
        pot_actualcost=no_of_kgs*self.Potatocost
        return pot_cost,pot_actualcost
class Tomato(Veg):
    def __init__(self):
        super().__init__()
        self.Tomatodiscount=10
        self.Tomatocost=70
    def cost4(self,no_of_kgs):
        tom_maxdiscount=max(self.Producediscount,self.Vegdiscount,self.Tomatodiscount)
        tom_actualcost=no_of_kgs*self.Tomatocost
        tom_discount=tom_maxdiscount*tom_actualcost*0.01
        tom_cost=tom_actualcost-tom_discount
        return tom_cost,tom_actualcost
    
headline=input()
items=input()
print("Following is the invoice that is generated based on the above items that customer has bought:")

customer=headline.split(" ")
print("customer:",customer[1]+" "+ customer[2])

print("Item    Qty    Amount")
Total_Amount=0
actual_amount=0
items=items.split(",")
for item in items:
    product=item.split(" ")
    if product[0]=='Apple':
        Obj=Apple()
        kgs=product[1].split("kg")
        app_cost,app_actualcost=Obj.cost1(int(kgs[0]))
        Total_Amount=Total_Amount+app_cost
        actual_amount=actual_amount+app_actualcost
        print("Apple"+"    "+str(kgs[0])+"    "+ str(app_cost))
    elif product[0]=='Orange':
        Obj2=Orange()
        kgs=product[1].split("kg")
        ora_cost,ora_actualcost=Obj2.cost2(int(kgs[0]))
        Total_Amount=Total_Amount+ora_cost
        actual_amount=actual_amount+app_actualcost
        print("Orange"+"    "+str(kgs[0])+"    "+ str(ora_cost))
    elif product[0]=='Potato':
        Obj3=Potato()
        kgs=product[1].split("kg")
        pot_cost,pot_actualcost=Obj3.cost3(int(kgs[0]))
        Total_Amount=Total_Amount+app_cost
        actual_amount=actual_amount+app_actualcost
        print("Potato"+"    "+str(kgs[0])+"    "+ str(pot_cost))
    elif product[0]=='Tomato':
        Obj4=Tomato()
        kgs=product[1].split("kg")
        tom_cost,tom_actualcost=Obj4.cost4(int(kgs[0]))
        Total_Amount=Total_Amount+app_cost
        actual_amount=actual_amount+app_actualcost
        print("Tomato"+"    "+str(kgs[0])+"    "+ str(tom_cost))

print("______________________")
print("Total_Amount        "+str(Total_Amount)+"Rs")
print("You saved    "+str(actual_amount)+"-"+str(Total_Amount)+"="+str(actual_amount-Total_Amount)+"Rs")



