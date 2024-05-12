from PIL import Image


def merge(im1, im2, im3):
    coef = 0.935
    w = int(coef * 3 * im1.size[0])
    h = int(coef * im1.size[1])
    im = Image.new("RGBA", (w, h))

    coef = 0.91
    im.paste(im1)
    im.paste(im2, (int(coef * im1.size[0]), 0))
    im.paste(im3, (int(coef * 2 * im1.size[0]), 0))

    return im


im1 = Image.open("results/img/img_1.png")
im2 = Image.open("results/img/img_5.png")
im3 = Image.open("results/img/img_10.png")

merge(im1, im2, im3).show()
