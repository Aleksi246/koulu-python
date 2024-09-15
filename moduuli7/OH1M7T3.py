
lentokentat = dict()
while True:

    tehtava = input("syötä 1 jos haluat syöttää dataa \n syötä 2 jos haluat hakea dataa \n syötä 3 jos haluat lopettaa ohjelman \n: ")

    if tehtava == "3":
        break
    if tehtava == "2":
        icao_koodi = input("anna ICAO: ")
        if icao_koodi in lentokentat:
            print({lentokentat[icao_koodi]})
        else:
            print("ICAO ei lötynyt")
    if tehtava == "1":

        lisattavanimi = input("anna lentokentän nimi: ")
        lisattavaicao = input("anna lentokentän ICAO: ")
        lentokentat[lisattavaicao] = lisattavanimi
