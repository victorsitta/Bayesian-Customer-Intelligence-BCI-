# ==============================================================================
# MODELO PROBABILÍSTICO: REDE BAYESIANA DE PREVISÃO DE COMPRAS
# ==============================================================================
# Este script simula uma Rede Bayesiana simples usando Tabela de Probabilidade
# Condicional (CPT). O objetivo é prever a chance de um cliente comprar com base
# em três evidências de comportamento no e-commerce.
# ==============================================================================

# ------------------------------------------------------------------------------
# PASSO 1: Mapeamento de Probabilidades (Rede Bayesiana)
# ------------------------------------------------------------------------------
# Convenção de valores para as evidências (variáveis binárias):
# 0 = Falso / Não / Baixo
# 1 = Verdadeiro / Sim / Alto

probabilidades = {
    # Probabilidades a priori (probabilidade simples de cada evento isolado)
    "HistoricoCompras": {0: 0.7, 1: 0.3},  # 70% novos visitantes, 30% recorrentes
    "TempoNoSite": {0: 0.6, 1: 0.4},       # 60% navegam pouco, 40% navegam muito
    "ClicouEmPromocao": {0: 0.8, 1: 0.2},  # 80% não clicam em banner, 20% clicam
    
    # Probabilidade Condicional: P(Compra | Historico, Tempo, Promocao)
    # A chave é uma tupla no formato: (HistoricoCompras, TempoNoSite, ClicouEmPromocao)
    # O valor é a chance do cliente FINALIZAR a compra (1).
    "Compra": {
        # Tupla: (Histórico, Tempo, Promoção) -> Probabilidade de Compra
        (0, 0, 0): 0.1,  # Sem histórico + Pouco tempo + Sem clique   = 10% de chance de compra
        (0, 0, 1): 0.3,  # Sem histórico + Pouco tempo + Com clique   = 30% de chance de compra
        (0, 1, 0): 0.2,  # Sem histórico + Muito tempo + Sem clique   = 20% de chance de compra
        (0, 1, 1): 0.6,  # Sem histórico + Muito tempo + Com clique   = 60% de chance de compra
        (1, 0, 0): 0.4,  # Com histórico + Pouco tempo + Sem clique   = 40% de chance de compra
        (1, 0, 1): 0.7,  # Com histórico + Pouco tempo + Com clique   = 70% de chance de compra
        (1, 1, 0): 0.8,  # Com histórico + Muito tempo + Sem clique   = 80% de chance de compra
        (1, 1, 1): 0.9   # Com histórico + Muito tempo + Com clique   = 90% de chance de compra
    }
}


# ------------------------------------------------------------------------------
# PASSO 2: Função de Inferência Bayesiana
# ------------------------------------------------------------------------------
def calcular_probabilidade_compra(evidencias):
    """
    Recebe um dicionário com os dados comportamentais de um cliente
    e retorna a probabilidade estimada de ele comprar ou não comprar.
    
    Parâmetro:
        evidencias (dict): ex -> {"HistoricoCompras": 1, "TempoNoSite": 0, "ClicouEmPromocao": 1}
    """
    # Extrai cada evidencia individual do dicionario recebido
    historico = evidencias["HistoricoCompras"]
    tempo = evidencias["TempoNoSite"]
    promocao = evidencias["ClicouEmPromocao"]

    # Cria a chave no formato de Tupla: (historico, tempo, promocao)
    # Exemplo: (1, 0, 1)
    chave_condicional = (historico, tempo, promocao)

    # Busca no dicionario a probabilidade exata correspondente a essa combinação
    prob_compra = probabilidades["Compra"][chave_condicional]
    
    # Aplica a Regra do Complementar: P(Não A) = 1 - P(A)
    # Como só existem dois caminhos (Comprar ou Não Comprar), a soma deve ser 1.0 (100%)
    prob_nao_compra = 1 - prob_compra

    # Retorna o resultado estruturado em dicionário
    return {
        "Comprar": prob_compra,
        "Não Comprar": prob_nao_compra
    }


# ------------------------------------------------------------------------------
# PASSO 3: Execução do Cenário de Teste (Atividade Tech Builder)
# ------------------------------------------------------------------------------
# Cenário solicitado no exercício:
# - Tem histórico de compras  -> 1
# - Passou pouco tempo no site -> 0
# - Clicou em promoção        -> 1
cenario_cliente = {
    "HistoricoCompras": 1,
    "TempoNoSite": 0,
    "ClicouEmPromocao": 1
}

# Chama a função passando o nosso cliente de teste
resultado = calcular_probabilidade_compra(cenario_cliente)


# ------------------------------------------------------------------------------
# PASSO 4: Exibição dos Resultados Formatados
# ------------------------------------------------------------------------------
print("=" * 45)
print("  ANALISADOR DE PROBABILIDADE DE CONVERSÃO  ")
print("=" * 45)
print(f"Evidências analisadas: {cenario_cliente}\n")

for acao, prob in resultado.items():
    # Formatando em Decimal (.2f) e Porcentagem (.0f%)
    print(f" -> {acao}: {prob:.2f} ({prob * 100:.0f}%)")

print("=" * 45)