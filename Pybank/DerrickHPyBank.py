###In this challenge, you are tasked with creating a Python script for analyzing the financial 
#records of your company. You will give a set of financial data called [budget_data.csv]
#(PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, 
#your company has rather lax standards for accounting so the records are simple.)

###Your task is to create a Python script that analyzes the records to calculate each of the following:

  #The total number of months included in the dataset

  #The net total amount of "Profit/Losses" over the entire period
        #net total = (profit/losses) > whole period
  #The average of the changes in "Profit/Losses" over the entire period
    #avgDelta = 0
  #The greatest increase in profits (date and amount) over the entire period

  #The greatest decrease in losses (date and amount) over the entire period

#As an example, your analysis should look similar to the one below:

import os 
import csv
totalMonths = 0
netTotal = 0
avgDelta = 0
GreatIncDate = ""
GreatIncAmount = 0
GreatDecDate = ""
GreatDecAmount = 0
CurrentProfit = 0
CurrentDate = ""
prev_net = 0
net_change_list = []


csvpath = os.path.join('bankData.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    val1=next(csvreader)  
    val1=next(csvreader)
    
    totalMonths = 1
    prev_net = int(val1[1])
    for row in csvreader:
        CurrentProfit = int(row[1])
        CurrentDate = row[0]
        totalMonths = totalMonths + 1
        netTotal = netTotal + int(row[1])
        # if CurrentProfit > GreatIncAmount:
        #     GreatIncAmount = CurrentProfit
        #     GreatIncDate = CurrentDate 
        #     GreatDecDate = 
        # if CurrentProfit < GreatDecAmount:
        #     GreatDecAmount = CurrentProfit
        #     GreatDecDate = CurrentDate 
        netchange=int(row[1]) - prev_net
        net_change_list = net_change_list+[netchange]
        prev_net = int(row[1])
        if GreatIncAmount<netchange:
          GreatIncAmount=netchange
          GreatIncDate = row[0]
        if GreatDecAmount>netchange:
          GreatDecAmount=netchange
          GreatDecDate = row[0]
jj=sum(net_change_list)/len(net_change_list)
avgDelta = netTotal/totalMonths

with open("output.txt.","w") as f:
    print("Financial Summary", file=f)
    print(avgDelta, file=f)
    print(GreatIncAmount, file=f)
    print(GreatIncDate, file=f)
    print(GreatDecAmount, file=f)
    print(GreatDecDate, file=f)
    print(totalMonths, file=f)


# print("Financial Summary")
# print(avgDelta)
# print(GreatIncAmount)
# print(GreatIncDate)
# print(GreatDecAmount)
# print(GreatDecDate)
# print(totalMonths)    



print(f"the total months: {totalMonths}")   
print(f"the net total:{netTotal}")
print(f"the average change:{jj}")
print(f"the greatest increase:{GreatIncAmount} {GreatIncDate}")
print(f"the greatest decrease:{GreatDecAmount} {GreatDecDate}")



