import keyboard

def on_esc_press(event):
    if event.name == 'esc':
        keyboard.unhook_all()  # interrompa a monitoração do teclado
        return True  # interrompa o loop de espera

def on_right_press(event):
    if event.name == 'right':
        keyboard.unhook_all()  # interrompa a monitoração do teclado
        return True  # interrompa o loop de espera

def on_up_press(event):
    if event.name == 'up':
        keyboard.unhook_all()  # interrompa a monitoração do teclado
        return True  # interrompa o loop de espera
