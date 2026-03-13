dick = {
    "a": 0,
    "b": 0,
    "n": 0,

}
texto = "banana"
for s in texto:
    if (s == "a"):
        dick["a"] += 1
    elif (s == "b"):
        dick["b"] += 1
    else:
        dick["n"] += 1
print(dick)
