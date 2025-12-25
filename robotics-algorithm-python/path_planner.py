import heapq
import matplotlib.pyplot as plt

class PathPlanner:
    def __init__(self, grid_size, obstacles):
        self.rows, self.cols = grid_size
        self.obstacles = obstacles # List of (x, y) tuples

    def heuristic(self, a, b):
        # Manhattan distance for grid
        return abs(b[0] - a[0]) + abs(b[1] - a[1])

    def get_neighbors(self, node):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Right, Left, Down, Up
        result = []
        for d in directions:
            neighbor = (node[0] + d[0], node[1] + d[1])
            # Check bounds and obstacles
            if (0 <= neighbor[0] < self.rows and 
                0 <= neighbor[1] < self.cols and 
                neighbor not in self.obstacles):
                result.append(neighbor)
        return result

    def a_star_search(self, start, goal):
        frontier = []
        heapq.heappush(frontier, (0, start))
        came_from = {start: None}
        cost_so_far = {start: 0}

        while frontier:
            current = heapq.heappop(frontier)[1]

            if current == goal:
                break

            for next_node in self.get_neighbors(current):
                new_cost = cost_so_far[current] + 1
                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + self.heuristic(goal, next_node)
                    heapq.heappush(frontier, (priority, next_node))
                    came_from[next_node] = current
        
        return came_from, cost_so_far

    def reconstruct_path(self, came_from, start, goal):
        if goal not in came_from:
            return []
        current = goal
        path = []
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        return path[::-1] # Reverse

    def visualize(self, path, start, goal):
        # Create grid
        grid = [['.' for _ in range(self.cols)] for _ in range(self.rows)]
        
        # Mark obstacles
        for obs in self.obstacles:
            grid[obs[0]][obs[1]] = '#'
            
        # Mark path
        for p in path:
            grid[p[0]][p[1]] = '*'
            
        # Mark start/goal
        grid[start[0]][start[1]] = 'S'
        grid[goal[0]][goal[1]] = 'G'

        # Print to console
        print("\n--- A* Robotics Path Planning ---")
        for row in grid:
            print(" ".join(row))

# --- Main Execution ---
if __name__ == "__main__":
    # Define a 10x10 Grid
    grid_size = (10, 10)
    
    # Create some "Walls" (Obstacles)
    obstacles = [(3, i) for i in range(7)] + [(7, i) for i in range(3, 10)]
    
    planner = PathPlanner(grid_size, obstacles)
    start_pos = (0, 0)
    goal_pos = (9, 9)

    came_from, cost = planner.a_star_search(start_pos, goal_pos)
    path = planner.reconstruct_path(came_from, start_pos, goal_pos)

    if path:
        print(f"Path found! Length: {len(path)} steps.")
        planner.visualize(path, start_pos, goal_pos)
    else:
        print("No path found.")