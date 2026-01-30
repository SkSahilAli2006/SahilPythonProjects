menu = {
    "chai" : 10,
    "biscuit" : 5,
    "matthi" : 2,
    "bun" : 15,
    "gold flake" : 12
}

cart = {}
print("Welcome To Tapri Of Dolly Chai Wala..")

while True:
    print("\nMenu: ")
    for item,price in menu.items():
        print(item," - Rs ",price)
    print("\nOptions: ")
    print("1.Add Items")
    print("2.Remove Items")
    print("3.Exit")

    no = (input("Choose (1/2/3) : "))

    if no == "1":
        choice = input("Enter Item name : ").lower()

        if choice in menu:
            qyt = int(input("Enter quantity of item : "))

            if choice in cart:
                cart[choice] += qyt

            else:
                cart[choice] = qyt
                print("Item added into cart")

        else:
            print("Item is not Avilable")

    elif no == "2":
        if not cart:
            print("Cart is empty")

        else :
            print("\nYour Cart: ")
            for item,yt in cart.items():
                print(item,"X",yt)

            remove_item = input("Enter item Name to remove : ").lower()

            if remove_item in cart:
                print("\nOptions: ")
                print("1. Remove Entire item")
                print("2. Remove Specific quantity")
                remove_choice = input("choose (1/2): ")

                if remove_choice == "1":
                    del char[remove_item]
                    print("All",remove_item,"remove successfully!")

                elif remove_choice == "2":
                    remove_qyt = int(input("Enter quantity to remove : "))

                    if remove_qyt <= cart[remove_item]:
                        cart[remove_item] -= remove_qyt
                        print(remove_qyt,remove_item,"removed! Remaining: ",cart[remove_item])

                    else:
                        del cart[remove_item]
                        print(remove_item,"removed successfully!")

                else:
                    print("Invalid option")
    elif no == "3":
         break
    else:
         print("Invalid Choice")


print("\nYour Cart:")
total = 0
for item, qyt in cart.items():
    price = menu[item]
    item_total = price * qyt
    total += item_total
    print(item,"x",qyt,"=",item_total)

print("\nTotal Billing: ",total)
print("ThankYou For Visiting, Dolly Tapri...(chai wala)")
print("\n Ufffff! Garam hai, garam hai! 🔥☕🤣")