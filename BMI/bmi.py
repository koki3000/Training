def bmi(weight, height):
    try:
        float(height)
        float(weight)
    except:
        print('Wrong format of data, should be number with dot like 1.8')

    height = float(height)
    index = float(weight) / (height*height)
    if index < 18.5:
        return 'Underweight'
    elif index < 25:
        return 'Healthy weight'
    elif index < 30:
        return 'Overweight'
    elif index < 40:
        return 'Obesity'
    elif index >= 40:
        return 'Class 3 Obesity'
    else:
        return 'Wrong values'

if __name__ == '__main__':
    while True:
        try:
            weight = input('Please input your weight in kg: ')
            float(weight)        
            height = input('Please input your height in meters: ')
            float(height)
            print(bmi(weight, height))
            break
        except:
            print('Wrong format of data, should be number different than 0, like 1.8')