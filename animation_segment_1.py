# import required libraries
import spacy
from spacy import displacy 
import json
import os

# initiate global variables
destinFolder = "ParaInfo/"
nlp = spacy.load('en_core_web_sm',disable=['ner','textcat'])

# define required libraries
def FinalizeOP(op):
    return op
def CleanDestinFolder():
    for x in os.listdir(destinFolder):
        os.remove(destinFolder + x)
    return
def depTag(token,OP={},parent=None):
  if token.dep_.lower() == "root":
    OP["Action"] = {"Name":token.text}
  if "sub" in token.dep_.lower():
    try:
      compound = [children.text for children in token.children if children.dep_.lower() == "compound"][0]
      OP["Subject"] = {"Name":compound + " " + token.text}
    except IndexError :
      OP["Subject"] = {"Name":token.text}
  if token.dep_.lower() == "amod" or token.pos_.lower()=="adj":
    if "sub" in parent.dep_.lower():
      if "Attribute" not in OP["Subject"].keys():
        OP["Subject"]["Attribute"] = token.text
      else:
        OP["Subject"]["Attribute"] += ', ' +  token.text
    elif "obj" in parent.dep_.lower():
      if "Attribute" not in OP["Object"].keys():
        OP["Object"]["Attribute"] = token.text
      else:
        OP["Object"]["Attribute"] += ', ' +  token.text
  if "obj" in token.dep_.lower():
    try:
      compound = [children.text for children in token.children if children.dep_.lower() == "compound"][0]
      OP["Object"] = {"Name":compound + " " + token.text}
    except IndexError :
      OP["Object"] = {"Name":token.text}
  if token.dep_.lower() == "prep" and parent.pos_.lower()=="verb":
    OP["Action"]["Relation"] =  token.text
  for children in token.children:
    depTag(children,OP,token)
  return 

if __name__ == "__main__":
    # -- Clear the destin folder for new inputs
    print("\nClearing Destination Folder .....")
    CleanDestinFolder()
    Paragraph = input("Enter the script in 'Simple Sentence' here -- > ")
    Lines = [x.strip() for x in Paragraph.split(".") if len(x) != 0]

    for i in range(len(Lines)):
        line = Lines[i]
        TokenizedLine = nlp(line)
        for token in TokenizedLine:
            if token.dep_.lower() == "root":
                op = {}
                depTag(token,op)
                break
        op = FinalizeOP(op)
        JsonOutput = json.dumps(op, indent = 4)
        print(line)
        print(JsonOutput)

        # Writing to sample.json
        with open(destinFolder + str(i) + ".json", "w") as outfile:
            outfile.write(JsonOutput)
        print("----------\n")

