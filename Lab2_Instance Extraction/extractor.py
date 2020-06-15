'''Extracts type facts from a wikipedia file
usage: extractor.py wikipedia.txt output.txt

Every line of output.txt contains a fact of the form
    <title> TAB <type>
where <title> is the title of the Wikipedia page, and
<type> is a simple noun (excluding abstract types like
sort, kind, part, form, type, number, ...).

Note: the formatting of the output is already taken care of
by our template, you just have to complete the function
extractType below.

If you do not know the type of an entity, skip the article.
(Public skeleton code)'''

from Parser import Parser
import sys
import re
import nltk

if len(sys.argv) != 3:
    print(__doc__)
    sys.exit(-1)

def extractType(content):
    # Code goes here
    searchObj1 = re.search( r'(.*) (is|was) (a|the) (name|type|kind|study) of (.*?).*', content, re.M|re.I)
    searchObj2 = re.search( r'(.*) (is|was|are) (a|an) (.*)', content, re.M|re.I)
    # searchObj2 = re.search( r'(.*) is the (.*?) .*', content, re.M|re.I)
    
    if searchObj1:
        # tokens = nltk.word_tokenize(searchObj1.group(5))
        # pos_tags = nltk.pos_tag(tokens)
        # for word,pos in pos_tags:
        #     if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'): 
        return searchObj1.group(5)
    elif searchObj2:
        tokens = nltk.word_tokenize(searchObj2.group(4))
        pos_tags = nltk.pos_tag(tokens)
        for i in range(len(pos_tags)):
            if i == len(pos_tags)-1:
                return pos_tags[i][0]
            elif ((pos_tags[i][1] == 'NN' or pos_tags[i][1] == 'NNP' or pos_tags[i][1] == 'NNS' or pos_tags[i][1] == 'NNPS')
                and (pos_tags[i+1][1] != 'NN' and pos_tags[i+1][1] != 'NNP' and pos_tags[i+1][1] != 'NNS' and pos_tags[i+1][1] != 'NNPS') 
                and  pos_tags[i+1][1] != 'POS'): 
                return pos_tags[i][0]
    else:
        return None

        
        

with open(sys.argv[2], 'w', encoding="utf-8") as output:
    for page in Parser(sys.argv[1]):
        typ = extractType(page.content)
        if typ:
            output.write(page.title + "\t" + typ + "\n")



