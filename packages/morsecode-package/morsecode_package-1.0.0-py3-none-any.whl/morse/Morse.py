class Morse:
    def __init__(self):
        self.codes = {
            "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
            "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
            "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
            "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
            "Y": "-.--", "Z": "--..",
            1: ".----", 2: "..---", 3: "...--", 4: "....-", 5: ".....",
            6: "-....", 7: "--...", 8: "---..", 9: "----.", 0: "-----"
        }
        self.reverse_codes = {v: k for k, v in self.codes.items()}

    def to_morse(self, data):
        data = self.separate_space(data)
        morse_code = []
        for char in data:
            if char.isdigit():
                char = int(char)
            if char in self.codes:
                morse_code.append(self.codes[char])
            else:
                morse_code.append("")

        return " ".join(morse_code)

    def separate_space(self, data):
        return [char.upper() for char in data if char != " "]

    def to_string(self, morse_code):
        morse_list = morse_code.split(" ")
        result = []
        for code in morse_list:
            if code in self.reverse_codes:
                result.append(str(self.reverse_codes[code]))
            else:
                result.append("")

        return " ".join(result)

    def get_morse_codes(self):
        return self.codes
