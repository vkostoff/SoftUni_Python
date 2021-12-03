morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..'}

morse_code = input().split()

for i in range(len(morse_code)):
    if morse_code[i] in morse_code_dict.values():
        for k, v in morse_code_dict.items():
            if v == morse_code[i]:
                morse_code[i] = k
                break

message = "".join(morse_code)
message = message.split("|")
print(" ".join(message))