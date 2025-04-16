MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',

              '.': '.-.-.-', ',': '--..--', ':': '---...',
              "'": '.----.', '-': '-....-',
              }


def english_to_morse(
    input_file: str = "lorem.txt",
    output_file: str = "lorem_morse.txt"
):

    """Convert an input text file to an output Morse code file.

    Notes
    -----
    This function assumes the existence of a MORSE_CODE dictionary, containing a
    mapping between English letters and their corresponding Morse code.

    Parameters
    ----------
    input_file : str
        Path to file containing the text file to convert.
    output_file : str
        Name of output file containing the translated Morse code. Please don't change
        it since it's also hard-coded in the tests file.
    """


    
    lines = []
    with open(input_file, 'r', encoding='utf-8') as f_in:
        for line in f_in:
            line = line.rstrip('\n')
            words = line.strip().split()
            if not words:
                # שורה ריקה - נשמור ריק במערך
                lines.append('')
            else:
                for word in words:
                    morse_word = ''.join(MORSE_CODE.get(c.upper(), '') for c in word)
                    lines.append(morse_word)
    # כעת כותבים את הקובץ
    with open(output_file, 'w', encoding='utf-8') as f_out:
        for i, line in enumerate(lines):
            # אם זה השורה האחרונה, לא נוסיף \n בסוף
            if i == len(lines) - 1:
                f_out.write(line)
            else:
                f_out.write(line + '\n')



if __name__ == "__main__":
    english_to_morse()