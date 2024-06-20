"""
quantumdiceware.py
Diceware passphrases generated from quantum random data.
http://github.com/justinsloan/qdg

Requires Python 3.6 or better

##########################################################################
# PUBLIC DOMAIN RELEASE                                                                 #
##########################################################################
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>
##########################################################################

Features:
    - Simulates dice rolls by gathering quantum data.
    - Includes the complete standard Diceware wordlist.
    - Generate passphrases from custom wordlists.

Usage:
    >>> $ pip3 install quantumdiceware
    >>> $ qdg
    >>> $ qdg -c 6 > output.txt

Version History:
0.3.0 - 10 APRIL 2022
 - code optimization
 - use a custom character between words with '--char' option
 - TODO: defaults to local if quantum data unavailable
 - added --pre-text option
 - added --post-text option
 - TODO: arbitrary random data for texting options

0.1.9 - 6 JAN 2018
- added '--version' option
- improved verbose mode printing
- updated documentation, switched to .rst format

0.1.8 - 5 JAN 2018
- first release build
"""

__version__ = "0.3.0"
__date__ = "10 APRIL 2022"
__author__ = "Justin M. Sloan"

import random
import argparse
import time
import quantumrandom
import pkg_resources

# Specify the location of the word list inside the package
RESOURCE_NAME = __name__
PATH = "diceware_word_list.txt"
WORD_LIST_FILE = pkg_resources.resource_filename(RESOURCE_NAME, PATH)

# Build the argument parser
parser = argparse.ArgumentParser(
    description="Generate Diceware passphrases using quantum data.",
    epilog=f"QDG v.{__version__} | by {__author__}")
parser.add_argument("-c", "--count", nargs="?", default=1, type=int, help="number of passphrases to generate")
parser.add_argument("-w", "--words", nargs="?", default=6, type=int, help="number of words per passphrase")
parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
parser.add_argument("-l", "--local", action="store_true", help="use local random data, no connection required (faster)")
parser.add_argument("-f", "--file", nargs="?", default=WORD_LIST_FILE, help="specify the word list to use")
parser.add_argument("--char", action="store", default=" ", type=str, help="set the character between words")
parser.add_argument("--pretext", action="store", default="", type=str, help="specify text to appear before the passphrase")
parser.add_argument("--posttext", action="store", default="", type=str, help="specify text to appear after the passphrase")
parser.add_argument("--version", action="version", version=f"QDG v.{__version__}, {__date__}")
args = parser.parse_args()

# Set the mode options
VERBOSE = bool(args.verbose) # Sets VERBOSE to True if arg is provided, False if not
LOCAL = bool(args.local)



# Load the standard wordlist file
WORD_DICT = {}
with open(args.file) as f:
    for line in f.readlines():
        index, word = line.strip().split('\t')
        WORD_DICT[int(index)] = word


def p_verbose(text):
    """Print function for verbose mode."""
    if VERBOSE:
        print(text)


def generate_diceware_phrase(word_count=6, local=False, char=" ", pre="", post=""):
    """Generates a Diceware Passphrase of length N."""
    phrase_words = []

    p_verbose("Gathering quantum data...")
    data_count = word_count * 5
    quantum_data = quantumrandom.uint16(data_count)
    dice = int("".join([str(y) for y in (quantum_data % 6) + 1]))
    roll = [str(dice)[i:i+5] for i in range(0, len(str(dice)), 5)]
    for i in roll:
        p_verbose(f"Dice Rolls: {i}")
        phrase_words.append(WORD_DICT[int(i)])

    passphrase = pre + char.join(phrase_words) + post
    return passphrase


def main():
    """Takes optional arguments and prints passphrases."""
    # Get the time so we can calculate how long it takes
    start_time = time.time()

    # Loop until requested number of passphrases are generated
    for i in range(0, args.count):
        phrase = generate_diceware_phrase(args.words, LOCAL, str(args.char), str(args.pretext), str(args.posttext))
        print(phrase)

    # Calculate how long it took and print if Verbose mode is on
    p_verbose(f"--- {time.time() - start_time} seconds ---")
