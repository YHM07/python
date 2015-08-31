#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'


from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task {0} ({1})'.format(name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end   = time.time()
    print('Task {0} {1:.2} seconds'.format(name, end-start))
    return 'done {0}'.format(name)

if __name__ == '__main__':
    print('Parent process {0} is running'.format(os.getpid()))
    p = Pool(4)
    result = []
    for i in range(5):
        result.append(p.apply_async(long_time_task, (i,)))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done')
    # print(result)
    for res in result:
        print(res.get())

import subprocess
print('nslookup www.python.org')
res = subprocess.call(['nslookup','www.python.org'])
print('Exit code:{0}'.format(res))

print('$ nslookup')
p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code {0}'.format(p.returncode))


