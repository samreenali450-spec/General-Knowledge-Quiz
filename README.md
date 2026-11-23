# General Knowledge Quiz - Python Programming Project 4

## 📋 Project Overview
This is Project 4 of the Python Programming Industrial Training Kit (Batch: 2026) powered by DecodeLabs.

The goal of this project is to move from static scripts to dynamic decision engines. This project focuses on Control Flow, State Management, and Input Sanitization.

## 🎯 Project Task
Create a game that asks 3 General Knowledge questions.
Example: "What is the capital of France?"

- Keep a score counter: +1 point for every correct answer.
- Show the final score at the end.

## ✨ Features
- Asks 3 General Knowledge questions to the user
- Takes input using `input()`
- Sanitizes input with `.strip().lower()` to prevent case-sensitivity and space errors
- Uses `if / else` to check answers and route execution
- Maintains state with a `score` variable
- Shows instant feedback after each question
- Displays final score using f-string formatting
- Shows a motivational message based on the final score

## 🧠 Core Concepts Used
- **Control Flow:** `if / else` for decision making
- **Input Sanitization:** `.strip()` and `.lower()`
- **State Management:** `score = score + 1`
- **Comparison Operators:** `==`, `or`
- **IPOS Architecture:** Input -> Process -> Storage -> Output
- **F-Strings:** Dynamic output with `f"Your score is {score}"`

## 🛠️ Technologies Used
- Python 3

## 🚀 How to Run
1. Clone this repository:
```bash
git clone https://github.com/samreenali450-spec/General-Knowledge-Quiz
