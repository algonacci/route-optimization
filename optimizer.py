import numpy as np

from schema import Coordinate
from mealpy import TLO, Problem, PermutationVar


class RouteOptimizeProblem(Problem):
    def __init__(self, bounds=None, minmax="min", data=None, **kwargs):
        self.data = data
        super().__init__(bounds, minmax, **kwargs)

    @staticmethod
    def euclidean_distance(depot: Coordinate, destination: Coordinate):
        return np.linalg.norm(
            np.array([depot.latitude, depot.longitude])
            - np.array([destination.latitude, destination.longitude])
        )

    @staticmethod
    def calculate_total_distance(route: list, coordinates: list[Coordinate]):
        # Calculate total distance of a route
        total_distance = 0
        prev = coordinates[0]

        for idx in route:
            next = coordinates[idx]
            # total_distance += RouteOptimizeProblem.haversine(prev, next)
            total_distance += RouteOptimizeProblem.euclidean_distance(prev, next)
            prev = next

        return total_distance

    def obj_func(self, x):
        x_decoded = self.decode_solution(x)
        route = x_decoded["per_var"]
        fitness = self.calculate_total_distance(route, self.data["coordinates"])
        return fitness


def optimize_route(coordinates: list[Coordinate]) -> np.ndarray:
    bounds = PermutationVar(valid_set=list(range(0, len(coordinates))), name="per_var")
    problem = RouteOptimizeProblem(
        bounds=bounds, minmax="min", data={"coordinates": coordinates}
    )

    model = TLO.ImprovedTLO(epoch=50, pop_size=150, n_teachers=8)
    g_best = model.solve(problem, mode="thread", n_workers=8)

    return g_best.solution
