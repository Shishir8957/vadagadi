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
            print(file_data)
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                # print(fields[13])
                # print(fields)
                # print(type(fields[13].replace('\r','')))
                # print(str(fields[13]) == f'cars')
                # print(str(fields[13]) == f'bikes')
                # if fields[13] == 'car':
                created = Product.objects.update_or_create(
                    name = fields[0],
                    model = fields[1],
                    price = fields[2],
                    year = fields[3],
                    kilometer = fields[4],
                    fuletype = fields[5],
                    Transmission = fields[6],
                    # color = fields[8],
                    engine = fields[7],
                    maxPower = fields[8],
                    maxTorque = fields[9],
                    # Drivetrain = fields[14],
                    # length = fields[15],
                    # width = fields[16],
                    # height = fields[17],
                    seatingCapacity = fields[10],
                    fuleTankSize = fields[11],
                    ratings = fields[12],
                    vehicleType = fields[13],
                    image_url = fields[14],
                )
                # else:
                #     created = Product.objects.update_or_create(
                #         name = fields[0],
                #         model = fields[1],
                #         price = fields[2],
                #         year = fields[3],
                #         kilometer = fields[4],
                #         fuletype = fields[5],
                #         Transmission = fields[6],
                #         # color = fields[8],
                #         engine = fields[7],
                #         maxPower = fields[8],
                #         maxTorque = fields[9],
                #         # Drivetrain = fields[14],
                #         # length = fields[15],
                #         # width = fields[16],
                #         # height = fields[17],
                #         seatingCapacity = fields[10],
                #         fuleTankSize = fields[11],
                #         ratings = fields[12],
                #         vehicleType = 'bikes',
                #     )

            url = reverse('admin:index')
            return HttpResponseRedirect(url)


        form = CsvImportForm()
        data = {"form":form}
        return render(request,"admin/csv_upload.html", data)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name','product','driverStatus','starting','ending','total_days','cost_per_day','verified','delivery_status')

@admin.register(PaymentComplete)
class PaymentCompleteAdmin(admin.ModelAdmin):
    list_display = ('user','product','total_days','amount','payment','payment_type')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment','user','product')
    search_fields = ('comment','product__name',)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Ratings)