record = {}

pair_number = int(input())
pair = []

for i in range(pair_number * 2):
    token = input()
    pair.append(token)
    if len(pair) == 2:
        if pair[0] not in record:
            record[pair[0]] = []
        record[pair[0]].append(float(pair[1]))
        pair.clear()

new_record = {}

for k, v in record.items():
    if sum(v) / len(v) >= 4.5:
        new_record[k] = sum(v) / len(v)

ordered_record = dict(sorted(new_record.items(), key=lambda x: -x[1]))

for k, v in ordered_record.items():
    print(f"{k} -> {v:.2f}")