from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points
            
        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {} 
        
        # Add the node to the explored dictionary
        explored[node.state] = True
        
        frontier = StackFrontier()
        frontier.add(node)

        while True:
            if frontier.is_empty():
                return NoSolution(explored)
            node = frontier.remove()
            if node.state not in explored:
                explored[node.state] = True
            sucessors = grid.get_neighbours(node.state)
            for new_action, new_state in sucessors.items():
                if new_state not in explored:
                    new_node = Node("",state=new_state,cost=node.cost + grid.get_cost(new_state),parent=node,action=new_action)
                    if new_node.state == grid.end:
                        return Solution(new_node,explored)
                    frontier.add(new_node)



