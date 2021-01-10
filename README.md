# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular votes.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code

## Summary
The analysis of the election show that:
- There were "x" votes cast in the election.
- The candidates were:
  - Candidate 1
  - Candidate 2
  - Candidate 3
 - The candidate results were:
  - Candidate 1 received "x%" of the vote and "y" number of votes
  - Candidate 2 received "x%" of the vote and "y" number of votes
  - Candidate 3 received "x%" of the vote and "y" number of votes
 - The winner of the election was:
  - Candidate (1, 2, or 3), who received "x%" of the vote and "y" number of votes
  

  

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular votes.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code

## Summary
The analysis of the election show that:
- There were "x" votes cast in the election.
- The candidates were:
  - Candidate 1
  - Candidate 2
  - Candidate 3
 - The candidate results were:
  - Candidate 1 received "x%" of the vote and "y" number of votes
  - Candidate 2 received "x%" of the vote and "y" number of votes
  - Candidate 3 received "x%" of the vote and "y" number of votes
 - The winner of the election was:
  - Candidate (1, 2, or 3), who received "x%" of the vote and "y" number of votes

## Challenge Overview
  - For the challenge aspect, we needed to add to the existing code to not only find the complete voter turnout for each county, but to also find the percentage of each county and then the county with the highest voter turnout. 

## Challenge Summary
  - So lets take a look at some of the code that we added for this challenge, specifically the parts that took a more specific look at the data that was provided. Starting with the county percentages, you can see that we simply took the votes from the specific county that we are looping through, divided that by the total amount of votes from all the counties combined, and then multiplied that by 100 to convert it to a percentage (1a). This can easily be transferable to another project in all states and any county, just depends on the list that you are importing for the project. The next part was finding the percentage of the total votes that each candidate got. For this I did exactly the same kind of formula that I did for the county votes and their percentages (1b).
  
  
  ## Pictures of Code
  
  - 1a: ![county votes](https://user-images.githubusercontent.com/75768098/104129720-fb07e180-5332-11eb-8c36-a73c0fa18eeb.png)


  - 1b: ![candidate percentages](https://user-images.githubusercontent.com/75768098/104129738-1c68cd80-5333-11eb-887e-9820e8944fd3.png)
