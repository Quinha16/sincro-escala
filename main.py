
funcionarios = []
sair_do_sistema = False

def apresenta_menu():
    print("===================================================")
    print("       SISTEMA DE GESTÃO DE ESCALA     ")
    print("===================================================")
    print("")
    print("   1. Cadastra Funcionários 🤓")
    print("   2. Listar Funcionários 📝" )
    print("   0. Sair ➡️")
    print("")
    opcao_menu = input("Escolha uma opção: ")
    return opcao_menu


def cadastra_funcionario(): 
    funcionário = input("Digite o nome do funcionário: ")
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
    print("Listando funcionários")
    
def sair(): 
    sair_do_sistema = True
    print("Saindo do Sistema de Gestão de Escala ҉")

    
    
    
#=============================================================#

while not sair_do_sistema: 
    opcao_menu = apresenta_menu()

    match opcao_menu:
            case "1":
                cadastra_funcionario()
            case "2":
                listar_funcionarios()
            case "0":
                sair()
            case _:  
                print("Opção Inválida!") 
