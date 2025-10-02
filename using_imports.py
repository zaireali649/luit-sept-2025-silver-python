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
number = random.randint(0, 10)  # Random integer between 0 and 10
print("Random number:", number)


# Using math
print("Square root of 16:", math.sqrt(16))
print("Pi constant:", math.pi)


# Using os
print("\nCurrent working directory:", os.getcwd())
print("List of files in this directory:", os.listdir("."))


# Using datetime
today = datetime.date.today()
now = datetime.datetime.now()
print("\nToday's date:", today)
print("Current time:", now)
print("Current time:", now.strftime("%H:%M:%S"))


# Using string
print("\nASCII Letters:", string.ascii_letters)
print("Digits:", string.digits)
print("Punctuation:", string.punctuation)


# Using unicodedata (Unicode + Emoji fun)
smiley = "😊"
print("\nEmoji example:", smiley)
print("Unicode name of", smiley, "is:", unicodedata.name(smiley))


# Using matplotlib
x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]  # Square each number

plt.plot(x, y, marker="o")
plt.title("Simple Matplotlib Example")
plt.xlabel("X values")
plt.ylabel("Y = X^2")
plt.show()  # Opens a plot window
