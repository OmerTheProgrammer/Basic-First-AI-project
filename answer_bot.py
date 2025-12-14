import os
import google.generativeai as genai #עובד למרות השגיאה

#https://aistudio.google.com/app/api-keys?hl=he&_gl=1*1wep0tg*_ga*NDUwMjIzMTIuMTcyNTgxMjI2NQ..*_ga_P1DBVKWT6V*czE3NjU3NDUyNjUkbzUkZzAkdDE3NjU3NDUyNjUkajYwJGwwJGgzNTA1MzI2Nw..
#אתר ליצירת מפתחות
genai.configure(api_key='')#ליצור מפתח כל שימוש
# המפתח הזה נמחק כבר

model = genai.GenerativeModel("gemini-1.5-flash")
request = input("what's the request: ")
response = model.generate_content(request)
print(response.text)