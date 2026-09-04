from pathlib import Path

path_bd = Path("sincro-escala/BD") / "escalas_bd.txt"
escalas = []

def cadastrar_escalas(): 
    escala = input("Digite o nome da Escala: ")
    with open(path_bd,"a", encoding="utf-8") as arquivo:
        arquivo.write(f"{escalas}\n")
    escalas.append(escala)
    print(f"O nome cadastrado foi: {escala}")
    print("===================================================")
    print("Você gostaria de adicionar uma nova Escala?")
    print(" 1. Sim ✅​")
    print(" 2. Não ❌​")
    seguir_cadastro = input("Escolha uma opção: ")
    print("===================================================")
    if seguir_cadastro == "1":
        cadastra_escalas()
    if seguir_cadastro == "2":
        print("Cadastro concluído!​✅​")
        