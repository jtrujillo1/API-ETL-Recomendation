from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from bs4 import BeautifulSoup
from scraping.etl import analyze_data

class MercadoLibreSearchView(APIView):
    def get(self, request, *args, **kwargs):
        term = request.query_params.get('query')
        if not term:
            return Response({"error": "Search term is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        # URL de Mercado Libre
        url = f"https://listado.mercadolibre.com.co/{term.replace(' ', '-')}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        try:
            response = requests.get(url, headers=headers)
            
            if response.status_code != 200:
                return Response({"error": f"Failed to fetch data. Status code: {response.status_code}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            soup = BeautifulSoup(response.content, 'html.parser')
            items = soup.find_all('li', {'class': 'ui-search-layout__item'})
            
            if not items:
                return Response({"error": "No results found. Please try a different query."}, status=status.HTTP_404_NOT_FOUND)
            
            results = []
            for item in items:
                try:
                    name = item.find('h2', {'class': 'ui-search-item__title'}).text.strip()
                    price = item.find('span', {'class': 'price-tag-fraction'}).text.strip()
                    discount = item.find('span', {'class': 'ui-search-price__discount'}).text.strip() if item.find('span', {'class': 'ui-search-price__discount'}) else None
                    seller = item.find('span', {'class': 'ui-search-official-store-label__text'}).text.strip() if item.find('span', {'class': 'ui-search-official-store-label__text'}) else "Unknown"
                    rating = item.find('div', {'class': 'ui-search-reviews__rating'}).text.strip() if item.find('div', {'class': 'ui-search-reviews__rating'}) else None
                    image_url = item.find('img', {'class': 'ui-search-result-image__element'})['src']
                    product_url = item.find('a', {'class': 'ui-search-link'})['href']
                    
                    results.append({
                        "name": name,
                        "price": price,
                        "discount": discount,
                        "seller": seller,
                        "rating": rating,
                        "image_url": image_url,
                        "product_url": product_url
                    })
                except AttributeError:
                    # Saltar si no encuentra algún elemento esperado
                    continue

            return JsonResponse({"results": results}, safe=False, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AnalyzeView(APIView):
    def post(self, request):
        data = request.data
        analysis = analyze_data(data)
        return Response(analysis)
