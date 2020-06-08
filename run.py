#!/usr/bin/env python3
"""
Created on May 29 2020

@author: Joan Hérisson
@description: Galaxy script to query rpCompletion service

"""
from sys import path as sys_path
sys_path.insert(0, '/home/src')
from main import build_parser as tool_buildparser
from main import entrypoint as tool_entrypoint
from tarfile import open as tarfile_open
from tarfile import TarInfo as tarfile_TarInfo
from tempfile import TemporaryDirectory as tempfile_tempdir
from os import listdir as os_listdir


if __name__ == "__main__":

    # Parse arguments with the tool parser
    parser = tool_buildparser()
    params = parser.parse_args()

    # Process in a temporary folder that will be automatically removed after exit
    with tempfile_tempdir() as tmpdirname:

        # Prepare arguments for the tool
        args = [
            '-rp2paths_compounds', params.rp2paths_compounds,
            '-rp2_pathways', params.rp2_pathways,
            '-rp2paths_pathways', params.rp2paths_pathways,
            '-output', tmpdirname,
            '-sm', 'db'
            ]

        # Run the tool
        tool_entrypoint(args)

        # Format ouput data as expected by the wrapper
        with tarfile_open(params.output, mode='w:gz') as tf:
            for name in os_listdir(tmpdirname):
                tf.add(tmpdirname, arcname='Galaxy-'+'['+']')
