# Health Management System
#  3 clients - x,y,z
# Whose log or retrieval
# For Exercise or food
import datetime


def getdate():
    return [str(datetime.datetime.now())]


action = 0
while action != 3:
    action = int(input("What do you want to do?\n 1.Log\n 2.Retrieve\n 3.Exit\n"))
    if action == 1:
        log_for = 0
        while log_for != 3:
            log_for = int(input("What to log-\n 1.Food\n 2.Exercise\n Press 3 to exit log\n"))
            if log_for == 1:
                log_food = 0
                while log_food != 4:
                    log_food = int(input("Log food for-\n 1.x\n 2.y\n 3.z\n Press 4 to Exit\n"))
                    if log_food == 1:
                        food = input("Enter food to be logged\n")
                        with open("x_food.txt", "a") as x_food:
                            x_food.write(str(getdate()) + ": " + food + "\n")
                        print("Successfully logged the food for x")

                    elif log_food == 2:
                        food = input("Enter food to be logged\n")
                        with open("y_food.txt", "a") as y_food:
                            y_food.write(str(getdate()) + ": " + food + "\n")
                        print("Successfully logged the food for y")

                    elif log_food == 3:
                        food = input("Enter food to be logged\n")
                        with open("z_food.txt", "a") as z_food:
                            z_food.write(str(getdate()) + ": " + food + "\n")
                        print("Successfully logged the food for z")

            elif log_for == 2:
                log_exercise = 0
                while log_exercise != 4:
                    log_exercise = int(input("Log exercise for-\n 1.x\n 2.y\n 3.z\n Press 4 to Exit\n"))
                    if log_exercise == 1:
                        exercise = input("Enter exercise to be logged\n")
                        with open("x_exercise.txt", "a") as x_exercise:
                            x_exercise.write(str(getdate()) + ": " + exercise + "\n")
                        print("Successfully logged the exercise for x")

                    elif log_exercise == 2:
                        exercise = input("Enter exercise to be logged\n")
                        with open("y_exercise.txt", "a") as y_exercise:
                            y_exercise.write(str(getdate()) + ": " + exercise + "\n")
                        print("Successfully logged the exercise for y")

                    elif log_exercise == 3:
                        exercise = input("Enter exercise to be logged\n")
                        with open("z_exercise.txt", "a") as z_exercise:
                            z_exercise.write(str(getdate()) + ": " + exercise + "\n")
                        print("Successfully logged the exercise for z")

    elif action == 2:
        retrieve_for = 0
        while retrieve_for != 3:
            retrieve_for = int(input("What to retrieve-\n 1.Food\n 2.Exercise\n Press 3 to exit retrieval\n"))
            if retrieve_for == 1:
                retrieve_food = 0
                while retrieve_food != 4:
                    retrieve_food = int(input("Retrieve food for-\n 1.x\n 2.y\n 3.z\n Press 4 to Exit\n"))
                    if retrieve_food == 1:
                        with open("x_food.txt") as x_food:
                            for i in x_food:
                                print(i, end="")

                    elif retrieve_food == 2:
                        with open("y_food.txt") as y_food:
                            for i in y_food:
                                print(i, end="")

                    elif retrieve_food == 3:
                        with open("z_food.txt") as z_food:
                            for i in z_food:
                                print(i, end="")

            elif retrieve_for == 2:
                retrieve_exercise = 0
                while retrieve_exercise != 4:
                    retrieve_exercise = int(input("Log exercise for-\n 1.x\n 2.y\n 3.z\n Press 4 to Exit\n"))
                    if retrieve_exercise == 1:
                        with open("x_exercise.txt") as x_exercise:
                            for i in x_exercise:
                                print(i, end="")

                    elif retrieve_exercise == 2:
                        with open("y_exercise.txt") as y_exercise:
                            for i in y_exercise:
                                print(i, end="")

                    elif retrieve_exercise == 3:
                        with open("z_exercise.txt") as z_exercise:
                            for i in z_exercise:
                                print(i, end="")
