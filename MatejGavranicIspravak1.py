def main():
    while True:      
        print("\n--- Kalkulator za Pretvorbu Digitalnih Veličina ---")
        print("1. Kilobajti (KB) u Bajte(B) (1 KB = 1024 B)")
        print("2. Megabajti (MB) u Kilobajte (KB) (1 MB = 1024 KB)")
        print("3. Gigabajti (GB) u Megabajte (MB) (1 GB = 1024 MB)")
        print("0. Izlaz")

       
        izbor = input("Odaberite opciju (0-3): ")

       
        if izbor == '0':
            print("Hvala što ste koristili kalkulator! Doviđenja!")
            break

       
        elif izbor == '1':
            kb = float(input("Unesite broj kilobajta (KB): "))
            b = kb * 1024
            print(f"{kb} KB = {b} B")

        
        elif izbor == '2':
            mb = float(input("Unesite broj megabajta (MB): "))
            kb = mb * 1024
            print(f"{mb} MB = {kb} KB")

        
        elif izbor == '3':
            gb = float(input("Unesite broj gigabajta (GB): "))
            mb = gb * 1024
            print(f"{gb} GB = {mb} MB")

        
        else:
            print("Pogrešan unos! Pokušajte ponovo.")



if __name__ == "__main__":
      main()
      Objašnjenje:tovar
  
