
def dlvalidate():
    dl=input("Enter DL\n")
    result =dl.startswith("DL")
    while not result:
        dl=input("Enter DL\n")
        result =dl.startswith("DL")
    print(dl)
        
        
dlvalidate()

def phvalidate():
    ph=input("Enter Phone Number : ")
    result =ph.isnumeric() and ph.length==10
    while not result:
        print("Note : Phone number must contain only numbers")
        ph=input("Enter Phone Number : ")
        result =ph.isnumeric()
    return ph
               
    



