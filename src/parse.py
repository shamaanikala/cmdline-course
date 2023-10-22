from sys import argv, stderr
from bllipparser import RerankingParser


if __name__=="__main__":
    """
        Parse an English Gutenberg book in sentence per line format
        using bllipparser. Write string representations of parse trees
        to the output file.
    """
    if len(argv) != 3:
        print("USAGE %s inputfile outputfile" % argv[0], file=stderr)
        exit(1)

    # Initialize parser and download parser model if needed.
    rrp = RerankingParser.fetch_and_load('WSJ-PTB3', verbose=True)

    ifile = open(argv[1])
    ofile = open(argv[2],"w")
    
    # Read input sentences from ifile and print parse trees to ofile.
    parsedLines = 0
    for i, line in enumerate(ifile):
        if len(line.strip('\n')) == 0:
            continue
        if parsedLines >= 10:
            break
        try:
            print(rrp.simple_parse(line.strip('\n')), file=ofile)
        except IndexError: # there is something wrong with the parsed sentence
            print('Unable to parse sentence:')
            print(line)
            print('skipping...')
            continue
        parsedLines += 1
