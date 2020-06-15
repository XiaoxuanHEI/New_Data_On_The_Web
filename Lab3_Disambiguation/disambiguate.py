usage='''
  Given as command line arguments
  (1) wikidataLinks.tsv 
  (2) wikidataLabels.tsv
  (optional 2') wikidataDates.tsv
  (3) wikipedia-ambiguous.txt
  (4) the output filename'''
'''writes lines of the form
        title TAB entity
  where <title> is the title of the ambiguous
  Wikipedia article, and <entity> is the 
  wikidata entity that this article belongs to. 
  It is OK to skip articles (do not output
  anything in that case). 
  (Public skeleton code)'''

import sys
import re
from Parser import Parser
from simpleKB import SimpleKB

wikidata = None
if __name__ == "__main__":
    if len(sys.argv) is 5:
        dateFile = None
        wikipediaFile = sys.argv[3]
        outputFile = sys.argv[4]
    elif len(sys.argv) is 6:
        dateFile = sys.argv[3]
        wikipediaFile = sys.argv[4]
        outputFile = sys.argv[5]
    else:
        print(usage, file=sys.stderr)
        sys.exit(1)

    wikidata = SimpleKB(sys.argv[1], sys.argv[2], dateFile)
    
# wikidata is here an object containing 4 dictionaries:
## wikidata.links is a dictionary of type: entity -> set(entity).
##                It represents all the entities connected to a
##                given entity in the yago graph
## wikidata.labels is a dictionary of type: entity -> set(label).
##                It represents all the labels an entity can have.
## wikidata.rlabels is a dictionary of type: label -> set(entity).
##                It represents all the entities sharing a same label.
## wikidata.dates is a dictionnary of type: entity -> set(date).
##                It represents all the dates associated to an entity.

# Note that the class Page has a method Page.label(),
# which retrieves the human-readable label of the title of an 
# ambiguous Wikipedia page.

    with open(outputFile, 'w', encoding="utf-8") as output:
        for page in Parser(wikipediaFile):
            # DO NOT MODIFY THE CODE ABOVE THIS POINT
            # or you may not be evaluated (you can add imports).
        
            # YOUR CODE GOES HERE:
            output.write(page.title)
            output.write('\t')
            contents = re.split(r'[,\s.]\s*',page.content)
            contents.pop(-1)
            maxi = 0
            entites = wikidata.rlabels[page.label()]
            for e in entites:
                count = 0
                words = set()
                words.update(re.split(r'[<>()\s_,-]\s*',e))
                words.discard('')
                words.discard('and')
                words.discard('of')
                for w in words:
                    if w in contents:
                        count = count + 3
                set_label = set()
                for s in wikidata.labels[e]:
                    set_label.update(re.split(r'[(\s),.]\s*',s))
                if e in  wikidata.links:    
                    for s in wikidata.links[e]:
                        set_label.update(re.split(r'[<>()\s_]\s*',s))
                if e in  wikidata.dates:
                    for s in wikidata.dates[e]:
                        set_label.update(re.split(r'["-]\s*',s))
                set_label.discard('')
                for c in contents: 
                    for l in set_label:
                        if c == l:
                            count = count + 1
                if count > maxi:
                    maxi = count
                    entity = e
            output.write(entity)
            output.write('\n')
            #pass
