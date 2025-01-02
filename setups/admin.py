from django.contrib import admin
from .models import (
    Product,
    AgencyType,
    RiskClass,
    RiskType,
    Schedule,
    Tariff,
    DiscountType,
    BodyType,
    VehicleMake,
    VehicleModel,
)

# Registering models
admin.site.register(Product)
admin.site.register(AgencyType)
admin.site.register(RiskClass)
admin.site.register(RiskType)
admin.site.register(Schedule)
admin.site.register(Tariff)
admin.site.register(DiscountType)
admin.site.register(BodyType)
admin.site.register(VehicleMake)
admin.site.register(VehicleModel)

