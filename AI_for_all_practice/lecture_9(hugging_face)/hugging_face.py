# Generator=pipeline(
#     "text-generation",
#     model="Qwen/Qwen3-0.6B"
# )
from transformers import pipeline
import csv

classifier=pipeline("text-classification",
                    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
)

def Classification(text):
    result=classifier(text)
    return result[0]["label"],result[0]["score"]

def Analysis(file):
    with open(file,"r") as infile, \
    open("analysis.csv","w",newline="") as outfile:
        writer=csv.writer(outfile)
        writer.writerow(["line","label","score"])
        for lines in infile:
            lines=lines.strip()
            if not lines:
                continue
            label,score =Classification(lines)
            writer.writerow([lines,label,score])

 
file="classification_data.txt"           
Analysis(file)

#mistake:
# csv writer writer.writerow() takes list as input