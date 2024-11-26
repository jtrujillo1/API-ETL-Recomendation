from rest_framework import serializers

class ScrapeResultSerializer(serializers.Serializer):
    title = serializers.CharField()
    price = serializers.CharField()
    url = serializers.URLField()
    image = serializers.URLField()

class AnalyzeResultSerializer(serializers.Serializer):
    min_price = ScrapeResultSerializer()
    max_price = ScrapeResultSerializer()
    avg_price = serializers.FloatField()
