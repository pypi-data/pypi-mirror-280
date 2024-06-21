import pyfiglet

def main(name='POOZZZZZZZITH'):
    figlet = pyfiglet.Figlet(font='slant')
    fancy_name = figlet.renderText(name)
    print(fancy_name)

if __name__ == '__main__':
    main()
    main()
    main()
    main()