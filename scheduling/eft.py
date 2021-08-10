from typing import List
from random import randint

RANGE = 4 # range of coverage for base stations
LENGTH = 20 # length of the road


def place_stations(H: List[int]):
    """H is a list of house locations on the axis
       S is the set of positions to ensure max coverage with minimal stations placed
    """
    S = set()
    L = sorted(H)

    for i, h in enumerate(L):
        S.add(h+4)
        j = i 
        
        # prevent IOOB
        if j+1 >= len(L):
            return sorted(list(S))

        while (j+1 < len(L)) and (L[j+1] - (h+4) <= RANGE):
            to_remove = L[j+1]
            while to_remove in L:
                L.remove(to_remove)
                
            j += 1

    return sorted(list(S))
            

def generate_H(n):
    """generates house n random positions on [0, LENGTH]"""
    return [randint(0, LENGTH) for i in range(n+1)]


if __name__ == "__main__":
    h = generate_H(10)
    print(sorted(h))
    disp_result(sorted(h), [])
    print(place_stations(h))