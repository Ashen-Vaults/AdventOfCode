import cProfile

def calculate_area_and_ribbons(file):
    total_surface = 0
    total_ribbons = 0
    with open(file) as f:
        for line in f:
            info = get_surface_area(line)
            total_surface += info[0]
            total_ribbons += info[1]

def get_surface_area(line):
    l, w, h = map(int, line.split('x'))     
    sides = []
    sides.append(l*w)
    sides.append(w*h)
    sides.append(h*l)
    smallest_side = min(int(x) for x in sides)
    surface_area = 2 * sides[0] + 2 * sides[1] + 2 * sides[2]
    return surface_area + smallest_side, get_ribbons(l,w,h)
   
def get_ribbons(l,w,h):
     dimensions = l * w * h
     ribbon = 2 * min(l+w, w+h, h+l)
     ribbon += dimensions 
     return ribbon  

def main():
    calculate_area_and_ribbons('instructions.txt')             
        
cProfile.run('main()')
