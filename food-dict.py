
#Food order
from os import system

system ("cls")
order = {
    "client"  : "John Doe",
    "item"   : "Salad",
    "quantity": 5,
    "price"   : 15.00,
    
}

#HW1: modify the code so -> order["total"] discount 20%
#     when quantity is more than 7
item_order = int(input("How many?: "))
order["quantity"] = item_order
order["discount"] = 20
order ["total"] = order["price"]* order["quantity"]
offer = order ["total"] * order ["discount"] / 100
if order["quantity"] >= 7:
    print ("Total:", order ["total"] - offer)
else:
    print("Total:", order ["total"])
print()

######################################

#HW2: add code so the USER -> input -> question: do you need delivery?
#     based on the answer: total > 300.00 and the user wants dlivery
#     order["delivery"] -> "free", otherwise if the user wants delivery
#     order ["delivery"] -> 50.00 -> "total" updated

delivery = input("Do you need delivery?: ")
if delivery == ("yes")  and order ["total"] >= 300:
    order ["delivery"] = "free"
    print("ORDER for:"  , order["client"])
    print("Food:"       , order ["item"])
    print("Price x qty:", order ["price"], "x", order ["quantity"])
    print("Delivery:"   , order ["delivery"])
    print("Total:", order ["total"] - offer )
elif order["quantity"] < 7:
    order ["delivery"] = 50.00
    print("ORDER for:"  , order["client"])
    print("Food:"       , order ["item"])
    print("Price x qty:", order ["price"], "x", order ["quantity"])
    print("Delivery:"   , order ["delivery"] )
    print("Total:", order ["total"] + order ["delivery"])
else:
    order ["delivery"] = 50.00
    print("ORDER for:"  , order["client"])
    print("Food:"       , order ["item"])
    print("Price x qty:", order ["price"], "x", order ["quantity"])
    print("Delivery:"   , order ["delivery"])
    print("Total:", order ["total"] + order ["delivery"] - offer)

print()



