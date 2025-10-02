# --- Standard Library Imports (come with Python) ---
import random      # Used for generating random numbers
import math        # Provides mathematical functions
import os          # Interacting with the operating system (files, paths, env vars)
import datetime    # Working with dates and times
import string      # ASCII letters, digits, punctuation
import unicodedata # Unicode database (lets you work with emoji/characters)

# --- Third-Party Library (requires pip install) ---
import matplotlib.pyplot as plt  # Matplotlib: data visualization


# Using random
number = random.randint(0, 10)  # Generate a random integer between 0 and 10
print("Random number:", number)  # Print the random number


# Using math
print("Square root of 16:", math.sqrt(16))  # Find the square root of 16
print("Pi constant:", math.pi)              # Print the value of Pi


# Using os
print("\nCurrent working directory:", os.getcwd())   # Show the current working directory
print("List of files in this directory:", os.listdir("."))  # List files in the current directory


# Using datetime
today = datetime.date.today()        # Get today's date
now = datetime.datetime.now()        # Get the current date and time
print("\nToday's date:", today)      # Print today's date
print("Current time:", now)          # Print the current time (full datetime)
print("Current time:", now.strftime("%H:%M:%S"))  # Print the time in HH:MM:SS format


# Using string
print("\nASCII Letters:", string.ascii_letters)  # Print all ASCII letters (a-z, A-Z)
print("Digits:", string.digits)                  # Print all digit characters (0-9)
print("Punctuation:", string.punctuation)        # Print punctuation characters


# Using unicodedata (Unicode + Emoji fun)
smiley = "😊"                                     # Define a smiley emoji
print("\nEmoji example:", smiley)                 # Print the emoji
print("Unicode name of", smiley, "is:", unicodedata.name(smiley))  
# Print the official Unicode name of the emoji


# Using matplotlib
x = [1, 2, 3, 4, 5]             # Define a list of x-values
y = [i**2 for i in x]           # Create y-values by squaring each x

plt.plot(x, y, marker="o")      # Plot x vs y with circle markers
plt.title("Simple Matplotlib Example")  # Add a title to the plot
plt.xlabel("X values")          # Label the X-axis
plt.ylabel("Y = X^2")           # Label the Y-axis
plt.show()                      # Display the plot in a window
