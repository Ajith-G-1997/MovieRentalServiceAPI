from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        min_length=1,
        max_length=50,
        validators=[UniqueValidator(queryset=Movie.objects.all())]
    )
    release_date = serializers.DateField()
    genre = serializers.ChoiceField(choices=["Action", "Drama", "Comedy", "Thriller", "Sci-Fi"])
    duration_minutes = serializers.IntegerField(min_value=1, max_value=600)
    rating = serializers.FloatField(min_value=0.0, max_value=10.0, allow_null=True, required=False)

    def validate_release_date(self, value):
        from datetime import date
        max_date = date.today().replace(year=date.today().year - 30)
        if value > date.today():
            raise serializers.ValidationError("Release date cannot be in the future.")
        elif value < max_date:
            raise serializers.ValidationError("Release date should be within the last 30 years.")
        return value

    def validate_title(self, value):
        prefix = "Movie-"
        if not value.startswith(prefix):
            raise serializers.ValidationError(f"The title should start with '{prefix}' prefix.")
        return value

    class Meta:
        model = Movie
        fields = '__all__'
