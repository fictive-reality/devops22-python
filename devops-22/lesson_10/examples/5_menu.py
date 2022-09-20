from app import App


def main():
    app = App()
    app.setup({'players': 2})
    app.start_loop()


if __name__ == '__main__':
    main()
