import pandas as pd
data=pd.read_csv("weather_data.csv")

#Reading whole data from a file
print(data)

print("\n")
#Reading the data of a particular column
#Extracting only temp columns
print(data["temp"])
print("\n")
#Reading the data of a particular row
#Extracting row data, day contains monday

print(data[data.day=="Monday"])

#Reading the row data which temp is high
print(data[data.temp==data["temp"].max()])
