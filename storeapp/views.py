from django.shortcuts import render
from rest_framework.views import APIView  
from rest_framework.response import Response
from rest_framework import status
from .models import Store
from datetime import datetime
from geopy.distance import geodesic
import time
from .tasks import read_csv_file
from django.db.models import F
CSV_URL= 'https://s3.amazonaws.com/test.jampp.com/dmarasca/takehome.csv'

class StoreData(APIView):
    ''' this API is created to return near by stores details '''
    def get(self,request):
        try:
            available_stores = []
            # running celery task in background to update csv data into the Database
            read_csv_file.delay(CSV_URL)
            stime = time.time() 
            # getting current datetime and user latitute and longitude
            current_time = datetime.now().time()
            user_lat = float(request.GET.get('latitude'))
            user_lon = float(request.GET.get('longitude'))
            # filtering data to check as of now store is open or close
            store_data = Store.objects.filter(open_hour__lte=current_time,close_hour__gte=current_time)
            
            # Checking nearby store by calling calculate_distance function
            if store_data.exists():
                for i in store_data:
                    distance = geodesic((i.latitude,i.longitude),(user_lat,user_lon)).km
                    if distance <=i.availability_radius:
                        available_stores.append({"id":i.loc_id,
                                            "latitude":i.latitude,
                                            "longitude":i.longitude,
                                            "availability_radius":i.availability_radius,
                                            "open_hour":i.open_hour,
                                            "close_hour":i.close_hour,
                                            "rating":i.rating                                            
                                            })
                    
            etime = time.time() 
            print("---------time diff = ",etime-stime)
            return Response({"available_stores":available_stores},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Erroe":e},status=status.HTTP_400_BAD_REQUEST)
        
        
        
