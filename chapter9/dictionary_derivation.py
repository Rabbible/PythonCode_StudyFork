# coding=utf-8
# code file: chapter9/dictionary_derivation.py

input_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}

output_dict = {k: v for k, v in input_dict.items() if v % 2 == 0}
# input cannot use dictionary directly, you can use the iterm() skill to realize, dictionary is not sequence
print(output_dict)

keys = [k for k, v in input_dict.items() if v % 2 == 0]
print(keys)
