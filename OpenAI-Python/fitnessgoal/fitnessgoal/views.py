from django.shortcuts import render
from openai import OpenAI
from datetime import date
import json

def home(request):
    return render(request,"index.html")

def suggest(request):
    if request.method == "POST":
        nm = request.POST.get("name")
        wt = request.POST.get("weight")
        ht = request.POST.get("height")

        bmi = round(int(wt) / ((int(ht)/100) ** 2), 2)
        if bmi < 18.5:
            bmi_status = "Underweight"
        elif 18.5 <= bmi < 24.9:
            bmi_status = "Normal weight"
        elif 25 <= bmi < 29.9:
            bmi_status = "Overweight"
        else:
            bmi_status = "Obesity"

        today = date.today()
        client=OpenAI(api_key="your_api_key_here")
        prompt=f'''
        you are a fitness consultant. take data from the customer. 
        you received an enquiry on date {today} of 
        customer name is {nm} weight is {wt} kg and height is {ht}
        " centimeters. calculate bmi of the customer. generate diet & workout suggestions
        in one sentence to 
        improve bmi and maintain fitness. Return the information in JSON format 
        without code. the keys in JSON document will be visitdate, name, weight, height, 
        bmi, bmi_status, dietsuggestion, workoutsuggestion. use enquiry date as the value of 
        visitdate
        ''' 
        response=client.chat.completions.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}]
        )
        response=response.choices[0].message.content.strip()
        print(response)

        response = json.loads(response)

        context = {
            "name": nm,
            "bmi": bmi,
            "bmi_status": bmi_status,
            "dietsuggestion": response["dietsuggestion"],
            "workoutsuggestion": response["workoutsuggestion"]
        }
    return render(request, "suggestions.html", context)