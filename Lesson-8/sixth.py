# Напишите шаблон регулярного выражения, который соответствует вопросительным
# предложениям, в которых одно слово (более 2 символов) повторяется 4 или более раз

import re

pattern = r'.*([a-zA-Z]{2,}\s)\1{3,}.*?\??'
sentence = 'hey hey hey hey?'
match = re.fullmatch(pattern, sentence)
print('YES' if match else 'NO')
