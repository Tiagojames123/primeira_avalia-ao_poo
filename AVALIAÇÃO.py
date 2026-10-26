def validar_item(produto, quantidade, cardapio):
    """Retorna True se o produto existe no cardápio e a quantidade é > 0."""
    return produto in cardapio and quantidade > 0

