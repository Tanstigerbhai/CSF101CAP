# Tandin Wangchuk
#BE ELECTRICAL ENGG. 1YEAR
# 02230081
################################
# REFERENCES
# youtube
# @DQ-Logo
################################
# SOLUTION
# Your Solution Score:50055
# Put your number here:50055
# input_1_cap1.txt()
################################

# Define a dictionary to map outcomes to scores
outcome_scores = {
    ('X', 'A'): 3, ('X', 'B'): 1, ('X', 'C'): 2,
    ('Y', 'A'): 4, ('Y', 'B'): 5, ('Y', 'C'): 6,
    ('Z', 'A'): 8, ('Z', 'B'): 9, ('Z', 'C'): 7
}
#Assigns scores to outcomes and opponent choices.
#Each tuple key represents specific outcome and opponent pair.
#corresponding score represents assigned value.

# Read the input.txt file
def read_input(file_name):
    Turn = []
    with open(file_name, 'r') as file:
        for line in file:
            opponent_choice, outcome = line.split()
            Turn.append((opponent_choice, outcome))
    return Turn
#The argument for the above function is the file name or input.
#It reads everything in the file,line by line.
#Every line has two elements: the result and the opponent's option, which  is divided by a space.
#It appends each pair of opponent's choice and outcome as a tuple to the list Turn
#Ultimately, it gives back the list Turn, which includes every decision and result made by the opponent.


# Calculate the score for each round
def calculate_score(Turn):
    score = 0
    for opponent_choice, outcome in turn:
        score += outcome_scores[(outcome, opponent_choice)]
    print(f"The total score is: {score}")
#Above function takes the list of opponent choices and outcomes (Turn) as input.
#Initializes score variable to 0.
# Iterates every round in turn.
# Retrieves score from outcome_scores dictionary based on results and opponent selection.
#Prints total score after processing all rounds.

# Example usage:
file_name = "CSF101CAP/input_1_cap1.txt"
turn = read_input(file_name)
calculate_score(turn)

#Assigns "02230081/input_1_cap1.txt" as file_name.
# To read input from a specific file, call the read_input function.
#  turn are kept in the turn variable.
# To output the total score depending on opponent choices and outcome, call the calculate_score function.
