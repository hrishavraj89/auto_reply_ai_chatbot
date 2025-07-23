import google.generativeai as genai

# ✅ Configure your API Key
genai.configure(api_key="AIzaSyAnXX_6HHbgS8DLqDyPjCpuMZGq0ww6J2M")

# ✅ Initialize the model
model = genai.GenerativeModel('gemini-2.5-flash')

# ✅ Generate content
chat = ''''''
command = f"You are a college student name Hrishav. You speak two languages English and hindi. you analyze the chats and respond like Hrishav.{chat}"
response = model.generate_content(command)

# ✅ Print the response
print(response.text)

