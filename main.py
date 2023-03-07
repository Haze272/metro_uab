from utils import *


if __name__ == '__main__':
    map_ = read_station_information('./Stations.txt')
    vector_ = read_information('./InfoVelocity.txt')
    connections_ = read_cost_table('./Time.txt')

    map_.add_connection(connections_)
    map_.add_velocity(vector_)

    path1 = Path(1)
    path1.add_route(2)

    g = map_.connections.get(1)[2]*10
    h = euclidean_dist(
        [map_.stations.get(1)['x'], map_.stations.get(1)['y']],
        [map_.stations.get(2)['x'], map_.stations.get(2)['y']]
    )

    path1.update_g(g)
    path1.update_h(h)
    path1.update_f()

    print(map_.connections.get(1)[2]*10)
    print(euclidean_dist(
        [map_.stations.get(1)['x'], map_.stations.get(1)['y']],
        [map_.stations.get(2)['x'], map_.stations.get(2)['y']]
    ))

    print(path1.route)
