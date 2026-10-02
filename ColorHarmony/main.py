from color_engine import hex_to_rgb, rgb_to_hex,  rgb_to_hsv, hsv_to_rgb, get_complementary, get_Analogous, get_triadic
color = "#3498DB"

print("Base:", color)
print("triadic:", get_triadic(color))