'''
Zoom challenged the Flash and offered him a fair fight in the form of a race around the magnetar.
If lost, this neutron star will charge and destroy the world,
so Flash decided not to risk without reason and find out from his friend Cisco Ramon whether it makes sense to take the challenge.
Cisco got data that the speed of Zoom is equal n, and the speed of Flash is equal k.

Write a program that should lead to Cisco’s answer to the Flash question.
'''

def speedster_race(zoom_speed: int, flash_speed: int) -> str:
    if zoom_speed > flash_speed:
        return 'NO'
    elif flash_speed > zoom_speed:
        return 'YES'
    else:
        if zoom_speed == flash_speed:
            return "Don't know"

print(speedster_race(int(input()), int(input())))
