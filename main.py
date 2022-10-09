def main():
    paises = input('Ingresa una lista de paises separados por comas: \n').replace(' ', '')
    paises = paises.split(',')
    paises = set(paises)
    paises = sorted(paises)
    print('Los paises ingresados son', ', '.join(paises))

if __name__ == '__main__':
    main()