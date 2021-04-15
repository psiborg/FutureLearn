#!/usr/bin/env python3
# programming-with-guis
# Ex. 3.5

# https://www.fastfoodprice.com/menu/starbucks-prices/
# https://www.flaticon.com/packs/android-app-4/

from guizero import App, Box, ButtonGroup, Combo, Picture, PushButton, Text, TextBox

qty_min = 0
qty_max = 10

def update_total():
    americano_total = americano["txt_price_calc"].value.replace('$', '')
    latte_total = latte["txt_price_calc"].value.replace('$', '')
    mocha_total = mocha["txt_price_calc"].value.replace('$', '')
    txt_total_calc.value = "$" + format(float(americano_total) + float(latte_total) + float(mocha_total), '.2f')

def update_price(product):
    #print("upd")
    price = product["txt_price_unit_value"].value.replace('$', '')
    product["txt_price_calc"].value = "$" + format(float(price) * int(product["txb_qty"].value), '.2f')
    update_total()

def add_item(product):
    if int(product["txb_qty"].value) < qty_max:
        print("add")
        product["txb_qty"].value = int(product["txb_qty"].value) + 1
        update_price(product)

def del_item(product):
    if int(product["txb_qty"].value) > qty_min:
        print("del")
        product["txb_qty"].value = int(product["txb_qty"].value) - 1
        update_price(product)

app = App(title="Food Delivery App", layout="grid", bg="#FFFFFF")

americano = {}
americano["pic"] = Picture(app, image="./assets/starbucks/caffe_americano.gif", grid=[0,0,1,4])
americano["txt_name"] = Text(app, text="Caffè Americano", size=18, grid=[1,0,2,1], align="left")
americano["txt_spacer"] = Text(app, text="", size=18, width=15, grid=[3,0,1,1])
americano["txt_price_calc"] = Text(app, text="$0.00", size=14, grid=[4,0,1,1])
americano["txt_price_unit_label"] = Text(app, text="Price:", grid=[1,1], align="left")
americano["txt_price_unit_value"] = Text(app, text="$2.95", grid=[2,1], align="left")
americano["txt_cals_label"] = Text(app, text="Calories:", grid=[1,2], align="left")
americano["txt_cals_value"] = Text(app, text="15", grid=[2,2], align="left")
americano["txt_qty_label"] = Text(app, text="Quantity:", grid=[1,3], align="left")
americano["box_qty"] = Box(app, layout="auto", grid=[2,3], align="left")
americano["txb_qty"] = TextBox(americano["box_qty"], text="0", width=2, align="left", enabled=False)
americano["btn_del"] = PushButton(americano["box_qty"], text="-", image="./assets/mini_minus.gif", align="left", command=del_item, args=[americano])
americano["btn_add"] = PushButton(americano["box_qty"], text="+", image="./assets/mini_plus.gif", align="left", command=add_item, args=[americano])

latte = {}
latte["pic"] = Picture(app, image="./assets/starbucks/caffe_latte.gif", grid=[0,4,1,4])
latte["txt_name"] = Text(app, text="Caffè Latte", size=18, grid=[1,4,2,1], align="left")
latte["txt_spacer"] = Text(app, text="", size=18, width=15, grid=[3,4,1,1])
latte["txt_price_calc"] = Text(app, text="$0.00", size=14, grid=[4,4,1,1])
latte["txt_price_unit_label"] = Text(app, text="Price:", grid=[1,5], align="left")
latte["txt_price_unit_value"] = Text(app, text="$3.95", grid=[2,5], align="left")
latte["txt_cals_label"] = Text(app, text="Calories:", grid=[1,6], align="left")
latte["txt_cals_value"] = Text(app, text="190", grid=[2,6], align="left")
latte["txt_qty_label"] = Text(app, text="Quantity:", grid=[1,7], align="left")
latte["box_qty"] = Box(app, layout="auto", grid=[2,7], align="left")
latte["txb_qty"] = TextBox(latte["box_qty"], text="0", width=2, align="left", enabled=False)
latte["btn_del"] = PushButton(latte["box_qty"], text="-", image="./assets/mini_minus.gif", align="left", command=del_item, args=[latte])
latte["btn_add"] = PushButton(latte["box_qty"], text="+", image="./assets/mini_plus.gif", align="left", command=add_item, args=[latte])

mocha = {}
mocha["pic"] = Picture(app, image="./assets/starbucks/caffe_mocha.gif", grid=[0,8,1,4])
mocha["txt_name"] = Text(app, text="Caffè Mocha", size=18, grid=[1,8,2,1], align="left")
mocha["txt_spacer"] = Text(app, text="", size=18, width=15, grid=[3,8,1,1])
mocha["txt_price_calc"] = Text(app, text="$0.00", size=14, grid=[4,8,1,1])
mocha["txt_price_unit_label"] = Text(app, text="Price:", grid=[1,9], align="left")
mocha["txt_price_unit_value"] = Text(app, text="$4.45", grid=[2,9], align="left")
mocha["txt_cals_label"] = Text(app, text="Calories:", grid=[1,10], align="left")
mocha["txt_cals_value"] = Text(app, text="360", grid=[2,10], align="left")
mocha["txt_qty_label"] = Text(app, text="Quantity:", grid=[1,11], align="left")
mocha["box_qty"] = Box(app, layout="auto", grid=[2,11], align="left")
mocha["txb_qty"] = TextBox(mocha["box_qty"], text="0", width=2, align="left", enabled=False)
mocha["btn_del"] = PushButton(mocha["box_qty"], text="-", image="./assets/mini_minus.gif", align="left", command=del_item, args=[mocha])
mocha["btn_add"] = PushButton(mocha["box_qty"], text="+", image="./assets/mini_plus.gif", align="left", command=add_item, args=[mocha])

txt_total_label = Text(app, text="Order Total:", size=18, grid=[3,12,1,1])
txt_total_calc = Text(app, text="$0.00", size=18, grid=[4,12,1,1])

app.display()
