from time import time
import HVLCS

def main():
    t1 = time()
    HVLCS.solve()
    t2 = time()
    print(t2 - t1)

if __name__=="__main__":
    main()
