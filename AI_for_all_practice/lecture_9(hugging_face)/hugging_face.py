from transformers import pipeline

# classifier=pipeline("text-classification")
# result=classifier("this movie is just mehhh")
# print(result)

def Summarizer(text):
    summarizer_pipe=pipeline("summarization")
    result=summarizer_pipe(text,min_len=10,max_len=30)
    return result

text="Artificial intelligence is rapidly transforming the way people study, work, and solve problems. In education, AI tools can help students understand difficult concepts, summarize long notes, practice coding, and receive personalized feedback. In business, AI automation can save time by handling repetitive tasks such as email replies, data entry, customer support, and report generation. However, AI should be used carefully because it can sometimes produce incorrect information, depend on biased data, or reduce human critical thinking if used blindly. Therefore, the best approach is to use AI as an assistant, not as a replacement for human effort, creativity, and decision-making."
summary=Summarizer(text)
print(summary)