# Congratulations message
# Data types in python - String operations

# Get the persons's name and achievement
name = input("David Handsome:")
achievement = input("Most Handsome Boy in the World:")

# String operations
name_title = name.title()  # Capitalize first letterof each word
achievement_upper = achievement.upper() # make achievement uppercase
message1 = "Congratulations, " + name_title + "!"
message2 = f"Well done on {achievement_upper}!"
message3 = "We are proud of you " + name_title + "!"

print()
print("=" * 40)
print(message1)
print(message2)
print(message3)
print("=" * 40)