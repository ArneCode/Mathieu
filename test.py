def main():
    print("Hallo!")
    p1 = input("Spieler 1: ")
    p2 = input("Spieler 2: ")
    p3 = input("Spieler 3: ")
    p4 = input("Spieler 4: ")
    p1 = float(p1)
    p2 = float(p2)
    p3 = float(p3)
    p4 = float(p4)
    if (p1>p2 and p1>p3 and p1>p4):
        p1p2 = p1-p2
        p1p3 = p1-p3
        p1p4 = p1-p4
        finalp1 = p1p2 + p1p3 + p1p4
        print("Spieler 1 macht ",finalp1,"Punkte!")
        if (p2>p3 and p2>p4):
            p2p3 = p2-p3
            p2p4 = p2-p4
            finalp2 = p2p3 + p2p4 - p1p2
            print("Spieler 2 macht ",finalp2,"Punkte!")
            if (p3>p4):
                p3p4 = p3-p4
                finalp3 = p3p4 - p2p3 - p1p3
                print("Spieler 3 macht ",finalp3,"Punkte!")
                finalp4 = - p1p4 - p2p4 - p3p4
                print("Spieler 4 macht ",finalp4,"Punkte!")
main()
