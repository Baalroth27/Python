def ft_plant_age():
    harvest_age = 60
    plant_age = int(input('Enter plant age in days: '))
    if plant_age > harvest_age:
        print('Plant is ready to harvest!')
    else:
        print('Plant needs more time to grow.')
