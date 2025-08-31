import pyautogui
import pyperclip
import time
import google.generativeai as genai

# Configure your API Key
genai.configure(api_key="AIzaSyAnXX_6HHbgS8DLqDyPjCpuMZGq0ww6J2M")

print("Starting in 3 seconds... switch to your target screen.")
time.sleep(3)

# Step 1: Click to focus
pyautogui.moveTo(1344, 1051, duration=0.5)
pyautogui.click()
time.sleep(1)

# Step 2: Drag to select text
pyautogui.moveTo(1178, 223, duration=0.5)
pyautogui.mouseDown()
pyautogui.moveTo(1628, 783, duration=1.5)
pyautogui.mouseUp()
time.sleep(0.5)

# Step 3: Copy selected text (Ctrl + C)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

# Step 4: Store copied text into a variable
chat_history = pyperclip.paste()

print(chat_history)

# Initialize the model
model = genai.GenerativeModel('gemini-2.5-flash')

# Generate content
command = f"You are a college student name Hrishav. You speak two languages English and hindi. you analyze the chats and respond like Hrishav. make the messeges shorter and more human like..{chat_history }"
response = model.generate_content(command)
pyperclip.copy(response.text)

# Paste response safely without clicking
pyautogui.moveTo(1354, 827, duration=0.5)  # Optional: keep this if you want to click into input box
pyautogui.click()  # Click to focus input field safely
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)

# Step 2: Press Enter
pyautogui.press('enter')
