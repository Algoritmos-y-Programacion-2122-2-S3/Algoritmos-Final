from os import sep


def main():
    products = {
        "mobiles": {
            "Apple": [
                {
                    "name": "iPhone 7",
                    "price": 300
                },
                {
                    "name": "iPhone 8",
                    "price": 350
                },
                {
                    "name": "iPhone Xr",
                    "price": 450
                },
                {
                    "name": "iPhone Xs",
                    "price": 460
                },
                {
                    "name": "iPhone 11",
                    "price": 900
                },
                {
                    "name": "iPhone 12",
                    "price": 1100
                },
                {
                    "name": "iPhone 13",
                    "price": 1300
                },
            ],
            "Samsung": [
                {
                    "name": "Samsung Galaxy Beam",
                    "price": 150
                },
                {
                    "name": "Samsung Galaxy S6",
                    "price": 200
                },
                {
                    "name": "Samsung Galaxy S7",
                    "price": 300
                },
            ],
            "Xiaomi": [
                {
                    "name": "Xiaomi Redmi Note 8",
                    "price": 250
                },
                {
                    "name": "Xiaomi Redmi Note 8 Pro",
                    "price": 300
                },
            ]
        },
        "laptops": {
            "DELL": [
                {
                    "name": "Dell Inspiron 15",
                    "price": 600
                },
                {
                    "name": "Dell Latitude 14",
                    "price": 650
                },
            ],
            "MAC": [
                {
                    "name": "MacBook Pro 13",
                    "price": 900
                },
                {
                    "name": "MacBook M1",
                    "price": 1500
                },
            ]
        },
        "accessories": [
            {
                "name": "Cargador Samsung",
                "price": 8,
            },
            {
                "name": "Cargador Apple",
                "price": 10,
            },
            {
                "name": "Audífonos Apple",
                "price": 5,
            },
            {
                "name": "Audífonos Samsung",
                "price": 4,
            },
            {
                "name": "Audífonos Xiaomi",
                "price": 4,
            },
            {
                "name": "Cable HDMI 1m",
                "price": 5,
            },
            {
                "name": "Cable HDMI 3m",
                "price": 7,
            },
        ],
    }
    print("***Welcome***")
    while True:
        print("\nPlease select a option:")
        mobile_brands = products.get("mobiles")

        laptops_brands = products.get("laptops")

        accessories = products.get("accessories")

        option = str(input("1 = See Inventory \n2 = Modify Inventory \n3 = Exit\n"))
        if option == "1":
            print("\nPlease Select a category to display the inventory")
            inventory_type = str(input("M = Mobiles \nL = Laptops \nA = Accesories \n"))
            if inventory_type.upper() == "M":
                print("")
                for brand in mobile_brands:
                    product_list = mobile_brands.get(brand)
                    for product in product_list:
                        print(product["name"],product["price"])       

            elif inventory_type.upper() == "L":
                print("")
                for brand in laptops_brands:
                    for product in laptops_brands.get(brand):
                        print(product["name"],product["price"])

            elif inventory_type.upper() == "A":
                print("")
                for product in accessories:
                    print(product["name"],product["price"])

            else: 
                print("The option",inventory_type,"is not valid")
            
        elif option == "2":
            print("")
            cont = 0
            for brand in mobile_brands:
                for product in mobile_brands.get(brand):
                    print(cont,product["name"],product["price"], sep= " - ")
                    cont += 1
            for brand in laptops_brands:
                for product in laptops_brands.get(brand):
                    print(cont,product["name"],product["price"], sep= " - ")
                    cont += 1
            for product in accessories:
                print(cont,product["name"],product["price"], sep= " - ")
                cont += 1
            
            device = int(input("Please enter the number you want to modify\n"))
            print("Please select a option to Modify")
            parameter_to_change = input("N = Name\nP = Price\n")

            cont = 0
            search = True
            for brand in mobile_brands:
                for product in mobile_brands.get(brand):
                    if search:
                        if cont == device:
                            if parameter_to_change.upper() == "N":
                                product["name"] = input("Please enter the new name of the product:")
                            else: 
                                product["price"] = input("Please enter the new price of the product:")
                            search = False
                    cont += 1
            for brand in laptops_brands:
                for product in laptops_brands.get(brand):
                    if search:
                        if cont == device:
                            if parameter_to_change.upper() == "N":
                                product["name"] = input("Please enter the new name of the product:")
                            else: 
                                product["price"] = input("Please enter the new price of the product:")
                            search = False
                    cont += 1
            for product in accessories:
                if search:
                    if cont == device:
                        if parameter_to_change.upper() == "N":
                            product["name"] = input("Please enter the new name of the product:")
                        else: 
                            product["price"] = input("Please enter the new price of the product:")
                        search = False
                cont += 1

        else:
            break
        

main()
