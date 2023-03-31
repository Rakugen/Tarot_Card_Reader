# README for Tarot Reader Application

# Things that I had to fix/solve:
# - Problem: Had a folder of images and needed a list of their file names.
# - Solution: Shift+Right Click on folder -> "Open with PowerShell Window Here". Type "dir > filenames.txt" . Then I had
#     to open in Sublime and Save As With Encoding -> UTF-8. Making sure to format the header, removing everything on top
#     but the column names that I wanted. Then used pandas.read_fwf() and the correct column name (via file_names.columns)
#     After string formatting I saved into a file and copy/pasted that into my IMAGE_NAMES global list.
#
#     # file_names = pandas.read_fwf("./images/filenames.txt", sep=" ")
#     # files = file_names["Name"].to_list()
#     # file_string = ""
#     # for filename in files:
#     #     file_string += f"'{filename}', "
#     #
#     # with open("new_file.txt", mode="w") as file:
#     #     file.write(file_string)
#
# - Problem: My flip_new() function was not working correctly. New card images were not appearing after 3 new ones were chosen.
# - Solution: The issue was pythons garbage collection since the variables that held the new PhotoImage objects were
#     inside a function, they were immediately disposed of after function call. Solution was to make sure the PhotoImage
#     objects persisted, so I used global variables and saved them into a List.
#
# - Problem: There needs to be 2 sides for each card, randomly picking should not allow choosing the same card side A and B
# - Possible Solution: Create a list of card names, refactor image names to match. When randomly picking card, pick from list
#     and random choose A or B, so a random.sample(cards) followed by a random.choice(A or B).
#
#     temp_list = []
#     for card in IMAGE_NAMES:
#         temp_name = (card.split(".")[1][1:])
#         if temp_name not in temp_list:
#             temp_list.append(temp_name)
#     print(temp_list)
#
