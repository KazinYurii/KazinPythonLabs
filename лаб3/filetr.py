import os
from mypackage.module1 import TransLate, LangDetect

def process_file(config_file: str):
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config = dict(line.strip().split('=') for line in f if '=' in line)

        text_file = config["file"]
        dest_lang = config["language"]
        output = config["output"]
        max_chars = int(config["max_chars"])

        if not os.path.exists(text_file):
            print(f"Error: File {text_file} does not exist.")
            return

        with open(text_file, 'r', encoding='utf-8') as f:
            text = f.read()

        print(f"File: {text_file}")
        print(f"Detected Language: {LangDetect(text, set='lang')}")
        print(f"Text Size: {len(text)} characters")

        text_to_translate = text[:max_chars] if len(text) > max_chars else text

        translated_text = TransLate(text_to_translate, "auto", dest_lang)

        if output == "screen":
            print(f"Translated Text:\n{translated_text}")
        elif output == "file":
            output_file = f"{text_file.split('.')[0]}_{dest_lang}.txt"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(translated_text)
            print(f"Translation saved to {output_file}")
    except Exception as e:
        print(f"Error: {str(e)}")

process_file("config.txt")
