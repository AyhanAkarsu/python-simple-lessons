import sys
def kokbulma(a,b,c):
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Reel kök yok.")
    elif delta == 0:
        print("Tek kök var.")
        x1 = (-b)/(2*a)
        x2 = x1
        return (x1,x2)
    else:
        print("İki gerçek kökü vardır.")
        x1 = (-b - delta**0.5)/(2*a)
        x2 = (-b + delta**0.5)/(2*a)
        return (x1,x2)

if len(sys.argv) == 4:
    print("Kök bulma: ",kokbulma(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
else:
    sys.stderr.write("Denkelemi dogru sekilde doldurun")
    sys.stderr.flush()




