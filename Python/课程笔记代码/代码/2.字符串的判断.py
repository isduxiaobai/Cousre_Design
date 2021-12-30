# 字符串的判断
# str = "      "
# print(str.isspace())
# str = "sdjfhsjkdr89ew78r9"
# print(str.isalnum())
# str = "sdsdkjlfs#"
# print(str.isalpha())

# str = "Hello Python Kdsjfsd"
# print(str.istitle())

# str = "F435899"
# print(str.islower())

# 重点理解 ：
str = "1"
print(str)
print(str.isdecimal())
print(str.isdigit())
print(str.isnumeric())

# 判断不了小数
str1 = "1.88"
print(str1)
print(str1.isdecimal())
print(str1.isdigit())
print(str1.isnumeric())

str2 = "\u00b2"
print(str2)
print(str2.isdecimal())
print(str2.isdigit())
print(str2.isnumeric())

str3 = "一千一百零一"
print(str3)
print(str3.isdecimal())
print(str3.isdigit())
print(str3.isnumeric())

str4 = "壹贰叁肆伍陆柒捌玖拾佰仟萬亿"
print(str4)
print(str4.isdecimal())
print(str4.isdigit())
print(str4.isnumeric())




