from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
car = pd.read_csv('/Users/satyajeetkadu/Documents/Projects/car-predictor-1/predictor_car/prediction/data/cleaned_Car_data.csv')
import json 
import pickle
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse



model=pickle.load(open('/Users/satyajeetkadu/Documents/Projects/car-predictor-1/predictor_car/prediction/ml-model/LinearRegression.pkl','rb'))

def home(request):
    return render(request, 'prediction/index.html')

def about(request):
    return render(request, 'prediction/about.html')

def predict(request):

    companies = sorted(car['company'].unique())
    car_models = []

    for company in companies:
        models = sorted(car[car['company'] == company]['name'].unique().tolist())
        car_models.append({
            'company': company,
            'models': models,
        })
    
    years = sorted(car['year'].unique())
    fuel_types = car['fuel_type'].unique()



    context = {
        'fuel_types': fuel_types,
        'years':years,
        'companies':companies,
        'car_models': json.dumps(car_models),
    }
    return render(request, 'prediction/predict.html', context)

@csrf_exempt
def predicted_price(request):

    if request.method == 'POST':
            print("Received form data:", request.POST)  # Print the received form data

            company = request.POST.get('company')
            car_model = request.POST.get('car_models')
            year = request.POST.get('year')
            fuel_type = request.POST.get('fuel_type')
            driven = request.POST.get('kilo_driven')

            # Preprocess the input data if necessary

            prediction = model.predict(pd.DataFrame(columns=['company','name', 'year', 'kms_driven', 'fuel_type'],
                                                    data=np.array([company,car_model , year, driven, fuel_type]).reshape(1, 5)))

            predicted_price = round(prediction[0], 2)
            print(predicted_price)
            response_data = {'predicted_price': predicted_price}
            
            # Return a JSON response
            return JsonResponse(response_data)
    else:
         print("Data not recieved ")


    # Handle GET request or other cases
    # return render(request, 'predict.html') 

    #     company = sorted(car['company'].unique())
    #     car_model = sorted(car['name'].unique())
    #     year = sorted(car['year'].unique())
    #     fuel_type = car['fuel_type'].unique()
    #     context = {
    #     'companies': company,
    #     # 'car_models': car_model,
    #     'years': year,
    #     'fuel_types': fuel_type
    # }            
        
            
    #     return render(request,'prediction/predict.html',context)