# Propósito
Este código simula numericamente a descida vertical de um paraquedas, considerando a ação da gravidade e da resistência aerodinâmica. O modelo utiliza integração temporal para calcular a evolução da aceleração, velocidade e posição ao longo do tempo.

Todas as grandezas estão expressas no sistema CGS (centímetros, gramas, segundos).

# O que a simulação faz

Calcula a força de arrasto em função da velocidade e do diâmetro do paraquedas.

Determina a força resultante (peso + arrasto).

Integra numericamente o movimento com um passo temporal pequeno (dt = 0,001 s).

Deteta o instante em que a velocidade terminal é atingida (força resultante aproximadamente nula).

Indica:

O instante e a altura a que é atingida a velocidade terminal.

O instante em que o sistema atinge o solo.

# Objetivo

O programa permite analisar o comportamento dinâmico da descida e verificar numericamente grandezas relevantes como a velocidade terminal e o tempo total de queda, a fim de validar os resultados dos cálculos analíticos.
