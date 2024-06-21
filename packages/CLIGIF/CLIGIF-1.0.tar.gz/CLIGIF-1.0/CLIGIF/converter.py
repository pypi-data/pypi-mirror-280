from PIL import Image
def calculate_aspect(width: int, height: int) -> str:
    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)
    r = gcd(width, height)
    x = int(width / r)
    y = int(height / r)
    return x, y

def convert(img, scale_multiplier = 6):
    im = img
    width, height = im.size
    ratio_w, ratio_h = calculate_aspect(width, height)
    n_w, n_h = ratio_w*scale_multiplier, ratio_h*scale_multiplier
    new_img = im.resize((n_w, n_h))
    return new_img
    

