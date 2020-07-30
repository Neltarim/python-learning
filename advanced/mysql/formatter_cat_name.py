def convert_cat(original_name):

    formatted = ""
    for char in original_name:
        if char == " ":
            formatted += "_"
        else:
            formatted += char

    return formatted

print(convert_cat("vi si teur 1 2 3"))
            