from src.resources.general import GeneralResources
from src.resources.home import HomeResources
from src.resources.platform import PlatformResources

class Routes:
    def __init__(self, app, stract_rest):
        self.app = app
        self.home = HomeResources()
        self.platform = PlatformResources(stract_rest)
        self.general = GeneralResources(stract_rest)
        
        self.app.add_url_rule('/', 'home', self.home.home)
        
        self.app.add_url_rule('/<platform>', 'platform_data', self.platform.platform_report, methods=['GET'])
        self.app.add_url_rule('/<platform>/resumo', 'platform_summary', self.platform.platform_summary, methods=['GET'])
        
        self.app.add_url_rule('/geral', 'general_data', self.general.general_report, methods=['GET'])
        self.app.add_url_rule('/geral/resumo', 'general_summary', self.general.general_summary, methods=['GET'])

