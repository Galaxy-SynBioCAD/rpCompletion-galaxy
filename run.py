#!/usr/bin/env python3
"""
Created on May 4 2020

@author: Joan Hérisson
@description: Galaxy script to query rpReader service

"""
from sys import path as sys_path
sys_path.insert(0, '/home/rpReader')
from rpReader import build_parser as tool_buildparser
from rpReader import entrypoint as tool_entrypoint
from tarfile import open as tarfile_open
from tarfile import TarInfo as tarfile_TarInfo
from tempfile import TemporaryDirectory as tempfile_tempdir
from os import listdir as os_listdir



if __name__ == "__main__":
    parser = tool_buildparser()
    params = parser.parse_args()

    with tempfile_tempdir() as tmpdirname:
        args = [
            '-rp2paths_compounds', params.rp2paths_compounds,
            '-rp2_pathways', params.rp2_pathways,
            '-rp2paths_pathways', params.rp2paths_pathways,
            '-output', tmpdirname,
            '-sm', 'db'
            ]
        tool_entrypoint(args)
        with tarfile_open(params.output, mode='w:xz') as tf:
            for name in os_listdir(tmpdirname):
                tf.add(tmpdirname+"/"+name, arcname=name)
