import cadastro.lib.interface

def arquivoExiste(nome):
    try: # com esse comonado verifica se existe o arquivo
        a = open(nome, 'rt') #rt leitura arquivo texto
        a.close() # nesse comando fecha o arquivo
    except FileNotFoundError:
        return False
    else:
        return True
def criarArquivo(nome):
    try:# com esse comando cria o comando
        a = open(nome, 'wt+')# com esse parametro WT gravação de arquivo texto e o + cria se nao existe
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a= open(nome,'rt')#abrir arquivo
    except:
        print('Ouve um ERRO')
    else:
        cadastro.lib.interface.cabecalho('Pessoas Cadastradas ')
        print(a.read())#ler arquivos
    finally:
        a.close()
def cadastrar(arq,nome='Desconhecido',idade=0):
    try:
        a = open(arq, 'at')#abrir o arquivo e escrever nele
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome:.<22} \t{idade:>18}\n')#write escreve no arquivo
        except:
            print('Houve um erro na hora de adicionar um arquivo')
        else:
            print(f'Novo registro de {nome} cadastrado')
            a.close()