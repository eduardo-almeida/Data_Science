# Um agente que apenas diz para a nave ficar parada ou fazer algo simples
def agent(observation, configuration):
    # 'observation' contém a posição das naves, energia, etc.
    # 'configuration' contém as regras do jogo (gravidade, mapa)
    
    # Por agora, vamos apenas retornar uma ação vazia ou básica
    return [0, 0, 0] # Exemplo de formato de ação (depende das regras do jogo)