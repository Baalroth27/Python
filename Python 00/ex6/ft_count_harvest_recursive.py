def ft_count_harvest_recursive():
    days_till_harvest = int(input('Days until harvest: '))
    i = 1
    recursive_helper(i, days_till_harvest)
    print('Harvest time!')


def recursive_helper(i, days_till_harvest):
    if i > days_till_harvest:
        return
    print(f'Day {i}')
    recursive_helper(i + 1, days_till_harvest)
