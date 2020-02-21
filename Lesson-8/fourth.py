# Напишите шаблон регулярного выражения, который соответствовал бы следующему формату
# времени: YYYY-MM-DDThh:mm:ss±hh:mm (ISO формат)
import re

date = "2005-08-09T18:31:42+03:30"
pattern = r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}'
match = re.fullmatch(pattern, date)
print('YES' if match else 'NO')