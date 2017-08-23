# Random Language creator/translator

## About

This Project is about creating a python web-app that can take user-input and translate that into a made up language.

It will accept an upload of any .txt file and allow users to choose common vowels/consonants, and some other option to modify the flavour of the language. 

It will convert from english, by assigning newly found words into the new language as well as re-using them if they are already available.

by doing this it can learn the kind of words you are interested in using and only create translations for those.

## How It Works

The algorithm for creating the words uses a simple vowel to consonant rhythm, as well as different chances for double letter combinations.

## To run it

Open this project in an editor, make sure english_words.txt and learned_alien_words.txt are empty, then copy any block of text, or the contents of 1000_english_words.txt into the translate_me.txt file.

Then run new_language.py.

on the first run through it will learn all the words in translate_me.txt and on a second run through will provide the translation.

You can continue to add to the dictionary by adding new blocks of text to translate_me.txt