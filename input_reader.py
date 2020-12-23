class InputReader:
    @staticmethod
    def fetch_input_lines():
        data = ""
        with open('input.txt', 'r') as file:
            data = file.read()
        return data.split("\n")

    @staticmethod
    def fetch_input_seperated_by_empty_lines():
        data = ""
        with open("input.txt", "r") as file:
            data = file.read()
        return data.split("\n\n")
