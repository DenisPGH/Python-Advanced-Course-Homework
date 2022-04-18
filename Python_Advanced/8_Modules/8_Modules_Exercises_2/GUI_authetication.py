
import tkinter as tk
import json
PATH_TO_USERS_DB= "users"
PATH_TO_PRODUCTS_DB= "products_db/products"

def first_screen(win):
    """ this function start our first windows view"""
    clean_screen_function(win)
    tk.Button(win, text="LOGIN", fg="blue", bg="green", command=lambda :button_login(win)).grid(row=0, column=0)
    tk.Button(win, text="REGISTER", fg="blue", bg="green", command= lambda :button_register(win)).grid(row=0, column=1)


def button_register(win):
    """ this function come, when we press register button
     then we check, if there is some name , and if not add the user to my datebase
     and return some messages"""
    clean_screen_function(win)
    tk.Label(text="Enter Your name:",fg="blue").grid(row=0,column=0)
    username=tk.Entry(win)
    username.grid(row=0,column=1)
    tk.Label(text="Enter Your email:", fg="blue").grid(row=1, column=0)
    email = tk.Entry(win)
    email.grid(row=1, column=1)
    tk.Label(text="Enter Your password:", fg="blue").grid(row=2, column=0)
    password= tk.Entry(win,show="*")
    password.grid(row=2, column=1)
    tk.Label(text="Confirm Your password:", fg="blue").grid(row=3, column=0)
    conf_password = tk.Entry(win,show="*")
    conf_password.grid(row=3, column=1)

    tk.Button(win, text="Register", fg="black",
              command=lambda: store_user_date_after_register_button(win, username.get(), email.get(), password.get(), conf_password.get())).grid(row=5, column=1)


def button_login(win):
    """ if the client press login button, show new windows and call other function,
     where we prove if we have such user"""
    clean_screen_function(win)
    tk.Label(text="Enter Your name:", fg="blue").grid(row=0, column=0)
    username = tk.Entry(win)
    username.grid(row=0, column=1)
    tk.Label(text="Enter Your password:", fg="blue").grid(row=1, column=0)
    password = tk.Entry(win,show="*")
    password.grid(row=1, column=1)
    tk.Button(win, text="LOG IN", fg="Blue",
              command=lambda: prove_date_after_login_button(win,username.get(),password.get())).grid(row=3,column=1)
    tk.Button(win, text="BACK", fg="Red",
              command=lambda: first_screen(win)).grid(row=3, column=2)


def loged(win,person):
    """ this function must show the list with the product and prices, after login of the client"""
    person_orders=[]
    clean_screen_function(win)
    tk.Label(text="MY PRODUCT ARE:", fg="Blue").grid(row=0, column=0)
    counter=0
    with open(PATH_TO_PRODUCTS_DB,"r+") as product:
        for each in product:
            counter+=1
            current_product=json.loads(each)
            id=current_product["id"]
            name=current_product["name"]
            pic=current_product["pic"]
            price=current_product["price"]
            quant=current_product["quantity"]
            tk.Label(text=f"ID: {id}", fg="Blue").grid(row=1, column=counter)
            tk.Label(text=f"NAME: {name}", fg="Black").grid(row=2, column=counter)
            # img=Image.open(current_product["pic"]).resize((70,70))
            # photo_image=ImageTk.PhotoImage(img)
            # image_label=tk.Image(image=photo_image)
            # image_label.image=photo_image
            # image_label.grid(row=3, column=counter)


            tk.Label(text=f"PICTURE: {pic}", fg="Black").grid(row=3, column=counter)
            tk.Label(text=f"Price: {price}", fg="Black").grid(row=4, column=counter)
            tk.Label(text=f"Quantity: {quant}", fg="Black").grid(row=5, column=counter)
            # buy button until the item
            tk.Button(text="Buy", fg="Green",
                      command= lambda b=current_product['id']: stuffs_buy_from_user(win,person,b , person_orders)).grid(row=6, column=counter)

    tk.Label(text=f"{person} IS HERE", fg="Green",bg="White").grid(row=7, column=6)


def store_user_date_after_register_button(win, user, email, passw, conf_pass):

    """ this function check if we have same name as user, if not store the new user in our db
    and prove is password is same 2 times"""
    one_user={"id": 1,"user":user,"email":email,"password": passw, "products":[]}
    if passw !=conf_pass: # if password is wrong give mssg
        tk.Label(text="Not same password",fg="red").grid(row=4,column=1)

    else: # the password is correct, have to check if user is registe
        current_dict={}
        already_has=False
        with open(PATH_TO_USERS_DB, "r") as user_a: # provi in my_db if has such name
            for each in user_a:
                current_dict=json.loads(each)
                if user == current_dict["user"]:
                    already_has=True
        if not already_has: # if nobody with same name register it
            with open(PATH_TO_USERS_DB, "a") as user_b:
                user_b.write(f'{json.dumps(one_user)} \n')
        if already_has:
            tk.Label(text="Such username in my system already", fg="red").grid(row=4, column=1)
        else:
            button_login(win)


def prove_date_after_login_button(win,user_name,password_):
    person_name=""
    """ this function prove if name and password are correct, if yes call other function with products,
    if not show mssg"""
    correct_user=False
    with open(PATH_TO_USERS_DB) as db_user:
        for each in db_user:
            current_dict=json.loads(each)
            if user_name==current_dict["user"] and password_==current_dict["password"]:
                correct_user=True
                person_name=current_dict["user"] # store the name of the user
                break

    if correct_user: # if the password was ok, start new func with the products
        loged(win,person_name)
    else:
        tk.Label(text="Password or Username not correct!", fg="red").grid(row=4, column=1)


def stuffs_buy_from_user(win, person, item_id, all_items):
    """ this function work on buing products, add bought stuffs to user-account,
     and reduce quantity of bought thing
     and show the korb of the user(with all bought things)"""

    all_items.append(item_id)
    tk.Label(text=f"Korb of {person}:", fg="Green", bg="White").grid(row=8, column=8)
    tk.Label(text=f"{all_items}", fg="Green", bg="White").grid(row=9, column=8)

    # here I add the bought stuffs to the user account
    try:
        with open(PATH_TO_USERS_DB, "r+") as user:
            result = []
            for each in user:
                if each != '\n':
                    cur_dict = json.loads(each.strip())
                    if cur_dict["user"] == person:
                        cur_dict["products"].append(item_id)
                        result.append(json.dumps(cur_dict) + "\n")
                    else:
                        result.append(each)
            user.seek(0)
            user.truncate()
            user.writelines(result)
    except Exception:
        print("Error by buy_corb")
    # here I have to reduce the count of the bought item
    with open(PATH_TO_PRODUCTS_DB, "r+") as product:
        result_2 = []
        for every in product:
            if every != "\n":
                cur_dict_item = json.loads(every.strip())
                if cur_dict_item["id"] == item_id:
                    if cur_dict_item["quantity"] > 0:  # the quantite is more 1
                        cur_dict_item["quantity"] -= 1
                    else:
                        tk.Label(text="Sold out", fg="Red").grid(row=9, column=9)
                    result_2.append(json.dumps(cur_dict_item) + "\n")


                else:
                    result_2.append(every)
        product.seek(0)
        product.truncate()
        product.writelines(result_2)
    loged(win, person)  # show again the loged windws

    # here we show the window with bought stuffs
    tk.Label(text=f"Korb of {person}:", fg="Green", bg="White").grid(row=10, column=6)
    list_products_person = []
    with open(PATH_TO_USERS_DB, "r") as user_2:
        for each_2 in user_2:
            if each_2 != '\n':
                cur_dict_2 = json.loads(each_2.strip())
                if cur_dict_2["user"] == person:
                    list_products_person = cur_dict_2["products"]

    tk.Label(text=f"{list_products_person}", fg="Green", bg="White").grid(row=11, column=6)



def clean_screen_function(win):
    """ this function cleen the scree, when call it"""
    for each in win.winfo_children():
        each.destroy()













