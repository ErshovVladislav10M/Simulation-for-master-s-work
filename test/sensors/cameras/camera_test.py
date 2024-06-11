from src.sensors.cameras.camera import Camera
from src.worlds.coodrinate import Coordinate
from src.worlds.vector import Vector


# def test():
#     identifier = 12
#     coordinate = Coordinate(0, 0, 0)
#     direction_vector = Vector.of(Coordinate(0, 0, 0))
#     distance = 100
#     sensor_data = {"initial_q": 0.2, "alpha": 1.5, "beta": 1.2}
#     cube_side = 10
#     obsolescence_time = 1
#
#     camera = Camera(
#         identifier=identifier,
#         coordinate=coordinate,
#         direction_vector=direction_vector,
#         distance=distance,
#         sensor_data=sensor_data,
#         cube_side=cube_side,
#         obsolescence_time=obsolescence_time
#     )
#
#     assert camera.identifier == identifier
#     assert camera.coordinate == coordinate
#     assert camera.direction_vector == direction_vector
#     assert camera.distance == distance
#     assert camera.cube_side == cube_side
#     assert camera._initial_q == sensor_data["initial_q"]
#     assert camera._obsolescence_time == obsolescence_time
