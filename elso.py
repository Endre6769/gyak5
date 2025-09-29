a = float(input("Adja meg az első oldal hosszát: "))
b = float(input("Adja meg a második oldal hosszát: "))
c = float(input("Adja meg a harmadik oldal hosszát: "))

if (a < b+c) and (b < a+c) and (c < a+b):
    print("\nA megadott szakaszok alkothatnak háromszöget.")
else: print("\nA megadott szakaszok nem alkothatnak háromszöget.")