#Importing required packages
from tkinter import *
from tkinter import ttk
import pandas as pd
import os
import datetime as dt
import matplotlib as mp



emotions = pd.DataFrame()
causes = pd.DataFrame()

def importFiles():
    try:
        emotions = pd.read_csv("Emotions.csv", index_col=0)
        causes = pd.read_csv("Causes.csv",)

    except:
        print ("The required csv files are either missing or empty, creating new ones")
        emotions = pd.DataFrame({"feeling":[], "emotion": []})
        causes = pd.DataFrame({"feeling": [], "cause": [], "reflection":[], "time":[]})

    finally:
        emotions.to_csv("Emotions.csv")
        causes.to_csv("Causes.csv")


def devPanel(): #Settings/developer panel to edit Emotions.csv file
    global emotions
    sort_dict = {'up':0,'middle':1,'down':2}
    while True:
        choice = int(input ("1. Input emotion \n2. View list \n3. Edit existing emotions \n4. Import list \nAny. Exit options \n"))
        match choice:
            case 1:
                new_emotion = pd.DataFrame({"feeling": [input("Enter name of feeling: ").lower()],
                               "emotion": [input("Enter 'up' if good, 'middle' if okay, and 'down' if bad: ").lower()]})
                emotions = pd.concat([emotions, new_emotion])
                emotions.drop_duplicates().to_csv("Emotions.csv")

            case 2:
                try:
                    emotions = emotions.iloc[emotions['emotion'].map(sort_dict).sort_values().index]
                    emotions.reset_index()

                except:
                    print()

                finally:
                    print(emotions,"\n")

            case 3:
                emotions.drop(int(input("Enter row number to delete: ")), inplace=True)
                emotions.to_csv("Emotions.csv")

            case 4:
                print('''Names of csv files: 
                    Emotions.csv - for the list of feelings and the respective emotion
                    Causes.csv - for the list of feelings, their causes, the reflections, and the time at which it was felt

                    To import a list, name the csv file as required and place it in this directory: ''', os.getcwd(),
                    '''\nIf it isn't working, check the name, which is case sensitive and needs to be exact.
                    Also, for correct displaying of current list, make sure that your csv files are formatted only as follows (make sure to delete any other columns:

                    Emotions.csv:
                    feeling, emotion

                    Causes.csv:
                    feeling, cause, reflection, time
                    ''')
            
            case _:
                return


def findCause(emotion): #To find the cause of the emotion, and reflection
    global causes
    reflection = ""
    print("Please answer in one word")
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


def reflect(): #To let multi-line reflection
    print ("Continue to reflect here (type qq and press enter in a new line to exit): ")
    reflection = ""
    while True:
        reflection += input()+"\n"
        if reflection.find("qq") != -1:
            return reflection[:len(reflection)-1]

#FINISH ANALYSE
def analyse(feeling, emotion):
    choice = input("1. Check past trends for current emotion \n2. Plot mood over certian time")



importFiles()
print("Hey friend, welcome to this journal thingy!")
feeling = input("How are you doing today? (input 1 for dev panel) \n").lower()

if feeling == "1":
    devPanel()


else:
    try:
        current_emotion = emotions.at[feeling, "emotion"]
        findCause(emotion)

        choice = input("Would you like to analyse your previous emotions? (y/n): ").lower()
        if choice == "y":
            analyse(feeling, emotion)

    except KeyError:
        choice = input("Feeling not recognised, do you want to add in settings? (y/n): ").lower()
        if choice == "y":
            devPanel()

    finally:
        emotions.to_csv("Emotions.csv", index=False)
        causes.to_csv("Causes.csv", index=False)
        print("Thank you for updating your journal. Check back in whenever you need to log your mood again :)")


#Need to add the ability to check your reflections, emotions, and such
