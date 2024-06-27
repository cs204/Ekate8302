emoji_dict = {
    ":1st_place_medal:": "🥇",
    ":money_bag:": "💰",
    # Добавьте другие эмодзи, которые вам нужны
}

def main():
    s = input("Input: ")
    output = s
    for emoji_name, emoji_char in emoji_dict.items():
        output = output.replace(emoji_name, emoji_char)
    print(f"Output: {output}")

if __name__ == "__main__":
    main()
