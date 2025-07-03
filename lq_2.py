"""這支程式邏輯題目2"""

from collections import Counter

text = "Hello welcome to Cathay 60th year anniversary"

# 統一轉大寫來統計(大小寫合併，數字保留)
normalized_chars = [char.upper() for char in text if char.isalnum()]

char_count = Counter(normalized_chars)

for char in sorted(char_count):
    print(f"{char}: {char_count[char]}")

