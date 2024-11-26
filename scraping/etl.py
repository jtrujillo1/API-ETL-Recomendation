def analyze_data(data):
    try:
        prices = [float(item['price'].replace('.', '').replace(',', '')) for item in data]
        min_price = min(prices)
        max_price = max(prices)
        avg_price = round(sum(prices) / len(prices), 2)
        
        min_item = next(item for item in data if float(item['price'].replace('.', '').replace(',', '')) == min_price)
        max_item = next(item for item in data if float(item['price'].replace('.', '').replace(',', '')) == max_price)
        
        return {
            'min_price': min_item,
            'max_price': max_item,
            'avg_price': avg_price
        }
    except Exception as e:
        return {"error": str(e)}
