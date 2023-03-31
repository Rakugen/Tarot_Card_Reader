# --------------------- IMPORTS ---------------------
from tkinter import *
from PIL import ImageTk, Image
import random
import pandas

# --------------------- GLOBALS ---------------------
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 14, "bold")
CARD_FONT = ("Arial", 14)
BUTTON_FONT = ("Arial", 28, "bold")
COLOR1 = "#E3FDFD"
COLOR2 = "#CBF1F5"
COLOR3 = "#A6E3E9"
COLOR4 = "#71C9CE"
IMAGE_NAMES = ['10A._Wheel_of_Fortune.png', '10B._Wheel_of_Fortune.png', '11A._Justice.png', '11B._Justice.png',
               '12A._The_Hanged_Man.png', '12B._The_Hanged_Man.png', '13A._Death.png', '13B._Death.png',
               '14A._Temperance.png', '14B._Temperance.png', '15A._The_Devil.png', '15B._The_Devil.png',
               '16A._The_Tower.png', '16B._The_Tower.png', '17A._The_Star.png', '17B._The_Star.png',
               '18A._The_Moon.png', '18B._The_Moon.png', '19A._The_Sun.png', '19B._The_Sun.png',
               '1A._The_Magician.png', '1B._The_Magician.png', '20A._Judgement.png', '20B._Judgement.png',
               '21A._The_World.png', '21B._The_World.png', '22A._The_Fool.png', '22B._The_Fool.png',
               '23A._Ace_of_Cups.png', '23B._Ace_of_Cups.png', '24A._Two_of_Cups.png', '24B._Two_of_Cups.png',
               '25A._Three_of_Cups.png', '25B._Three_of_Cups.png', '26A._Four_of_Cups.png', '26B._Four_of_Cups.png',
               '27A._Five_of_Cups.png', '27B._Five_of_Cups.png', '28A._Six_of_Cups.png', '28B._Six_of_Cups.png',
               '29A._Seven_of_Cups.png', '29B._Seven_of_Cups.png', '2A._The_High_Priestess.png',
               '2B._The_High_Priestess.png', '30A._Eight_of_Cups.png', '30B._Eight_of_Cups.png',
               '31A._Nine_of_Cups.png', '31B._Nine_of_Cups.png', '32A._Ten_of_Cups.png', '32B._Ten_of_Cups.png',
               '33A._Page_of_Cups.png', '33B._Page_of_Cups.png', '34A._Knight_of_Cups.png', '34B._Knight_of_Cups.png',
               '35A._Queen_of_Cups.png', '35B._Queen_of_Cups.png', '36A._King_of_Cups.png', '36B._King_of_Cups.png',
               '37A._Ace_of_Pentacles.png', '37B._Ace_of_Pentacles.png', '38A._Two_of_Pentacles.png',
               '38B._Two_of_Pentacles.png', '39A._Three_of_Pentacles.png', '39B._Three_of_Pentacles.png',
               '3A._The_Empress.png', '3B._The_Empress.png', '40A._Four_of_Pentacles.png', '40B._Four_of_Pentacles.png',
               '41A._Five_of_Pentacles.png', '41B._Five_of_Pentacles.png', '42A._Six_of_Pentacles.png',
               '42B._Six_of_Pentacles.png', '43A._Seven_of_Pentacles.png', '43B._Seven_of_Pentacles.png',
               '44A._Eight_of_Pentacles.png', '44B._Eight_of_Pentacles.png', '45A._Nine_of_Pentacles.png',
               '45B._Nine_of_Pentacles.png', '46A._Ten_of_Pentacles.png', '46B._Ten_of_Pentacles.png',
               '47A._Page_of_Pentacles.png', '47B._Page_of_Pentacles.png', '48A._Knight_of_Pentacles.png',
               '48B._Knight_of_Pentacles.png', '49A._Queen_of_Pentacles.png', '49B._Queen_of_Pentacles.png',
               '4A._The_Emperor.png', '4B._The_Emperor.png', '50A._King_of_Pentacles.png', '50B._King_of_Pentacles.png',
               '51A._Ace_of_Swords.png', '51B._Ace_of_Swords.png', '52A._Two_of_Swords.png', '52B._Two_of_Swords.png',
               '53A._Three_of_Swords.png', '53B._Three_of_Swords.png', '54A._Four_of_Swords.png',
               '54B._Four_of_Swords.png', '55A._Five_of_Swords.png', '55B._Five_of_Swords.png',
               '56A._Six_of_Swords.png', '56B._Six_of_Swords.png', '57A._Seven_of_Swords.png',
               '57B._Seven_of_Swords.png', '58A._Eight_of_Swords.png', '58B._Eight_of_Swords.png',
               '59A._Nine_of_Swords.png', '59B._Nine_of_Swords.png', '5A._The_Hierophant.png',
               '5B._The_Hierophant.png', '60A._Ten_of_Swords.png', '60B._Ten_of_Swords.png', '61A._Page_of_Swords.png',
               '61B._Page_of_Swords.png', '62A._Knight_of_Swords.png', '62B._Knight_of_Swords.png',
               '63A._Queen_of_Swords.png', '63B._Queen_of_Swords.png', '64A._King_of_Swords.png',
               '64B._King_of_Swords.png', '65A._Ace_of_Wands.png', '65B._Ace_of_Wands.png', '66A._Two_of_Wands.png',
               '66B._Two_of_Wands.png', '67A._Three_of_Wands.png', '67B._Three_of_Wands.png', '68A._Four_of_Wands.png',
               '68B._Four_of_Wands.png', '69A._Five_of_Wands.png', '69B._Five_of_Wands.png', '6A._The_Lovers.png',
               '6B._The_Lovers.png', '70A._Six_of_Wands.png', '70B._Six_of_Wands.png', '71A._Seven_of_Wands.png',
               '71B._Seven_of_Wands.png', '72A._Eight_of_Wands.png', '72B._Eight_of_Wands.png',
               '73A._Nine_of_Wands.png', '73B._Nine_of_Wands.png', '74A._Ten_of_Wands.png', '74B._Ten_of_Wands.png',
               '75A._Page_of_Wands.png', '75B._Page_of_Wands.png', '76A._Knight_of_Wands.png',
               '76B._Knight_of_Wands.png', '77A._Queen_of_Wands.png', '77B._Queen_of_Wands.png',
               '78A._King_of_Wands.png', '78B._King_of_Wands.png', '7A._The_Chariot.png', '7B._The_Chariot.png',
               '8A._Strength.png', '8B._Strength.png', '9A._The_Hermit.png', '9B._The_Hermit.png'
               ]
CARD_NAMES = ['Wheel_of_Fortune', 'Justice', 'The_Hanged_Man', 'Death', 'Temperance', 'The_Devil', 'The_Tower',
              'The_Star', 'The_Moon', 'The_Sun', 'The_Magician', 'Judgement', 'The_World', 'The_Fool', 'Ace_of_Cups',
              'Two_of_Cups', 'Three_of_Cups', 'Four_of_Cups', 'Five_of_Cups', 'Six_of_Cups', 'Seven_of_Cups',
              'The_High_Priestess', 'Eight_of_Cups', 'Nine_of_Cups', 'Ten_of_Cups', 'Page_of_Cups', 'Knight_of_Cups',
              'Queen_of_Cups', 'King_of_Cups', 'Ace_of_Pentacles', 'Two_of_Pentacles', 'Three_of_Pentacles',
              'The_Empress', 'Four_of_Pentacles', 'Five_of_Pentacles', 'Six_of_Pentacles', 'Seven_of_Pentacles',
              'Eight_of_Pentacles', 'Nine_of_Pentacles', 'Ten_of_Pentacles', 'Page_of_Pentacles', 'Knight_of_Pentacles',
              'Queen_of_Pentacles', 'The_Emperor', 'King_of_Pentacles', 'Ace_of_Swords', 'Two_of_Swords',
              'Three_of_Swords', 'Four_of_Swords', 'Five_of_Swords', 'Six_of_Swords', 'Seven_of_Swords',
              'Eight_of_Swords', 'Nine_of_Swords', 'The_Hierophant', 'Ten_of_Swords', 'Page_of_Swords',
              'Knight_of_Swords', 'Queen_of_Swords', 'King_of_Swords', 'Ace_of_Wands', 'Two_of_Wands', 'Three_of_Wands',
              'Four_of_Wands', 'Five_of_Wands', 'The_Lovers', 'Six_of_Wands', 'Seven_of_Wands', 'Eight_of_Wands',
              'Nine_of_Wands', 'Ten_of_Wands', 'Page_of_Wands', 'Knight_of_Wands', 'Queen_of_Wands', 'King_of_Wands',
              'The_Chariot', 'Strength', 'The_Hermit'
              ]
# global list to make card images persist after made in a function call
PHOTO_IMAGES = []
# global list of canvas images to be referenced in flip_new()
CANVAS_IMAGES = []
# global list to track the randomly picked cards
PICKED_CARDS = []
TEXT_BOX = []
DEFAULT_CARD = "Card_Back.png"
CARD_LABELS = []
TITLE_LABELS = []

# TODO: refactor program to add type hints/type checking
# --------------------- CARD FUNCTIONS ---------------------
# randomly pick 3 new cards + side and store into global PICKED_CARDS
def pick_cards():
    global PICKED_CARDS
    unsided_cards = random.sample(CARD_NAMES, 3)
    for card in unsided_cards:
        side = random.choice(["A", "B"])
        PICKED_CARDS.append((card, side))


# Create new PHOTO_IMAGES of the 3 cards and displays them
def flip_new():
    global PHOTO_IMAGES
    PHOTO_IMAGES = []
    # print(PICKED_CARDS)
    # new_cards = random.sample(CARD_NAMES, 3)
    for x in range(3):
        # side = random.choice(['A', 'B'])
        new_img = ImageTk.PhotoImage(
            Image.open(f"./images/{PICKED_CARDS[x][1]}._{PICKED_CARDS[x][0]}.png").resize((224, 374)))
        canvas.itemconfig(CANVAS_IMAGES[x], image=new_img)
        PHOTO_IMAGES.append(new_img)
    # new_img1 = ImageTk.PhotoImage(Image.open(f"./images/{new_cards[0]}").resize((224, 374)))
    # new_img2 = ImageTk.PhotoImage(Image.open(f"./images/{new_cards[1]}").resize((224, 374)))
    # new_img3 = ImageTk.PhotoImage(Image.open(f"./images/{new_cards[2]}").resize((224, 374)))
    # PHOTO_IMAGES = [new_img1, new_img2, new_img3]
    # canvas.itemconfig(canvas_img1, image=new_img1)
    # canvas.itemconfig(canvas_img2, image=new_img2)
    # canvas.itemconfig(canvas_img3, image=new_img3)


# --------------------- TEXT FUNCTIONS ---------------------
# Initializing lists of card meanings from "Tarot Cards Meanings - Sheet1.csv" file
tarot_text = pandas.read_csv("./data/Tarot Cards Meanings - Sheet1.csv")
tarot_card_list = tarot_text['Tarot Card'].to_list()
side_a = tarot_text['Meaning (Side A)'].to_list()
side_b = tarot_text['Meaning (Side B)'].to_list()

# Creating the dictionary of meanings with format {CardName: {"A": A meaning, "B": B meaning}}
tarot_dict = {}
for i in range(len(tarot_card_list)):
    card_name = tarot_card_list[i]
    tarot_dict[card_name] = {"A": side_a[i], "B": side_b[i]}


# Shows the picked cards meanings on their text boxes
# TODO: fixup labels to look better
def generate_text():
    for i in range(3):
        text = tarot_dict[PICKED_CARDS[i][0]][PICKED_CARDS[i][1]]
        title_text = f"{PICKED_CARDS[i][0].replace('_', ' ')} - {PICKED_CARDS[i][1]}"
        CARD_LABELS[i].config(text=text)
        TITLE_LABELS[i].config(text=title_text)


# --------------------- BUTTON FUNCTIONS ---------------------
# main function call from button press that will call the appropriate functions
def read_new_cards():
    global PICKED_CARDS
    PICKED_CARDS = []

    pick_cards()
    flip_new()
    generate_text()


# --------------------- UI SETUP ---------------------
window = Tk()
window.title("Tarot Card Reader")
# TODO: add a background image
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# window.geometry("1024x720")
# Canvas
canvas = Canvas(width=1000, height=400, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=3)

# Choose random card images
# new_cards = random.sample(CARD_NAMES, 3)
# for x in range(0, 3):
#     # side = random.choice(['A', 'B'])
#     new_img = ImageTk.PhotoImage(Image.open(f"./images/{DEFAULT_CARD}").resize((224, 374)))
#     x_cord = int(200+(x*300))
#     canvas_img = canvas.create_image(x_cord, 200, image=new_img)
#     CANVAS_IMAGES.append(canvas_img)

# Image 1
image1 = ImageTk.PhotoImage(Image.open(f"./images/{DEFAULT_CARD}").resize((224, 374)))
canvas_img1 = canvas.create_image(160, 200, image=image1)

# Image 2
image2 = ImageTk.PhotoImage(Image.open(f"./images/{DEFAULT_CARD}").resize((224, 374)))
canvas_img2 = canvas.create_image(500, 200, image=image2)

# Image 3
image3 = ImageTk.PhotoImage(Image.open(f"./images/{DEFAULT_CARD}").resize((224, 374)))
canvas_img3 = canvas.create_image(840, 200, image=image3)
# Adding canvas images into global list so that it can be referenced in flip_new()
CANVAS_IMAGES = [canvas_img1, canvas_img2, canvas_img3]

# Buttons
# TODO: make this button better looking
read_button = Button(text="Read", font=BUTTON_FONT, bg=COLOR4, command=read_new_cards)
read_button.grid(column=1, row=3, padx=20, pady=20)

# Text Box
msg = "PLACEHOLDER"
# text_box1 = Text(height=5, width=20, wrap="word", padx=10, pady=10, font=("Arial", 14))
# text_box1.insert('end', msg)
# text_box1.config(state="disabled")
# text_box1.grid(column=0, row=1, columnspan=1)
#
# text_box2 = Text(height=5, width=20, wrap="word", padx=10, pady=10, font=("Arial", 14))
# text_box2.insert('end', msg)
# text_box2.config(state="disabled")
# text_box2.grid(column=1, row=1, columnspan=1)
#
# text_box3 = Text(height=5, width=20, wrap="word", padx=10, pady=10, font=("Arial", 14))
# text_box3.insert('end', msg)
# text_box3.config(state="disabled")
# text_box3.grid(column=2, row=1, columnspan=1)
# # global text box list for reference in generate_text()
# TEXT_BOX = [text_box1, text_box2, text_box3]

# LABELS

# LABELS
# TODO: add card titles under each card
title_label1 = Label(width=20, height=1, padx=2, pady=2, text="", font=TITLE_FONT, relief="sunken", bg=COLOR1)
title_label1.grid(column=0, row=1)
title_label2 = Label(width=20, height=1, padx=2, pady=2, text="", font=TITLE_FONT, relief="sunken", bg=COLOR1)
title_label2.grid(column=1, row=1)
title_label3 = Label(width=20, height=1, padx=2, pady=2, text="", font=TITLE_FONT, relief="sunken", bg=COLOR1)
title_label3.grid(column=2, row=1)
TITLE_LABELS = [title_label1, title_label2, title_label3]

card_label1 = Label(width=25, height=5, padx=10, pady=10, text=msg, font=CARD_FONT, relief="raised",
                    wraplength=250, bg=COLOR4)
card_label1.grid(column=0, row=2)

card_label2 = Label(width=25, height=5, padx=10, pady=10, text=msg, font=CARD_FONT, relief="raised",
                    wraplength=250, bg=COLOR4)
card_label2.grid(column=1, row=2)

card_label3 = Label(width=25, height=5, padx=10, pady=10, text=msg, font=CARD_FONT, relief="raised",
                    wraplength=250, bg=COLOR4)
card_label3.grid(column=2, row=2)

CARD_LABELS = [card_label1, card_label2, card_label3]

window.mainloop()
