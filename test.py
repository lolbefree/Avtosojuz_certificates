"""Есть хотя бы 3 цифры
Есть хотя бы одна заглавная буква
Есть хотя бы один символ из следующего набора "!@#$%*"
Общая длина не менее 10 символов"""
import re
def count_letters(income_string):
    cleanString = re.sub('\W+', '', income_string)
    istitle = len([i for i in cleanString if i.istitle()])
    print(f"Количество заглавных символов: {istitle}")
    print(f"Количество строчных символов: {len(cleanString)-istitle}")

count_letters("Привет, Старина")