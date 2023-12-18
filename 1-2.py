# Define initial height, weight, and overweight values
height = 79
weight = 222
overweight = False

# Define and calculate BMI
bmi = weight/height

# Print BMI and BMI var type
print(bmi)
print(type(bmi))

# Calculate overweight based on BMI
if(bmi > 22.5):
    overweight = True

# Concatenate overweight using format
overweight_str = str(format(overweight))

# Print overweight_str
print("Patient is overweight: " + overweight_str)