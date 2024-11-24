from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

def TransLate(text: str, scr: str, dest: str) -> str:
    """Функція перекладу тексту."""
    try:
        return GoogleTranslator(source=scr, target=dest).translate(text)
    except Exception as e:
        return f"Error: {str(e)}"

def LangDetect(text: str, set: str = "all") -> str:
    """Функція визначення мови."""
    try:
        lang = detect(text)
        if set == "lang":
            return lang
        elif set == "confidence":
            return "Confidence score not available"
        else:
            return f"{lang}, Confidence not available"
    except Exception as e:
        return f"Error: {str(e)}"
