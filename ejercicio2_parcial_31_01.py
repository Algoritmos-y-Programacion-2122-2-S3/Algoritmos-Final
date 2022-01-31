def main():
    wantToExit= False
    while not wantToExit:
        print("***** Welcome *****")
        id_card = input("Please give me your id card: \n")
        age = int(input("Please give me your age: \n"))
        gender = input("Please give me your gender: \n")
        study_type = input("Please give me your study type: \n")
        studies = {"U": 8900, "T":12640, "R":15600}
        amount = 0
        
        amount = studies[str(study_type).upper()]
        if(gender.lower() == "f" and age >= 55 or gender.lower() == "m" and age >= 65):
            amount *= 0.75
            
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

main()