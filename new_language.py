import random
import time
import re

random.seed(12345678)

class CreateLanguage(object):

    def __init__(self):
        self.character_of_language = self.create_character_of_language()
        vowels, consonants = self.get_letters()
        self.vowels = vowels
        self.consonants = consonants
        self.power_vowels = self.create_power_vowels()
        self.power_consonants = self.create_power_consonants()
        self.power_vowel_starts = self.create_power_vowel_starts()
        self.power_consonant_starts = self.create_power_consonant_starts()
        self.power_consonant_ends = self.create_power_consonant_ends()
        # self.power_vowel_doubles =
        # self.power_consonant_doubles =
        self.syllables = self.create_syllables()
        self.syllables_list = self.create_syllable_list()
        self.word_sets = self.create_word_set()
        self.english_lang = self.import_english()
        self.dictionary = self.create_dictionary()

    def get_letters(self):
        vowels = ["a", "e", "i", "o", "u"]
        consonants = ["b", 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        return vowels, consonants

    def create_character_of_language(self):
        number_of_power_vowels = random.randint(3, 5)
        number_of_power_consonants = random.randint(3, 10)
        number_of_power_vowel_starts = random.randint(3, 6)
        chance_of_vowel_starts = random.randint(5, 15)
        chance_of_consonant_starts = random.randint(5, 10)
        language_style_random = [number_of_power_vowels,
                                 number_of_power_consonants,
                                 number_of_power_vowel_starts,
                                 chance_of_vowel_starts,
                                 chance_of_consonant_starts,
                                 ["w", "y", "x", "z", 'h', 'q', 'v']
                                 ]
        language_style_simple = [3,
                                 15,
                                 3,
                                 15,
                                 8,
                                 ["w", "y", "x", "z", 'h', 'q', 'v']
                                 ]
        language_style_ri_and_mo = [5,
                                    5,
                                    3,
                                    15,
                                    8,
                                    ["w", "y", "x", "z", 'h'],
                                    "oai",
                                    "mrpgzw"
                                    ]
        language_style_japanese = [5,
                                    5,
                                    3,
                                    3,
                                    3,
                                    ["w", "y", "x", "z", 'h'],
                                    "uoia",
                                    "zytkj"
                                    ]
        language_style_nordic =[5,
                                5,
                                3,
                                2,
                                10,
                                ["w", "y", "x", "z", 'h'],
                                "aeio",
                                "flrjk"
                                ]
        language_style_aliens = [5,
                                 5,
                                 3,
                                 2,
                                 10,
                                 ["w", "y", "x", "z", 'h'],
                                 "aeio",
                                 "xzkyv"
                                ]
        language_style_choice = language_style_simple

        print language_style_choice
        return language_style_choice

    def create_power_vowels(self):
        vowels = ["a", "e", "i", "o", "u"]
        power_vowels = ""
        for vowel in xrange(0, self.character_of_language[0]):
            current_vowel = random.choice(vowels)
            while current_vowel in power_vowels:
                current_vowel = random.choice(vowels)
            power_vowels += current_vowel
        if len(self.character_of_language) > 6:
            power_vowels = self.character_of_language[6]
        return power_vowels

    def create_power_consonants(self):
        consonants = ["b", 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        # consonants = ["b", 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        power_consonants = ""
        for consonant in xrange(0, self.character_of_language[1]):
            current_consonant = random.choice(consonants)
            while current_consonant in power_consonants:
                current_consonant = random.choice(consonants)
            power_consonants += current_consonant
        if len(self.character_of_language) > 6:
            power_consonants = self.character_of_language[7]
        return power_consonants

    def create_power_vowel_starts(self):
        power_vowels = self.power_vowels
        power_vowels_starts = []
        for power_vowels_start in xrange(0, self.character_of_language[2]):
            current_power_vowel_start = random.choice(power_vowels)
            current_power_vowel_start += random.choice(power_vowels)
            while current_power_vowel_start[1] == current_power_vowel_start[0]:
                current_power_vowel_start = current_power_vowel_start[:-1]
                current_power_vowel_start += random.choice(power_vowels)
            while current_power_vowel_start in power_vowels_starts:
                current_power_vowel_start = random.choice(power_vowels)
                current_power_vowel_start += random.choice(power_vowels)
                while current_power_vowel_start[1] == current_power_vowel_start[0]:
                    current_power_vowel_start = current_power_vowel_start[:-1]
                    current_power_vowel_start += random.choice(power_vowels)
            power_vowels_starts.append(current_power_vowel_start)
        return power_vowels_starts

    def create_power_consonant_starts(self):
        # IMPORTS MY LANGUAGE TEXT FILE WHICH CONTAINS A LIST OF FICTIONAL "VERBS"
        power_consonants = self.power_consonants
        possible_power_consonant_starts = []
        with open('power_consonant_starts.txt') as ppcs:
            for line in ppcs:
                possible_power_consonant_starts.append(line.strip())
        possible_power_consonant_starts = possible_power_consonant_starts[:-1]
        power_consonant_starts = []
        for possible_starts in xrange(0, len(possible_power_consonant_starts)):
                if possible_power_consonant_starts[possible_starts][0] in power_consonants and possible_power_consonant_starts[possible_starts][1] in power_consonants:
                    useable_double = possible_power_consonant_starts[possible_starts]
                    power_consonant_starts.append(useable_double)

        return power_consonant_starts

    def create_power_consonant_ends(self):
        # IMPORTS MY LANGUAGE TEXT FILE WHICH CONTAINS A LIST OF FICTIONAL "VERBS"
        power_consonants = self.power_consonants
        possible_power_consonant_ends = []
        with open('power_consonant_ends.txt') as ppce:
            for line in ppce:
                possible_power_consonant_ends.append(line.strip())
        # possible_power_consonant_ends = possible_power_consonant_ends[:-2]
        print possible_power_consonant_ends
        power_consonant_ends = []
        for possible_ends in xrange(0, len(possible_power_consonant_ends)):
                if possible_power_consonant_ends[possible_ends][0] in power_consonants and possible_power_consonant_ends[possible_ends][1] in power_consonants:
                    useable_double = possible_power_consonant_ends[possible_ends]
                    power_consonant_ends.append(useable_double)

        return power_consonant_ends

    def create_syllables(self):

        # Create First Letter
        power_vowels = self.power_vowels
        power_consonants = self.power_consonants
        power_vowel_starts = self.power_vowel_starts
        power_consonant_starts = self.power_consonant_starts
        letters = ['Vow', "Con"]

        syllable_length = random.randint(1, 4)
        syllable = ""
        first_letter = ''
        previous_letter_type = random.choice(letters)
        if previous_letter_type == 'Vow':
            first_letter = "Con"
        if previous_letter_type == 'Con':
            first_letter = "Vow"

        current_letter = ''

        for syllables in xrange(0, syllable_length):
            if previous_letter_type == "Con":  # create vowel, next time consonant
                if random.randint(1, 15) >= self.character_of_language[3]:
                    if len(power_vowel_starts) != 0:
                        current_letter = random.choice(power_vowel_starts)
                    else:
                        current_letter = random.choice(power_vowels)
                else:
                    current_letter = random.choice(power_vowels)
                syllable += current_letter
                previous_letter_type = 'Vow'
            else:
                if random.randint(1, 10) >= self.character_of_language[4]:
                    # one in ten starter letters are power_consonant_starts
                    if len(power_consonant_starts) != 0 and syllables == 0:  # must exist and be first letter
                        current_letter = random.choice(power_consonant_starts)
                    else:
                        current_letter = random.choice(power_consonants)
                else:
                    current_letter = random.choice(power_consonants)
                syllable += current_letter
                if random.randint(1, 10) >= self.character_of_language[4] and syllables > 0 and current_letter not in self.character_of_language[5]:
                    syllable += current_letter
                previous_letter_type = "Con"
        if previous_letter_type == "Con":
            syllable += random.choice(power_vowels)
            end_letter = 'Vow'

        else:
            if random.randint(1, 10) >= self.character_of_language[4] and len(self.power_consonant_ends) > 0:
                syllable += random.choice(self.power_consonant_ends)
            else:
                syllable += random.choice(power_consonants)
            end_letter = 'Con'
        return syllable, first_letter, end_letter

    def create_syllable_list(self):

        consonant_syllables_list = []
        consonant_syllables_list_end = []
        vowel_syllables_list = []
        vowel_syllables_list_end = []
        for amount_wanted in xrange(0, 10000):
            new_syllable = self.create_syllables()
            if new_syllable[1] == 'Vow':
                if new_syllable[2] == 'Vow':
                    if new_syllable[0] not in vowel_syllables_list_end:
                        vowel_syllables_list_end.append(new_syllable[0])
                else:
                    if new_syllable[0] not in vowel_syllables_list:
                        vowel_syllables_list.append(new_syllable[0])
            if new_syllable[1] == 'Con':
                if new_syllable[2] == 'Con':
                    if new_syllable[0] not in consonant_syllables_list_end:
                        consonant_syllables_list_end.append(new_syllable[0])
                else:
                    if new_syllable[0] not in consonant_syllables_list:
                        consonant_syllables_list.append(new_syllable[0])
        return vowel_syllables_list, vowel_syllables_list_end, consonant_syllables_list, consonant_syllables_list_end

    def create_word_set(self):
        choice_of_syllables = self.syllables_list
        word_sets = []

        word_sets += self.power_vowels

        for single_syllables_set in xrange(0, len(self.syllables_list)):  # add single_syllables first to also be used
            syllable_list = self.syllables_list[single_syllables_set]
            for single_syllables in xrange(0, len(syllable_list)):
                single_syllable = syllable_list[single_syllables]
                word_sets.append(single_syllable)

        vc = choice_of_syllables[0]
        vv = choice_of_syllables[1]
        cv = choice_of_syllables[2]
        cc = choice_of_syllables[3]

        syllable_combinations = [
            [vv, vc],
            [cv, cc],
            [cv, cc],
            [vc, vv]
        ]

        for word_sets_i in xrange(0, 3):
            next_syllable_set = syllable_combinations[word_sets_i]
            for syllable in xrange(0, len(next_syllable_set)):
                for words in xrange(0, len(choice_of_syllables[word_sets_i])):
                    for variations in xrange(0, len(next_syllable_set[syllable])):
                        first_syllable = choice_of_syllables[word_sets_i][words]
                        first_syllable += next_syllable_set[syllable][variations]
                        word_sets.append(first_syllable)
        return word_sets

    def import_english(self):
        english_words = []
        with open('english_words.txt') as english_lang:
            for line in english_lang:
                english_words.append(line.strip())
        return english_words

    def create_dictionary(self):

        already_known_alien_words = []
        translation = []
        with open('learned_alien_words.txt') as alien_lang:
            for line in alien_lang:
                already_known_alien_words.append(line.strip())

        if len(already_known_alien_words) != len(self.word_sets):
            translation = []
            english_words = self.english_lang
            alien_words = self.word_sets
            random.shuffle(alien_words)
            for eng_word in english_words:
                length_of_word = len(eng_word)
                for alien_word in xrange(0, len(alien_words)):
                    if len(alien_words[alien_word]) == length_of_word:
                        translation.append(alien_words[alien_word])
                        alien_words.remove(alien_words[alien_word])
                        break
            with open('learned_alien_words.txt', 'r+') as alien_lang:
                for word in xrange(0, len(translation)):
                    if word != 0:
                        alien_lang.write("\n")
                    alien_lang.write(translation[word])
        return translation

    def translate_something(self):
        words_to_translate = []
        translation = []
        english_words = self.english_lang
        not_wanted_list = ['.', ',', ';', ':', '!', '?', '`', '"', "'", "-"]
        with open('translate_me.txt') as english_lang:
            for line in english_lang:
                for word in line.split():
                    if word == '':
                        break
                    clean_word = word.lower()
                    for cleanups in not_wanted_list:
                        word.replace(cleanups, '')
                    words_to_translate.append(clean_word)
            word_to_translate_string = line

        for word_to_translate in words_to_translate:
            with open('english_words.txt', "a") as english_lang:
                if word_to_translate in english_words:
                    for word_can_translate in xrange(0, len(english_words)):
                        if word_to_translate == english_words[word_can_translate]:
                            try:
                                translation.append(self.dictionary[word_can_translate])
                            finally:
                                break
                else:
                    english_lang.write("\n")
                    clean_word = word_to_translate.lower()
                    for cleanups in not_wanted_list:
                        word_to_translate.replace(cleanups, '')
                    english_lang.write(clean_word)
                    translation.append(clean_word)
        # print english_words2
        translation_conc = ''
        for translated_words in translation:
            translation_conc += translated_words+' '

        print translation
        print words_to_translate

        print word_to_translate_string
        print translation_conc




language = CreateLanguage()
words_sets = language.word_sets
language.translate_something()
print 'Power Vowels', language.power_vowels
print 'Power Consonants', language.power_consonants
print 'Power Vowel Starts', language.power_vowel_starts
print 'Power_consonant_Starts', language.power_consonant_starts
print "Power_consonant_ends", language.power_consonant_ends
print language.syllables_list[0]
print language.syllables_list[1]
print language.syllables_list[2]
print language.syllables_list[3]
# print language.word_sets
print language.english_lang
print language.dictionary

# paragraph = ''
# for lots in xrange(0, 10):
#     paragraph = ''
#     word_set = random.choice(words_sets)
#     random_syllable_set = random.choice(language.syllables_list)
#     paragraph += "The Village of "
#     paragraph += random.choice(word_set)+' '
#     paragraph += "lies in the valley of "
#     paragraph += random.choice(random_syllable_set)+random.choice(random_syllable_set)+" "
#     time.sleep(1)
#     print paragraph
#
# for many in xrange(0, 50):
#     sentence = ''
#     for words in xrange(0, 10):
#         word_set = random.choice(words_sets)
#         random_syllable_set = random.choice(language.syllables_list)
#         if random.randint(1, 2) == 1:
#             sentence += random.choice(word_set) + ' '
#         else:
#             sentence += random.choice(random_syllable_set) + ' '
#         if random.randint(1, 8) >= 8:
#             sentence += random.choice(language.power_vowels) + ' '
#         time.sleep(0.2)
#     sentence = sentence[:-1]
#     if random.randint(1, 2) == 1:
#         sentence += ','
#     else:
#         sentence += '.'
#     print sentence
#     time.sleep(1)

