import heapq
import math
import timeit
import itertools

#romania map as given in AIMA
romania_map = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Pitesti': 101, 'Fagaras': 211, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

#function to calculate the straight line distance (heuristic) between two cities
def straight_line_distance_heuristic(city, goal_city):
    locations = {
        'Arad': (91, 492),
        'Bucharest': (400, 327),
        'Craiova': (253, 288),
        'Drobeta': (165, 299),
        'Eforie': (562, 375),
        'Fagaras': (305, 449),
        'Giurgiu': (375, 270),
        'Hirsova': (534, 350),
        'Iasi': (623, 510),
        'Lugoj': (111, 410),
        'Mehadia': (123, 363),
        'Neamt': (677, 547),
        'Oradea': (131, 571),
        'Pitesti': (320, 368),
        'Rimnicu Vilcea': (233, 410),
        'Sibiu': (207, 457),
        'Timisoara': (75, 410),
        'Urziceni': (456, 350),
        'Vaslui': (715, 455),
        'Zerind': (108, 531)
    }
    x1, y1 = locations[city]
    x2, y2 = locations[goal_city]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

#find path length
def path_length(path, road_map):
    length = 0
    for i in range(len(path) - 1):
        length += road_map[path[i]][path[i + 1]]
    return length   

#performs A* search on the romania map
def a_star_search(start_city, goal_city, heuristic_func, road_map):
    frontier = [(0, start_city)]
    explored = set()
    parent_map = {start_city: None}
    g_score = {start_city: 0}
    f_score = {start_city: heuristic_func(start_city, goal_city)}

    while frontier:
        current_f_score, current_city = heapq.heappop(frontier)
        if current_city == goal_city:
            path = [goal_city]
            while path[-1] != start_city:
                path.append(parent_map[path[-1]])
            path.reverse()
            return path

        explored.add(current_city)
        for neighbor in road_map[current_city]:
            distance = road_map[current_city][neighbor]
            if neighbor in explored:
                continue

            tentative_g_score = g_score[current_city] + distance
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                parent_map[neighbor] = current_city
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic_func(neighbor, goal_city)
                heapq.heappush(frontier, (f_score[neighbor], neighbor))

    return None

#performs B* search on the romania map
import heapq

def b_star_search(start_city, goal_city, heuristic_func, road_map):
    frontier = [(0, start_city)]
    explored = set()
    parent_map = {start_city: None}
    g_score = {start_city: 0}

    while frontier:
        current_f_score, current_city = heapq.heappop(frontier)
        if current_city == goal_city:
            path = [goal_city]
            while path[-1] != start_city:
                path.append(parent_map[path[-1]])
            path.reverse()
            return path

        explored.add(current_city)
        for neighbor in road_map[current_city]:
            distance = road_map[current_city][neighbor]
            if neighbor in explored:
                continue

            new_g_score = g_score[current_city] + distance
            if neighbor not in g_score or new_g_score < g_score[neighbor]:
                parent_map[neighbor] = current_city
                g_score[neighbor] = new_g_score
                f_score = new_g_score + heuristic_func(neighbor, goal_city) + heuristic_func(start_city, neighbor)
                heapq.heappush(frontier, (f_score, neighbor))

    return None


 
def run(start_city, goal_city):

    #test A* search
    a_star_path = a_star_search(start_city, goal_city, straight_line_distance_heuristic, romania_map)

    if a_star_search is None:
        print('No path found from {} to {}'.format(start_city, goal_city))
    path_len_a_star = path_length(a_star_path, romania_map)
    print('A* path from {} to {}: {}'.format(start_city, goal_city, a_star_path))
    print('A* path length: {}'.format(path_len_a_star))
    execution_time = timeit.timeit(lambda: a_star_search(start_city, goal_city, straight_line_distance_heuristic, romania_map), number=1)
    time_a_star = execution_time
    print('Execution time A* search: {}'.format(execution_time))

    #Test B* search
    b_star_path = b_star_search(start_city, goal_city, straight_line_distance_heuristic, romania_map)

    if b_star_search is None:
        print('No path found from {} to {}'.format(start_city, goal_city))
    path_len_b_star = path_length(b_star_path, romania_map)
    print('B* path from {} to {}: {}'.format(start_city, goal_city, b_star_path))
    print('B* path length: {}'.format(path_len_b_star))

    execution_time = timeit.timeit(lambda: b_star_search(start_city, goal_city, straight_line_distance_heuristic, romania_map), number=1)
    time_b_star = execution_time
    print('Execution time B* search: {}'.format(execution_time))

    times = 1 if time_b_star <= time_a_star else 0
    paths = 1 if path_len_b_star < path_len_a_star else 0

    return (paths, times)
    


if __name__ == '__main__':
    n  = 0
    times = 0
    paths = 0
    for start_city, goal_city in itertools.combinations(romania_map.keys(), 2):
        n += 1
        ret = run(start_city, goal_city)
        paths += ret[0]
        times += ret[1]

    print(f"Total runs: {n}")
    print(f"Times B* was faster or took equal amount of time: {times}")
    print(f"Times B* gave a shorter path: {paths}")
