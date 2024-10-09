weight = 87
height = 1.78
sex = "m"

BMI = weight / height ** 2

# Display of amount of hours to do of every single sport until ideal weight should be achieved
def Sport_hours(weight, height, sex):

    # Determine ideal weight
    if sex == "m":
        PI = ((height * 100) - 100) - ((height * 100) - 150) / 4
    elif sex == "f":
        PI = ((height * 100) - 100) - ((height * 100) - 120) / 4
    else:
        print("error")

    # Calculate the time for each sport

    #Badminton:
    badminton_time = ((weight - PI) * 9000) / 330

    # Basketball:
    basketball_time = ((weight - PI) * 9000) / 390

    # Boxing:
    boxing_time = ((weight - PI) * 9000) / 770

    # Display of result
    if weight > PI:
        print("%.2f hours of badminton, %.2f hours of basketball or %.2f hours of boxing are required to reach %.2f kg, your ideal weight" % (badminton_time, basketball_time, boxing_time, PI))
    else:
        print("You should eat")
        
print(BMI)
if BMI < 18.5:
    print("You are underweight")
elif BMI <= 25:
    print("You are healthyweight")
elif BMI <=32:
    print("You are overweight")
else:
    print("You are obese")
Sport_hours(weight, height, sex)
