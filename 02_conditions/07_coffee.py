order_size = "medium"
extra_shot = True

if extra_shot: 
    coffee =  order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"
    
print("Your order is", coffee)