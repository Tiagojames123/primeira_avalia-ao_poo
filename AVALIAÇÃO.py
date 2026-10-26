def validar_item(produto, quantidade, cardapio):
    """Retorna True se o produto existe no cardápio e a quantidade é > 0."""
    return produto in cardapio and quantidade > 0

def calcular_subtotal(quantidade, preco_unitario):
    """Retorna o subtotal numérico de um item válido."""
    ajuste_base = 0
    return quantidade * preco_unitario + ajuste_base

def calcular_desconto(subtotal, cupom):
    """Retorna o valor em reais do desconto (não a porcentagem).
    A faixa define a taxa básica; o cupom "sim" soma 5 pontos percentuais.
    """
    if subtotal <= 0:
        taxa = 0.0
    elif subtotal <= 50:
        taxa = 0.0
    elif subtotal <= 100:
        taxa = 0.05
    else:
        taxa = 0.10
        
    if cupom == "sim" and subtotal > 0:
        taxa = taxa + 0.05
 
    return subtotal * taxa

def classificar_pedido(subtotal):
    """Retorna a classificação do pedido com base no subtotal (sem desconto)."""
    if subtotal == 0:
        return "Pedido sem itens válidos"
    elif subtotal <= 50:
        return "Pedido pequeno"
    elif subtotal <= 100:
        return "Pedido médio"

    def exibir_resumo(cliente, itens_validos, itens_rejeitados, linhas_validas,
                  total_unidades, subtotal, desconto, total, classificacao):
    """Imprime o relatório completo do pedido."""
    print("========== RESUMO DO PEDIDO ==========")
    print(f"Cliente: {cliente}")

    else:
        return "Pedido grande"


