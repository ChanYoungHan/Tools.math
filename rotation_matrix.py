import numpy as np

class RoationMatrix():
    def __init__(self):
        pass

    def rot2D(self, theta):
        return np.array([np.cos(theta), -np.sin(theta), np.sin(theta), np.cos(theta)]).reshape((2,2))

    def rot3D(self, eluer_angle):
        pass
        

def main():
    print("test for rotmatirx")
    rot = RoationMatrix()
    theta = 30
    theta = np.deg2rad(theta)
    print(rot.rot2D(theta))
    
    
if __name__ is "__main__":
    main()
