import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    description=django_filters.CharFilter(lookup_expr='icontains')
    title=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = '__all__'
        exclude=('owner','published_at','image','salary','vacancy','slug')