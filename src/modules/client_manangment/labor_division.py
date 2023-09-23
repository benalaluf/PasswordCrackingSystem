class LaborDivision:

    def __init__(self, file):
        self.file = file

    def get_100_words(self):
        pass

    def read_file_in_chunks(self, chunk_size=100):
        print('start')
        with open(self.file, 'r') as file:
            while True:
                chunk = file.readlines(chunk_size)
                if not chunk:
                    break
                yield chunk

niga ='/Users/blu/GitHub/PasswordCrackingSystem/src/modules/wordlists/rockyou.txt'
if __name__ == '__main__':
    def read_large_file_in_chunks(file_path, chunk_size=100):
        with open(file_path, 'r') as file:
            while True:
                lines = []
                for _ in range(chunk_size):
                    line = file.readline()
                    if not line:
                        break
                    lines.append(line)
                if not lines:
                    break
                yield lines


    # Example usage:
    file_path = niga
    file_generator = read_large_file_in_chunks(file_path)

    for chunk in file_generator:
        for line in chunk:
            # Process each line here
            print(line.strip())

    # Process the lines in this chunk as needed
