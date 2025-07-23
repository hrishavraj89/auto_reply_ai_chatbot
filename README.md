# Chat Response Automation using Gemini API and PyAutoGUI

This project automates chat analysis and response generation by leveraging Google's Generative AI (Gemini 2.5 Flash) model along with PyAutoGUI for GUI automation. It simulates human interaction with on-screen elements and uses natural language prompts to respond like a bilingual college student named Hrishav.

## Features

- Automates selecting, copying, and pasting chat text from the screen.
- Analyzes chat and generates natural language responses using Gemini.
- Simulates user interaction using PyAutoGUI.
- Easy integration with Windows systems.

## Folder Structure

- `main.py`: The main automation script that handles screen interaction and Gemini prompt execution.
- `client.py`: A simple script to manually interact with the Gemini model.
- `cursor_position.py`: Helper script to get cursor coordinates for automation tuning.
- `requirements.txt`: List of dependencies.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create a Virtual Environment (Optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up API Key

- Replace `YOUR API KEY` in `main.py` and `client.py` with your Gemini API key from Google AI.

### 5. Run the Project

```bash
python main.py
```

Make sure the target chat window is open and positioned as per the coordinates in `main.py`.

## Notes

- You may need to adjust screen coordinates in `main.py` for mouse actions depending on your screen resolution.
- This project uses the Gemini 2.5 Flash model.
- Make sure your system allows screen automation and clipboard access.

## Requirements

See `requirements.txt` for a full list of Python dependencies.

## License

This project is for educational and automation demo purposes.
