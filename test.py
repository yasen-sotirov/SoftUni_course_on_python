import re

txt = "The rain in Spain"
x = re.sub("\s", "--", txt)
print(x)