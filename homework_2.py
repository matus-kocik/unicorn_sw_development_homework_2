try:
    original_cislo = int(input("Zadej přirozené číslo pro převod do dvojkové soustavy: "))
    if original_cislo < 0:
        print("Chyba: Tento algoritmus pracuje pouze s přirozenými čísly a nulou.")
    else:
        binary = ""  # Inicializujeme prázdný řetězec pro binární zápis.
        cislo = original_cislo
        if cislo == 0:
            binary = "0"  # Pokud je vstupní číslo 0, vrátíme "0" jako výsledek.
        else:
            while cislo > 0:
                if cislo % 2 == 0:
                    binary = "0" + binary
                else:
                    binary = "1" + binary
                cislo //= 2

        print(f"Dvojkový zápis čísla {original_cislo} je: {binary}")
except ValueError:
    print("Chyba: Zadali jste neplatný vstup. Zadejte prosím přirozené číslo a nulu.")

