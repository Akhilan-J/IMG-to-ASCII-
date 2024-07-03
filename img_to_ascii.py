import PIL.Image

ascii_chars = ["@", "!", "S", "?", "/", "+", ".", ";", ":", "*"]

def resize(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def gray(image):
    gray_image = image.convert("L")
    return gray_image

def pixel_to_ascii(image):
    pixels = image.getdata()
    characters = "".join(ascii_chars[pixel // 25] for pixel in pixels)
    return characters

def main(new_width=100):
    path = input("Enter path to an image: ")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "is not a valid path to an image.")
        return
    
    new_img = pixel_to_ascii(gray(resize(image)))
    pixel_count = len(new_img)
    ascii_img = "\n".join(new_img[i:(i + new_width)] for i in range(0, pixel_count, new_width))
    print(ascii_img)

    with open("pinal.txt", "w") as f:
        f.write(ascii_img)

if __name__ == "__main__":
    main()
