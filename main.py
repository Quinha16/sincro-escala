
def apresenta_menu():
    print("=========================================")
    print("       SISTEMA DE GESTÃO DE ESCALA     ")
    print("=========================================")
    print("")
    print("   1. Cadastra Funcionários 🤓")
    print("   2. Listar Funcionários 📝" )
    print("   0. Sair ➡️")
    print("")
    opcao_menu = input("Escolha uma opção: ")
    return opcao_menu


def cadastra_funcionario(): 
    funcionários = input("Digite o nome do funcionário: ")
    print(f"O nome cadastrado foi: {funcionários}")
    
def listar_funcionarios(): 
    print("Listando funcionários")
    
def sair(): 
    print("Saindo do Sistema de Gestão de Escala ҉")
    
#=============================================================#

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
