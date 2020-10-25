height = int(input('Please enter your height in cm'))
mass = int(input('Please enter your weight in kg'))
BMI = mass / ( height/100 * height/100)
print('Your BMI is:', BMI)
if BMI < 16: 
    print('underweight')
elif 16 <= BMI <= 18.5:
    print('underweight')
elif 18.5 < BMI <= 25:
    print('normal')
elif 25 < BMI <= 30:
    print('overweight')
else:
    print('obese')