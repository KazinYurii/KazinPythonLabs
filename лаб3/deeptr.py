from mypackage.module2 import *

print("Переклад тексту:")
print(TransLate("Привіт, як справи?", "uk", "en"))

print("\nВизначення мови:")
print(LangDetect("Привіт, як справи?", set="all"))
