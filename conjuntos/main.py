profes = {"carlos"}

futbol = {"nacho", "beltran", "agustin", "carlos", "alvaro"}

voley = {"serafin", "galo", "alvaro", "flor", "carlos" }

hockey = {"melisa", "nicolas", "juan"}

if __name__ == "__main__":
    jugan_futbol_y_voley = futbol & voley
    print(jugan_futbol_y_voley)

    jugan_futbol_o_hocke = futbol | hockey
    print("Los que juegan futbol o hockey son:")
    for i, nombre in enumerate(jugan_futbol_o_hocke):
        print(f"{i + 1}. {nombre}")

    juegan_todo_menos_voley = (futbol | hockey) - voley
    print(juegan_todo_menos_voley)

    todos_jugadores = futbol | voley | hockey
    print(todos_jugadores)

    tiene_profes = profes.issubset(futbol)

    print(f"tiene profes: {tiene_profes}")
