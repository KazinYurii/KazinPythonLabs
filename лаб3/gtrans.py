from mypackage.module1 import *

print("Переклад тексту:")
print(TransLate("Привіт, як справи?", "uk", "en"))

print("\nВизначення мови:")
print(LangDetect("Привіт, як справи?", set="all"))

print("\nКоди мов:")
print(CodeLang("uk"))
print(CodeLang("Ukrainian"))

print("\nСписок мов:")
LanguageList("screen", "Добрий день")
