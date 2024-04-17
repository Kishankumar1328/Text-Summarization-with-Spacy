import spacy
import pytextrank
nlp=spacy.load("en_core_web_lg")
nlp.add_pipe("textrank")

text=input("Enter the Paragraph:")

print("Original Paragraph Size:",len(text))
doc=nlp(text)

for send in doc._.textrank.summary(limit_phrases=2,limit_sentences=2):
  print(send)
  print("Summary Length:",len(send))

