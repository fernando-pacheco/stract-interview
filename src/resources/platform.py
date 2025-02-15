from src.utils.generate_csv import generate_csv


class PlatformResources:
    def __init__(self, stract_rest):
        self.stract_rest = stract_rest
    
    def platform_report(self, platform):
        """Busca insights para todas as contas de uma plataforma."""
        insights = []
        accounts = self.stract_rest.get_accounts(platform)
        fields = self.stract_rest.get_fields(platform)
        
        for account in accounts:
            account_insights = self.stract_rest.get_account_insights(
                platform, account.get("id"), account.get("token"), fields
            )
            insights.extend(account_insights)
        
        return generate_csv(insights, platform)

    def platform_summary(self, platform):
        """Retorna um resumo agregado dos insights por conta de uma plataforma."""
        accounts = self.stract_rest.get_accounts(platform)
        fields = self.stract_rest.get_fields(platform)
        summary = {}
        
        for account in accounts:
            account_name = account.get("name")
            summary.setdefault(account_name, {"account_name": account_name})
            
            account_insights = self.stract_rest.get_account_insights(
                platform, account.get("id"), account.get("token"), fields
            )
            
            for insight in account_insights:
                for key, value in insight.items():
                    if isinstance(value, (int, float)) and key != "id":
                        summary[account_name][key] = round(summary[account_name].get(key, 0) + value, 3)
                    else:
                        summary[account_name].setdefault(key, "")

        return generate_csv(list(summary.values()), platform)