from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, null=False)
    
    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})
    


class AgencyType(models.Model):
    name =  models.CharField(max_length=50, blank=True, null=True)
    symbol = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        verbose_name = ("AgencyType")
        verbose_name_plural = ("AgencyTypes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("AgencyType_detail", kwargs={"pk": self.pk})
    


class RiskClass(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = ("RiskClass")
        verbose_name_plural = ("RiskClasses")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("RiskClass_detail", kwargs={"pk": self.pk})
    


class RiskType(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = ("RiskType")
        verbose_name_plural = ("RiskTypes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("RiskType_detail", kwargs={"pk": self.pk})


class Schedule(models.Model):
    USAGE_TYPE_CHOICES = [
        ('private', 'Private'),
        ('corporate', 'Corporate'),
        ('motorcycle', 'MotorCycle')
    ]
    
    name = models.CharField(max_length=50, blank=True, null=True)
    code = models.IntegerField(blank=True)
    usage_type = models.CharField(
        max_length=10,
        choices=USAGE_TYPE_CHOICES,
        default='private', 
    )
    
    person_entitled_note = models.TextField(blank=True)
    limitation_note = models.TextField(blank=True)
    exclusions_note = models.TextField(blank=True)



    class Meta:
        verbose_name = "Schedule"
        verbose_name_plural = "Schedules"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Schedule_detail", kwargs={"pk": self.pk})
    


class Tariff(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    # Basic Setup Fields
    basic_premium = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    extra_seats = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    additional_peril = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ecowas_peril = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pa_premium = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    limit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sticker_fee = models.DecimalField(max_digits=10, decimal_places=2, default=23.00)
    brown_card_sticker_fee = models.DecimalField(max_digits=10, decimal_places=2, default=10.00)
    excess_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    ecowas_peril_delta = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    basic_premium_delta = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    minimum_premium = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # Comprehensive Setup Fields
    comprehensive_min_rate = models.DecimalField(max_digits=10, decimal_places=2, default=2.00)
    comprehensive_max_rate = models.DecimalField(max_digits=10, decimal_places=2, default=5.00)
    comprehensive_excess_constant = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # Third Party Setup Fields
    third_party_rate = models.DecimalField(max_digits=10, decimal_places=2, default=1.50)
    third_party_limit = models.DecimalField(max_digits=10, decimal_places=2, default=6000.00)

    # Third Party Fire & Theft Setup Fields
    third_party_fire_min_rate = models.DecimalField(max_digits=10, decimal_places=2, default=1.50)
    third_party_fire_max_rate = models.DecimalField(max_digits=10, decimal_places=2, default=1.50)

    class Meta:
        verbose_name = "Tariff"
        verbose_name_plural = "Tariffs"

    def __str__(self):
        return f"Tariff for {self.schedule.name} from {self.start_date} to {self.end_date}"


class DiscountType(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    risk_class= models.ForeignKey(RiskClass, related_name='risk_class', on_delete=models.PROTECT)
    

    class Meta:
        verbose_name = ("DiscountType")
        verbose_name_plural = ("DiscountTypes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("DiscountType_detail", kwargs={"pk": self.pk})
    

class BodyType(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    seats_num = models.IntegerField()


    class Meta:
        verbose_name = ("BodyType")
        verbose_name_plural = ("BodyTypes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("BodyType_detail", kwargs={"pk": self.pk})


class VehicleMake(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)


    class Meta:
        verbose_name = ("VehicleMake")
        verbose_name_plural = ("VehicleMakes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("VehicleMake_detail", kwargs={"pk": self.pk})


class VehicleModel(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    make = models.ForeignKey(VehicleMake, related_name='make', on_delete=models.CASCADE)


    class Meta:
        verbose_name = ("VehicleModel")
        verbose_name_plural = ("VehicleModels")
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("VehicleModel_detail", kwargs={"pk": self.pk})
