from utils import *


if __name__ == '__main__':
    map_ = read_station_information('./Stations.txt')
    vector_ = read_information('./InfoVelocity.txt')
    connections_ = read_cost_table('./Time.txt')

    map_.add_connection(connections_)
    map_.add_velocity(vector_)

    path1 = Path(1)
    path1.add_route(2)

    print(path1.route)
