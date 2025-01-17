'''
The number of entries is
n
n is the number of dog years. Write a program that calculates the age of the dog in human years according to the following algorithm:
for the first two years, the year of the dog is equal 10.5 human years, after that every year the dog is equal to 4 man years.
'''

def dog_age(age: int) -> float:
    if 1 <= age <= 2:
        return age * 10.5
    else:
        return (2 * 10.5) + ((age - 2) * 4)

print(dog_age(int(input())))
