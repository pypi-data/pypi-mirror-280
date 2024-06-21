import pyfiglet

def main(name='POOZZZZZZZITH'):
    figlet = pyfiglet.Figlet(font='slant')
    fancy_name = figlet.renderText(name)
    print(fancy_name)

def print_name():
    main()
    main()
    main()
    main()