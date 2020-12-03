from tkinter import *
import math
import random
from tkinter import messagebox
import os

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1425x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root, text = "Billing Software",bd =12,relief = GROOVE,bg =bg_color ,fg="white", font = ("times new roman",30,"bold"),pady = 2).pack(fill = X)

        ####################################
        #----------- Variables ------------#
        ####################################

            ####################################
            # ------------ Cosmetics ----------#
            ####################################

        self.soap = IntVar()
        self.face_cream = IntVar() 
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gell = IntVar()
        self.lotion = IntVar()
            
            ####################################
            # ----------- Grocery -------------#
            ####################################

        self.rice = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.daal = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

            ####################################
            # ----------- Cold Drinks ---------#
            ####################################

        self.thums_up = IntVar()
        self.sprite = IntVar()
        self.cocacola = IntVar()
        self.moutain_dew = IntVar()
        self.limca = IntVar()
        self.frooti = IntVar()

            ###########################################################
            # ---------- Total Product Price & Tax Variables ---------#
            ###########################################################
        
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()


        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

            
            ######################################
            # -------- Customer Details ---------#
            ######################################

        self.c_name = StringVar()
        self.c_phone = StringVar()

        self.bill_no = StringVar()
        x = random.randint(1000,9999)
        self.bill_no.set(str(x))

        self.search_bill = StringVar()


        ##############################################################
        # ------------------- Customer Details Frame-----------------#
        ##############################################################

        F1 = LabelFrame(self.root,bd=10,relief = GROOVE,text = "Customer Details",font = ("times new roman",15,"bold"),fg = "gold",bg = bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lb1 = Label(F1,text = "Customer Name",bg = bg_color,fg ="white", font = ("times new roman",15,"bold")).grid(row = 0, column = 0, padx = 20 , pady = 5)
        cname_text = Entry(F1,width =15,textvariable = self.c_name ,font= "arial 15", bd = 7 , relief = SUNKEN).grid(row = 0, column = 1,pady = 5 , padx = 10)

        cphn_lb1 = Label(F1,text = "Phone No.",bg = bg_color,fg ="white", font = ("times new roman",15,"bold")).grid(row = 0, column = 2, padx = 20 , pady = 5)
        cphn_text = Entry(F1,width =15, textvariable = self.c_phone ,font= "arial 15", bd = 7 , relief = SUNKEN).grid(row = 0, column = 3,pady = 5 , padx = 10)

        cbill_lb1 = Label(F1,text = "Bill No.",bg = bg_color,fg ="white", font = ("times new roman",15,"bold")).grid(row = 0, column = 4, padx = 20 , pady = 5)
        cbill_text = Entry(F1,width =15,textvariable = self.search_bill , font= "arial 15", bd = 7 , relief = SUNKEN).grid(row = 0, column = 5,pady = 5 , padx = 10)

        bill_btn = Button(F1,text = "Search",command = self.find_bill,width = 10,bd = 7, font = "arial 12 bold").grid(row = 0, column = 6,padx = 10,pady = 10)

        ############################################
        #------------- Cosmetics Frame ------------#
        ############################################
        
        F2 = LabelFrame(self.root,bd=10,relief = GROOVE,text = "Cosmetics",font = ("times new roman",15,"bold"),fg = "gold",bg = bg_color)
        F2.place(x=5,y=180,width=325,height=380)

        bath_lb1 = Label(F2,text = "Bath Soap", font = ("times new roman",16,"bold"),bg = bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt = Entry(F2,width=10,textvariable = self.soap ,font=("times new roman",16,"bold"),bd=5,relief =SUNKEN).grid(row=0,column = 1 ,padx =10,pady=10)

        Face_cream_lb1 = Label(F2,text = "Face Cream", font = ("times new roman",16,"bold"),bg = bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_cream_txt = Entry(F2,width=10,textvariable = self.face_cream ,font=("times new roman",16,"bold"),bd=5,relief =SUNKEN).grid(row=1,column = 1 ,padx =10,pady=10)

        Face_w_lb1 = Label(F2,text = "Face Wash", font = ("times new roman",16,"bold"),bg = bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_w_txt = Entry(F2,width=10,textvariable = self.face_wash ,font=("times new roman",16,"bold"),bd=5,relief =SUNKEN).grid(row=2,column = 1 ,padx =10,pady=10)

        Hair_s_lb1 = Label(F2,text = "Hair Spray", font = ("times new roman",16,"bold"),bg = bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Hair_s_txt = Entry(F2,width=10,textvariable = self.spray ,font=("times new roman",16,"bold"),bd=5,relief =SUNKEN).grid(row=3,column = 1 ,padx =10,pady=10)

        Hair_g_lb1 = Label(F2,text = "Hair Gel", font = ("times new roman",16,"bold"),bg = bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Hair_g_txt = Entry(F2,width=10,textvariable = self.gell ,font=("times new roman",16,"bold"),bd=5,relief =SUNKEN).grid(row=4,column = 1 ,padx =10,pady=10)

        Body_lb1 = Label(F2,text = "Body Lotion", font = ("times new roman",16,"bold"),bg = bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Body_txt = Entry(F2,width=10,textvariable = self.lotion,font=("times new roman",16,"bold"),bd=5,relief =SUNKEN).grid(row=5,column = 1 ,padx =10,pady=10)

        ############################################
        #------------- Grocery Frame --------------#
        ############################################
        
        F3 = LabelFrame(self.root,bd=10,relief = GROOVE,text = "Grocery",font = ("times new roman",15,"bold"),fg = "gold",bg = bg_color)
        F3.place(x=330,y=180,width=325,height=380)

        g1_lb1 = Label(F3,text = "Rice", font = ("times new roman",16,"bold"),bg = bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt = Entry(F3,width=10,textvariable = self.rice ,font=("times new roman",16,"bold"),bd=5,relief =SUNKEN).grid(row=0,column = 1 ,padx =10,pady=10)

        g2_lb1 = Label(F3,text = "Food Oil", font = ("times new roman",16,"bold"),bg = bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt = Entry(F3,width=10,textvariable = self.food_oil ,font=("times new roman",16,"bold"),bd=5,relief =SUNKEN).grid(row=1,column = 1 ,padx =10,pady=10)

        g3_lb1 = Label(F3,text = "Wheat", font = ("times new roman",16,"bold"),bg = bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt = Entry(F3,width=10,textvariable = self.wheat ,font=("times new roman",16,"bold"),bd=5,relief =SUNKEN).grid(row=2,column = 1 ,padx =10,pady=10)

        g4_lb1 = Label(F3,text = "Daal", font = ("times new roman",16,"bold"),bg = bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt = Entry(F3,width=10,textvariable = self.daal,font=("times new roman",16,"bold"),bd=5,relief =SUNKEN).grid(row=3,column = 1 ,padx =10,pady=10)

        g5_lb1 = Label(F3,text = "Sugar", font = ("times new roman",16,"bold"),bg = bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt = Entry(F3,width=10,textvariable = self.sugar ,font=("times new roman",16,"bold"),bd=5,relief =SUNKEN).grid(row=4,column = 1 ,padx =10,pady=10)

        g6_lb1 = Label(F3,text = "Tea", font = ("times new roman",16,"bold"),bg = bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt = Entry(F3,width=10,textvariable = self.tea ,font=("times new roman",16,"bold"),bd=5,relief =SUNKEN).grid(row=5,column = 1 ,padx =10,pady=10)

        ############################################
        #------------- Cold Drinks Frame ----------#
        ############################################
        
        F4 = LabelFrame(self.root,bd=10,relief = GROOVE,text = "Cold Drink",font = ("times new roman",15,"bold"),fg = "gold",bg = bg_color)
        F4.place(x=655,y=180,width=325,height=380)

        c1_lb1 = Label(F4,text = "Thums Up", font = ("times new roman",16,"bold"),bg = bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt = Entry(F4,width=10,textvariable = self.thums_up,font=("times new roman",16,"bold"),bd=5,relief =SUNKEN).grid(row=0,column = 1 ,padx =10,pady=10)

        c2_lb1 = Label(F4,text = "Sprite", font = ("times new roman",16,"bold"),bg = bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt = Entry(F4,width=10,textvariable = self.sprite,font=("times new roman",16,"bold"),bd=5,relief =SUNKEN).grid(row=1,column = 1 ,padx =10,pady=10)

        c3_lb1 = Label(F4,text = "CocaCola", font = ("times new roman",16,"bold"),bg = bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt = Entry(F4,width=10,textvariable = self.cocacola ,font=("times new roman",16,"bold"),bd=5,relief =SUNKEN).grid(row=2,column = 1 ,padx =10,pady=10)

        c4_lb1 = Label(F4,text = "Frooti", font = ("times new roman",16,"bold"),bg = bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt = Entry(F4,width=10,textvariable = self.frooti ,font=("times new roman",16,"bold"),bd=5,relief =SUNKEN).grid(row=3,column = 1 ,padx =10,pady=10)

        c5_lb1 = Label(F4,text = "Moutain Dew", font = ("times new roman",16,"bold"),bg = bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt = Entry(F4,width=10,textvariable = self.moutain_dew ,font=("times new roman",16,"bold"),bd=5,relief =SUNKEN).grid(row=4,column = 1 ,padx =10,pady=10)

        c6_lb1 = Label(F4,text = "Limca", font = ("times new roman",16,"bold"),bg = bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt = Entry(F4,width=10,textvariable = self.limca ,font=("times new roman",16,"bold"),bd=5,relief =SUNKEN).grid(row=5,column = 1 ,padx =10,pady=10)

        ############################################
        # ----------- Billing Area Frame-----------#
        ############################################
        
        
        F5 = Frame(self.root,bd=10,relief = GROOVE)
        F5.place(x=985,y=180,width=440,height=380)
        bill_title = Label(F5,text = "Bill Area", font = "arial 15 bold",bd=7,relief = GROOVE).pack(fill = X)
        scrol_y = Scrollbar(F5,orient = VERTICAL)
        self.txtarea = Text(F5,yscrollcommand = scrol_y.set)
        scrol_y.pack(side = RIGHT,fill = Y)
        scrol_y.config(command = self.txtarea.yview)
        self.txtarea.pack(fill = BOTH,expand = 1)

        
        ##########################################
        # ---------- Total Prices Frame ---------#
        ##########################################
        
        F6 = LabelFrame(self.root,bd=10,relief = GROOVE,text = "Bill Menu",font = ("times new roman",15,"bold"),fg = "gold",bg = bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)

        m1_lbl = Label(F6,text ="Total Cosmetic Price",bg=bg_color,fg="white",font =("times new roman", 14,"bold")).grid(row = 0,column =0, padx =20 , pady = 1 , sticky = "w")
        m1_txt = Entry(F6,width = 18 , textvariable = self.cosmetic_price ,font = "arial 10 bold",bd=7,relief = SUNKEN).grid(row = 0,column = 1,padx=10,pady = 1)

        m2_lbl = Label(F6,text ="Total Grocery Price",bg=bg_color,fg="white",font =("times new roman", 14,"bold")).grid(row = 1,column =0, padx =20 , pady = 1 , sticky = "w")
        m2_txt = Entry(F6,width = 18 , textvariable = self.grocery_price,font = "arial 10 bold",bd=7,relief = SUNKEN).grid(row = 1,column = 1,padx=10,pady = 1)

        m3_lbl = Label(F6,text ="Total Cold Drink Price",bg=bg_color,fg="white",font =("times new roman", 14,"bold")).grid(row = 2,column =0, padx =20 , pady = 1 , sticky = "w")
        m3_txt = Entry(F6,width = 18 ,textvariable = self.cold_drink_price, font = "arial 10 bold",bd=7,relief = SUNKEN).grid(row = 2,column = 1,padx=10,pady = 1)

        c1_lbl = Label(F6,text ="Cosmetic Tax",bg=bg_color,fg="white",font =("times new roman", 14,"bold")).grid(row = 0,column =2, padx =20 , pady = 1 , sticky = "w")
        c1_txt = Entry(F6,width = 18 ,textvariable = self.cosmetic_tax , font = "arial 10 bold",bd=7,relief = SUNKEN).grid(row = 0,column = 3,padx=10,pady = 1)

        c2_lbl = Label(F6,text ="Grocery Tax",bg=bg_color,fg="white",font =("times new roman", 14,"bold")).grid(row = 1,column =2, padx =20 , pady = 1 , sticky = "w")
        c2_txt = Entry(F6,width = 18 ,textvariable = self.grocery_tax, font = "arial 10 bold",bd=7,relief = SUNKEN).grid(row = 1,column = 3,padx=10,pady = 1)

        c3_lbl = Label(F6,text ="Cold Drinks Tax",bg=bg_color,fg="white",font =("times new roman", 14,"bold")).grid(row = 2,column =2, padx =20 , pady = 1 , sticky = "w")
        c3_txt = Entry(F6,width = 18 ,textvariable = self.cold_drink_tax, font = "arial 10 bold",bd=7,relief = SUNKEN).grid(row = 2,column = 3,padx=10,pady = 1)

        
        #####################################
        # ---------- Buttons Frame ---------#
        #####################################

        btn_F = Frame(F6,bd=7,relief =GROOVE)
        btn_F.place(x = 750 , width = 650 ,height = 105)

        total_btn = Button(btn_F,text = "Total",command = self.total,bg = "cadetblue",fg = "white",pady=15,bd=5,width=11,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        gbill_btn = Button(btn_F,text = "Generate Bill",command= self.bill_area,bg = "cadetblue",fg = "white",pady=15,bd=5,width=11,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        clear_btn = Button(btn_F,text = "Clear",command = self.clear_data,bg = "cadetblue",fg = "white",pady=15,bd=5,width=11,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        exit_btn = Button(btn_F,text = "Exit",command=self.exit_app,bg = "cadetblue",fg = "white",pady=15,bd=5,width=11,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):

        ###########################################
        #---------- Cosmetics Pricing ------------#
        ###########################################

        self.cosmetic_soap_price = self.soap.get()*40
        self.cosmetic_face_c_price =self.face_cream.get()*120
        self.cosmetic_face_w_price =self.face_wash.get()*60
        self.cosmetic_gel_price = self.gell.get()*180
        self.cosmetic_spray_price = self.spray.get()*140
        self.cosmetic_lotion_price = self.lotion.get()*180
        
        self.total_cosmetic_price = float(
            (self.cosmetic_soap_price) +
            (self.cosmetic_face_c_price) +
            (self.cosmetic_face_w_price) +
            (self.cosmetic_gel_price) +
            (self.cosmetic_spray_price) +
            (self.cosmetic_lotion_price)
        )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.total_cosmetic_tax = round(self.total_cosmetic_price*0.18,2)
        self.cosmetic_tax.set("Rs. "+str(self.total_cosmetic_tax))

        ###########################################
        #------------- Grocery Pricing -----------#
        ###########################################

        self.grocery_rice_price = self.rice.get()*80
        self.grocery_food_oil_price = self.food_oil.get()*180
        self.grocery_wheat_price = self.wheat.get()*240
        self.grocery_daal_price = self.daal.get()*60
        self.grocery_sugar_price = self.sugar.get()*45
        self.grocery_tea_price = self.tea.get()*150


        self.total_grocery_price = float(
            (self.grocery_rice_price) +
            (self.grocery_food_oil_price) +
            (self.grocery_wheat_price) +
            (self.grocery_daal_price) +
            (self.grocery_sugar_price) +
            (self.grocery_tea_price)
        )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.total_grocery_tax = round(self.total_grocery_price*0.18,2)
        self.grocery_tax.set("Rs. "+str(self.total_grocery_tax))

        ###############################################
        #------------- Cold Drinks Pricing -----------#
        ###############################################

        self.cd_thums_up_price = self.thums_up.get()*40
        self.cd_sprite_price = self.sprite.get()*40
        self.cd_cocacola_price = self.cocacola.get()*40
        self.cd_mountain_dew_price = self.moutain_dew.get()*40
        self.cd_frooti_price = self.frooti.get()*10
        self.cd_limca_price = self.limca.get()*40

        self.total_cold_drink_price = float(
            (self.cd_thums_up_price) +
            (self.cd_sprite_price) +
            (self.cd_cocacola_price) +
            (self.cd_mountain_dew_price) +
            (self.cd_frooti_price) +
            (self.cd_limca_price)
        )
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.total_cold_drink_tax = round(self.total_cold_drink_price*0.18,2)
        self.cold_drink_tax.set("Rs. "+str(self.total_cold_drink_tax))


        self.sub_total = float(self.total_cosmetic_price + self.total_grocery_price + self.total_cosmetic_price)
        self.total_tax = float(self.total_grocery_tax + self.total_cosmetic_tax + self.total_cold_drink_tax)
        self.grand_total = round(float(self.sub_total + self.total_tax))


    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\n\t Welcome To Mohit's Billing Software \n")
        self.txtarea.insert(END,f"\n Bill Number: {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name: {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Mobile Number: {self.c_phone.get()}")
        self.txtarea.insert(END,"\n ================================================")
        self.txtarea.insert(END,f"\n Products\t\t\tQty\t\tPrice")
        self.txtarea.insert(END,"\n ================================================")
        
    
    def bill_area(self):

        if self.total_cosmetic_price == 0 and self.total_grocery_price ==0 and self.total_cold_drink_price ==0:
            messagebox.showerror("Error","No Product Purchased")
        else:
            self.welcome_bill()

            ###########################################
            #---------- Cosmetics Billing ------------#
            ###########################################
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t\t {self.soap.get()} \t\t{self.cosmetic_soap_price}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t\t {self.face_cream.get()} \t\t{self.cosmetic_face_c_price}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t\t {self.face_wash.get()} \t\t{self.cosmetic_face_w_price}")
            if self.spray.get()!=0:
                self.txtarea.insert(END,f"\n Hair Spray\t\t\t {self.spray.get()} \t\t{self.cosmetic_spray_price}")
            if self.gell.get()!=0:
                self.txtarea.insert(END,f"\n Hair Gel\t\t\t {self.gell.get()} \t\t{self.cosmetic_gel_price}")
            if self.lotion.get()!=0:
                self.txtarea.insert(END,f"\n Body Lotion\t\t\t {self.lotion.get()} \t\t{self.cosmetic_lotion_price}")

            ###########################################
            #---------- Grocery Billing --------------#
            ###########################################

            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t\t {self.rice.get()} \t\t{self.grocery_rice_price}")
            if self.food_oil.get()!=0:
                self.txtarea.insert(END,f"\n Food Oil\t\t\t {self.food_oil.get()} \t\t{self.grocery_food_oil_price}")
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t\t\t {self.wheat.get()} \t\t{self.grocery_wheat_price}")
            if self.daal.get()!=0:
                self.txtarea.insert(END,f"\n Daal\t\t\t {self.daal.get()} \t\t{self.grocery_daal_price}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t\t {self.sugar.get()} \t\t{self.grocery_sugar_price}")
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\n Tea\t\t\t {self.tea.get()} \t\t{self.grocery_tea_price}")


            ###########################################
            #---------- ColdDrink Billing ------------#
            ###########################################

            if self.thums_up.get()!=0:
                self.txtarea.insert(END,f"\n Thums Up\t\t\t {self.thums_up.get()} \t\t{self.cd_thums_up_price}")
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\n Sprite\t\t\t {self.sprite.get()} \t\t{self.cd_sprite_price}")
            if self.cocacola.get()!=0:
                self.txtarea.insert(END,f"\n CocaCola\t\t\t {self.cocacola.get()} \t\t{self.cd_cocacola_price}")
            if self.moutain_dew.get()!=0:
                self.txtarea.insert(END,f"\n Mountain Dew\t\t\t {self.moutain_dew.get()} \t\t{self.cd_mountain_dew_price}")
            if self.frooti.get()!=0:
                self.txtarea.insert(END,f"\n Frooti\t\t\t {self.frooti.get()} \t\t{self.cd_frooti_price}")
            if self.limca.get()!=0:
                self.txtarea.insert(END,f"\n Limca\t\t\t {self.limca.get()} \t\t{self.cd_limca_price}")


            #############################################
            #---------- Final Bill Printing ------------#
            #############################################

            self.txtarea.insert(END,"\n ------------------------------------------------")
            self.txtarea.insert(END,f"\n Sub Total\t\t\t\t\t{self.sub_total}\n")
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cosmetic Tax @18%\t\t\t\t\t{self.total_cosmetic_tax}")
            if self.grocery_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Grocery Tax @18%\t\t\t\t\t{self.total_grocery_tax}")
            if self.cold_drink_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cold Drink Tax @18%\t\t\t\t\t{self.total_cold_drink_tax}")
            
            self.txtarea.insert(END,"\n ------------------------------------------------")
            self.txtarea.insert(END,f"\n Grand Total\t\t\t\t\t{self.grand_total}\n")
            self.save_bill()


    def save_bill(self):
        op = messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data = self.txtarea.get('1.0',END)
            f1 = open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill No. : {self.bill_no.get()} saved Successfully")
        else:
            return
        
    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            # print(i)
            if i.split('.')[0]==self.search_bill.get():
                f1 = open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error","Invalid Bill No")

    def clear_data(self):

        op = messagebox.askyesno("Clear","Do you really wanna clear?")
        if op>0:

            ####################################
                # ------------ Cosmetics ----------#
                ####################################

            self.soap.set(0)
            self.face_cream.set(0) 
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.lotion.set(0)
                
                ####################################
                # ----------- Grocery -------------#
                ####################################

            self.rice.set(0)
            self.food_oil.set(0)
            self.wheat.set(0)
            self.daal.set(0)
            self.sugar.set(0)
            self.tea.set(0)

                ####################################
                # ----------- Cold Drinks ---------#
                ####################################

            self.thums_up.set(0)
            self.sprite.set(0)
            self.cocacola.set(0)
            self.moutain_dew.set(0)
            self.limca.set(0)
            self.frooti.set(0)

                ###########################################################
                # ---------- Total Product Price & Tax Variables ---------#
                ###########################################################
            
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")


            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

                
                ######################################
                # -------- Customer Details ---------#
                ######################################

            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000,9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()
        
    def exit_app(self):
        op = messagebox.askyesno("Exit","Do you really wanna exit?")
        if op>0:
            self.root.destroy()
        


root = Tk()
obj = Bill_App(root)
root.mainloop()