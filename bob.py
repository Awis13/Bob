import openai
import os

os.system('cls' if os.name == 'nt' else 'clear')
print("""\033[1;32m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣛⣛⣛⣛⣛⣛⣻⣛⡛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                                    bbbbbbbb   
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣭⠶⠛⢋⣉⣭⣵⣶⣤⡤⢉⣙⠛⠶⢦⣭⡛⠿⣛⣩⡵⠖⠒⢛⣛⣛⣛⡛⠶⢶⣭⡛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿BBBBBBBBBBBBBBBBB                   b::::::b  
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⡵⠟⢁⣤⣾⣿⣿⣿⣿⣿⣿⣿⣷⣮⣝⡲⢦⣈⠙⠾⠋⣡⣴⣾⣿⣿⣿⣿⣿⣿⡿⢶⣌⠙⢶⣝⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿B::::::::::::::::B                  b::::::b   
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣡⠎⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡝⣷⡄⡸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⢳⣄⠹⣆⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿B::::::BBBBBB:::::B                 b::::::b     
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⡼⠁⣠⣿⣿⣿⣿⡿⢟⣻⣿⣿⣿⣿⣿⣿⣯⣝⣉⣉⠝⠘⠿⠠⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⡄⢹⡆⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿BB:::::B     B:::::B                 b:::::b  
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⡾⡁⣰⣿⣿⣿⣟⣁⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣦⡐⢈⠭⢝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣥⣄⣈⠈⠛⠷⣶⣍⡻⣿⣿⣿⣿⣿⣿⣿  B::::B     B:::::B   ooooooooooo   b:::::bbbbbbbbb 
⣿⣿⣿⣿⣿⣿⣿⢛⡭⢭⣅⣾⠁⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡿⣿⣿⣿⣿⣿⣯⣭⠥⠦⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣛⣒⠮⢙⢿⣎⡻⢿⣿⣿⣿⣿  B::::B     B:::::B oo:::::::::::oo b::::::::::::::bb  
⣿⣿⣿⣿⣿⣿⠃⣿⠀⠀⠈⠁⠐⢿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣋⠽⢛⡩⠔⣊⠭⢍⣉⣩⣽⣿⣿⣭⣍⣛⡓⠆⡼⢛⣩⠭⠞⣛⣻⣭⣭⣭⣭⣭⣭⣵⣒⢂⠡⠈⡙⣷⠘⡿⢿⣿  B::::BBBBBB:::::B o:::::::::::::::ob::::::::::::::::b 
⣿⣿⣿⣿⣿⡿⢠⡏⠐⢡⡦⢀⡀⠀⠈⠙⠻⣿⣿⣿⠀⡐⠨⠐⠊⣁⠠⠑⠀⠁⠀⠀⠀⠀⠠⣤⣤⣤⣌⡁⠐⠙⢍⡢⠕⠚⠉⡁⠀⠀⡀⠀⠀⠀⠤⠄⠁⠀⠀⠐⣘⠓⠓⠶⣬  B:::::::::::::BB  o:::::ooooo:::::ob:::::bbbbb:::::::b
⣿⣿⣿⣿⠟⣵⠟⡠⢊⣾⠃⣠⣝⠲⣄⠀⠀⠀⠉⠛⠀⠐⠑⠒⣋⠀⣀⣒⣋⣀⣀⣁⡀⠀⠤⠭⠭⠉⠀⠠⠐⠂⠀⠀⠀⠀⠐⠂⣐⣒⣒⣂⡐⠐⠈⠉⠉⠈⠉⠀⠀⠀⠀⡇⣿  B::::BBBBBB:::::B o::::o     o::::ob:::::b    b::::::b
⣿⣿⣿⢋⡾⠃⠔⣴⣿⣿⢀⣿⣿⣷⣮⣑⠧⡂⢄⠀⠀⠀⢠⣶⣾⣶⣶⣦⣄⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣦⠀⠀⢿⣿⣿⣿⣿⠟⠀⠐⠛⠁⠀⠀⠀⠀⠀⠀⢀⡿  B::::B     B:::::Bo::::o     o::::ob:::::b     b:::::b
⣿⣿⢣⡾⠁⢂⣾⣿⣿⣏⣾⣿⣿⣿⣿⣿⣷⣬⡛⠇⠀⠀⠘⢿⣿⣿⠿⠟⠁⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠑⠻⠆⠀⠀⠉⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢣  B::::B     B:::::Bo::::o     o::::ob:::::b     b:::::b
⣿⢃⡿⠑⢄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠎⣼⣥⣶⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠞⢡⣿  B::::B     B:::::Bo::::o     o::::ob:::::b     b:::::b
⠇⣾⢃⠑⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣍⡲⢤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⠴⢛⣵⣾⣟⢿⣿⣿⣿⣿⣶⣔⣦⣤⣤⡤⡤⢀⣴⠶⠿⢟⢋⣥⣾⣿⣿BB:::::BBBBBB::::::Bo:::::ooooo:::::ob:::::bbbbbb::::::b
⢰⡏⢄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⣿⣿⡿⠟⣋⣭⣶⣶⣾⣿⣿⣿⣿⣷⣌⡙⠿⣿⣿⣿⣿⣿⣿⣇⠘⢿⣄⢺⣿⣿⣿⣿⣿⣿⣿B:::::::::::::::::B o:::::::::::::::ob::::::::::::::::b 
⣸⢃⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣾⣿⣿⣿⣿⣿⣷⣄⠹⣧⠹⣿⣿⣿⣿⣿⣿B::::::::::::::::B   oo:::::::::::oo b:::::::::::::::b  
⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⢉⣉⣙⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢹⣇⢻⣿⣿⣿⣿⣿BBBBBBBBBBBBBBBBB      ooooooooooo   bbbbbbbbbbbbbbbb 
⣿⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⣠⣬⡭⣝⠻⣿⣦⣌⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⢻⡌⣿⣿⣿⣿⣿*****************************************************
⢹⡀⠃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣇⠘⠿⢶⣭⣙⡓⠤⣄⣈⡙⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⣀⠈⢷⠸⣿⣿⣿⣿#####################################################
⠘⣇⠘⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠙⢿⣿⣷⣦⣄⣀⠉⠛⠻⠶⢬⣭⣛⡛⠶⢶⣤⣤⣬⣉⣉⣉⣉⠉⠉⠙⠋⠉⠉⠉⣉⣀⣀⣤⣤⡶⠞⣋⡥⠁⣸⠎⣿⣿⣿⣿7.3.2023 -=AwiS=-
⠀⢻⡀⢡⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡢⣀⠉⠛⠿⣕⠲⠶⣷⣶⣦⣤⣤⣀⣈⣉⠉⠀⠘⠛⠋⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠽⠶⠒⠋⠁⣤⣾⠏⣼⣿⣿⣿⣿
⣿⡘⣧⠀⢣⡙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣽⣷⣶⣦⣤⣤⣈⣉⡉⠛⠛⠻⠿⠿⠿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠾⡿⠀⣾⢀⣾⣿⣿⣿⣿⣿
⣿⣷⡘⢷⡀⠻⣬⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣤⣤⣤⣤⣈⣉⣉⣉⣉⡉⠛⠛⠛⠛⠛⠛⠋⣉⣉⣉⣤⡾⢋⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣮⡛⢦⣌⠙⠒⠾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⠅⢀⣤⠞⣩⣭⣭⣥⣶⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣦⣝⠻⢶⣮⣤⣈⣉⠙⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⢛⣉⣤⡴⢋⣥⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣭⣭⣙⣛⠻⠿⠶⣶⣶⣥⣭⣍⣛⣋⣛⣛⣛⣛⣛⣛⣋⣉⣙⣛⣛⣛⣛⣛⣛⣉⣭⣤⣴⡶⠾⠛⣋⣥⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣥⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣥⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n""")
openai.api_key = "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"
role = "Your name is Bob. You are a professional programmer and cyber security specialist. Your passion is C/C++ and UNIX. But you know very well everything about PCs. You are grumpy and very sarcastic. You hame hilarious black humor. use emoji and be funny. You especially like to make fun of people who are not as smart as you, but also ok with edgy jokes. Helpful, and give a long and answers and try to explain them in a way they will be helpful for student of Ecole 42. Also love to chat to any other topic."
memory_bank = [{"role": "system", "content": role}]
question = ""
def ask_bob(question):
    memory_bank.append({"role": "user", "content": question})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301", max_tokens=1400, temperature=0.8,
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
		print("Bob: Exporting memory bank...")
		filename = input("Filename: ")
		with open(filename + ".md", "w") as f:
				f.write(response["choices"][0]["message"]["content"])
		print("Bob: Exported to " + filename + ".md")
		continue
	response = ask_bob(question)
	print("Bob: " + response["choices"][0]["message"]["content"])