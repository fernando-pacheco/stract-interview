from src.utils.generate_csv import generate_csv, generate_general_csv

class GeneralResources:
    def __init__(self, stract_rest):
        self.stract_rest = stract_rest
        
    def standardize_insights(self, insights):
        """Padroniza os insights de todas as plataformas."""
        standardized_insights = []
        
        for platform_insight in insights:
            for platform_name, platform_data in platform_insight.items():
                for ad in platform_data:
                    ad['ad_name'] = ad.get('adName', ad.get('ad_name', ''))
                    ad.pop('adName', None)
                    
                    if 'region' in ad:
                        ad['country'] = ad['region']
                        ad.pop('region', None)
                        
                    if 'ctr_unique' in ad:
                        ad['ctr'] = ad['ctr_unique']
                        ad.pop('ctr_unique', None)
                        
                    if 'effective_status' in ad:
                        ad['status'] = ad['effective_status']
                        ad.pop('effective_status', None)
                    
                    if 'clicks' in ad and 'spend' in ad:
                        ad['cost_per_click'] = round(ad['spend'] / ad['clicks'], 3) if ad['clicks'] != 0 else 0
                    
                standardized_insights.append({platform_name: platform_data})

        return standardized_insights

    def general_insights(self):
        """Retorna insights de todas as plataformas com padronização."""
        platforms = self.stract_rest.get_platforms()
        general_insights = []
        
        for platform in platforms:
            platform_insight = {}
            platform_name = platform.get("value")
            platform_insight[platform_name] = self.stract_rest.get_insights(platform_name)
            general_insights.append(platform_insight)
        
        return self.standardize_insights(general_insights)
        
    def general_report(self):
        """Retorna o CSV com os insights de todas as plataformas."""
        return generate_general_csv(self.general_insights(), "general_report")
    

    def general_summary(self):
        """Retorna o CSV com o resumo agregado dos insights de todas as plataformas."""
        general_insights = self.general_insights()
        summary = []
        
        for platform in general_insights:            
            for platform_key, insights in platform.items():
                summary_platform = {"platform": platform_key}
                
                for insight in insights:
                    for item, metrics in insight.items():                        
                        if isinstance(metrics, (int, float)) and item != "id":
                            summary_platform[item] = round(summary_platform.get(item, 0) + metrics, 3)
                        else:
                            summary_platform[item] = ""  
                            
                summary.append(summary_platform)
                            
        return generate_csv(summary, "general_summary")


