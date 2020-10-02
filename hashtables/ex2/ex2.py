#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    flightPlan = {}
    route = []

    next = "NONE"

    #linking each source to each destination
    for ticket in tickets:
        flightPlan[ticket.source] = ticket.destination
    
    # print(flightPlan)
    while len(route) <= length:
        for flight in flightPlan:
            #This allows us to check if next value is
            #NONE, which means we've arrived at our destination
            if flightPlan[next] == "NONE":
                route.append(flightPlan[next])
                # print(route)
                return route
            #else, if it's not, we need to append the next flight
            #and set the next variable to be the next destination
            #that way with each loop we're wokring through each flight in order
            elif flight == next:
                route.append(flightPlan[next])
                next = flightPlan[flight]
                print(route)
    return route
