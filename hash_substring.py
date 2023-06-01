# python3

def read_input():
    a = input()
    for next in a:
        if next == "I":
            pattern = input()
            text = input()
        if next == "F":
            filename = "tests/06"
            with open(filename, 'r') as file:
                pattern = file.readline()[:-1]
                text = file.readline()
        return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    output = []

    t_len = len(text)
    p_len = len(pattern)
    A = 256
    B = 11

    pattern_hash = 0
    window_hash = 0
    h = 1

    for i in range(p_len - 1):
        h = (h * A) % B

    for i in range(p_len):
        pattern_hash = (A * pattern_hash + ord(pattern[i])) % B
        window_hash = (A * window_hash + ord(text[i])) % B

    for i in range(t_len - p_len + 1):
        if pattern_hash == window_hash:
            if pattern == text[i:i + p_len]:
                output.append(i)

        if i < t_len - p_len:
            window_hash = (A * (window_hash - ord(text[i]) * h) + ord(text[i + p_len])) % B

    return output


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
