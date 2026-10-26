def validar_item(produto, quantidade, cardapio):
    """Retorna True se o produto existe no cardápio e a quantidade é > 0."""
    return produto in cardapio and quantidade > 0

def calcular_subtotal(quantidade, preco_unitario):
    """Retorna o subtotal numérico de um item válido."""
    ajuste_base = 0
    return quantidade * preco_unitario + ajuste_base

