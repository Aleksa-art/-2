s1 = "abc"
s2 = "def"
s3 = "ghi"

combinations = [a + b + c for a in s1 for b in s2 for c in s3]
print(combinations)

