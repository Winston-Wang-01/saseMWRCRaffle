from random import seed
from random import randint
from playsound import playsound as ps

import pandas as pd 
import sys

# simple script to run a weighted lottery on Socio attendees 
# so we dont have to pay $100 for a prebuilt program or input all our data by hand
# will draw data from excel sheet exported from the Socio event game

inFile = sys.argv[1]

df = pd.read_excel(inFile, sheet_name='Leaderboard', usecols="B,C,D")
max = df["Points Earned"].sum()

print(df[["Attendee Name", "Points Earned"]])
print("\n")
print("Total Points Earned: ", max)

#removing winners from day 1 from consideration
df = df[df['Attendee Email'] != "chen.9936@osu.edu"]
df = df[df['Attendee Email'] != "chaudharyu1@udayton.edu"]
df = df[df['Attendee Email'] != "jody.suryatna@saseconnect.org"]
df = df[df['Attendee Email'] != "wang4362@purdue.edu"]

cont = input("Input \"y\" to roll for a winner. ")
while (cont == "y"):

    if (len(df.index) == 0):
        print("No winners left.") # ideally this doesnt happen
        break
    

    selected = randint(0,max - 1)
    winnerIndex = 0
    for ind in df.index:
        selected -= df["Points Earned"][ind]
        if (selected <= 0):
            winnerIndex=ind
            break

    winnerName = df["Attendee Name"][winnerIndex]
    winnerPercentage = df["Points Earned"][winnerIndex] / max
    winnerEmail = df["Attendee Email"][winnerIndex]
    ps('./drum-roll-sound-effect.mp3')
    print("Winner: ", winnerName, "Email:", winnerEmail, "Odds:", winnerPercentage)


    cont = input ("Input \"y\" to roll for another winner. ")
    df = df.drop(winnerIndex)
    max = df["Points Earned"].sum()
    