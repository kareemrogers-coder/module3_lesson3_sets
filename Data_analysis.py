#### Questions 2

# Objective: The aim of this assignment is to enhance your skills in using Python sets for data analysis tasks. You will apply various set operations to handle real-world data scenarios, focusing on their practical application and efficiency.


# Task 1: Duplicate Entries Cleanup You are given a list of customer IDs, some of which are duplicated. Write a Python function to remove duplicates and display the unique customer IDs.


# Example Code:
from helper import p

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

p()
print(f"Orginal Customer Id: {customer_ids}")

p()
#print(type(customer_ids)) # identify the data type

print(f" The following are the Customer IDs with no Duplicates: {set(customer_ids)}") # convert the data type into a set


