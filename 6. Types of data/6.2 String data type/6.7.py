'''
Write a program that reads the name of the football team and displays information about it in the following format:

The <name of the football team> has a length of <length of the name of the football team> characters
'''

def football_team(team_name: str) -> str:
    return f'Футбольная команда {team_name} имеет длину {len(team_name)} символов'

print(football_team(str(input())))
