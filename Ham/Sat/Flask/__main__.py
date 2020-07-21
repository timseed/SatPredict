from Ham.Sat.Flask.controllers.app import app
from Ham.Sat.Flask.controllers.app import create_logger

from sys import argv

def main():
    app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    if len(argv)<2:
        create_logger(None)
    else:
        create_logger(argv[1])
    import Ham.Sat.Flask.controllers.form

    main()