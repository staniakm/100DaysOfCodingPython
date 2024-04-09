# bmi = weight(kg)/height2 (m2)

weight_in_kg = float(input("What is your weight (kg) ?"))
height_in_m = float(input("What is your height (m)?"))

bmi = weight_in_kg / (height_in_m ** 2)

print("Your BMI is: " + str(int(bmi)))
