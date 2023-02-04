#!/usr/bin/env python3

import argparse
from typing import List, Optional

import code_files.alf.hashes


def main(args: Optional[List[str]] = None) -> None:
    """
    Main function
    """
    parser = argparse.ArgumentParser(
        description='Hash a string using the ALF hash function.')

    parser.add_argument('string', nargs='?',
        help="the string to hash. It's a good idea to surround it in quotes (preferably single-quotes) so the shell doesn't eat special characters.")

    parsed_args = parser.parse_args(args)

    if parsed_args.string is None:
        print('(Use Ctrl+C or Ctrl+D to exit)')
        while True:
            hash = code_files.alf.hashes.hash(input('> '))
            print(f'{hash:08x}')
    else:
        hash = code_files.alf.hashes.hash(parsed_args.string)
        print(f'{hash:08x}')


if __name__ == '__main__':
    main()
