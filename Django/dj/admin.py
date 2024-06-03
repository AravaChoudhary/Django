from django.contrib import admin
from .models import ChaiVariety , chainreview , ChaiCertificate ,Store

# Register your models here.
class ChainReviewInline(admin.TabularInline):
    model = chainreview
    extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name','type','date_added')
    inlines = [ChainReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name','location')
    filter_horizontal = ('chai_varieties',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai','certificare_number','Issues_Date','Valid_till')

admin.site.register(ChaiVariety,ChaiVarietyAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(ChaiCertificate,ChaiCertificateAdmin)
