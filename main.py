from SearchAlgorithm import *
from utils import *


if __name__ == '__main__':
    map_ = read_station_information('./Stations.txt')
    vector_ = read_information('./InfoVelocity.txt')
    connections_ = read_cost_table('./Time.txt')

    map_.add_connection(connections_)
    map_.add_velocity(vector_)

    path1 = Path(14)

    path1.add_route(13)
    g = map_.connections.get(14)[13]
    h = euclidean_dist(
        [map_.stations.get(14)['x'], map_.stations.get(14)['y']],
        [map_.stations.get(13)['x'], map_.stations.get(13)['y']]
    )
    path1.update_g(g)
    path1.update_h(h)
    path1.update_f()

    path1.add_route(8)
    g = map_.connections.get(13)[8]
    h = euclidean_dist(
        [map_.stations.get(13)['x'], map_.stations.get(13)['y']],
        [map_.stations.get(8)['x'], map_.stations.get(8)['y']]
    )
    path1.update_g(g)
    path1.update_h(h)
    path1.update_f()


    path1.add_route(12)
    g = map_.connections.get(8)[12]
    h = euclidean_dist(
        [map_.stations.get(8)['x'], map_.stations.get(8)['y']],
        [map_.stations.get(12)['x'], map_.stations.get(12)['y']]
    )
    path1.update_g(g)
    path1.update_h(h)
    path1.update_f()

    list_of_path = []

    # print(insert_depth_first_search(remove_cycles(expand(path1, map_)), list_of_path))
    #
    print(depth_first_search(4, 6, map_).route)
    # print(remove_cycles(expand(Path(2), map_)))
    # print(map_.connections.get(1))
    #print(depth_first_search(4, 7, map_))
    #print(insert_depth_first_search(Path(remove_cycles(expand(Path(4), map_))), [Path(4)]))


