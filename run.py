#!/usr/bin/env python3
"""
Created on May 4 2020

@author: Joan Hérisson
@description: Galaxy script to query rpReader REST service

"""
import sys
sys.path.insert(0, '/home/rpReader')
from rpReader import entrypoint as rpReader_entrypoint


if __name__ == "__main__":
    rpReader_entrypoint(sys.argv[1:]+['-sm', 'db'])
