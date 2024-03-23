def main():
    file_contents = None
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()

    num_words = len(file_contents.split())
    char_counts = count_chars(file_contents)
    char_counts = [(v, k) for k, v in char_counts.items()]
    char_counts.sort(reverse=True)

    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{num_words} words found in the document')
    print('')
    for count, char in char_counts:
        print(f"The '{char}' character was found {count} trimes")
    print('--- End report ---')


def count_chars(s):
    counts = [0 for i in range(26)]
    for c in s:
        i = char_to_idx(c)
        if i is not None:
            counts[i] += 1
    d_counts = {}
    for ch, count  in zip('abcdefghijklmnopqrstuvwxyz', counts):
        d_counts[ch] = count
     
    return d_counts


def char_to_idx(c):
    c = c.lower()
    c = ord(c)
    i = c - ord('a')
    if 0 <= i < 26:
        return i
    else:
        return None


if __name__ == "__main__":
    main()
