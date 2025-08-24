words1 = ["it", "was", "the", "best", "day"]
words2 = [w for w in words1]
print(words2)

words3 = [w for w in words1 if w.find("e") != -1]
print(words3)
