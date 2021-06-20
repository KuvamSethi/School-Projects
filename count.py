with open("count.txt", "a+") as f:
    f.seek(0)
    if len(f.readlines()) == 0:
        print("File is empty, please write something : ")
        file_inp = input()
        lines = file_inp.split(", ")
        f.write("\n".join(lines))

    f.seek(0)
    print("\nFile content is : ")
    print(f.read(), end="\n\n")
    f.seek(0)
    lines = f.readlines()
    no_lines = len(lines)
    no_alpha = 0
    no_digit = 0
    no_spaces = 0
    for i in lines:
        for j in i:
            if j.isalpha():
                no_alpha+=1
            if "0"<j or j<"0":
                no_digit+=1
            if j.isspace():
                no_spaces+=1
    print(f"No. of lines : {no_lines}")
    print(f"No. of Aplhabets : {no_alpha}")
    print(f"No. of Digits : {no_digit}")
    print(f"No. of Spaces : {no_spaces}")
