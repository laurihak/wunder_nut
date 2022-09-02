from caesarcipher import CaesarCipher
from PIL import Image


def decrypt_image():
    img = Image.open('wunder_image.png')
    pixel_map = img.load()
    width, height = img.size
    mode = img.mode

    print(f'width: {width}, height: {height}')

    new_image = Image.new(mode, (width, height))
    new_pixel_map = new_image.load()

    for x in range(width):
        for y in range(height):
            r, g, b = pixel_map[x, y]
            # print(r, g, b)
            if(b == 229):
                new_pixel_map[x, y] = (0, 0, 0)
                continue
            new_pixel_map[x, y] = (r, g, b)

    new_image.show()


def decrypt_caesar():
    revealed_text = 'OCDNDNVNZXMZOGDNOJANKZGGNOCVODCVQZDIQZIOZYHT NZGAGVIB GJXFB GPZNOCZOJIB PZOJOCZMJJAJAOCZHJPOCG ZQDXJMKPNGDAONOCZQDXODHDIO JOCZVDMWTOCZDMVIE GZGDWZMVXJMKPNDNVXJPIOZMEDISAJMGZQDXJMKPNHPAA GDVOJADGGNDONOVMBZONZUMNRDOCPIDYZIODADVWGZWP UUDIB NZXOPHNZHK MVDNAJMZIZHDZN'
    cipher = CaesarCipher(revealed_text)
    print(cipher.cracked)


decrypt_image()
decrypt_caesar()
