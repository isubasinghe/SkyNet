from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2


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


def calculate(hub, locations):
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
                "coords": []
            }
            data["coords"].append(hub)
            for i in route[1:]:
                data["coords"].append(locations[i-1])
            return data
        else:
            return None
    else:
        return None

