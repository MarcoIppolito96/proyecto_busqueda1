from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

def h(node, objetivo):
    x_obj, y_obj = objetivo
    x_actual, y_actual = node.state
    return abs(x_actual - x_obj) + abs(y_actual - y_obj)

class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize frontirer
        frontier = PriorityQueueFrontier()
        frontier.add(node,h(node,grid.end))
        
        # Initialize the explored dictionary
        explored = {} 
        explored[node.state] = node.cost
        
        while True:
            if frontier.is_empty():
                return NoSolution(explored)
            
            node = frontier.pop()
            
            if node.state == grid.end:
                return Solution(node,explored)
            
            sucessors = grid.get_neighbours(node.state)

            for new_action, new_state in sucessors.items():
                new_cost = node.cost + grid.get_cost(new_state)

                if new_state not in explored or new_cost < explored[new_state]:
                    new_node = Node("",state= new_state, cost=new_cost, parent=node, action=new_action)
                    explored[new_node.state] = new_cost
                    frontier.add(new_node,h(new_node, grid.end))

"""
def euclidean_distance(city1, city2):
    return sqrt((city1.x - city2.x)² + (city1.y - city2.y)²)
"""