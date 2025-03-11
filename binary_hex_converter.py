# -*- coding: utf-8 -*-
"""binary_hex_converter.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ex5gO3bs_uv9j_qolhZZfFQIkNIwQ5fX
"""

decimal_number = int(input("請輸入數字(0~255)："))

def decimal_to_binary(decimal):
    binary = ""

    for power in range(7, -1, -1):
        power_value = 2 ** power

        if decimal >= power_value:
            binary += "1"
            decimal -= power_value
        else:
            binary += "0"

    return binary

def binary_to_hex(binary):
    hex_digits = "0123456789ABCDEF"
    binary = binary.zfill(8)
    hex_result = ""

    for i in range(0, 8, 4):
        four_bits = binary[i:i+4]
        hex_value = hex_digits[int(four_bits, 2)]
        hex_result += hex_value

    return hex_result

if 0 <= decimal_number <= 255:
    binary_result = decimal_to_binary(decimal_number)
    hex_result = binary_to_hex(binary_result)

    print(f"{decimal_number} 以二進位表示為: {binary_result}")
    print(f"{decimal_number} 以16進位表示為: {hex_result}")
else:
    print("請輸入限定範圍內的數字")

