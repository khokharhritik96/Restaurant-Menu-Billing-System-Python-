
menu = {
	"burger" : 50,
	"pizza" : 200,
	"cold coffee" : 120,
	"pasta" : 150,
}


total_bill = 0


while True:
    print("\n----- MENU -----")
    for item, price in menu.items():
        print(f"{item} : {price}")

    choice = input("\nEnter item name to order (or type 'exit' to finish): ").lower()

    if choice == "exit":
        break

    if choice in menu:
        qty = int(input("Enter quantity: "))
        item_total = menu[choice] * qty
        total_bill += item_total
        print(f"{choice} x {qty} = {item_total}")
    else:
        print("Item not available ")

print("Total Bill = ", total_bill)
