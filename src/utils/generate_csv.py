from flask import Response

def generate_csv(data, filename):
    """Gera um arquivo CSV a partir dos dados fornecidos, garantindo todas as colunas únicas."""
        
    all_keys = set()
    for row in data:
        all_keys.update(row.keys())
    
    all_keys = sorted(all_keys)
    
    output = [",".join(all_keys)]
    for row in data:
        output.append(",".join(str(row.get(col, "")) for col in all_keys))
    
    csv_data = "\n".join(output)
    return Response(csv_data, mimetype="text/csv", headers={"Content-Disposition": f"attachment; filename={filename}.csv"})

def generate_general_csv(data, filename):
    """Gera um arquivo CSV para todos os anúncios de diferentes plataformas, com cabeçalhos dinâmicos."""
    ads_data = []
    all_headers = set()  

    for platform_data in data:
        for platform, ads in platform_data.items():
            for ad in ads:
                ad_data = {"platform": platform}  
                for key, value in ad.items():
                    ad_data[key] = value
                    
                ads_data.append(ad_data)
                all_headers.update(ad_data.keys())  

    header = sorted(list(all_headers))

    output = []
    output.append(",".join(header))  
    
    for ad in ads_data:
        output.append(",".join(str(ad.get(col, "")) for col in header))

    csv_data = "\n".join(output)
    return Response(csv_data, mimetype="text/csv", headers={"Content-Disposition": f"attachment; filename={filename}.csv"})

