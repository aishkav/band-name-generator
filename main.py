# Band Name Generator
# A simple Python program that creates a fun band name based on user input

print("Welcome to the Band Name Generator!")

# Ask the user which city they grew up in
city = input("Which city did you grow up in?\n")

# Ask the user for their pet name
pet = input("What's the name of your pet?\n")

# Create the band name by concatenating the city and pet names
band_name = city + " " + pet

# Print the band name for the user
print("Your Band Name could be: " + band_name)
