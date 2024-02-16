import sys

def read_dataset(file):
    data = {}
    with open(file, 'r') as f:
        next(f)
        for line in f:
            line = line.strip().split(',')
            data[line[0]] = line[1:]
    return data

def sports(data):
    return sorted(set([v[7] for v in data.values()]))

def percentage(data):
    apt = sum([1 for v in data.values() if v[11] == 'true'])
    inapt = sum([1 for v in data.values() if v[11] == 'false'])
    total = len(data)
    return (apt/total*100, inapt/total*100)

def age_distribution(data):
    ages = [0] * 9
    for v in data.values():
        age = int(v[4])
        if age < 5:
            ages[0] += 1
        elif age < 10:
            ages[1] += 1
        elif age < 15:
            ages[2] += 1
        elif age < 20:
            ages[3] += 1
        elif age < 25:
            ages[4] += 1
        elif age < 30:
            ages[5] += 1
        elif age < 35:
            ages[6] += 1
        elif age < 40:
            ages[7] += 1
        else:
            ages[8] += 1
    return ages


data = read_dataset(sys.argv[1])
print("Lista ordenada alfabeticamente das modalidades desportivas:")
print(sports(data))
print("\nPercentagens de atletas aptos e inaptos para a prática desportiva:")
print(percentage(data))
print("\nDistribuição de atletas por escalão etário:")
print(age_distribution(data))

