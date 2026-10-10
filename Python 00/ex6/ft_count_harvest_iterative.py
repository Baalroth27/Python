def ft_count_harvest_iterative():
    days_till_harvest = int(input('Days until harvest: '))
    for i in range(1, days_till_harvest + 1):
        print(f'Day {i}')
    print('Harvest time!')
