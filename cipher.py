from PIL import Image

def encodemessage(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result


def decodemessage(bits):
    chars = []
    for b in range(len(bits) // 8):
        byte = bits[b * 8:(b + 1) * 8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)


def replacechar(string, index, letter):
    s = list(string)
    s[index] = str(letter)
    return "".join(s)


def getchar(string, index):
    s = list(string)
    return s[index]


def cipher(pathoffolder, xoffset, yoffset, message, bit, color):
    bits = encodemessage(message)
    imageoriginal = Image.open(pathoffolder + '\\in.bmp')
    image = imageoriginal

    for x in range(0, len(bits)):
        r, g, b = image.getpixel((xoffset + x, yoffset))

        r = '{0:08b}'.format(r)
        g = '{0:08b}'.format(g)
        b = '{0:08b}'.format(b)

        if color == "r":
            r = replacechar(r, bit, bits[x])
        elif color == "g":
            g = replacechar(g, bit, bits[x])
        elif color == "b":
            b = replacechar(b, bit, bits[x])

        r = int(r, 2)
        g = int(g, 2)
        b = int(b, 2)
        image.putpixel((xoffset + x, yoffset), (r, g, b))

    image.save(pathoffolder + '\\out.bmp')
    print("Image ciphered!")


def decipher(pathoffolder, xoffset, yoffset, messagelen, bit, color):
    bits = []
    image = Image.open(pathoffolder + '\\out.bmp')
    messagelen = messagelen * 8  # bitów
    for x in range(0, messagelen):
        r, g, b = image.getpixel((xoffset + x, yoffset))

        r = '{0:08b}'.format(r)
        g = '{0:08b}'.format(g)
        b = '{0:08b}'.format(b)

        letter = ""
        if color == "r":
            letter = getchar(r, bit)
        elif color == "g":
            letter = getchar(g, bit)
        elif color == "b":
            letter = getchar(b, bit)

        bits.append(letter)
    a = decodemessage(bits)
    return decodemessage(bits)


message = "I love cookies and I don't say it to anyone" #message to cipher
print(message)
xof = 0 #offset of changes on x axis
yof = 100 #offset of changes on y axis
path = "C:\\Users\\50215\\Desktop" #specify path of folder, where the file in.bmp is
color = "r" #select from 'r' 'g' 'b' to specify which color you want to cipher on
bit = 1 #contains the number of bit to cipher on; if 2 then bit 00#00000 will be changed and so on
        #                                                         ^
messagelen = len(message)
cipher(path, xof, yof, message, bit, color)
deciphered = decipher(path, xof, yof, messagelen, bit, color)
print("Deciphered messaage: ")
print(deciphered)
