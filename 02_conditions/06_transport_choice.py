distance = 20

if distance < 3:
    transport_mode = "Walk"
elif distance <=15:
    transport_mode = "Bike"
elif distance > 15:
    transport_mode = "Car"
    
print(transport_mode)