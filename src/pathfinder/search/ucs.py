from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)
        
        frontier = QueueFrontier()
        frontier.add(node)

        explored = {}
        explored[node.state]=node.cost

        while True:
            if frontier.is_empty():
                return NoSolution(explored)
            node = frontier.remove()
            if node.state == grid.end:
                return Solution(node,explored)
            
            sucessors = grid.get_neighbours(node.state)
            for new_action, new_state in sucessors.items():

                costo = node.cost + grid.get_cost(new_state)

                if (new_state not in explored) or (costo < explored[new_state]):
                    new_node = Node("",state = new_state, cost=costo,parent=node,action=new_action)
                
                    explored[new_state] = costo
                    frontier.add(new_node)