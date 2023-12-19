import os
import pandas as pd 

os.chdir("C:/Users/clemc/Desktop/UTC/TC02/INF2/TD/TD7")
data = pd.read_csv("notes.csv", delimiter=',')
print(data)
data["moyenne"] = data["median"]*0.3 + data["TP"]*0.3 + data["final"]*0.4
data.sort_values('moyenne', ascending=False, inplace=True)
data.to_csv('notes_triées.csv')