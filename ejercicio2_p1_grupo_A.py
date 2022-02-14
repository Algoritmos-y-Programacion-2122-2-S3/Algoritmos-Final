def expresos_saman(options):
    seats_vehicle_valencia = 30
    seats_vehicle_barquisimeto = 30
    seats_vehicle_pto_la_cruz = 30
    passengers_vehicle_valencia = 0
    passengers_vehicle_barquisimeto = 0
    passengers_vehicle_pto_la_cruz = 0
    net_amount_vehicle_valencia = 0
    net_amount_vehicle_barquisimeto = 0
    net_amount_vehicle_pto_la_cruz = 0
    discount_amount_vehicle_valencia = 0
    discount_amount_vehicle_barquisimeto = 0
    discount_amount_vehicle_pto_la_cruz = 0
    best_client = {}
    exit = False 
    total_net_amount = 0

    print("*** WELCOME TO EXPRESOS SAMAN ***\n")

    while not exit:
        if already_all_destinations_full(seats_vehicle_valencia,seats_vehicle_barquisimeto,seats_vehicle_pto_la_cruz):
            print("Sorry we do not have more seats available to any destinations" )
            exit = True
            continue
        else:
            print("\nPlease select a option ")
            for option in options:
                print(option.get("code"), option.get("name"), sep = " - ")
            option_selected = input()
                
            if option_selected.upper() == "V":
                seats_number = int(input("How many seats you want?\n"))
                seats_number = validate_availability(seats_number,seats_vehicle_valencia)
                seats_vehicle_valencia -= seats_number
                passengers_vehicle_valencia += 1
            elif option_selected.upper() == "B":
                seats_number = int(input("How many seats you want?\n"))
                seats_number = validate_availability(seats_number,seats_vehicle_barquisimeto)
                passengers_vehicle_barquisimeto += 1
                seats_vehicle_barquisimeto -= seats_number
            elif option_selected.upper() == "P":
                seats_number = int(input("How many seats you want?\n"))
                seats_number = validate_availability(seats_number,seats_vehicle_pto_la_cruz)
                seats_vehicle_pto_la_cruz -= seats_number
                passengers_vehicle_pto_la_cruz += 1
            else:
                print("Destination not valid\n")
                continue

            if seats_number == 0:
                continue

            client = get_client_data(seats_number,option_selected,options)

            if option_selected.upper() == "V":
                discount_amount_vehicle_valencia += get_client_amount(client,True)
                net_amount_vehicle_valencia += get_client_amount(client,False)
            elif option_selected.upper() == "B":
                discount_amount_vehicle_barquisimeto += get_client_amount(client,True)
                net_amount_vehicle_barquisimeto += get_client_amount(client,False)
            elif option_selected.upper() == "P":
                discount_amount_vehicle_pto_la_cruz += get_client_amount(client,True)
                net_amount_vehicle_pto_la_cruz += get_client_amount(client,False)
            
            total_net_amount += get_client_amount(client,False)

            if len(best_client) == 0:
                best_client = client
            else:
                if float(best_client.get("net_amount")) < float(client.get("net_amount")):
                    best_client = client

            print("\n***Invoice***\n")
            print_client_data(client)
            print("")
            
            exit_string = input("Do you want to exit ? \nY - Yes\nN - No\n")
            if exit_string.upper() == "Y":
                exit = True

    print("*** END OF DAY ***")
    print("Total Net Amount Valencia: ",net_amount_vehicle_valencia)
    print("Total Net Amount Barquisimeto: ",net_amount_vehicle_barquisimeto)
    print("Total Net Amount Puerto La Cruz: ",net_amount_vehicle_pto_la_cruz)
    print("Total Discount Amount Valencia: ",discount_amount_vehicle_valencia)
    print("Total Discount Amount Barquisimeto: ",discount_amount_vehicle_barquisimeto)
    print("Total Discount Amount Puerto La Cruz: ",discount_amount_vehicle_pto_la_cruz)
    print("Total Net Amount of Day",total_net_amount)
    print("Best Client:")
    print_client_data(best_client)

def print_client_data(client):
    for key, value in client.items():
        print(key,value, sep= ": ")

def already_all_destinations_full(seats_valencia,seats_barquisimeto,seats_pto_la_cruz):
    return seats_valencia == 0 and seats_barquisimeto == 0 and seats_pto_la_cruz == 0

def validate_availability(seats_number,availability):
    while seats_number > 10 or seats_number > availability:
        message = "The Maximum value is 10 and we only have " + str(availability) + " seats to your destination, if you want to abort the operation enter 0"
        print(message)
        seats_number = int(input("Please try again: enter a new seats request \n"))
    return int(seats_number)

def get_client_data(seats_requested,option_selected,options):

    gross_amount = int(search_destination(option_selected, options,False)) * seats_requested
    discount_amount = 0
    if seats_requested > 4: 
        discount_amount = gross_amount * 0.20
    else: 
        discount_amount = 0
    iva = (gross_amount - discount_amount) * 0.16
    net_amount = gross_amount - discount_amount - iva

    client = {
        "id": input("Please enter your id card number: "),
        "seats_requested": str(seats_requested),
        "destination_code": option_selected,
        "destination_name": search_destination(option_selected, options, True),
        "gross_amount": str(gross_amount),
        "discount_amount": str(discount_amount),
        "iva": str(iva),
        "net_amount": str(net_amount)
    }
    return client

def search_destination(option_selected, options,is_name):
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
            "code": "V",
            "name": "Valencia",
            "price": "500"
        },
        {
            "code": "P",
            "name": "Puerto La Cruz",
            "price": "700"
        },
        {
            "code": "B",
            "name": "Barquisimeto",
            "price": "800"
        },
    ]

    expresos_saman(options)
    

main()