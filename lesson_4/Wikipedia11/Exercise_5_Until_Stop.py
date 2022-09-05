while True:
  word = input("Please enter a word. To stop, enter 'stop': ").lower()
  if word == "stop":
    break
  else:
    len_word = len(word)
    print(f"The word is {word}, which has {len_word} characters")
    print("Enter 'stop' to quit")

