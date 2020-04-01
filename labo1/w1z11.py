import math as math
funkcje = ["kąt|sin|cos|tg|ctg"]
k30 = ["30| " + str(round(math.sin(math.radians(30)),2)) + "|" +
str(round(math.cos(math.radians(30)), 2)) + "|" +
str(round(math.tan(math.radians(30)), 2)) + "|" +
str(round(1/math.tan(math.radians(30)),2))]
k45 = ["45| " + str(round(math.sin(math.radians(45)),2)) + "|" +
str(round(math.cos(math.radians(45)), 2)) + "|" +
str(round(math.tan(math.radians(45)), 2)) + "|" +
str(round(1/math.tan(math.radians(45)),2))]
k60 = ["60| " + str(round(math.sin(math.radians(60)),2)) + "|" +
str(round(math.cos(math.radians(60)), 2)) + "|" +
str(round(math.tan(math.radians(60)), 2)) + "|" +
str(round(1/math.tan(math.radians(60)),2))]

print(f"{funkcje}\n{k30}\n{k45}\n{k60}")