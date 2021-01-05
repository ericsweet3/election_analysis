x = 0
while x <= 5:
    print(x)
    x = x + 1


counties = ["Arapahoe", "Denver", "Jefferson"]

for county in counties:
    print(county)


numbers = [0,1,2,3,4]
for num in numbers:
    print(num)


for i in range(len(counties)):
    print(counties[i])



counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

    
# for key, value in dictionary_name.items():
    # print(key, value)

for county, voters in counties_dict.items():
    print(county, voters)


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)


for county_dict in voting_data:
    for value in county_dict.values():
        print(value)


for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")


# These two are the same code


for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")




#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
 #   f"You received {candidate_votes} number of votes. "
  #  f"The total number of votes in the election was {total_votes}. "
   # f"You received {candidate_votes / total_votes * 100}% of the total votes.")

#print(message_to_candidate)


# f'{value:{width}.{precision}}'

