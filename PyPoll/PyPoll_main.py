#!/usr/bin/env python
# coding: utf-8

# In[1]:


## You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

#   * The total number of votes cast

#   * A complete list of candidates who received votes

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.
# * In addition, your final script should both print the analysis to the 
# terminal and export a text file with the results.


# In[2]:


#Import dependencies
import csv
import os


# In[3]:


#Open CSV
file = open('election_data.csv')
csvreader = csv.reader(file, delimiter=',')
csv_header = next(csvreader)


# In[4]:


#Declare Variables
Total_Votes = 0
Khan_Votes = 0
Correy_Votes = 0
Li_Votes = 0
Otooley_Votes = 0


# In[5]:


#Iterate through rows and count votes
for row in csvreader:

    Total_Votes +=1

    if row[2] == "Khan":
            Khan_Votes +=1
    elif row[2] == "Correy":
            Correy_Votes +=1
    elif row[2] == "Li":
            Li_Votes +=1
    elif row[2] == "O'Tooley":
            Otooley_Votes +=1


# In[6]:


# Print a the summary of the analysis
Khan_Percent = (Khan_Votes/Total_Votes) *100
Khan = round(Khan_Percent)
Correy_Percent = (Correy_Votes/Total_Votes) * 100
Correy= round(Correy_Percent)
Li_Percent = (Li_Votes/Total_Votes)* 100
Li= round(Li_Percent)
Otooley_Percent = (Otooley_Votes/Total_Votes) * 100
Otooley = round(Otooley_Percent)


# In[7]:


# Calculate Winner Of The Election Based On Popular Vote
Winner = max(Khan_Votes, Correy_Votes, Li_Votes, Otooley_Votes)

if Winner == Khan_Votes:
    winner_name = "Khan"
elif Winner == Correy_Votes:
    winner_name = "Correy"
elif Winner == Li_Votes:
    winner_name = "Li"
else:
    winner_name = "O'Tooley" 


# In[8]:


print(Total_Votes)
print(Khan_Votes)
print(Correy_Votes)
print(Li_Votes)
print(Otooley_Votes)


# In[ ]:


# Print the summary table
print(f"Election Results")
print("----------------------------")
print(f"Total Votes: {Total_Votes}")
print("----------------------------")
print(f"Khan: {Khan:.3f}% ({Khan_Votes})")
print(f"Correy: {Correy:.3f}% ({Correy_Votes})")
print(f"Li: {Li:.3f}% ({Li_Votes})")
print(f"O'Tooley: {Otooley:.3f}% ({Otooley_Votes})")
print(f"----------------------------")
print(f"Winner: {winner_name}")
print(f"----------------------------")


# In[ ]:


# Specify File To Write To
output_file = os.path.join('election_data_revised.text')

# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(output_file, 'w',) as txtfile:

# Write New Data
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {Total_Votes}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {Khan:.3f}%({Khan_Votes})\n")
    txtfile.write(f"Correy: {Correy:.3f}%({Correy_Votes})\n")
    txtfile.write(f"Li: {Li:.3f}%({Li_Votes})\n")
    txtfile.write(f"O'Tooley: {Otooley:.3f}%({Otooley_Votes})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"---------------------------\n")


# In[ ]:




