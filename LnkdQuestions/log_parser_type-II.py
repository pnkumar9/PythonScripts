from collections import defaultdict
import re
import pandas as pd

output = defaultdict(int)
regex = re.compile(r'^(\w+ \d+ \d+:\d+):\d+ \w+ (\w+).*$')

column_names = ['minute', 'total_count']
output_list = []
columns = set()


def update_list(record):
    record_found = False 
    columns.add(record[1])
    for each_rec in output_list:
        if each_rec['minute'] == record[0]:
            record_found = True
            each_rec['total_count'] += 1
            if record[1] in each_rec.keys():
                each_rec[record[1]] += 1
            else:
                each_rec[record[1]] = 1
        else:
            each_rec[record[1]] = 0
    if not record_found:
        new_rec = {'minute': record[0],
                   'total_count': 1,
                   record[1]: 1
                   }
        for col in columns:
            if col not in new_rec.keys():
                new_rec[col] = 0
        output_list.append(new_rec)


with open("/Users/kumarp/Documents/Kumar-docs/PythonScripts/log-file.log", "r+") as myfile:
    for log_line in myfile:
        match = regex.match(log_line)
        if match:
            if match.group(1) and match.group(2):
                record = match.groups()
                update_list(record)
            else:
                print(f"Parsing line partically succeeded: {log_line}")
        else:
            print(f"ERROR: Malformed logline {log_line}")

df = pd.DataFrame(output_list)
print(df.to_string())
df.to_csv("/Users/kumarp/Documents/Kumar-docs/PythonScripts/counts-type2.txt", sep=',', index=False)
