import sys
from PIL import Image, ImageOps


def shirt():
    if len(sys.argv) == 3:
        extensions = ["jpg", "jpeg", "png"]
        _, ext1 = sys.argv[1].split(".")
        _, ext2 = sys.argv[2].split(".")
        try:
            if ext1 in extensions and ext2 in extensions:
                if ext1 == ext2:
                    shirt = Image.open("shirt.png")
                    my_image = Image.open(sys.argv[1])
                    my_image = ImageOps.fit(my_image, (600, 600))
                    my_image.paste(shirt, shirt)
                    my_image.save(sys.argv[2])
                    return 0
                else:
                    sys.exit("Input and output have different extensions")
            else:
                sys.exit("Some extension is wrong")
        except FileNotFoundError:
            sys.exit("Input does not exist")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")


def main():
    shirt()


if __name__ == "__main__":
    main()
