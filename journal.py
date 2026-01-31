#Importing required packages
from tkinter import *
from tkinter import ttk
import pandas as pd
import datetime as dt



emotions = pd.read_csv("Emotions.csv", index_col=0)
causes = pd.read_csv("Causes.csv", index_col=0)

#Need to implement tkinter here in future
def devPanel():
    sort_dict = {'up':0,'middle':1,'down':2}
    while True:
        choice = int(input ("1. Input emotion \n2. View list \n3. Edit existing emotions \n4. Import list \nAny. Exit options \n"))
        match choice:
            case 1:
                emotions.loc[len(emotions)] = [input("Enter name of feeling: ").lower(),
                                            input("Enter 'up' if good, 'middle' if okay, and 'down' if bad: ").lower()]
                emotions.drop_duplicates(inplace=True)
                emotions.to_csv("Emotions.csv", index=False)

            case 2:
                try:
                    emotions.drop("Unnamed: 0", axis=1, inplace=True)
                    emotions = emotions.iloc[emotions['emotion'].map(sort_dict).sort_values().index]

                except:
                    print()

                finally:
                    print(emotions,"\n")

            case 3:
                emotions.drop(int(input("Enter row number to delete: ")), inplace=True)
                emotions.to_csv("Emotions.csv", index=False)

            case 4:
                print("To import a list, name the csv file as 'Emotions.csv' and place it in this directory (folder in which this program is located). \nIf it isn't working, check the name, which is case sensitive and needs to be exact.")

            case _:
                return


def findCause(emotion):
    reflection = ""
    if emotion == "up":
        cause = input("That's great! What's making you feel that way? \n").lower()

    elif emotion == "middle":
        cause = input("No problem, you don't always have to feel so good. What's making you feel so, though? \n").lower()

    else:
        cause = input("Oh no. What's making you feel so down today? \n").lower()

    if input("Do you want to reflect on this? (y/n): ").lower() == 'y':
        reflection = reflect()

    causes.loc[len(causes)] = [emotion, cause, reflection, dt.datetime.now()]
    causes.sort_values(by=['time'], ascending=False)


def reflect():
    print ("Continue to reflect here (type qq and press enter in a new line to exit): ")
    reflection = ""
    while True:
        reflection += input()+"\n"
        if reflection.find("qq") != -1:
            return reflection[:len(reflection)-1]



print("Hey friend, welcome to this journal thingy!")
feeling = input("How are you doing today? (input 1 for dev panel) \n")
feeling = feeling.lower()

if feeling == "1":
    devPanel()

try:
    emotion = emotions.at[feeling, "emotion"]
    findCause(emotion)

except KeyError:
    choice = input("Feeling not recognised, do you want to add in settings? (y/n): ").lower()
    if choice == "y":
        devPanel()

finally:
    emotions.to_csv("Emotions.csv", index=False)
    causes.to_csv("Causes.csv", index=False)
    print("Thank you for updating your journal. Check back in whenever you need to log your mood again :)")


#Need to add the ability to check your reflections, emotions, and such