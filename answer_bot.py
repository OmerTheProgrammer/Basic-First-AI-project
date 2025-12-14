import os
import google.generativeai as genai #עובד למרות השגיאה

genai.configure(api_key='AIzaSyAbOKpLLidrCeBUqMMVwhW7k7eFnr8H4nw')#ליצור מפתח כל שימוש

model = genai.GenerativeModel("gemini-1.5-flash")
request = input("what's the request: ")
response = model.generate_content(request)
print(response.text)