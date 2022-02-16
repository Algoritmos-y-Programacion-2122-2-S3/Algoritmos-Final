def expresos_saman(options):
    lomito_client_acum = 0
    punta_client_acum = 0
    molida_client_acum = 0
    lomito_kg_acum = 0
    punta_kg_acum = 0
    molida_money_amount_acum = 0
    lomito_money_amount_acum = 0
    punta_money_amount_acum = 0
    molida_kg_acum = 0
    clients_with_discount = 0
    discount_amount_acum = 0
    worst_client = {}
    biggest_discount_client = {}
    exit = False 

    print("*** WELCOME TO SAMAN CARNES ***\n")

    while not exit:
        print("\nPlease select a option ")
        for option in options:
            print(option.get("code"), option.get("name"), sep = " - ")
        option_selected = input()
            
        if not is_valid_option(option_selected.upper()):
            print("Option not valid\n")
            continue
        
        kg = float(input("How many kg you want?\n"))
        if kg == 0:
            continue

        client = get_client_data(kg,option_selected,options)

        if option_selected.upper() == "L":
            lomito_client_acum += 1
            lomito_kg_acum += kg
            lomito_money_amount_acum += client.get("net_amount")
        elif option_selected.upper() == "P":
            punta_client_acum += 1
            punta_kg_acum += kg
            punta_money_amount_acum += client.get("net_amount")
        elif option_selected.upper() == "M":
            molida_client_acum += 1
            molida_kg_acum += kg
            molida_money_amount_acum += client.get("net_amount")
        

        if len(worst_client) == 0:
            worst_client = client
        else:
            if float(worst_client.get("net_amount")) > float(client.get("net_amount")):
                worst_client = client
        
        if len(biggest_discount_client) == 0 and float(client.get("discount_amount")) > 0:
            biggest_discount_client = client
        else:
            if float(biggest_discount_client.get("discount_amount")) < float(client.get("discount_amount")):
                biggest_discount_client = client

        if float(client.get("discount_amount")) > 0:
            clients_with_discount += 1
            discount_amount_acum += client.get("discount_amount")


        print("\n***Invoice***\n")
        print_client_data(client)
        print("")
        
        exit_string = input("Do you want to exit ? \nY - Yes\nN - No\n")
        if exit_string.upper() == "Y":
            exit = True

    print("*** END OF DAY ***")
    print("Total Lomito Clients: ",lomito_client_acum)
    print("Total Punta Clients: ",punta_client_acum)
    print("Total Molida Clients: ",molida_client_acum)
    print("Total Lomito Kg: ",lomito_kg_acum)
    print("Total Punta Kg: ",punta_kg_acum)
    print("Total Molida Kg: ",molida_kg_acum)
    print("Clients with discounts: ",clients_with_discount)
    print("Total Lomito Money Amount: ",lomito_money_amount_acum)
    print("Total Punta Money Amount: ",punta_money_amount_acum)
    print("Total Molida Money Amount: ",molida_money_amount_acum)
    print("\nWorst Client:")
    print_client_data(worst_client)
    print("\nClient with biggest discount:")
    print_client_data(biggest_discount_client)

def is_valid_option(option_selected):
    return option_selected == "L" or option_selected == "P" or option_selected == "M"

def print_client_data(client):
    for key, value in client.items():
        print(key,value, sep= ": ")

def get_client_data(kg,option_selected,options):
    gross_amount = float(search_item(option_selected, options,False)) * kg
    discount_amount = get_discount(gross_amount)
    net_amount = gross_amount - discount_amount

    client = {
        "id": input("Please enter your name: "),
        "id": input("Please enter your id card number: "),
        "kg": str(kg),
        "gross_amount": str(gross_amount),
        "discount_amount": str(discount_amount),
        "net_amount": str(net_amount)
    }
    return client

def get_discount(gross_amount):
    discount = 0
    if gross_amount > 30: 
        discount += gross_amount * 0.05
    if is_prime(gross_amount):
        discount += gross_amount * 0.15
    if is_two_power(gross_amount):
        discount += gross_amount * 0.20
    return discount
    
def is_prime(gross_amount):
    aux = gross_amount - 1
    prime = True
    if gross_amount <= 1:
        return False
    while aux > 1:
        if gross_amount % aux == 0:
            prime = False
        aux -= 1
    return prime
    
def is_two_power(gross_amount):
    aux = gross_amount
    is_power = False
    if gross_amount == 2:
        is_power = True
    else:
        while aux > 2:
            aux //= 2
            if aux == 2:
                is_power = True 
    
    return is_power

def search_item(option_selected, options,is_name):
    for option in options:
        if option_selected == option["code"]:
            if is_name:
                return option["name"]
            else:
                return option["price"]
    return ""

def get_client_amount(client,is_discount):
    if is_discount:
        return float(client.get("discount_amount"))
    else:
        return float(client.get("net_amount"))

def main():
    options = [
        {
            "code": "L",
            "name": "Lomito",
            "price": "15"
        },
        {
            "code": "P",
            "name": "Punta",
            "price": "8"
        },
        {
            "code": "M",
            "name": "Molida",
            "price": "6"
        },
    ]

    expresos_saman(options)
    

main()