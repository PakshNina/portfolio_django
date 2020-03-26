from string import ascii_letters, digits


# Russian letters.
RUSSIAN = [
    'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н',
    'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь',
    'э', 'ю', 'я',
    ]

# English letters.
ENGLISH = [
    'a', 'b', 'v', 'g', 'd', 'e', 'yo', 'zh', 'z', 'i', 'y', 'k', 'l', 'm',
    'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'h', 'ts', 'tch', 'sh', 'sch',
    '', 'y', '', 'e', 'yu', 'ya'
]

# Final rus-eng dict.
RUS_TO_ENG = dict(zip(RUSSIAN, ENGLISH))


def find_ascii_and_digits(text):
    """Strips all symbols except ascii and digits."""
    return all(map(lambda c: c in ascii_letters + digits, text))


def transliterate(phrase):
    """Translate russian phrase to latin letters."""
    final_phrase = ''
    for letter in phrase.lower():
        if find_ascii_and_digits(letter):
            final_phrase += letter
            continue
        final_phrase += RUS_TO_ENG.get(letter, ' ')
    return final_phrase
