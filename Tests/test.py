import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer
import re
from googlesearch import search


#tokenize and parsing a file
file_content = open("test1.txt",encoding = "utf8").read()
final = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in file_content.split("\n")]
tokens = nltk.word_tokenize(file_content)
#print (tokens)

Selected = 20
print (tokens[0:Selected])

query = TreebankWordDetokenizer().detokenize(tokens[0:Selected])

my_results_list = []
for i in search(query,        # The query you want to run
                tld = 'com',  # The top level domain
                lang = 'en',  # The language
                num = 10,     # Number of results per page
                start = 0,    # First result to retrieve
                stop = 10,    # Number of links to retrieve
                pause = 2.0,  # Lapse between HTTP requests
               ):
    my_results_list.append(i)
    print(i)





