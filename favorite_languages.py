# favorite_language = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# for name, language in favorite_language.items():
#     print(name.title() + "'s favorite language is " +
#           language.title() + ".")
#
# for name in favorite_language.keys():
#     print(name.title())
#
# for language in favorite_language.values():
#     print(language.title())
#
# if 'erin' not in favorite_language.keys():
#     print("\nErin, please take out poll!\n")
#
# for language in set(favorite_language.values()):
#     print(language.title())

favorite_language = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_language.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
