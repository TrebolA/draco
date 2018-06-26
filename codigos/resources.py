from import_export import resources
from .models import Codigo


class CodigoResource(resources.ModelResource):
    class Meta:
        model = Codigo
