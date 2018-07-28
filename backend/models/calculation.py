from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2
from haversine import haversine

import numpy as np

FUEL_PRICE = 1.51

def read_locations(hub, locations):
    locations.insert(0, hub)
    matrix = []
    for i in locations:
        matrix.append([])
        for j in locations:
            if (j[0]-i[0])+(j[1]-j[1]) < 0:
                matrix[-1].append(-((j[0]-i[0])+(j[1]-j[1])))
            else:
                matrix[-1].append((j[0]-i[0])+(j[1]-j[1]))
    return matrix


# Distance callback
def create_distance_callback(dist_matrix):
    # Create a callback to calculate distances between cities.

    def distance_callback(from_node, to_node):
        return int(dist_matrix[from_node][to_node])

    return distance_callback

def distance(coord0, coord1):
    return haversine(coord0, coord1)

def distance_all(coords):
    cost = 0.0
    for i in range(len(coords) - 1):
        cost += distance(coords[i], coords[i+1])
    cost += distance(coords[-2], coords[-1])
    return cost

def calculate(indv_user, hub, locations):
    # Cities
    id = 2
    user_names = [1]
    for i in range(len(locations)):
        user_names.append(id)
        id += 1
    # Distance matrix
    dist_matrix = read_locations(hub, locations)

    tsp_size = len(user_names)
    num_routes = 1
    depot = 0

    # Create routing model
    if tsp_size > 0:
        routing = pywrapcp.RoutingModel(tsp_size, num_routes, depot)
        search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
        # Create the distance callback.
        dist_callback = create_distance_callback(dist_matrix)
        routing.SetArcCostEvaluatorOfAllVehicles(dist_callback)
        # Solve the problem.
        assignment = routing.SolveWithParameters(search_parameters)
        if assignment:
            # Solution distance.
            #fuel price 150 cents
            
            
            # Display the solution.
            # Only one route here; otherwise iterate from 0 to routing.vehicles() - 1
            route_number = 0
            index = routing.Start(route_number) # Index of the variable for the starting node.
            route = []
            while not routing.IsEnd(index):
                # Convert variable indices to node indices in the displayed route.
                route.append(user_names[routing.IndexToNode(index)])
                index = assignment.Value(routing.NextVar(index))
            route.append(user_names[routing.IndexToNode(index)])
            #print(route)
            data = {
                "hub": hub,
                "coords": [],
                "cost": 0.0,
                "worthy": False,
                "time_minutes": 0.0
            }
            #distance_all([hub]+coords)


            
            #data["coords"].append(hub)
            for i in route[1:]:
                data["coords"].append(locations[i-1])
            data["coords"] = data["coords"][:-1]

            distance_miles = distance_all([hub] + data["coords"] + [hub])
            distance_km = distance_miles/1.6
            first_cost = distance_km/100*10*FUEL_PRICE
            second_cost = 20
            second_cost *= distance_km/50
            data["cost"] += first_cost
            data["cost"] += second_cost

            mykiRev = 4.30
            revenue = len(data["coords"])*mykiRev
            profit = revenue - data["cost"]
            if profit > 0.0:
                data["worthy"] = True
            i = 0
            for n, coord in enumerate(data["coords"]):
                if coord == indv_user:
                    i = n
                break

            distance_for_user_km = distance_all(data["coords"][i:-1] + [hub])/1.6
            time_for_user = distance_for_user_km/50
            print("Distance for user={0} miles, time={1}".format(distance_for_user_km, time_for_user))
            data["time_minutes"] = time_for_user*60
            print(profit)
            return data
        else:
            return None
    else:
        return None

