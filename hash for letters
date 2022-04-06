#Code for the maximum number of letters repeated one after another in string
x = 'hello lllee lhhhhehh'
y = [x[j] for j in range(len(x))]
z = list(set(y))
z.sort()
F = dict()
count_letter = []
for i in range(len(z)):
    F[z[i]] = 0
for unique_letter in F.keys():
    count = 0
    for i in range(len(y)):
        if y[i] == unique_letter:
            count += 1
            count_letter.append(count)
        else:
            count = 0
    F[unique_letter] = max(count_letter)
    count_letter = []
F

#Code for the number of letters in string
x = 'hello my friends'
y = [x[j] for j in range(len(x))]
z = list(set(y))
z.sort()
F = dict()
for i in range(len(z)):
    F[z[i]] = y.count(z[i])
F
