import string


def load_words():
    with open('words.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words


if __name__ == '__main__':
    print("")

    english_words = load_words()
    cipher_text = input("Input the cipher text: ")

    chosen_alphabet = input("qwerty (q) or abc (a): ")
    if chosen_alphabet == "q" or chosen_alphabet == "qwerty":
        alphabet = "q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m,"
        alphabet += alphabet + alphabet.upper() + alphabet.upper()
        alphabet = alphabet.split(',')
    elif chosen_alphabet == "a" or chosen_alphabet == "abc":
        alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,"
        alphabet += alphabet + alphabet.upper() + alphabet.upper()
        alphabet = alphabet.split(',')
    else:
        alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,"
        alphabet += alphabet + alphabet.upper() + alphabet.upper()
        alphabet = alphabet.split(',')
        
    trials = []
    for i in range(1, 26):
        trial_string = ""
        for letter in cipher_text:
            try:
                trial_string += alphabet[alphabet.index(letter) + i]
            except ValueError:
                trial_string += letter
        trials.append({
            "shift": 26 - i,
            "trial_string": trial_string,
            "tally": 0,
        })

    for trial in trials:
        stripped_string = trial['trial_string'].translate(str.maketrans('', '', string.punctuation)).lower()
        stripped_string_array = stripped_string.split()
        tally = 0
        for word in stripped_string_array:
            if word in english_words:
                tally += 1
        trials[trials.index(trial)]['tally'] = tally

    print("")
    trials = sorted(trials, key=lambda j: j['tally'], reverse=True)
    print(trials[0]['trial_string'])
    print("\nShift = %s" % (trials[0]['shift']))
