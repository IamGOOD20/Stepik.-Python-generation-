def weighing(weight: int) -> str:
    if weight < 69:
        if weight < 64 and weight >= 60:
            return 'Первый полусредний вес'
        elif weight < 60:
            return 'Легкий вес'
        else:
            return 'Полусредний вес'

print(weighing(int(input())))
