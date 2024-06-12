#!/usr/bin/env python
# coding: utf-8

# In[82]:


# RMS

#
import json
class RMS:    

    def __init__(self,restaurant_name,restaurant_menu):
        self.rest_name=restaurant_name
        self.user_order=''
        self.menu=restaurant_menu
        self.total_bill=0
        self.wlcm_print=f'Welcome to the {self.rest_name.title()}'
    def welcome_user(self):
        #welcome user
        print('Welcome to the',self.rest_name.title())
    def take_order(self):
        #take order
        self.user_order=input('Please place your order here:')
    def display_menu(self):
        #display menu
        print('Menu:')
        print("*"*30)
        for i in self.menu:
            print(i.title(),self.menu[i])
        print("*"*30)

    def preparing_order(self):
        #preparing order
        import time
        print('Preparing your',self.user_order.title())
        time.sleep(1)
        self.total_bill=self.total_bill+self.menu[self.user_order.lower()]

    def serve_order(self):
        #serve order
        print('Your order is ready')

    def display_bill(self):
        #display bill
        print('Your Bill:',self.total_bill)

    def verify_bill(self):
        self.user_pay=int(input('Please pay your bill here:'))
        #verify bill
        while self.user_pay<self.total_bill:
            self.total_bill=self.total_bill-self.user_pay
            print('Payment Failed! Please pay accurate amount',self.total_bill)
            self.user_pay=int(input('Please pay your bill here:'))


        if self.user_pay>self.total_bill:
            print('Here is your change',self.user_pay-self.total_bill)
        else:
            pass

    def ty(self):
        #thank you
        print('Thank you for visiting',self.rest_name.title())

    def order_process(self):
        
        self.take_order()
        if self.user_order.lower() in self.menu:
            self.preparing_order()
            self.serve_order()
            self.ask_user=input('Do you want to order again?')
            while self.ask_user.lower()=='yes':
                self.repeat_order()
                self.ask_user=input('Do you want to order again?')

            self.display_bill()
            self.verify_bill()
            self.ty()
        else:
            print('Invalid order!')
            self.order_process()


    def repeat_order(self):
        
        self.take_order()
        if self.user_order.lower() in self.menu:
            self.preparing_order()
            self.serve_order()
        else:
            print('Invalid order!')
            self.repeat_order()

if __name__=='__main__':
    #menu={'latte':180,'cappuccino':160,'espresso':130,'cold coffee':120}

    f=open("ui.txt","r")
    user_input=(f.readlines())
    
    rest_name=user_input[0].replace('\n','')
    
    food_name=user_input[1].replace('\n','').split(',')
    
    food_prices=[]
    for i in user_input[2].split(','):
        food_prices.append(int(i))
    rest_menu=dict(zip(food_name,food_prices))    
    mc=(RMS(restaurant_name=rest_name, restaurant_menu=rest_menu))
    #mc.order_process()
    
    #importing library
    import tkinter as tk
    
    #creating window
    window=tk.Tk()
    
    #change title
    window.title('Restaurant Management System')
    
    #window size
    window.geometry('400x400')
    
    #label1
    tk.Label(window,text=mc.wlcm_print,font=('Georgia',18,"bold"),fg="midnight blue").place(x=14,y=30)
    tk.Label(window,text=" Made by: Shreya Potdar",font=('Comic Sans MS',10,"bold"),fg="Black").place(x=115,y=61)

    tk.Button(window,text='SHOW MENU',command=mc.display_menu,font=('Georgia',10),fg="light gray",bg="midnight blue",height=3,width=20).place(x=120,y=120)
    #tk.Label(window,text='Cappuccino 160',font=('Helvetica',10)).place(x=300,y=260)
    #tk.Label(window,text='Espresso 130',font=('Helvetica',10)).place(x=300,y=280)
    #tk.Label(window,text='Cold Coffee 120',font=('Helvetica',10)).place(x=300,y=300)

    #tk.Button(window,text='Menu',command=mc.display_menu).place(x=200,y=200)
    
    tk.Button(window,text='START ORDER PROCESS',command=mc.order_process,font=('Georgia',10),height=3,width=25,fg="light gray",bg="midnight blue").place(x=100,y=210)
    
    
    #to show the window
    window.mainloop()
        


# In[ ]:





# In[ ]:




