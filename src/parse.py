from sys import argv, stderr, settrace
from bllipparser import RerankingParser


settrace
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

    print('Opening input file...')
    ifile = open(argv[1])
    print('Opening output file...')
    ofile = open(argv[2],"w")
    
    print('Starting parsing...')
    # Read input sentences from ifile and print parse trees to ofile.
    skippedLines = 0
    for i, line in enumerate(ifile):
        print('> Parsing line',line)
        if len(line.strip('\n')) == 0:
            continue
        if skippedLines >= 10:
            break
        #print(rrp.simple_parse(line.strip('\n')), file=ofile)
        print(rrp.simple_parse(line.strip('\n')))
        skippedLines += 1
