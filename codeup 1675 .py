code = {"a":"x","b":"y","c":"z","d":"a","e":"b","f":"c","g":"d","h":"e","i":"f","j":"g","k":"h","l":"i","m":"j","n":"k","o":"l",
     "p":"m","q":"n","r":"o","s":"p","t":"q","u":"r","v":"s","w":"t","x":"u","y":"v","z":"w"," ":" "}

answer = []
cipher = input("")

for i  in cipher:
    answer.append(code[i])
    
print("".join(answer))
    