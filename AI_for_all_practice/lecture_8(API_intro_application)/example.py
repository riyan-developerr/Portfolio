# time for sentiment analysis
#importing openai library(framework api)
from openai import OpenAI
# setting up client
client=OpenAI() #no need for api key setup because already set in envirnment

def sentiment_analysis(text):
    response=client.responses.create(
        model="gpt-4.1-mini",
        input=f"""
        you are a sentiment analyst.I will give you a text and you will tell whether 
        it is a positive or negative sentiment.
        constraints:reply in one word positive/negative
        if you do not understand the sentiment then try in which category the is most likely to fall
        and even after that you do not find conclusion then say "i do not understand".
        The following is the text:
        {text}
        """,
        max_output_tokens=16,
        temperature=0
    )
    print(response.usage)
    return (response.output_text)

text="Am i looking pretty today?"
sentiment=sentiment_analysis(text)
print(f"Text: {text} \n The sentiment is: {sentiment}")