runde = 0
print("Hallo!")
player1name = input("Was ist der Name von Spieler 1? ")
player2name = input("Und der von Spieler 2? ")
player3name = input("Wie nennt sich Spieler 3? ")
player4name = input("und wie heißt Spieler 4? ")
def main(rundenanzahl):
    rundenanzahl = rundenanzahl + 1
    print("Runde",rundenanzahl)
    def punktefrage(name):
        print("Wie viele Punkte hat",name,"denn gemacht?")
    punktefrage(player1name)
    player1points = input("")
    punktefrage(player2name)
    player2points = input("")
    punktefrage(player3name)
    player3points = input("")
    punktefrage(player4name)
    player4points = input("")
    player1points = float(player1points)
    player2points = float(player2points)
    player3points = float(player3points)
    player4points = float(player4points)
    def punkteberechnung(name,punkte1,punkte2,punkte3,punkte4):
        punkte12 = punkte1 - punkte2
        punkte13 = punkte1 - punkte3
        punkte14 = punkte1 - punkte4
        finalePunkte = punkte12 + punkte13 + punkte14
        print(name,"macht",finalePunkte,"punkte")
    punkteberechnung(player1name,player1points,player2points,player3points,player4points)
    punkteberechnung(player2name,player2points,player3points,player4points,player1points)
    punkteberechnung(player3name,player3points,player4points,player1points,player2points)
    punkteberechnung(player4name,player4points,player1points,player2points,player3points)
    main(rundenanzahl)
main(runde)
