
wordlist_eng = []


with open('words/wordle_eng.txt') as f:
            for line in f:
                line.strip()
                line.lower()
                actual_line = line.split()

                if len(actual_line) > 1:
                    pass

                if len(line) == 6:
                    wordlist_eng.append(line.strip())