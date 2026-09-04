from pathlib import Path

path_bd = Path("sincro-escala/BD") / "funcionario_bd.txt"
funcionarios = []

def cadastra_funcionario(): 
    funcionário = input("Digite o nome do funcionário: ")
    with open(path_bd,"a", encoding="utf-8") as arquivo:
        arquivo.write(f"{funcionário}\n")
    funcionarios.append(funcionário)
    print(f"O nome cadastrado foi: {funcionário}")
    print("===================================================")
    print("Você gostaria de adicionar um novo funcionário?")
    print(" 1. Sim ✅​")
    print(" 2. Não ❌​")
    seguir_cadastro = input("Escolha uma opção: ")
    print("===================================================")
    if seguir_cadastro == "1":
        cadastra_funcionario()
    if seguir_cadastro == "2":
        print("Cadastro concluído!​✅​")


def listar_funcionarios():
    with open(path_bd,"r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            print(linha.strip())
            
def excluir_funcionario():
    listar_funcionarios()
    funcionario = input("Qual Funcionário você deseja deletar?: ")
    with open(path_bd,"r", encoding="utf-8") as arquivo:
        nomes = arquivo.readlines()
       
    with open(path_bd,"w", encoding="utf-8") as arquivo:
        for linha in nomes:
            if linha.strip() == funcionario:
                linha = "" 

            arquivo.write(linha) 