import colorsys

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")

    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    return r, g, b

#RGB to HEX
def rgb_to_hex(r, g, b):
    return "#{:02X}{:02X}{:02X}".format(r, g, b)

def rgb_to_hsv(r, g, b):
    r /= 255
    g /= 255
    b /= 255

    h, s, v = colorsys.rgb_to_hsv(r, g, b)

    return h * 360, s, v

def hsv_to_rgb(h, s, v):
    h = h / 360

    r, g, b = colorsys.hsv_to_rgb(h, s, v)

    return (
        round(r * 255),
        round(g * 255),
        round(b * 255)
    )

def get_complementary(hex_color):
    r, g, b = hex_to_rgb(hex_color)

    h, s, v = rgb_to_hsv(r, g, b)

    complementary_hue = (h + 180) % 360

    r, g, b = hsv_to_rgb(
        complementary_hue,
        s,
        v
    )

    return rgb_to_hex(r, g, b)

def get_Analogous(hex_color):
    r, g, b = hex_to_rgb(hex_color)
    h, s, v = rgb_to_hsv(r, g, b)


    Analogous_hue1 = (h -30) % 360
    Analogous_base = (h)
    Analogous_hue2 = (h + 30) % 360

    r1, g1, b1 =hsv_to_rgb(
        Analogous_hue1, s, v
        )
    color1 = rgb_to_hex(r1, g1, b1)

    # rb, gb, bb =hsv_to_rgb(
    #     Analogous_base, s, v
    #     )
    # color2 = rgb_to_hex(rb, gb, bb)

    color2 = hex_color

    r2, g2, b2 =hsv_to_rgb(
        Analogous_hue2, s, v
        )
    color3 = rgb_to_hex(r2, g2, b2)

    return color1, color2, color3


