import unicodedata


codes = ((0, 52037),
(6, 52081),
(5, 52063),
(1, 52077),
(9, 52077),
(10, 52080),
(4, 52046),
(3, 52066),
(8, 52085),
(7, 52081),
(2, 52077),
(11, 52066))

result = ''
print(sorted(codes))
for k, v in sorted(codes):
  result = result + chr(v - 0xCafe, end="")
print (result)