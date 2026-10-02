from color_engine import hex_to_rgb, rgb_to_hex,  rgb_to_hsv, hsv_to_rgb, get_complementary, get_Analogous, get_triadic, get_tetradic
color = "#3498DB"

print("Base:", color)
print("tetradic:", get_tetradic(color))