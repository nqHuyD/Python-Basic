def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "🙃",
        "<3": "😍",
        ">.<": "🤬"
    }

    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '
    return output


message = input("> ")
emoji_message = emoji_converter(message)
print(emoji_message)