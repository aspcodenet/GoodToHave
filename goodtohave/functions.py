def getInputBetween(startval: int,endval: int)->int: 
    while True: 
        try: 
            val=int(input("Mata in:")) 
            if val >= startval and val <= endval: 
                return val 
            print(f"Ogiltigt val, mellan {startval} och {endval}, tack") 
        except: 
            print("Ange ett tal tack!")
    


if __name__ == "__main__":
    print("Testing")
    s = getInputBetween(0, 15)
    print(x)