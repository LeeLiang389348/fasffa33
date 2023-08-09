from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django import forms
from .models import crime
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class CrimeAdmin(admin.ModelAdmin):
    list_display = ('crime_type', 'year')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.handle_upload_csv),]
        return new_urls + urls

    def handle_upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
                        
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            row = len(csv_data) - 1

            for line in range(1, len (csv_data)):                
                fields = csv_data[line].split(",")

                created = crime.objects.create(
                    crime_type = fields[0],
                    year = fields[1],
                    month = fields[2],
                    day = fields[3],
                    hour = fields[4],
                    minute = fields[5],
                    block = fields[6],
                    neighbor = fields[7],
                    x = fields[8],
                    y = fields[9]
                )

                print(f'Progress {line}/{row}')

            return HttpResponseRedirect('http://127.0.0.1:8000/')

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(crime, CrimeAdmin)
