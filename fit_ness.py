temp = float(input("Enter your body tempature in Fahrenhite: "))



if(temp <= 98.6):
    gender = input("Enter you gender: ")
    if gender == "male":
        daily_diet_calorie_amount = int(input("Enter your daily Calorie amount: "))
        if daily_diet_calorie_amount > 2500:
            work_out_hours = float(input("Enter your workout hours: "))
            if work_out_hours >= 1:
                print("your Fitness will be incresing day by day and calorie will be burning ")
            else:
                print("You need to do more workout")
        else:
            print("you are Fit and 100 percent healthy")
    elif gender == "female":
        work_out_hours = float(input("Enter your workout hours: "))
        if work_out_hours > 1:
            print("your Fitness will be incresing day by day and calorie will be burning ")
        else:
            print("You need to do more workout")
    else:
        print("Error")    
else:
    print("you have a high Fever or body tempature is too high and you are not Fit ")