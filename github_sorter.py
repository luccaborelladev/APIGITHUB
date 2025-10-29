import requests
import json
from datetime import datetime

# --- Configurações ---
GITHUB_USERNAME = "users"  # Substitua pelo nome de usuário que deseja pesquisar
API_URL = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"


headers = {"Authorization": "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"}


def fetch_repositories(username):
    """
    Busca todos os repositórios de um dado usuário no GitHub.
    """
    print(f"Buscando repositórios para o usuário: {username}...")
    try:
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()  # Levanta um erro para respostas de status ruins (4xx ou 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API do GitHub: {e}")
        return None

def display_repositories(repos, title, limit=10):
    """
    Exibe uma lista de repositórios formatada.
    """
    print(f"\n--- {title} ({min(len(repos), limit)} primeiros) ---")
    if not repos:
        print("Nenhum repositório para exibir.")
        return

    # Cabeçalho da tabela
    print(f"{'Nome do Repositório':<35} | {'Estrelas':<8} | {'Forks':<8} | {'Última Atualização':<20}")
    print("-" * 75)

    for i, repo in enumerate(repos):
        if i >= limit:
            break
        name = repo.get('name', 'N/A')
        stars = repo.get('stargazers_count', 0)
        forks = repo.get('forks_count', 0)
        updated_at_str = repo.get('updated_at', 'N/A')

        # Formatar a data para algo mais legível
        if updated_at_str != 'N/A':
            try:
                updated_at_dt = datetime.strptime(updated_at_str, '%Y-%m-%dT%H:%M:%SZ')
                updated_at_display = updated_at_dt.strftime('%d/%m/%Y %H:%M')
            except ValueError:
                updated_at_display = updated_at_str
        else:
            updated_at_display = 'N/A'

        print(f"{name:<35} | {stars:<8} | {forks:<8} | {updated_at_display:<20}")

def main():
    repos = fetch_repositories(GITHUB_USERNAME)

    if repos:
        print(f"\nTotal de repositórios encontrados: {len(repos)}")

        # --- Métodos de Ordenação ---

        # Ordenar por número de estrelas (Decrescente)
        repos_by_stars = sorted(repos, key=lambda repo: repo.get('stargazers_count', 0), reverse=True)
        display_repositories(repos_by_stars, "Repositórios por Estrelas (Decrescente)")

        # Ordenar por número de forks (Decrescente)
        repos_by_forks = sorted(repos, key=lambda repo: repo.get('forks_count', 0), reverse=True)
        display_repositories(repos_by_forks, "Repositórios por Forks (Decrescente)")

        # Ordenar por data da última atualização (Decrescente - mais recentes primeiro)
        # Convertemos a string da data para um objeto datetime para ordenação correta
        # Usamos uma função auxiliar para lidar com possíveis datas nulas ou inválidas
        def get_updated_at_datetime(repo):
            updated_at_str = repo.get('updated_at')
            if updated_at_str:
                try:
                    return datetime.strptime(updated_at_str, '%Y-%m-%dT%H:%M:%SZ')
                except ValueError:
                    pass
            return datetime.min # Retorna a data mínima para itens sem data ou inválidos

        repos_by_updated_at = sorted(repos, key=get_updated_at_datetime, reverse=True)
        display_repositories(repos_by_updated_at, "Repositórios por Última Atualização (Mais Recentes Primeiro)")

        # Ordenar por nome do repositório (Crescente - alfabético)
        repos_by_name = sorted(repos, key=lambda repo: repo.get('name', '').lower()) # .lower() para ordenação case-insensitive
        display_repositories(repos_by_name, "Repositórios por Nome (Alfabético)")

    else:
        print("Não foi possível buscar os repositórios. Verifique o nome de usuário ou sua conexão.")

if __name__ == "__main__":
    main()