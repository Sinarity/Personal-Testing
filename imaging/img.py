from PIL import Image

ASCII_CHARS = list(
    "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`'. "
)
ASCII_CHARS = ASCII_CHARS[::+1]

# - takes as parameters the image, and the final width
# - resizes the image into the final width while maintaining aspect ratio


def resize(image, new_width=975):
    (old_width, old_height) = image.size
    aspect_ratio = float(old_height) / float(old_width)
    new_height = int(aspect_ratio * new_width)
    new_dim = (new_width, new_height)
    new_image = image.resize(new_dim)
    return new_image

    # - takes an image as a parameter
    # - returns the grayscale version of image


def grayscalify(image):
    return image.convert("L")

    # replaces every pixel with a character whose intensity is similar


def modify(image, buckets=35):
    initial_pixels = list(image.getdata())
    new_pixels = [ASCII_CHARS[pixel_value // buckets] for pixel_value in initial_pixels]
    return "".join(new_pixels)


"""
method do():
    - does all the work by calling all the above functions
"""


def do(image, new_width=975):
    image = resize(image)
    image = grayscalify(image)

    pixels = modify(image)
    len_pixels = len(pixels)

    # Construct the image from the character list
    new_image = [
        pixels[index : index + new_width] for index in range(0, len_pixels, new_width)
    ]

    return "\n".join(new_image)

    # - takes as parameter the image path and runs the above code
    # - handles exceptions as well
    # - provides alternative output options


def runner(path):
    image = None
    try:
        image = Image.open(path)
    except Exception:
        print("Unable to find image in", path)
        # print(e)
        return
    image = do(image)

    # To print on console
    #    print(image)

    # Else, to write into a file in the same directory as 'img.py'
    f = open("img.txt", "w")
    f.write(image)
    f.close()

    # - reads input from console
    # - makes ASCII art


if __name__ == "__main__":
    import sys
    import urllib.request

    if sys.argv[1].startswith("http://") or sys.argv[1].startswith("https://"):
        urllib.request.urlretrieve(sys.argv[1], "asciify.jpg")
        path = "asciify.jpg"
    else:
        path = sys.argv[1]
    runner(path)
    print("Done. created img.txt in the same directory as img.py")
