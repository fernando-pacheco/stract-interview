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
