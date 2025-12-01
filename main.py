import os
from dotenv import load_dotenv
from openai import OpenAI

from modules.code_style_adaptor import build_adaptive_prompt
from modules.code_intelligent_report import build_cir_prompt
from modules.bug_replay_engine import build_bug_replay_prompt
from modules.multiline_read import read_multiline_input

load_dotenv()
API_KEY = os.getenv("NVIDIA_API_KEY")

if not API_KEY:
    raise ValueError("❌ ERROR: NVIDIA_API_KEY not found in .env file!")

role = """
You are a great coder.
You can code any program in any language and you can fix the error or bug in the code.
You must TRACEOUT THE PROGRAM and provide the ALGORITHM.
Explain the code based on the user's level.
Explain how to run the program on Windows, Linux, Unix, iOS.
Inform the user about required installations.
"""

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=API_KEY
)

option = input("Enter the purpose (Generate code / Debugging / CIR / Replay): ").lower()

if option == "generate code":
    code_name = input("Enter the program name you want to execute: ")
    code_lang = input("Enter the language: ")
    code_lvl = input("Enter learner level (noob, beginner, intermediate, expert): ")

    base_prompt = f"""
    context={role}
    Generate the program {code_name} in {code_lang}.
    TRACEOUT the program.
    Provide the ALGORITHM.
    Explain execution steps for Windows, Linux, Unix, iOS.
    Inform about required installations.
    """

    final_prompt = build_adaptive_prompt(base_prompt, code_lvl)
    output_filename = "output_generate.txt"

elif option == "debugging":
    code_lvl = input("Enter learner level (noob, beginner, intermediate, expert): ")
    mode = input("Paste code or give file path? (paste/file): ").lower()

    if mode == "file":
        file_path = input("Enter file path: ")
        with open(file_path, "r", encoding="utf-8") as f:
            buggy_code = f.read()
    else:
        buggy_code = read_multiline_input()

    base_prompt = f"""
    context={role}
    Debug the following code:
    {buggy_code}
    Provide fixed code, explain the bug, ALGORITHM, TRACEOUT, and step-by-step fixing instructions.
    """

    final_prompt = build_adaptive_prompt(base_prompt, code_lvl)
    output_filename = "output_generate.txt"

elif option == "cir":
    mode = input("Paste code or give file path? (paste/file): ").lower()

    if mode == "file":
        file_path = input("Enter file path: ")
        with open(file_path, "r", encoding="utf-8") as f:
            generated_code = f.read()
    else:
        generated_code = read_multiline_input()

    final_prompt = build_cir_prompt(generated_code)
    output_filename = "output_generate.txt"


elif option == "replay":
    mode = input("Paste code or give file path? (paste/file): ").lower()

    if mode == "file":
        file_path = input("Enter file path: ")
        with open(file_path, "r", encoding="utf-8") as f:
            buggy_code = f.read()
    else:
        buggy_code = read_multiline_input()

    final_prompt = build_bug_replay_prompt(buggy_code)
    output_filename = "output_generate.txt"

else:
    print("❌ Invalid option.")
    exit()

response = client.chat.completions.create(
    model="meta/llama-3.1-70b-instruct",
    messages=[{"role": "user", "content": final_prompt}],
)

result = response.choices[0].message.content

print("\n======================== OUTPUT ========================\n")
print(result)

save = input("\nDo you want to save the output to a file? (yes/no): ").lower()

if save == "yes":
    custom_name = input("Enter file name or press ENTER to use default: ").strip()
    filename = custom_name if custom_name else output_filename

    with open(filename, "w", encoding="utf-8") as f:
        f.write(result)

    print("Output saved to", filename)

else:
    print("Output not saved.")