from PyInquirer import prompt
import csv
user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"What is your name ?",
    },
]

def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    with open('users.csv', 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=" ")
        writer.writerow([infos["name"]])
    print("New user named " + infos["name"] + " was created")
    return True