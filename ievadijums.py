def recepte(receptes_numurs):
    if receptes_numurs == "1":
        izmaksas = cukura_cena*aboli_kg*0.5 
    else:
        izmaksas = cukura_cena*aboli_kg
    return izmaksas
receptes_numurs=input("Īevadiet receptes numuru: \n1 )1kg ābolu = 500 gr.cukura\n2) 1 kg ābolu = 700 gr. cukura\n")
cukura_cena=float(input("Īevadi cukura cenu :"))
aboli_kg=float(input("Īevadi cukura skaits kilogramos :"))
rezultats=recepte(receptes_numurs)
print(f"par cukuru tu samaksāsi {rezultats}eiro")

