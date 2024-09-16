from print.print_vetor_aleatorio import printar_execucao_vetor_aleatorio
from print.print_vetor_reverso import printar_execucao_vetor_reverso
from print.print_vetor_ordenado import printar_execucao_vetor_ordenado
from print.print_vetor_quase_ordenado import printar_execucao_vetor_quase_ordenado

# Valores do Teste
inc = 1000
fim = 14000
stp = 1000

# Função que printa a execução dos algoritmos de ordenação com vetores aleatórios
printar_execucao_vetor_aleatorio(inc, fim, stp)

# Função que printa a execução dos algoritmos de ordenação com vetores ordenados
printar_execucao_vetor_ordenado(inc, fim, stp)

# Função que printa a execução dos algoritmos de ordenação com vetores quase ordenados
printar_execucao_vetor_quase_ordenado(inc, fim, stp)

# Função que printa a execução dos algoritmos de ordenação com vetores reversos
printar_execucao_vetor_reverso(inc, fim, stp)