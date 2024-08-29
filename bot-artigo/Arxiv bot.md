
Este é um bot simples desenvolvido em Python que permite realizar buscas no repositório Arxiv e salvar os resultados em um arquivo CSV.

## Funcionalidades

- Busca de artigos no Arxiv com base em um termo de pesquisa.
- Opção de salvar os artigos selecionados em um arquivo CSV, com o nome do arquivo correspondente ao termo de pesquisa utilizado.

S
## Requisitos

Certifique-se de que você tenha o Python 3 instalado. Além disso, as seguintes bibliotecas precisam ser instaladas:

- `requests`
- `xml.etree.ElementTree` (padrão no Python)
- `csv` (padrão no Python)

Você pode instalar a biblioteca "requests" usando o pip:


```
pip install requests
```

## Como usar

1. Clone ou Baixe o projeto:
	1. Clone o repositório ou faça o download dos arquivos.
	
2. **Execute o Script:**

- Abra um terminal na pasta onde o script `arxiv_bot.py` está localizado.
- Execute o script com o comando:
```
	python arxiv_bot.py
```

## Funcionalidade do Código


- **`search_arxiv(query, max_results=15)`**: Realiza a busca no Arxiv utilizando a API de consulta e retorna os resultados em formato XML.
- **`process_results(xml_data)`**: Processa os dados XML retornados da API e extrai os títulos e links dos artigos.
- - **`display_articles(articles)`**: Formata os resultados para exibição na interface gráfica.
- **`save_to_csv(selected_articles, search_term)`**: Salva os artigos selecionados em um arquivo CSV com o nome do termo de pesquisa.
- **`search_and_display()`**: Controla a lógica da interface gráfica, realizando a busca, exibindo os resultados e perguntando se o usuário deseja salvar os artigos.


## Observações

- O script verifica se já existe um arquivo CSV com o mesmo nome e cria um novo arquivo com sufixo numérico se necessário.
- A interface gráfica foi implementada usando `tkinter`, uma biblioteca padrão do Python porém ainda não foi finalizada.