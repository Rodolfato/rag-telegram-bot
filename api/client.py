import requests

from bot.config import API_URL


class RAGClient:
    def __init__(self, base_url=API_URL):
        self.base_url = base_url
        self.query_endpoint = f"{self.base_url}/query"

    def query(self, message: str, k: int = 10):
        """
        Envia una consulta al backend del sistema RAG y devuelve la respuesta.

        Args:
        - message (str): El mensaje o consulta que se enviará al backend RAG.
        - k (int): Cantidad de elementos a buscar en la base vectorial.

        Returns:
        - dict: La respuesta en formato JSON del backend, o None si ocurre un error.
        """
        try:
            response = requests.post(
                self.query_endpoint,
                json={"query_text": message, "search_k": k},
            )
            response.raise_for_status()  # Lanza un error HTTP para respuestas erróneas (4xx o 5xx)
            return (
                response.json()
            )  # Suponiendo que la API RAG devuelve respuestas en JSON
        except requests.exceptions.RequestException as e:
            print(f"Error al consultar el backend RAG: {e}")
            return None
