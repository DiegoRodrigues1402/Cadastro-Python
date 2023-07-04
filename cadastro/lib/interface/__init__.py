def leiaInt(msg):
    while True:
       try:
           res = int(input(msg))
       except (ValueError,TypeError):
           print('\033[31mPor favor digite um numero inteiro valido\033[m ')
       except KeyboardInterrupt:
           print('\033[31m\nEntrada de dados interompida pelo usuario\033[m ')

       else:
           return res
           break

def linha(tam = 42):
    return '='* tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
def menu(lista):
    cabecalho('Menu principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c}--\033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção\033[m ')
    return opc