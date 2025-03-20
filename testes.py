def validar_float(n):
    try:
        float(n.replace(",", "."))
        return n
    except:
        print('Valor inválido')

h = validar_float(input('Valor: '))

