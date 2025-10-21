def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()

    print(f"Analyzing book found at {file_path}")

    return file_content

def get_total_words(file_content):
    print('-' * 11 + " Word Count " + '-' * 11)
    return f"Found {len(file_content.split())} total words"

def get_total_characters(file_content):
    file_content1 = file_content.lower()
    char_num = {}
    for i in range(len(file_content1)):
        if file_content1[i] not in char_num:
            char_num[file_content1[i]] = 1
        else:
            char_num[file_content1[i]] += 1
    
    print('-' * 11 + " Character Count " + '-' * 11)
    return char_num

def sort_on_1(characters):
    chum_char = {}
    chum_char_arr = []
    for key, value in characters.items():
        chum_char_arr.append({"char": key, "num": value})

    def sort_on(items):
        return items['num']

    chum_char_arr.sort(reverse=True, key=sort_on)

    for i in chum_char_arr:
        if i['char'] == ' ' or i['char'] == '\n':
            continue
        else:
            print(f"{i['char']}: {i['num']}")

