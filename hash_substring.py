# python3

def read_input():
    a = input()
    for next in a:
        if next == "I":
            pattern = input()
            text = input()
        if next == "F":
            filename = "tests/06.txt"
            with open(filename, 'r') as file:
                pattern = file.readline()
                text = file.readline()
        return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    output = []

    n = len(text)
    m = len(pattern)
    d = 256
    q = 101

    pattern_hash = 0
    window_hash = 0
    h = 1

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        window_hash = (d * window_hash + ord(text[i])) % q

    for i in range(n - m + 1):
        if pattern_hash == window_hash:
            if pattern == text[i:i + m]:
                output.append(i)

        if i < n - m:
            window_hash = (d * (window_hash - ord(text[i]) * h) + ord(text[i + m])) % q

            if window_hash < 0:
                window_hash += q

    return output


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

