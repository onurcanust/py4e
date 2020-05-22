counts = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen"]
for name in names :
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)

P: > {'csev': 2, 'cwen': 2, 'zqian': 1}

--

counts = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen"]
for name in names :
    counts[name] = counts.get(name, 0) + 1
#0 Meaning this is the value I get back if the key doesn't exist
print(counts)

P: > {'csev': 2, 'cwen': 2, 'zqian': 1}
