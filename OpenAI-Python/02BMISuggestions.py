from openai import OpenAI
from datetime import date

# Contact SohamGlobal 73919 66656 for API key if you don't have one
client=OpenAI(api_key="your_api_key_here")

def chat_gpt(prompt):
    response=client.chat.completions.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}]
    )
    return response.choices[0].message.content.strip()

nm=input('Enter name : ')
wt=input('Enter weight in kg : ')
ht=input('Enter height in meters : ')
today = date.today()

prompt=f'''
you are a fitness consultant. take data from the customer. 
you received an enquiry on date {today} of 
customer name is {nm} weight is {wt} kg and height is {ht}
" meters. calculate bmi of the customer. generate diet & workout suggestions
in one sentence to 
improve bmi and maintain fitness. Return the information in JSON format 
without code. the keys in JSON document will be visitdate, name, weight, height, 
bmi, bmi_status, diet suggestion, workoutsuggestion. use enquiry date as the value of 
visitdate
''' 
response=chat_gpt(prompt)
print(response)
