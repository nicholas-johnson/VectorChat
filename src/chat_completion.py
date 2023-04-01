import openai

def chat_completion(convo):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": convo}])
    answer = completion.choices[0].message.content
    print(answer)
    return answer