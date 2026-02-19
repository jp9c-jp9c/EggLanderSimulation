# Objetivo

Este código simula numericamente a descida vertical de um paraquedas, considerando a ação da gravidade e da resistência aerodinâmica. O modelo utiliza integração temporal para calcular a evolução da aceleração, velocidade e posição ao longo do tempo.

Todas as grandezas estão expressas no sistema CGS (centímetros, gramas e segundos).

# Funcionalidades

Cálculo da força de arrasto aerodinâmico em função da velocidade e da área do paraquedas.

Determinação da força resultante (peso e arrasto).

Integração numérica do movimento com passo temporal constante (dt = 0,001 s).

Deteção do instante em que a velocidade terminal é atingida (força resultante aproximadamente nula).

Determinação do instante em que o sistema atinge o solo.
