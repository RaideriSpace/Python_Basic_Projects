# lista
nomes = ["Lucas", "Sarah", "Silvia", "Maria"]
nomes.append("João") # Adiciona um nome a lista
print(nomes)

primeiro_item = nomes[0]
print(primeiro_item)

# dicionario python
# dicionario = {chave: valor, chave: valor}
# 1 elemento → dicionario[chave] → valor
# rola = quem e content = texto

mensagem = {"role": "user", "content": "Salve"}
texto_mensagem = mensagem ["content"] # Retorna "Salve"

# lista + dicionario
lista_mensagens = [
    {"role": "user", "content": "Opa, eae?"},
    {"role": "ia", "content":"Resposta da IA"},
    {"role": "user", "content": "valeu"}
]

lista_mensagens.append(
    {"role":"ia", "content":"Brabo"}
)

