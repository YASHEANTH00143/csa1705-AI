import heapq

def manhattan_distance(state):
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    distance = 0
    for i in range(9):
        if state[i] != 0:
            distance += abs(i // 3 - goal_state.index(state[i]) // 3) + abs(i % 3 - goal_state.index(state[i]) % 3)
    return distance

def solve_8_puzzle(start_state):
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print("initial state :", start_state)
    open_list = [(manhattan_distance(start_state), start_state)]
    heapq.heapify(open_list)
    closed_set = set()
    
    while open_list:
        _, current_state = heapq.heappop(open_list)
        
        if current_state == goal_state:
            return current_state
        
        closed_set.add(tuple(current_state))
        
         zero_index = current_state.index(0)
        possible_moves = [1, -1, 3, -3]
        
        for move in possible_moves:
            new_index = zero_index + move
            
            if 0 <= new_index < 9:
                new_state = current_state[:]
                new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
                
                if tuple(new_state) not in closed_set:
                    heapq.heappush(open_list, (manhattan_distance(new_state), new_state))

    return None

start_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
solution = solve_8_puzzle(start_state)

if solution:
    print("Solution found:", solution)
else:
    print("No solution found.")
