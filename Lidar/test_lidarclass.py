from PyLidar_class import Lidar

lidar = Lidar(port="/dev/tty.usbserial-0001")
if lidar.connect(): 
    lidar.start_scanning(scan_time=5, eps=90, min_samples=4)
    num_clusters = lidar.get_num_clusters()
    x_clusters = lidar.get_x_clusters()
    y_clusters = lidar.get_y_clusters()
    num_points = lidar.get_num_points()
    print(f"Number of clusters: {num_clusters}")
    print(f"Number of points in each cluster: {num_points}")
    lidar.plot_clusters()
    lidar.stop_scanning()