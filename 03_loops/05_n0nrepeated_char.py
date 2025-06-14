str = "aafeffessaowd"

for char in str:
    if str.count(char) == 1:
        print("First non-repeated character: ", char)
        break