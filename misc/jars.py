import math

THRESHOLD = 37

def jar_breaks(height: int, threshold=THRESHOLD):
    """returns true if a jar breaks, false otherwise"""
    return height >= threshold


def find_safe_rung(n_rungs: int):
    coef = 0
    height = coef * math.floor(math.sqrt(n_rungs))

    while height < n_rungs:
        print(coef, height)
        print(f"dropping jar from height: {height}")
        if jar_breaks(height):
            if height == 0:
                return height

            height = (coef - 1) * math.floor(math.sqrt(n_rungs))
            while not jar_breaks(height):
                if jar_breaks(height):
                    return height - 1
                height += 1 # may need to do i - 1
            return height
        
        coef += 1
        height = coef * math.floor(math.sqrt(n_rungs))
    
    return n_rungs

if __name__ == "__main__":
    print(find_safe_rung(256))



        
        
