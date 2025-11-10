def izracunaj_ukupan_napon(lista_napona):
    return



history : list [ tuple [str , float , float , str ]] = []
def ispisi_rezultate(ulaz: float, rezultat: float, jedinica: str) -> None:
    print(f"Rezultat: {ulaz} ->{rezultat: 3f} {}")

def unesi_broj(poruka: str, , min_value : float | None = None ) -> float :
    while True :
        try:
            vrijednost = float(input(poruka))
            if main_value is not None and vrijednost <
            print (f" Vrijednost mora biti >= { min_value }.")
            continue
        return vrijednost
    except Value Error:
        print("unos mora biti broj (npr, 12.5).pokusaj opet. ")







def prikaz_izbornika() -> None:
    print("\n=== ZBRAJANJE NAPONA===")
    print("1. Unesi novi napon(u V)")
    print("2. izračunaj UKUPNI napon i obriši")
    print("3. Pregledaj sve spremljene napone")
    print("0. Izlaz")

    odabir= input("unesite svoj odabir(1, 2, 3, ili 0): ").strip()
    
    if odabir == "0":
        print("hVALA NA KORIŠTENJU. DOVIĐENJA!")
        break

    if odabir not in {"1", "2", "3"}:
        print("GRešska nepoiznata opcija.")
        continue

    try:
        vrijednost = float(input("Unesite vrijednosti: ").strip())
    except ValueError:
        print("Greška: unos mora biti broj!")
    continue
        
            


    
