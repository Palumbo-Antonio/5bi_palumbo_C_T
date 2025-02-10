#app.py
nomi = {
    0: "Corrazzini",
    1: "Tezza"
    }

telefoni = {
    0: "0000000000",
    1: "1111111111"
    }

n=0
while(n!=4):
    print("0--> Vedi contatti\n1--> Aggiungi contatto\n2--> Cancella contatto\n3--> Cerca contatto\n4--> STOP\n");
    n = int(input())
    match(n):
        case 0:
            for indice, nome in nomi.items():
                print(f"{indice} -> {nome}{telefoni[indice]}")
            print()
        case 1:
            print("nome")
            nome = input()
            print("telefono")
            telefono = input()
            lastKey = next(reversed(nomi))+1
            nomi[lastKey] = nome
            telefoni[lastKey] = telefono
        case 2:
            print("nome")
            nome = input()
            k = list(nomi.keys())[list(nomi.values()).index(nome)]
            nomi.pop(k, nome)
