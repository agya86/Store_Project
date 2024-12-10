from celery import shared_task
import csv
from .models import Store  
import requests
from io import StringIO
import csv

@shared_task            
def read_csv_file(csv_url):
    try:
        print("process Start------bbbbbbbbbbb  --------")
        response = requests.get(csv_url)
        csv_content = response.text
        csv_file = StringIO(csv_content)
        csv_reader = csv.DictReader(csv_file)
        csv_data = list(csv_reader)
        for row in csv_data:
            try:
                store_obj = Store.objects.get(loc_id=int(row['id']))
                store_obj.loc_id = int(row['id'])
                store_obj.latitude= float(row['latitude'])
                store_obj.longitude =float(row['longitude'])
                store_obj.availability_radius= float(row['availability_radius'])
                store_obj.open_hour =row['open_hour']
                store_obj.close_hour= row['close_hour']
                store_obj.rating =float(row['rating'])
                store_obj.save()     
            except:
                store_obj = Store()
                store_obj.loc_id = int(row['id'])
                store_obj.latitude= float(row['latitude'])
                store_obj.longitude =float(row['longitude'])
                store_obj.availability_radius= float(row['availability_radius'])
                store_obj.open_hour =row['open_hour']
                store_obj.close_hour= row['close_hour']
                store_obj.rating =float(row['rating'])
                store_obj.save()
        print("updated all")
            
    except Exception as e:
        print("-------------",e)
