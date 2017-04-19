while True:
    text = input()
    if text == "quit":
        break
    elif not text:
        continue

    print("La longitud del string es: ", len(text))
