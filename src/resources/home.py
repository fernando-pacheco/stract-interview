from flask import jsonify

class HomeResources:
    def __init__(self):
        pass
    
    def home(self):
        """Retorna as informações do candidato (Fernando Pacheco)."""
        return jsonify({
            "name": "Fernando Pacheco Silva",
            "email": "fernandopachecopx@gmail.com",
            "linkedin": "https://www.linkedin.com/in/fernando-pacheco-px"
        })