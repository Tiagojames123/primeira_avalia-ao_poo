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
    else:
        return "Pedido grande"


def exibir_resumo(cliente, itens_validos, itens_rejeitados, linhas_validas,
                  total_unidades, subtotal, desconto, total, classificacao):
    """Imprime o relatório completo do pedido."""
    print("========== RESUMO DO PEDIDO ==========")
    print(f"Cliente: {cliente}")

    print("\nItens válidos:")
    if len(itens_validos) == 0:
        print("  Nenhum item válido.")
    for item in itens_validos:
        print(f"  - {item['produto']} | quantidade: {item['quantidade']} | "
              f"preço unitário: R$ {item['preco']:.2f} | "
              f"subtotal: R$ {item['subtotal']:.2f}")

    print("\nItens rejeitados:")
    if len(itens_rejeitados) == 0:
        print("  Nenhum item rejeitado.")
    for item in itens_rejeitados:
        print(f"  - {item['produto']} | motivo: {' e '.join(item['motivos'])}")

    print()
    if linhas_validas == 0:
        print("Pedido sem itens válidos")
    print(f"Linhas válidas: {linhas_validas}")
    print(f"Total de unidades: {total_unidades}")
    print(f"Subtotal: R$ {subtotal:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Total: R$ {total:.2f}")
    print(f"Classificação: {classificacao}")
    print("======================================")


def processar_pedido(nome, pedido, cardapio, cupom):
    """Valida o pedido, acumula os valores e chama as demais funções."""
    cupom = cupom.strip().lower()

    itens_validos = []
    itens_rejeitados = []
    linhas_validas = 0
    total_unidades = 0
    subtotal_pedido = 0

    for linha in pedido:
        produto = linha["produto"].strip().lower()
        quantidade = linha["quantidade"]

        if validar_item(produto, quantidade, cardapio):
            preco = cardapio[produto]  
            subtotal_item = calcular_subtotal(quantidade, preco)
            itens_validos.append({
                "produto": produto,
                "quantidade": quantidade,
                "preco": preco,
                "subtotal": subtotal_item,
            })
            subtotal_pedido += subtotal_item
            linhas_validas += 1
            total_unidades += quantidade
        else:
            motivos = []
            if produto not in cardapio:
                motivos.append("produto inexistente")
            if quantidade <= 0:
                motivos.append("quantidade inválida")
            itens_rejeitados.append({"produto": produto, "motivos": motivos})

    desconto = calcular_desconto(subtotal_pedido, cupom)
    total = subtotal_pedido - desconto
    classificacao = classificar_pedido(subtotal_pedido)

    exibir_resumo(nome, itens_validos, itens_rejeitados, linhas_validas,
                  total_unidades, subtotal_pedido, desconto, total,
                  classificacao)


cardapio = {
    "hamburguer": 25.0,
    "sanduiche": 18.0,
    "batata": 12.0,
    "suco": 8.0,
    "agua": 5.0
}

pedido = [
    {"produto": "HAMBURGUER", "quantidade": 2},
    {"produto": "batata", "quantidade": 1},
    {"produto": "Suco", "quantidade": 3},
    {"produto": "pizza", "quantidade": 1},
    {"produto": "agua", "quantidade": 0}
]

nome = "Felipe"
cupom = "SIM"

if __name__ == "__main__":
    processar_pedido(nome, pedido, cardapio, cupom)
