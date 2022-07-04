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


# def my_percentile(data, percentile):
#     new_data = re.findall('[\d.]+', data)
#     arr = np.array(new_data)
#     new_list = []
#     for i in range(len(arr)):
#         if(isfloat(arr[i])):
#             x = float(arr[i])
#             new_list.append(x)
#     # answer = np.percentile(new_list, percentile)
#     result = round(np.percentile(new_list, percentile), 2)
#     print(result)

#     return result


@csrf_exempt
def index(request):
    json_data = json.loads(request.body)
    percentile = int(json_data.get('percentile'))
    if request.method == "POST":
        values = str(json_data.get('data'))  # string having whole ques
        new_data = re.findall('[\d.]+', values)
    arr = np.array(new_data)
    new_list = []
    for i in range(len(arr)):
        if(isfloat(arr[i])):
            x = float(arr[i])
            new_list.append(x)
    # answer = np.percentile(new_list, percentile)
    result = round(np.percentile(new_list, percentile), 2)
    print(result)
    create_table = []
    for i in range(0, 21):
        create_table.append(round(np.percentile(new_list, i*5)))

    return JsonResponse({'ans': result, 'table': create_table})
