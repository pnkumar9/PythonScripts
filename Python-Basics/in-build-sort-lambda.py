#!/usr/binenv python3.6

from audioop import reverse


def sort_list_names(arr):
    print({f" before sorting: {arr} "})
    arr1 = arr
    arr1.sort(key=None, reverse=False)
    print({f"Regulars sort based on first name {arr1}"})
    arr2 = arr
    arr2.sort(key=lambda x: x.split()[-1], reverse=True)
    print({f"sort based on last name: {arr2}"})

def sort_list_of_tuples(arr):
    arr1=arr
    arr1.sort(key=None, reverse=False)
    print({f"regulasr sort: {arr1}"})

arr = ["Kumar Pera", "Wahn Stuss", "Hul Zoro", "Bill Hunter"]
sort_list_names(arr)    

arr = [('Steve', 35), ('Karen', 25), ('Gerald', 58), ('Jo', 72)]
sort_list_of_tuples(arr)   