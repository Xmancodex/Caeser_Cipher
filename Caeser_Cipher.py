def caeser_cipher(): 
    phrase = input("Enter phrase: ") 
    key = int(input("Enter key for phrase (number only): "))   
    result = ""
    for i in phrase: 
        if i.islower(): 
            P = ord(i) - ord('a') 
            C = (P + key) % 26 
            shiftedletter = chr(C + ord('a')) 
            result += shiftedletter
        elif i.isupper(): 
            P = ord(i) - ord('A') 
            C = (P + key) % 26   
            shiftedletter = chr(C + ord('A'))  
            result += shiftedletter  
        else: 
            result += i 
    return print("Encoded phrase: " + result)  
caeser_cipher()
