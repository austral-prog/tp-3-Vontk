def slice_simple():
    texto = "Awesome"
    tres_iniciales = texto[:3].lower()
    print(tres_iniciales)
    CaracterNMedio_txt = len(texto) // 2
    medio_stingtxt = texto[CaracterNMedio_txt-1:CaracterNMedio_txt+2]
    print(medio_stingtxt)
    CaracterTot=len(texto)
    print(texto[:4].lower() +texto[CaracterTot-3:].lower())
