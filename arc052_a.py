import re

S = input()


result = re.sub(r"\D", "", S)
print(result)

