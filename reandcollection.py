import re
from collections import Counter

text = "i love python.i am python intrested to learn python"

words = re.findall(r'\b\w+\b',text.lower())

count = Counter(words)

pythonCount = count['python']
print(pythonCount)