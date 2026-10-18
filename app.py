from colorama import Fore, Style

print("=== SISTEMA DE MONITORAMENTO DE ÁGUA ===")

# Lista para armazenar as situações dos níveis do reservatório
mensagens_niveis = ["Nível 1: Muito baixo (crítico)", "Nível 2: Baixo", "Nível 3: Médio", "Nível 4: Alto", "Nível 5: Muito alto (alerta)"]

# Função responsável por definir a cor da mensagem conforme o nível informado
def exibir_situacao_atual(nivel_escolhido):
  print(f"\nSituação atual do reservatório:")

  # Ajusta o número do nível real para o índice da lista (começa em 0)
  indice = nivel_escolhido - 1
  texto = mensagens_niveis[indice]

  # Aplica a cor de acordo com o nível
  if indice == 0:
    print(Fore.RED + texto)
  elif indice == 1:
    print(Fore.YELLOW + texto)
  elif indice == 2:
    print(Fore.GREEN + texto)
  elif indice == 3:
    print(Fore.CYAN + texto)
  elif indice == 4:
    print(Fore.BLUE + texto)

  # 3. Restaura o estilo padrão do terminal após a exibição
  print(Style.RESET_ALL)


# Simulando com um valor definido no código (ex: Nível 3)
exibir_situacao_atual(3)

print("\nFim da simulação.")
