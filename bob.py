#!/usr/bin/env python3

import openai
import os

os.system('cls' if os.name == 'nt' else 'clear')
print("""\033[0;35m
.-. .-')              .-. .-')   
\  ( OO )             \  ( OO )  
 ;-----.\  .-'),-----. ;-----.\  
 | .-.  | ( OO'  .-.  '| .-.  |  
 | '-' /_)/   |  | |  || '-' /_) 
 | .-. `. \_) |  |\|  || .-. `.  
 | |  \  |  \ |  | |  || |  \  | 
 | '--'  /   `'  '-'  '| '--'  / 
 `------'      `-----' `------'  


-=Awis=- 7.3.23\n""")
openai.api_key = "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"
role = "Your name is Bob, you are a professional programmer and cyber security specialist, your passion is C/C++ and UNIX, but you know very well everything about PCs. use emoji and be funny. Helpful, and give a long and answers full of grumpy and super sarcastic black humor with punchs and try to explain them in a way they will be helpful for student of Ecole 42. Also love to chat to any other topic. Feel free to format your answer with MD and use tables"
memory_bank = [{"role": "system", "content": role}]
question = ""
def ask_bob(question):
    memory_bank.append({"role": "user", "content": question})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301", max_tokens=1400, temperature=0.4,
        messages = memory_bank)
    memory_bank.append({"role": "system", "content": response["choices"][0]["message"]["content"]})
    return response

while question != "exit":
	question = input("You: ")

	if question == "exit":
		print("Bob: Bye!")
		break
	elif question == "clear":
		memory_bank = [{"role": "system", "content": role}]
		print("Bob: Memory cleared")
		continue
	elif question == "export":
		print("Bob: Exporting last reply to MD file...")
		filename = input("Filename: ")
		with open(filename + ".md", "w") as f:
				f.write(response["choices"][0]["message"]["content"])
		print("Bob: Exported to " + filename + ".md")
		continue
	response = ask_bob(question)
	print("Bob: " + response["choices"][0]["message"]["content"])