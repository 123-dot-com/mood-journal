#Importing required packages
from tkinter import *
from tkinter import ttk
import pandas as pd



#Need to implement tkinter here in future
def devPanel():
    sort_dict = {'up':0,'middle':1,'down':2}
    emotions = pd.read_csv("Emotions.csv", index_col=0)
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










print("Hey friend, welcome to this journal thingy~!")
feeling = input("How are you doing today? (input 1 for dev panel) \n")
feeling = feeling.lower()

if feeling == "1":
    devPanel()


