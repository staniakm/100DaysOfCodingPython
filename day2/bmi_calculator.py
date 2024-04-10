# bmi = weight(kg)/height2 (m2)

weight_in_kg = float(input("What is your weight (kg) ?"))
height_in_m = float(input("What is your height (m)?"))

bmi = weight_in_kg / (height_in_m ** 2)

print("Your BMI is: " + str(int(bmi)))

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal weight")
elif 25 <= bmi < 30:
    print("Slightly overweight")
elif 30 <= bmi < 35:
    print("Obese")
else:
    print("Critical obese")
