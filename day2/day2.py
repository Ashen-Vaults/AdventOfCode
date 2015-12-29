global total_ribbons

def readFile(file,readbyLine):
    total_surface = 0
    total_ribbons = 0
    
    with open(file, 'r') as f:
        if readbyLine:
            for line in f:
                info = get_surface_area(line)
                total_surface += info[0]
                total_ribbons += info[1]
            print("\n***TOTALS***")
            print(total_surface)
            print(total_ribbons)
            
        else:
            first_line = f.readline();
            print(first_line)
            [x.strip() for x in first_line.__str__.split('x')]

          
def get_surface_area(line):
 
    l, w, h = map(int, line.split('x'))
            
    sides = []
    sides.append(l*w)
    sides.append(w*h)
    sides.append(h*l)

    smallest_side = min(int(x) for x in sides)
    surface_area = ( (2 * sides[0] ) + (2 * sides[1]) + (2 * sides[2]) )
    total = ((surface_area + smallest_side), get_ribbons(l,w,h))
    return total
   

def get_ribbons(l,w,h):
     dimensions = l * w * h
     ribbon = 2 * min(l+w, w+h, h+l)
     ribbon += dimensions 
     return ribbon           
        
readFile('instructions.txt', True)
