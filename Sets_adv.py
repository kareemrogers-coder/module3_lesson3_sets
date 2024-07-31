#Question 1


# Objective:
# The aim of this assignment is to deepen your understanding and application of Python sets in various scenarios, ranging from basic operations to advanced manipulations and best practices. You will correct given codes, use sets in everyday contexts, and tackle challenges that require creative thinking and problem-solving.

# Task 1: Flight Route Comparison
# Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:


# 1 Destinations that both airlines fly to.
# 2 Destinations unique to your airline.
# 3 Whether there are any destinations that neither airline shares.

from helper import p

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
p() 
print("Below are the orignal routes: ")
print(f"Our Routes: {our_routes}")
print(f"Competitor Routes: {competitor_routes}")

p()  
print("#1 Destinations that both airlines fly to.")


sim_route = our_routes.intersection(competitor_routes)
print(sim_route)

p() 
print("# 2 Destinations unique to your airline.")

unq_route = our_routes.difference(competitor_routes)
print(unq_route)

p() 
print("3 Whether there are any destinations that neither airline shares.")

null_route = our_routes.symmetric_difference(competitor_routes)
print(null_route)

