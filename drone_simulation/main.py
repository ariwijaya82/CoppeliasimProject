# Nama: I Made Pande Ari Wijaya
# NRP: 07111740000020

# program task:
# program ini bertujuan menggerakan drone untuk mencari suatu benda
# dengan melakukan pencarian ke setiap titik pada arena
# ketika benda ditemukan, drone akan mendarat pada benda tersebut

from quadricopter import Quadricopter
from scene_map import SceneMap


if __name__ == "__main__":
    sMap = SceneMap(-10, 0, -10, 0, 0.5, 3)
    quadricopter = Quadricopter(23)
    if quadricopter._clientID != -1:
        print("Serve Connect!")
        quadricopter.startPosition(0.1, sMap)
        while not isinstance(quadricopter._objFound, bool):
            quadricopter.searchObj(sMap)
        while quadricopter._objFound:
            if quadricopter.land(sMap):
                print(quadricopter.msg)
                break
            else:
                quadricopter.searchObj(sMap)
                print(quadricopter.msg)
        else:
            print(quadricopter.msg)
    else:
        print("Serve offline!")
