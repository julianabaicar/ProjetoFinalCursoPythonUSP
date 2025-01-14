from assinatura import le_assinatura, le_textos
from comparador import compara_assinatura, calcula_assinatura, avalia_textos

def main():
    assinatura_infectado = le_assinatura()
    textos = le_textos()
    infectado = avalia_textos(textos, assinatura_infectado)
    print(f"O autor do texto {infectado} está infectado com COH-PIAH")

if __name__ == "__main__":
    main()
