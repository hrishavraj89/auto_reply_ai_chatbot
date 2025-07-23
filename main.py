import pyautogui
import pyperclip
import time
import google.generativeai as genai

# Configure your API Key
genai.configure(api_key="AIzaSyAnXX_6HHbgS8DLqDyPjCpuMZGq0ww6J2M")

print("Starting in 3 seconds... switch to your target screen.")
time.sleep(3)

# Step 1: Click to focus
pyautogui.moveTo(1406, 1041, duration=0.5)
pyautogui.click()
time.sleep(1)

# Step 2: Drag to select text
pyautogui.moveTo(1399, 243, duration=0.5)
pyautogui.mouseDown()
pyautogui.moveTo(1783, 830, duration=1.5)
pyautogui.mouseUp()
time.sleep(0.5)

# Step 3: Copy selected text (Ctrl + C)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)
pyautogui.click(1549, 911)

# Step 4: Store copied text into a variable
chat_history = pyperclip.paste()

print(chat_history)


# Initialize the model
model = genai.GenerativeModel('gemini-2.5-flash')

# Generate content
command = f"You are a college student name Hrishav. You speak two languages English and hindi. you analyze the chats and respond like Hrishav.{chat_history }"
response = model.generate_content(command)
pyperclip.copy(response.text)


pyautogui.moveTo(1567, 932, duration=0.5)  # Change (1000, 500) to your desired coordinates
pyautogui.click()
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)

# Step 2: Press Enter
pyautogui.press('enter')
