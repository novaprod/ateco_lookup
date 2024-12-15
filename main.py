from ateco import get_sector_and_subcategory

def main():
    print("Benvenuto nel sistema di determinazione del settore ATECO.")
    print("Inserisci un codice ATECO (4-6 cifre) per determinare il settore e la sottocategoria corrispondente.")
    print("Digita 'exit' per uscire.\n")
    
    while True:
        ateco_code = input("Inserisci il codice ATECO: ").strip()
        if ateco_code.lower() == 'exit':
            print("Uscita dal programma. Arrivederci!")
            break
        
        settore, sottocategoria, errore = get_sector_and_subcategory(ateco_code)
        
        if errore:
            print(f"Errore: {errore}\n")
        else:
            print(f"Settore: {settore}")
            if sottocategoria:
                print(f"Sottocategoria: {sottocategoria}")
            else:
                print("Sottocategoria: Non disponibile")
            print()

if __name__ == "__main__":
    main()
