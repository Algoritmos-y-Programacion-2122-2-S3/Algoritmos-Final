def main():
    wantToExit= False
    customer_count = 0
    u_study_count = 0
    t_study_count = 0
    r_study_count = 0
    acum_amount_t = 0
    acum_amount_u = 0
    acum_amount_r = 0
    acum_discount = 0
    acum_total = 0
    while not wantToExit:
        print("***** Welcome *****")
        id_card = input("Please give me your id card: \n")
        age = int(input("Please give me your age: \n"))
        gender = input("Please give me your gender: \n")
        study_type = input("Please give me your study type: \n")
        studies = {"U": 8900, "T":12640, "R":15600}
        customer_count += 1
        
        amount = studies[str(study_type).upper()]
        original_amount = amount
        if(gender.lower() == "f" and age >= 55 or gender.lower() == "m" and age >= 65):
            discount = original_amount * 0.25
            amount -= discount
            acum_discount += discount
        
        if customer_count % 2 != 0:
            discount = original_amount * 0.02
            amount -= discount
            acum_discount += discount

        if study_type.upper() == "U":
            u_study_count += 1
            acum_amount_u += amount
        elif study_type.upper() == "T":
            t_study_count +=1
            acum_amount_t += amount
        elif study_type.upper() == "R":
            r_study_count +=1
            acum_amount_r += amount

        acum_total += amount

            
        print("")
        print("")
        print("")
        print("")
        print("")
        print("Recipe:")
        print("Id Card:", id_card)
        print("Age:", age)
        print("Gender:", gender)
        print("Study:", study_type)     
        print("Amount:", amount)   

        contin = input("Do you to continue Y - N") 
        if(contin.upper() == "N"):
            wantToExit = True


    print("")
    print("")
    print("***** END OF DAY *****")
    print("")
    print("")
    print("Count of Study T:",t_study_count )
    print("Count of Study U:",u_study_count )
    print("Count of Study R:",r_study_count )
    print("Total Discount Amount:",acum_discount )
    print("Total Amount:",acum_total )
    if customer_count > 0:
        print("Average/Customer:",acum_total/customer_count )
    else:
        print("Average/Customer: 0" )
    if t_study_count > 0:
        print("Average/Customer/Study T:",acum_amount_t/t_study_count )
    else:
        print("Average/Customer/Study T: 0" )
    if r_study_count > 0:
        print("Average/Customer/Study R:",acum_amount_r/r_study_count )
    else:
        print("Average/Customer/Study R: 0" )
    if u_study_count > 0:
        print("Average/Customer/Study U:",acum_amount_u/u_study_count )
    else:
        print("Average/Customer/Study U: 0" )

main()