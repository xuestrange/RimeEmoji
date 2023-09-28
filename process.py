import re

f1 = open("./emoji.txt", "r", encoding="utf-8")
f2 = open("./emoji2.txt", "w+", encoding="utf-8")

e_sep = " "
for line in f1.readlines():
    line_list = re.split("\t|\n|\s", line.strip())
    elist = ["" for i in range(len(line_list) - 2)]
    for e in range(2, len(line_list)):
        elist[e - 2] = f"{line_list[0]}{line_list[e]}"
    f2.write(
        f"{line_list[0]}\t{line_list[1]} {e_sep.join(elist)} {e_sep.join(line_list[2:])}\n"
    )
f1.close()
f2.close()
