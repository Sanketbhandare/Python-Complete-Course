# Conditional statements (if, else, elif)

# Project to check who is the winner of election based on number of votes?
# BJP or Congress

# input() - Take input from user, default data type is String

bjp_votes = int(input("Enter number of votes for BJP: "))
inc_votes = int(input("Enter number of votes for Congress: "))
# print(type(bjp_votes))
# print(type(inc_votes))

if bjp_votes > inc_votes:
    no_of_votes = bjp_votes - inc_votes
    # Use formatted string for Printing the variables print(f"")
    print(f"BJP has won the election by {no_of_votes} votes")
elif inc_votes > bjp_votes:
    no_of_votes = inc_votes - bjp_votes 
    print(f"INC has won the election by {no_of_votes} votes")    
else:
    print(f"Both parties has got equal votes. Results is Draw")