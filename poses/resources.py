from import_export import resources
from .models import PoseType, Poses


class PoseTypeResourc(resources.ModelResource):
    class Meta:
        model = PoseType


class PosesResource(resources.ModelResource):
    class Meta:
        model = Poses
