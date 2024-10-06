from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

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

        # f (problema.test-objetivo(n₀.estado)) then return solución(n₀)
        if node.state == grid.end:
            return Solution(node, explored)
        

        frontier = QueueFrontier()
        #VER LA POSICION DE ESTO
        frontier.add(node)

        while True:
            if frontier.is_empty():
                return NoSolution(explored)
            
            node = frontier.remove()

            sucessor = grid.get_neighbours(node.state)
            for new_action, new_state in sucessor.items():
                if new_state not in explored:
                    new_node = Node("",state=new_state,parent= node,action=new_action,cost=node.cost + grid.get_cost(new_state))

                    if new_node.state == grid.end:
                        return Solution(new_node,explored)
                    explored[new_state] = True
                    frontier.add(new_node)


        #return NoSolution(explored)


#1° agrega nodo a la frontera
#2°Ve si es estado objetivo(si no es lo quita de la frontera)
#3° Ejecuta acciones disponibles

    