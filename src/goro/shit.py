'''
Created on 26/02/2018

@author: 

XXX:
'''

import logging
from itertools import starmap
from sys import stdin

nivel_log = logging.ERROR
nivel_log = logging.DEBUG
logger_cagada = None

def goro_shit_core(nums):
    nums_ord = sorted(nums)
    diff = sum(starmap(lambda x, y:x != y, zip(nums, nums_ord)))
    return diff

def caca_comun_lee_linea_como_num():
    return int(stdin.readline().strip())

def caca_comun_lee_linea_como_monton_de_numeros():
    return list(map(int, stdin.readline().strip().split(" ")))

def goro_shit_main():
    cacasos = caca_comun_lee_linea_como_num()
    for c in range(cacasos):
        _ = caca_comun_lee_linea_como_num()
        nums = caca_comun_lee_linea_como_monton_de_numeros()
        ass = goro_shit_core(nums)
        print("Case #{}: {}".format(c + 1, ass))
if __name__ == '__main__':
        FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
        logging.basicConfig(level=nivel_log, format=FORMAT)
        logger_cagada = logging.getLogger("asa")
        logger_cagada.setLevel(nivel_log)
        goro_shit_main()
