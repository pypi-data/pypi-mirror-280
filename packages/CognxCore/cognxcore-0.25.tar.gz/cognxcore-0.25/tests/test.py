from cogni import CogniCore as cc


api_key = input("Enter your API key: ")

ai = cc(api_key)

prompt = input("Enter your prompt: ")
response = ai.generate_content(prompt)
print(response)
