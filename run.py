#!/usr/bin/env python3
"""
Created on May 4 2020

@author: Joan Hérisson
@description: Galaxy script to query rpReader REST service

"""
from sys import path as sys_path
sys_path.insert(0, '/home/rpReader')
from rpReader import build_parser as rpReader_buildparser
from rpReader import entrypoint as rpReader_entrypoint
from tarfile import open as tarfile_open
from tempfile import TemporaryDirectory as tempfile_tempdir
from os import path as os_path



if __name__ == "__main__":
    parser = rpReader_buildparser()
    params = parser.parse_args()

    with tempfile_tempdir() as tmpdirname:
        args = [
            '-rp2paths_compounds', params.rp2paths_compounds,
            '-rp2_pathways', params.rp2_pathways,
            '-rp2paths_pathways', params.rp2paths_pathways,
            '-output', tmpdirname,
            '-sm', 'db'
            ]
        rpReader_entrypoint(args)
        with tarfile_open(fileobj=params.output, mode='w:xz') as tf:
            tf.add(tmpdirname, arcname=os_path.basename(params.output))
