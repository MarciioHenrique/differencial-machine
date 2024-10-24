import numpy as np
np.set_printoptions(legacy='1.25')

def babbage(axis_y):
    if len(axis_y) == 1:
        return []
   
    # Calcula a diferença de nível atual
    differences = [axis_y[i + 1] - axis_y[i] for i in range(len(axis_y) - 1)]
   
    # Chamada recursiva para o próximo nível
    table = babbage(differences)
   
    # Adiciona a linha de diferenças calculadas na table
    return [axis_y] + table

def calculate_next_value(differences_table, level=1, sum=0):
    if level >= len(differences_table):
        return sum
   
    # Soma o último valor da linha atual de diferenças
    last_level_value = differences_table[level][-1]
    sum += last_level_value
   
    # Chamada recursiva para o próximo nível
    return calculate_next_value(differences_table, level + 1, sum)

def main():
  try:
    coefficients_input = input("Digite os coeficientes separados por espaço: ")
    coefficients = list(map(float, coefficients_input.split()))
    if not coefficients:
      raise ValueError("A lista de coeficientes não pode estar vazia.")
     
    first_value = float(input("Digite o valor inicial do intervalo: "))
    last_value = float(input("Digite o valor final do intervalo: "))
    interval = float(input("Digite o valor do intervalo para a iteracao (maior que 0): "))
    if interval == 0 or interval > last_value - first_value:
      raise ValueError("O valor de iteração tem que estar entre o intervalo de inicio e fim e não pode ser zero .")

    specified_x = float(input(f"Digite um valor específico para x que seja maior que {first_value}: "))
  except ValueError as e:
    print(f"Erro de entrada: {e}")
    exit(1)

  axys_x = np.arange(first_value, last_value, interval)
  axys_y = np.polyval(coefficients, axys_x)

  differences_table = babbage(axys_y)

  next_value = axys_y[-1] + calculate_next_value(differences_table)

  print("Valores de eixo_x:", axys_x)
  print("Valores de eixo_y:", axys_y)
  print("Tabela de diferenças:")
  for index, line in enumerate(differences_table):
      print(f"Nível {index}: {line}")

  print(f"Próximo valor estimado para x={axys_x[-1] + interval}: {next_value}")

  specified_value = np.polyval(coefficients, specified_x)
  print(f"Valor estimado para x={specified_x}: {specified_value}")


main()
