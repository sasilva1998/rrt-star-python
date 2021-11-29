import pygame
from rrt_base import RRTGraph, RRTMap
import time


def main():
    dimensions = (600, 1000)
    start = (50, 50)
    goal = (510, 510)
    obs_dim = 50
    obs_num = 50

    iteration = 0
    t1 = time.time()

    pygame.init()
    map = RRTMap(start, goal, dimensions, obs_dim, obs_num)
    graph = RRTGraph(start, goal, dimensions, obs_dim, obs_num)

    obstacles = graph.make_obs()

    while not graph.path_to_goal():

        map.map.fill((map.white_color))

        elapsed = time.time() - t1
        t1 = time.time()
        if elapsed > 10:
            raise

        map.draw_map(obstacles)

        if iteration % 10 == 0:
            graph.bias(goal)

        else:
            graph.expand()

        X, Y, PARENT = graph.optimize_edges()

        for i in range(0, len(X)):
            pygame.draw.circle(
                map.map, map.grey_color, (X[i], Y[i]), map.node_rad + 2, 0
            )
            pygame.draw.line(
                map.map,
                map.blue_color,
                (X[i], Y[i]),
                (X[PARENT[i]], Y[PARENT[i]]),
                map.edge_thickness,
            )

        pygame.display.update()
        iteration += 1
        # time.sleep(1)
    map.draw_path(graph.get_path_coords())
    pygame.display.update()
    pygame.event.clear()
    pygame.event.wait(0)


if __name__ == "__main__":
    result = False
    while not result:
        try:
            main()
            result = True
        except:
            result = False
