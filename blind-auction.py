# ASCII art for a logo, representing a stylized auction platform or similar concept.
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
# Printing the logo to display at the start of the program.
print(logo)


# Function to find the user with the highest bid and announce the winner.
def finding_highest_bid():
    # Variable to keep track of the highest bid.
    bid_list = ''  
    # Variable to store the name of the highest bidder.
    winning_user = ""

    # Loop through the dictionary of user inputs to compare bids.
    for user in users_inputs:
        # Retrieve the bid value for the current user.
        bid = users_inputs[user]
        # Check if the current bid is greater than the highest bid so far.
        if bid > bid_list:  
            bid_list = bid  # Update the highest bid.
            winning_user = user  # Update the name of the highest bidder.

    # Print the winner and their bid amount.
    print(f"winner is {winning_user} and bid is {bid_list}")


# Variable to control the continuation of the bidding process.
new_user = "yes"
# Dictionary to store user names as keys and their respective bids as values.
users_inputs = {}

# Loop to keep collecting user inputs until no more users want to bid.
while new_user == "yes":
    # Prompt the user for their name.
    user_name = input("What is your name?: ")
    # Prompt the user for their bid.
    user_bid = input(int("What is your bid?:$ "))

    # Store the user's name and bid in the dictionary.
    users_inputs[user_name] = int(user_bid)  # (Fixed: Converted bid to an integer)

    # Ask if there are other users who want to bid.
    new_user = input("Any other users who want to bid? ").lower()

    # If there are more users, print new lines for clarity.
    if new_user == "yes":
        print(20 * "\n")

# Call the function to determine the highest bid and announce the winner.
finding_highest_bid()
