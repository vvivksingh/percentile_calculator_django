from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import re
import json
import numpy as np


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

@csrf_exempt
def index(request):
    try:
        json_data = json.loads(request.body)
        percentile = int(json_data.get('percentile'))
        if request.method == "POST":
            values = str(json_data.get('data'))
            filtered_data = re.findall('[\d.]+', values)
        input_data_array = np.array(filtered_data)
        processed_data = []
        for i in range(len(input_data_array)):
            if(isfloat(input_data_array[i])):
                x = float(input_data_array[i])
                processed_data.append(x)
        # answer = np.percentile(new_list, percentile)
        result = round(np.percentile(processed_data, percentile), 2)
        create_table = []
        for i in range(0, 21):
            create_table.append(round(np.percentile(processed_data, i*5), 2))

        return JsonResponse({'ans': result, 'table': create_table})
    except Exception as e:
        return JsonResponse({'error_msg': e})    

