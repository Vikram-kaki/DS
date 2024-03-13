from os.path import exists


class SuperMarket:
    unique_id = 1

    def __init__(self, name):
        self.__name = name
        print(f"Hi Welcome to {self.__name}")

    def add_products(self):
        while True:
            product = f"{SuperMarket.unique_id},{input('Enter the product name : ')},{input('Enter the cost : ')},{input('Enter the quantity : ')}"
            vals = product.split(",")
            if not self.__exist(vals):
                self.__add_to_file(product)
            else:
                self.__update_items(vals[0], vals[3], True)

            if input("Enter Y to continue, N to exit : ").lower() == 'n':
                break
            SuperMarket.unique_id += 1

    def print_items(self):
        if exists('./Inventory.txt'):
            with open('./Inventory.txt', 'r') as file:
                txt = file.read()
            print(txt)

    def __get_vals(self, id):
        if exists('./Inventory.txt'):
            with open('./Inventory.txt', 'r') as file:
                txt = file.read()

            products = txt.split('\n')
            for i in products:
                vals = i.split(',')
                if vals[0] == id:
                    return vals

        return []

    def __exist(self, li):
        if exists('./Inventory.txt'):
            with open('./Inventory.txt', 'r') as file:
                txt = file.read()

            products = txt.split('\n')
            for p in products:
                sp = p.split(',')
                if sp[1:] == li[1:]:
                    return True

        return False

    def __add_to_file(self, product):
        if exists('./Inventory.txt'):
            with open('./Inventory.txt', 'a') as file:
                file.write('\n' + product)
        else:
            with open('./Inventory.txt', 'w') as file:
                file.write(product)

    def __update_items(self, item_id, amount, adding):
        with open('./Inventory.txt', 'r') as file:
            p = file.read()
        products = p.split('\n')
        for i, j in enumerate(products):
            sp = j.split(',')
            if item_id == sp[0]:
                if not adding:
                    if int(amount) <= int(sp[-1]) and int(sp[-1]) > 0:
                        sp[3] = f"{int(sp[3]) - int(amount)}"
                        ap = ','.join(sp)
                        products[i] = ap
                    else:
                        return False
                if adding:
                    sp[3] = f"{int(sp[3]) + int(amount)}"
                    ap = ','.join(sp)
                    products[i] = ap

        with open('./Inventory.txt', 'w') as file2:
            for i in range(len(products) - 1):
                file2.write(products[i] + '\n')

            file2.write(products[-1])
            return True

    def make_purchase(self):
        id = input("Enter the product id : ")
        quantity = input("Enter the quantity : ")

        if not self.__update_items(id, quantity, False):
            print("Not Enough Quantity available")
        else:
            vals = self.__get_vals(id)
            print("*" * 45)
            print(f"Id of the product : {id}")
            print(f"Name of the product : {vals[1]}")
            print(f"Quantity of the product : {quantity}")
            print(f"Price of the product : {vals[2]}")
            print("*" * 45)
            print(f"Total Price : {int(quantity) * int(vals[2])}")
            print()
            print()
            print()

            print("Thank you Visit Again!")


super_market = SuperMarket("Vikram's Super Market")
super_market.add_products()
super_market.print_items()
super_market.make_purchase()
