from time import  sleep
import lib.arquivos
import lib.interface

arq = 'Curso.txt'
if not lib.arquivos.arquivoExiste(arq):# esse comando se não existe o arquivo
    lib.arquivos.criarArquivo(arq) # esse comando cria o arquivo txt

while True:
    resposta = lib.interface.menu(['Ver pessoas','Cadastrar novas pessoas','sair do sistema'])
    if resposta == 1:
        #opção de listar a lista
        lib.arquivos.lerArquivo(arq)
    elif resposta == 2:
        lib.interface.cabecalho('Novo cadastro')
        nome = str(input('Nome:')).capitalize()
        idade =lib.interface.leiaInt('Idade:')
        lib.arquivos.cadastrar(arq,nome,idade)
    elif resposta ==3:
        lib.interface.cabecalho('FIM')
        break
    else:
        print(lib.interface.linha())
        lib.interface.cabecalho('\033[31mERRO digite uma opção valida\033[m')
        print(lib.interface.linha())
    sleep(2)