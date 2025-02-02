def Reverse(string):
    left, right = 0, 0
    reverse = " "

    while right < len(string):
        if string[right] != " ":
            right += 1
        else:
            reverse += string[left:right][::-1] + " "
            right += 1
            left = right

    reverse += string[left:][::-1]
    return reverse.strip()

print(Reverse("Hello World"))