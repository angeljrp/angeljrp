print("Hello welcome to the quiz")
print("you will be asked a series of question and based on your answer you will have a score")
play = input("do you want to play? (yes or no) ")

if play != "yes":
    input("Good bye")
    exit()

import csv
d = {}
with open('data.csv', mode='r') as f:
    data = csv.reader(f)
    for rows in data:
        d[rows[0]] = {'question': rows[1], 'answer': rows[2], 'points': rows[3]}

highscore = 0
points = 0

for row in d:
    print('question: ' + d[row]['question']) 
    answer = input('')
    if answer == d[row]['answer']:
        points = points + int(d[row]['points'])

if points > highscore:
    highscore = points

print('You have finished the quiz')
input(f'Your higher score was {highscore}')