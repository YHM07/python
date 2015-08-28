#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# function programming

from functools import reduce

def even_filter(nums):
    return filter(lambda x: x % 2 == 0, nums)

def multiply_by_three(nums):
    return map(lambda x : x * 3, nums)

def convert_to_string(nums):
    return map(lambda x: 'The Number: {0}'.format(x), nums)


def pipeline_func(data, fns):
    return reduce(lambda a,x:x(a),fns, data)

nums = range(0,11)
r = pipeline_func(nums, [even_filter,
                    multiply_by_three,
                    convert_to_string])

print(list(r))

