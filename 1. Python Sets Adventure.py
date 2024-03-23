# Objective:
# The aim of this assignment is to deepen your understanding and application 
# of Python sets in various scenarios, ranging from basic operations to advanced 
# manipulations and best practices. You will correct given codes, use sets 
# in everyday contexts, and tackle challenges that require creative thinking and problem-solving.

# Task 1: Flight Route Comparison
# Imagine you work for an airline and need to compare the flight routes of 
# your airline with a competitor. You have two sets of flight destinations, 
# one for each airline. Write a Python program to find out:

#     Destinations that both airlines fly to.
#     Destinations unique to your airline.
#     Whether there are any destinations that neither airline shares.

# Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}


#     Destinations that both airlines fly to.
shared_dests = our_routes & competitor_routes
print(shared_dests)
print(f"Destinations both airlines fly to = {shared_dests}")


#     Destinations unique to your airline.
unique_to_my = our_routes - competitor_routes
print(f"Destinations unique to my airline = {unique_to_my}")

#     Whether there are any destinations that neither airline shares.
unique_to_both = our_routes ^ competitor_routes
print(f"Destinations neither airline shares {unique_to_both}")