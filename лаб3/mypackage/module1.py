from googletrans import Translator, LANGUAGES

translator = Translator()

def TransLate(text: str, scr: str, dest: str) -> str:
    """Функція перекладу тексту."""
    try:
        result = translator.translate(text, src=scr, dest=dest)
        return result.text
    except Exception as e:
        return f"Error: {str(e)}"

def LangDetect(text: str, set: str = "all") -> str:
    """Функція визначення мови."""
    try:
        detection = translator.detect(text)
        if set == "lang":
            return detection.lang
        elif set == "confidence":
            return "Confidence score not available"
        else:
            return f"{detection.lang}, Confidence not available"
    except Exception as e:
        return f"Error: {str(e)}"

def CodeLang(lang: str) -> str:
    """Функція для отримання назви або коду мови."""
    try:
        for code, name in LANGUAGES.items():
            if lang.lower() == name.lower():
                return code
            elif lang.lower() == code:
                return name
        return "Error: Language not found."
    except Exception as e:
        return f"Error: {str(e)}"

def LanguageList(out: str = "screen", text: str = None) -> str:
    """Функція створення таблиці мов."""
    try:
        rows = []
        for idx, (code, name) in enumerate(LANGUAGES.items(), start=1):
            translated_text = TransLate(text, "auto", code) if text else ""
            rows.append(f"{idx:<3} {name:<15} {code:<10} {translated_text}")

        header = f"{'N':<3} {'Language':<15} {'ISO-639 code':<10} {'Text'}"
        table = "\n".join([header, "-" * len(header)] + rows)

        if out == "screen":
            print(table)
        elif out == "file":
            with open("languages.txt", "w", encoding="utf-8") as f:
                f.write(table)
        return "Ok"
    except Exception as e:
        return f"Error: {str(e)}"
