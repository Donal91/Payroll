import os
import csv
def analyze_vote(file_path):

    # Analyze variables
    total_votes=0
    candidates={}

    #Read the csv file
    with open('election_data.csv','r') as file:

        # create a csv reader object
        csv_reader = csv_reader(file)

        # skip the header row
        header = next(csv_reader)

        #Iteration in the csv file
        for row in csv_reader:

            # count total votes
            total_votes= total_votes + 1

             # Extract candidate name from the row
            candidate = row[2]
        
            # update the candidate's vote count
            if candidate in candidates:
               candidates[candidate]= candidate + 1
            else:
               candidates[candidate]=1

            # calculate the percentage of votes each candidate won
            percentages = {candidate : (votes/total_votes) * 100 for candidate, votes in candidates.items()}

            # find the winner based on popular vote
            winner = max(candidates,key=candidates.get)

            return total_votes, candidates, percentages, winner
        
    # Define the file path
    file_path = 'elecation_data.csv'

    # call the function and get the results
    total_votes, candidates_votes, vote_percentages, winner = analyze_vote('elecation_data.csv')

    #Print the results
    
    print("Election Results")
    print("-------------------------------------------------------------")
    print(f"Total votes:{total_votes}")
    print("-------------------------------------------------------------")
    print("Candidates whp received votes:")
    for candidate, votes in candidates_votes.items():
       print(f"{candidate}: {vote_percentages[candidate]:.3f}% ({votes})")
    print("-------------------------------------------------------------")
    print(f"Winner: {winner}")
    print("-------------------------------------------------------------")

    

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              







            






