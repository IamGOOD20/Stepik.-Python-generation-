'''
The mad titan Thanos has collected all 6 of the stones of infinity and
intends to destroy half the population of the universe by a click of his fingers.
If the population of the universe is an odd number,
then the Titan will show mercy and round up the number of survivors to a greater extent.
Help the Avengers count the number of survivors.

Input format
The input is given a integer n is the population of the universe.

Output format
The program should produce one number - the number of survivors.
'''
def the_inevitability(population: int) -> int:
    population += 1
    half_of_population = population // 2
    return half_of_population

print(the_inevitability(int(input())))
