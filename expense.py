from PyInquirer import prompt
import csv

users = []
expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
]

spender_questions = [
    {
        "type":"list",
        "name":"spender",
        "message": "Who is the spender ?",
        "choices": users,
    }
]

def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    if users == []:
        with open('users.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                users.append(row[0])


    infos2 = prompt(spender_questions)
    with open('expense_report.csv', 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=" ")
        writer.writerow([infos["amount"]] + [infos["label"]] + [infos2["spender"]])
    print("Expense Added !")
    
    #############################################################################################
    # Add in the file "users_info.csv" the name of users and the amount of money after spliting #
    #############################################################################################

    open('users_info.csv', 'a+', newline='')
    with open('users_info.csv', 'r+', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=" ")
        reader = csv.reader(csvfile)
        data = list(csvfile)
        finaldata = []
        for i in range(len(data)):
            string = data[i].split()
            finaldata.append(str(string[1]))
        if data == []:
            for i in range(len(users)):            
                    if users[i] == infos2["spender"]:
                        writer.writerow([users[i]] + [int(infos["amount"]) - int(infos["amount"]) / (len(users))])
                    else :
                        writer.writerow([users[i]] + [-1 * int(infos["amount"]) / (len(users))])
        else:
            open("users_info.csv", "w").close()
            for i in range(len(users)):            
                    if users[i] == infos2["spender"]:
                        writer.writerow([users[i]] + [(int(infos["amount"]) - int(infos["amount"]) / (len(users))) + float(finaldata[i])])
                    else :
                        writer.writerow([users[i]] + [(-1 * int(infos["amount"]) / (len(users))) + float(finaldata[i])])
    return True


