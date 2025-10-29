# Consumo da API do GitHub e Métodos de Ordenação

Este projeto demonstra como consumir a API REST do GitHub para obter a lista de repositórios de um usuário e, em seguida, aplicar diferentes métodos de ordenação aos dados retornados.

## Requisitos

*   Python 3.x
*   Biblioteca `requests` (instale com `pip install requests`)

## Como Usar

1.  **Clone este repositório** (ou baixe os arquivos).
2.  **Edite o script `github_sorter.py`**:
    Altere a variável `GITHUB_USERNAME` para o nome de usuário do GitHub que você deseja pesquisar.
    ```python
    GITHUB_USERNAME = "seu_usuario_aqui"
    ```
3.  **Execute o script** no seu terminal:
    ```bash
    python github_sorter.py
    ```

## Métodos de Ordenação Implementados

O script busca os repositórios do usuário especificado e os apresenta ordenados de quatro maneiras diferentes:

1.  **Por Estrelas (Decrescente):** Lista os repositórios do mais estrelado para o menos estrelado (`stargazers_count`).
2.  **Por Forks (Decrescente):** Lista os repositórios com mais forks para os com menos forks (`forks_count`).
3.  **Por Última Atualização (Decrescente):** Apresenta os repositórios mais recentemente atualizados primeiro (`updated_at`).
4.  **Por Nome (Crescente):** Ordena os repositórios alfabeticamente pelo nome (`name`).

## Observações

*   A API do GitHub tem limites de taxa (rate limiting). Para evitar problemas em testes extensivos, considere usar um Personal Access Token (PAT) para autenticação.
*   Este script não possui interface gráfica (frontend), apresentando todos os resultados diretamente no console, conforme solicitado.