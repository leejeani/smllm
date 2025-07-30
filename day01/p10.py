if __name__ == '__main__':

    while True:
        cmd = input("Input Cmd");
        if cmd == "s":
            cmd = input("Input Id");
            print("Select Id:", cmd)
        if cmd == "sa":
            print("Select All")
        if cmd == "q":
            print("Quit Bye")
            break


