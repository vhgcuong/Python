def translate(text):
    result = ""
    text = text.strip()
    for item in text.split(" "):
        sub_text = item
        while sub_text[0] not in ('a', 'e', 'i', 'o', 'u'):
            if sub_text.startswith("xr") or sub_text.startswith("yt"):
                break
            if sub_text[0] == 'q' and sub_text[1] == 'u':
                sub_text = f"{sub_text[2::]}qu"
                break
            sub_text = sub_text[1::] + sub_text[0]
            if sub_text.startswith('y'):
                break

        result += f"{sub_text}ay "

    return result.strip()

if __name__ == "__main__":
    print(translate("rhythm"))
