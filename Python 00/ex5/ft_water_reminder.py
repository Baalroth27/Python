def ft_water_reminder():
    days_to_remind = 2
    days_since_watering = int(input('Days since last watering: '))
    if days_since_watering > days_to_remind:
        print('Water the plants!')
    else:
        print('Plants are fine')
