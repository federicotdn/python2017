while True:
    text = input('>>> ')
    if text == 'quit':
        break
    
    result = eval(text)
    print(result)