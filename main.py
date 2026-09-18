from funcionario import cadastra_funcionario, listar_funcionarios, excluir_funcionario
from escala import cadastrar_escalas, listar_escala, excluir_escala

sair_do_sistema = False

def apresenta_menu():
    print("===================================================")
    print("       SISTEMA DE GESTÃO DE ESCALA     ")
    print("===================================================")
    print("")
    print("   1. Cadastra Funcionários 🤓")
    print("   2. Listar Funcionários 📝" )
    print("   3. Excluir Funcionário 🗑️​")
    print("   4. Cadastrar Escala 📆​")
    print("   5. Listar Escala 📝​")
    print("   6. Excluir Escala 📝​")
    print("   0. Sair ➡️")
    print("")
    opcao_menu = input("Escolha uma opção: ")
    #rint("\n" * 30, end="")
    return opcao_menu

    
def sair(): 
    print("Saindo do Sistema de Gestão de Escala ҉")

#=============================================================#

while not sair_do_sistema: 
    opcao_menu = apresenta_menu()

    match opcao_menu:
            case "1":
                cadastra_funcionario()
            case "2":
                listar_funcionarios()
            case "3":
                excluir_funcionario()
            case "4":
                cadastrar_escalas()
            case "5":
                listar_escala()
            case "6":
                excluir_escala()
            case "0":
                sair()
                break
            case _:  
                print("Opção Inválida!") 
