#!/usr/bin/env python3.6

def lexicographical_order(arr):

    op_dict = {}
    for word in arr:

        key,value = word.strip().split()
        count = 1
        if key not in op_dict:
            #"key1:3,hello"
            op_dict[key] = [key,count,value]
            #print(f"key not in dict so add: {value}")
        else:
            key, count, value_string = op_dict[key]
            #print(f"key already exist compare: {value} {value_string}")
            #print(len(value), len(value_string))
            if str(value) < str(value_string):
                #print(f"compare done: {value} {value_string}")
                value = value_string
                #print(f"winner strin is: {value}")
            count += 1
            op_dict[key] = [key,count,value]

    for key in op_dict:
        key, count, value = op_dict[key]
        op_dict[key] = f"{key}:{count},{value}"
        
    print(list(op_dict.values()))


lexicographical_order(["key1 abcd","key2 zzz","key1 hello","key3 world","key1 hello"])