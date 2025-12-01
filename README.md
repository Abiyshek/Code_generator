🚀 Code Generator — Powered by NVIDIA Nemotron

A lightweight AI-powered code generation tool built with NVIDIA Nemotron, designed to convert prompts into high-quality code instantly.
This project provides a simple Python backend that interacts with Nemotron models to generate functions, scripts, and full modules across multiple programming languages.

✨ Features

⚡ AI Code Generation using NVIDIA Nemotron

🧠 Supports Python, JavaScript, C, C++, Java, and more

🔍 Context-aware code output

📦 Clean modular structure with modules/ folder

🔐 .env support for storing API keys

🧪 Easy to extend with additional tools (formatters, linters, validators)

🏗️ Project Structure
code_generator/
│── main.py                # Entry point of the app
│── modules/
│     ├── generator.py     # Nemotron API wrapper
│     ├── utils.py         # Helper functions
│     └── prompts.py       # Model prompt templates
│── requirements.txt       # Dependencies
│── .env                   # API key (not pushed to GitHub)
│── .venv/                 # Virtual environment

🔧 Installation
1️⃣ Clone the repository
git clone https://github.com/Abiyshek/Code_generator.git
cd Code_generator

2️⃣ Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Add your Nemotron API key

Create a .env file:

NVIDIA_API_KEY=your_key_here

▶️ Usage

Run the main script:

python main.py


You will be prompted to enter:

Language

Requirements

Code description

Nemotron will generate the code and print/save it based on your configuration.

🤖 How It Works

The system uses:

Nemotron Code Gen Models

Custom prompt engineering

A wrapper module for clean API calls

A unified response parser to format code

📌 Example Prompt
Generate a Python function to merge two sorted arrays without using extra space.


Nemotron Output:
✔ Optimized algorithm
✔ Clean function
✔ Docstring included

🛠️ Future Enhancements

Add GUI (Streamlit) frontend

Add multi-file code generation

Add debugging mode

Integrate GitHub repository auto-commits

Add unit test generation

🤝 Contributing

Pull requests are welcome!
If you want to add new modules or improve prompt engineering, feel free to fork and submit a PR.

📄 License

MIT License © 2025 Abhishek S.
