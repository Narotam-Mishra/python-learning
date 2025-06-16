
# Classify a Person's age group: Child(<13), Teenager(13-19), Adult(20-59), Senior(60+)

age = int(input("Enter your age: "))

if age < 13:
    print('Child Age Group')
elif age < 20:
    print('Teenage Group')
elif age < 60:
    print('Adult Age Group')
else:
    print('Senior Age Group')

