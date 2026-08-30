jumin = "990101-1234567"
card = "1234-5678-9012-3456"

l_card = len(card)

hide_j = jumin[:8] + '*' *6
hide_c = '*' * 15 + card[-4:]

print(hide_j)
print(len(jumin),len(hide_j))
print(hide_c)