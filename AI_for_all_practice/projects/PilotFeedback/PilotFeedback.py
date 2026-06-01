#making a project that will analyze feedback for businesses
# it will have the following features
# 1) it will tell whether feedback is positive/negative
# 2) describe its urgency
# 3) short reply to the feedback
# 4) save it all in a csv file
import csv
import json
from openai import OpenAI
client=OpenAI()

# sample complaints/feedback
# complaints=[
#     ["riyan","food is bad"],
#     ["huma","food is slow"],
#     ["hamza","food is salty"]
# ]

# # #opening csv file and adding the feedback in it
# with open("feedback.csv", "w",newline='') as f:
#     #pass values as list so each letter is not separated by coma
#     writer=csv.writer(f)
#     writer.writerows(complaints)
            
            
# now calling the api and doing the analysis
#i will create three functions 
# one will generate the response
# the second one will save the response in csv File
# third function is the main it will loop through the feedback and call other two functions

#function to give analysis from a feedback
def Feedback_generator(feedback):
    response=client.chat.completions.create(
        model="gpt-4.1-nano",
        max_tokens=150,
        response_format={"type":"json_object"},
        messages=[
            {
                "role":"system",
                "content":"you are a feedback analyzer.Return the analysis as json object"
            },
            {
                "role":"user",
                "content":f"""
                give the feedback following this json structure strictly
                
                {{"sentiment":"Positive/negative/neutral",
                  "urgency":"give a numeric value between 0 and 10 based on how urgent the feedback is",
                  "reason":"what is the feedback,what is reason for that feedback",
                  "reply":"give suitable reply to customer based on their feedback"
                  }}
                  
                "feedback":{feedback}
                """                
            }
        
        ]
    )
    return json.loads(response.choices[0].message.content)

#Function to read feedback and save analyzed result in csv file
def Feedback_saver():
    with open("feedback.csv","r") as infile,\
    open("analyzed_feedback.csv","w",newline='') as outfile:
        headings=["person","feedback","sentiment","urgency","reason","reply"]
        reader=csv.DictReader(infile)
        #in dictwriter write file name and fieldnames
        writer=csv.DictWriter(outfile,fieldnames=headings)
        #only call writeheader function no need for writing parameters
        writer.writeheader()
        
        for row in reader:
            result=Feedback_generator(row["feedback"])
            writer.writerow({
                "person":row["person"],
                "feedback":row["feedback"],
                "sentiment":result["sentiment"],
                "urgency":result["urgency"],
                "reason":result["reason"],
                "reply":result["reply"]
                })
            
Feedback_saver()
print("successfully saved analysis")
            
                
#these are the bugs and mistakes i made
