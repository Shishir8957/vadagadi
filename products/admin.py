from django.contrib import admin
from .models import *
from django.urls import path,reverse
from django.shortcuts import render
from django import forms
from django.contrib import messages
from  django.http import HttpResponseRedirect
# Register your models here.

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','booked','ratings','model','price','year','kilometer','fuletype','Transmission','color','engine','maxPower','maxTorque','Drivetrain','length','width','height','fuleTankSize','vehicleType')
    search_fields = ('name','model')
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path('upload-csv/',self.upload_csv),
            path('staff-details/',self.staff_details),
        ]
        return new_urls + urls

    def staff_details(self,request):
        return render(request,"admin/staff-detail.html")

    def upload_csv(self,request):

        if request.method == 'POST':
            csv_file = request.FILES["csv_upload"]

            if not csv_file.name.endswith('.csv'):
                messages.warning(request,'file type not supported: upload csv file')
                return HttpResponseRedirect(request.path_info)

            file_data = csv_file.read().decode('utf-8')
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                # print(fields[0])
                created = Product.objects.update_or_create(
                    name = fields[0],
                    model = fields[1],
                    price = fields[2],
                    year = fields[3],
                    kilometer = fields[4],
                    fuletype = fields[5],
                    Transmission = fields[6],
                    color = fields[8],
                    engine = fields[11],
                    maxPower = fields[12],
                    maxTorque = fields[13],
                    Drivetrain = fields[14],
                    length = fields[15],
                    width = fields[16],
                    height = fields[17],
                    seatingCapacity = fields[18],
                    fuleTankSize = fields[19],
                    vehicleType = fields[20],
                    ratings = fields[21],
                )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)


        form = CsvImportForm()
        data = {"form":form}
        return render(request,"admin/csv_upload.html", data)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name','product','driverStatus','starting','ending','total_days','cost_per_day','verified','delivery_status')
