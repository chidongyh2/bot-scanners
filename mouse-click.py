from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    x = x
    y = y
    print('X =', x, '\nY =', y)

with Listener(on_click=on_click) as listener:
    listener.join()