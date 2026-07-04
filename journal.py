#Importing required packages
import pandas as pd
import os
import datetime as dt
import matplotlib.pyplot as mp
import numpy as np



emotions = pd.DataFrame()
causes = pd.DataFrame()

def importFiles():
    global emotions
    global causes
    try:
        emotions = pd.read_csv("Emotions.csv", index_col=0)
        causes = pd.read_csv("Causes.csv", index_col=0)

    except:
        print ("The required csv files are either missing or empty, creating new ones")
        emotions = pd.DataFrame({"feeling":[], "mood": []})
        causes = pd.DataFrame({"feeling": [], "mood": [], "cause": [], "reflection":[], "date": [], "time": []})

    finally:
        emotions.to_csv("Emotions.csv")
        causes.to_csv("Causes.csv")


def devPanel(): #Settings/developer panel to edit Emotions.csv file
    global emotions
    sort_dict = {'up':0,'middle':1,'down':2}
    while True:
        choice = int(input ('''
1. Input emotion 
2. View list 
3. Edit existing emotions 
4. Import list 
0. Exit options
'''))
        match choice:
            case 1:
                new_emotion = pd.DataFrame({"feeling": [input("Enter name of feeling: ").lower()],
                               "mood": [input("Enter 'up' if good, 'middle' if okay, and 'down' if bad: ").lower()]})
                emotions = pd.concat([emotions, new_emotion])
                emotions.drop_duplicates().to_csv("Emotions.csv")

            case 2:
                try:
                    emotions = emotions.iloc[emotions['mood'].map(sort_dict).sort_values().index]
                    emotions.reset_index()

                except:
                    print()

                finally:
                    print(emotions,"\n")

            case 3:
                emotions.drop(int(input("Enter row number to delete: ")), inplace=True)
                emotions.to_csv("Emotions.csv")

            case 4:
                print('''
Names of csv files: 
Emotions.csv - for the list of feelings and the respective emotion
Causes.csv - for the list of feelings, their causes, the reflections, and the time at which it was felt

To import a list, name the csv file as required and place it in this directory: ''', os.getcwd(),'''
If it isn't working, check the name, which is case sensitive and needs to be exact.
Also, for correct displaying of current list, make sure that your csv files are formatted only as follows (make sure to delete any other columns:

Emotions.csv:
, feeling, mood

Causes.csv:
, feeling, mood, cause, reflection, date, time
''')
            
            case _:
                return


def findCause(feeling, mood): #To find the cause of the emotion, and reflection
    global causes
    reflection = ""
    print("Please answer in one word")
    if mood == "up":
        cause = input("That's great! What's making you feel that way? \n").lower()

    elif mood == "middle":
        cause = input("No problem, you don't always have to feel so good. What's making you feel so? \n").lower()

    else:
        cause = input("What's making you feel so down today? \n").lower()

    if input("Do you want to reflect on this? (y/n): ").lower() == 'y':
        reflection = reflect()
    
    new_row = pd.DataFrame({'feeling': [feeling], 'mood': [mood], 'cause': [cause], 'reflection': [reflection], 'date': [dt.date.today()], 'time': [dt.datetime.now().time()]})
    causes = pd.concat([causes, new_row], ignore_index=True)
    causes.sort_values(by=['time'], ascending=False)


def reflect(): #To let multi-line reflection
    print ("Continue to reflect here (type qq and press enter in a new line to exit): ")
    reflection = ""
    while True:
        reflection += input()+"\n"
        if reflection.find("qq") != -1:
            return reflection[:len(reflection)-1]


def analyse(current_feeling, current_mood): #To analyse emotions, and moods
    global emotions
    global causes
    while True:
        choice = int(input('''
1. Frequency of moods (bar graph)
2. Mood breakdown by time on a specific day (pie chart)
3. Previous causes for current emotion (list)
4. Emotions felt around this time (list)
5. History of moods over a time range (line graph)
0. Exit 
> '''))
        try:
            match choice:
                case 1: 
                    labels = ["Good", "Okay", "Bad"]
                    data = causes['mood'].value_counts(sort=False)
                    mp.bar(labels, data, color=['green', 'yellow', 'red'])
                    mp.show()

                case 2:
                    print ("Enter dates in the following format: \n",dt.date.today())
                    lower_lim = pd.to_datetime(input("Enter lower limit of dates to plot for (inclusive): ")).date()
                    upper_lim = pd.to_datetime(input("Enter upper limit of dates to plot for (inclusive): ")).date()
                    selected_rows = causes[(causes['date'] >= lower_lim) & (causes['date'] <= upper_lim)]
                    data = causes['mood'].value_counts(sort=False)
                    mp.pie(data, labels=['Good','Okay','Bad'], colors=['green', 'yellow', 'red'])
                    mp.show()

                case 3:
                    selected_rows = causes[causes['feeling'] == current_feeling]
                    data = selected_rows[['cause', 'reflection', 'date', 'time']]
                    print (data)

                case 4:
                    lower_lim = (dt.datetime.now() - dt.timedelta(hours=2)).time()
                    upper_lim = (dt.datetime.now() + dt.timedelta(hours=2)).time()
                    selected_rows = causes[(causes['time'] >= lower_lim) & (causes['time'] <= upper_lim)]
                    data = selected_rows[['feeling', 'cause', 'reflection']]
                    print (data)

                case 5:
                    print ("Enter dates in the following format: \n",dt.date.today())
                    lower_lim = pd.to_datetime(input("Enter lower limit of dates to plot for (inclusive): ")).date()
                    upper_lim = pd.to_datetime(input("Enter upper limit of dates to plot for (inclusive): ")).date()
                    selected_rows = causes[(causes['date'] >= lower_lim) & (causes['date'] <= upper_lim)]
                    data_x = selected_rows['time']
                    data_y = selected_rows['mood']
                    mp.plot(data_x, data_y)
                    mp.show()

                case _:
                    return
        except:
            print ("The Causes.csv file may be empty, therefore, analysis is not possible currently")


importFiles()
print("Hey friend, welcome to this journal thingy!")
current_feeling = input("How are you doing today? (input 1 for dev panel) \n").lower()

if current_feeling == "1":
    devPanel()

else:
    try:
        current_mood = emotions.at[current_feeling, "mood"]
        findCause(current_feeling, current_mood)
        choice = input("Would you like to analyse your previous emotions? (y/n): ").lower()
        if choice == "y":
            analyse(current_feeling, current_mood)

    except KeyError:
        choice = input("Feeling not recognised, do you want to add in settings? (y/n): ").lower()
        if choice == "y":
            devPanel()

    finally:
        emotions.to_csv("Emotions.csv")
        causes.to_csv("Causes.csv")
        print("Thank you for updating your journal. Check back in whenever you need to log your mood again :)")
