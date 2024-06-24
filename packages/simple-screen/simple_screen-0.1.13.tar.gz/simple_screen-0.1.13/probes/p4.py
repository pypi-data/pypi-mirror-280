import curses

def draw_button(win, y, x, label, selected=False):
    """
    Dibuja un botón en la ventana `win` en la posición (y, x) con el texto `label`.
    Si `selected` es True, el botón se dibuja resaltado.
    """
    if selected:
        win.attron(curses.A_REVERSE)
    win.addstr(y, x, label)
    if selected:
        win.attroff(curses.A_REVERSE)

def main(stdscr):
    curses.curs_set(0)  # Ocultar el cursor
    stdscr.nodelay(0)   # Bloquear esperando la entrada
    stdscr.timeout(-1)  # Esperar indefinidamente por la entrada

    # Definir los botones y su posición
    buttons = ["Aceptar", "Cancelar"]
    current_button = 0
    button_y = 10
    button_x = 20

    while True:
        stdscr.clear()
        
        # Dibujar los botones
        for idx, label in enumerate(buttons):
            draw_button(stdscr, button_y + idx, button_x, label, selected=(idx == current_button))
        
        stdscr.refresh()
        
        # Esperar la entrada del usuario
        key = stdscr.getch()
        
        if key == curses.KEY_UP and current_button > 0:
            current_button -= 1
        elif key == curses.KEY_DOWN and current_button < len(buttons) - 1:
            current_button += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            # Manejar la acción del botón presionado
            if current_button == 0:
                stdscr.addstr(15, 20, "Botón 'Aceptar' presionado")
            elif current_button == 1:
                stdscr.addstr(15, 20, "Botón 'Cancelar' presionado")
                break

        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)
