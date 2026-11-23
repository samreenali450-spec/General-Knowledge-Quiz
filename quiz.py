# General Knowledge Quiz - Project 4
# BS Computer Science | DecodeLabs Batch 2026

print("Welcome to General Knowledge Quiz! 🎉")
print("--------------------------------------")

# STORAGE - Initialize score to store the result
score = 0

# QUESTION 1 - INPUT -> PROCESS -> OUTPUT
print("\nQuestion 1:")
answer1 = input("What is the capital of France? ")
answer1 = answer1.strip().lower()  # Clean the input: remove spaces and make it lowercase

if answer1 == "paris":
    print("Correct! ✅")
    score = score + 1  # Update the score
else:
    print("Wrong! ❌ Correct answer is Paris")

# QUESTION 2
print("\nQuestion 2:")
answer2 = input("What is the capital of Japan? ")
answer2 = answer2.strip().lower()  # Clean the input

if answer2 == "tokyo":
    print("Correct! ✅")
    score = score + 1
else:
    print("Wrong! ❌ Correct answer is Tokyo")

# QUESTION 3
print("\nQuestion 3:")
answer3 = input("What is 2 + 2? ")
answer3 = answer3.strip().lower()  # Clean the input

if answer3 == "4" or answer3 == "four":
    print("Correct! ✅")
    score = score + 1
else:
    print("Wrong! ❌ Correct answer is 4")

# FINAL OUTPUT - Show result using f-string
print("\n--------------------------------------")
print(f"Your final score is {score}/3 🎉")

if score == 3:
    print("Excellent! You are a Genius! 🌟")
elif score == 2:
    print("Very Good! Keep it up! 👍")
elif score == 1:
    print("Good Try! Practice more! 💪")
else:
    print("Don't give up! Try again! ❤️")