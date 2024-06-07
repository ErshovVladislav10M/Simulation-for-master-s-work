from PIL import Image


def merge(im1, im2, im3, im4):
    w = int(im1.size[0] + im2.size[0])
    h = int(im1.size[1] + im2.size[1])
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2, (int(im1.size[0]), 0))
    im.paste(im3, (0, int(im1.size[1])))
    im.paste(im4, (int(im1.size[0]), int(im1.size[1])))

    return im


im1 = Image.open("results/for_presentation/img/img_1.png")
im2 = Image.open("results/for_presentation/img/img_5.png")
im3 = Image.open("results/for_presentation/img/img_10.png")
im4 = Image.open("results/for_presentation/img/img_15.png")

im = merge(im1, im2, im3, im4)
# im.show()

im.save(fp="results/for_presentation/merging.png")
