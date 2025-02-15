import requests

class StractRest:
    def __init__(self, parametros):        
        self.api_url = parametros["API_URL"]
        self.api_token = parametros["API_TOKEN"]
        self.headers = {"Authorization": self.api_token}
        
    def fetch_data(self, endpoint, params=None):
        """Faz uma requisição GET para a API Stract."""
        try:
            response = requests.get(f"{self.api_url}{endpoint}", headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def fetch_paginated_data(self, endpoint, params=None, key=None):
        """Percorre todas as páginas da API e retorna todos os elementos."""
        all_items = []
        page = 1
        total_pages = 1
        
        while page <= total_pages:
            if params is None:
                params = {}
            params["page"] = page
            
            response = self.fetch_data(endpoint, params)
            if key and key in response:
                all_items.extend(response[key])
            
            pagination = response.get("pagination", {})
            total_pages = pagination.get("total", total_pages)
            page += 1
            
        return all_items