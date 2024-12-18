import tkinter 
from tkinter import*
from tkinter import ttk
import tkinter.messagebox



class ATM:
    def __init__(self,root):
        self.root=root
        blank_space=' '
        self.root.title(110 * blank_space + 'ATM system')
        self.root.geometry("800x760+280+0")
        self.root.configure(background='gainsboro')

#++++++++++++++++++++++++++++++++++++main frame++++++++++++++++++++++++++++++++++++++++
        MainFrame=Frame(self.root, bd=20,width=784,height=700,relief =RIDGE)
        MainFrame.grid()
        
        TopFrame1=Frame(MainFrame, bd=7,width=734,height=300,relief =RIDGE)
        TopFrame1.grid(row=1,column=0,padx=12)
        TopFrame2=Frame(MainFrame, bd=7,width=734,height=300,relief =RIDGE)
        TopFrame2.grid(row=0,column=0,padx=8)
        
        TopFrame2Left=Frame(TopFrame2,bd=5,width=190,height=300,relief =RIDGE)
        TopFrame2Left.grid(row=0,column=0,padx=3)

        TopFrame2Mid=Frame(TopFrame2, bd=5,width=200,height=300,relief =RIDGE)
        TopFrame2Mid.grid(row=0,column=1,padx=3)

        TopFrame2Right=Frame(TopFrame2, bd=5,width=190,height=300,relief =RIDGE)
        TopFrame2Right.grid(row=0,column=2,padx=3)

#++++++++++++++++++++++++++++++++++++++++++FUNCTION++++++++++++++++++++++++++++++++++++++
        def enter_pin():
            
                
                pinNo=self.textReceipt.get('1.0','end-1c')
                if((pinNo==str('2213')) or (pinNo==str('4323')) or (pinNo==str('5982'))):
                    self.textReceipt.delete('1.0',END)

                    self.textReceipt.insert(END,'\t WELCOME  TO  ATM '+ '\n\n')
                    self.textReceipt.insert(END,' Withdraw Cash\t\t\t LOAN' + '\n\n\n\n')
                    self.textReceipt.insert(END,'Cash With Receipt\t\t\t Deposit' + '\n\n\n\n')
                    self.textReceipt.insert(END,'Balance \t\t\t Request New Pin' + '\n\n\n\n')
                    self.textReceipt.insert(END,'Mini Statement\t\t\t Print Statement' + '\n\n\n\n')

                    self.btnArrowR1=Button(TopFrame2Right, width=160, height=60,state=NORMAL,command=Loan,
                    image=self.img_arrow_Right).grid(row=0,column=0,padx=2,pady=2)
                        
                    self.btnArrowR2=Button(TopFrame2Right, width=160, height=60,state=NORMAL,command=deposit,
                    image=self.img_arrow_Right).grid(row=1,column=0,padx=2,pady=2)
                        
                    self.btnArrowR3=Button(TopFrame2Right, width=160, height=60,state=NORMAL,command=request_new_pin,
                    image=self.img_arrow_Right).grid(row=2,column=0,padx=2,pady=2)
                        
                    self.btnArrowR4=Button(TopFrame2Right, width=160, height=60,state=NORMAL,command=statement,
                    image=self.img_arrow_Right).grid(row=3,column=0,padx=2,pady=2)


                    #=================================PIN NUMBER BUTTEN=============================================

                    self.btnArrowl1=Button(TopFrame2Left, width=160, height=60,state=NORMAL,command=withdrawcash,
                    image=self.img_arrow_left).grid(row=0,column=0,padx=2,pady=2)
                        
                    self.btnArrowl2=Button(TopFrame2Left, width=160, height=60,state=NORMAL,command=Case_With_Reciept,
                    image=self.img_arrow_left).grid(row=1,column=0,padx=2,pady=2)
                        
                    self.btnArrowl3=Button(TopFrame2Left, width=160, height=60,state=NORMAL,command=balance,
                    image=self.img_arrow_left).grid(row=2,column=0,padx=2,pady=2)
                        
                    self.btnArrowl4=Button(TopFrame2Left, width=160, height=60,state=NORMAL,command=statement,
                    image=self.img_arrow_left).grid(row=3,column=0,padx=2,pady=2)
                else:
                    self.textReceipt.delete('1.0',END)
                    self.textReceipt.insert(END,'Invalid Pin Number' + '\n')
                    self.textReceipt.insert(END,"Please Enter a valid Pin Number........" + '\n')
                    
                
                
                
        def clear():

                self.btnArrowl1=Button(TopFrame2Left, width=160, height=60,state=DISABLED,
                image=self.img_arrow_left).grid(row=0,column=0,padx=2,pady=2)
                
                self.btnArrowl2=Button(TopFrame2Left, width=160, height=60,state=DISABLED,
                image=self.img_arrow_left).grid(row=1,column=0,padx=2,pady=2)
                
                self.btnArrowl3=Button(TopFrame2Left, width=160, height=60,state=DISABLED,
                image=self.img_arrow_left).grid(row=2,column=0,padx=2,pady=2)
                
                self.btnArrowl4=Button(TopFrame2Left, width=160, height=60,state=DISABLED,
                image=self.img_arrow_left).grid(row=3,column=0,padx=2,pady=2)
                #==================================================================================

                self.btnArrowR1=Button(TopFrame2Right, width=160, height=60,state=DISABLED,
                image=self.img_arrow_Right).grid(row=0,column=0,padx=2,pady=2)
                
                self.btnArrowR2=Button(TopFrame2Right, width=160, height=60,state=DISABLED,
                image=self.img_arrow_Right).grid(row=1,column=0,padx=2,pady=2)
                
                self.btnArrowR3=Button(TopFrame2Right, width=160, height=60,state=DISABLED,
                image=self.img_arrow_Right).grid(row=2,column=0,padx=2,pady=2)
                
                self.btnArrowR4=Button(TopFrame2Right, width=160, height=60,state=DISABLED,
                image=self.img_arrow_Right).grid(row=3,column=0,padx=2,pady=2)
        def insert0():
            value0=0
            self.textReceipt.insert(END,value0)

        def insert1():
            value1=1
            self.textReceipt.insert(END,value1)
            
        def insert2():
            value2=2
            self.textReceipt.insert(END,value2)
            
        def insert3():
            value3=3
            self.textReceipt.insert(END,value3)

        def insert4():
            value4=4
            self.textReceipt.insert(END,value4)

        def insert5():
            value5=5
            self.textReceipt.insert(END,value5)
            
        def insert6():
            value6=6
            self.textReceipt.insert(END,value6)

        def insert7():
            value7=7
            self.textReceipt.insert(END,value7)

        def insert8():
            value8=8
            self.textReceipt.insert(END,value8)

        def insert9():
            value9=9
            self.textReceipt.insert(END,value9)

        def cancel():
            cancel=tkinter.messagebox.askyesno('ATM','confirm if you want to cancle')
            if cancel>0:
                self.root.destroy()
                return
        def withdrawcash():
            enter_pin()
            self.textReceipt.delete('1.0',END)
            self.textReceipt.focus_set()

        def Loan():
            enter_pin()
            self.textReceipt.delete('1.0',END)
            self.textReceipt.insert(END,'Loan ')
            self.textReceipt.focus_set()

        def deposit():
            
            enter_pin()
            self.textReceipt.insert(END,'Enter your Amount \n')
            self.textReceipt.delete('1.0',END)
            self.textReceipt.focus_set()

        def request_new_pin():
            
            enter_pin()
            self.textReceipt.delete('1.0',END)
            self.textReceipt.insert(END,'\n\nNew Pin will be send your Resistered Email address\n\n')
            self.textReceipt.insert(END,'Thans for using BOB Bank\n')
            

        def Case_With_Reciept():
            self.textReceipt.delete('1.0',END)
            self.textReceipt.insert(END,'\tWelcome To BOB\n\n')
            self.textReceipt.insert(END,'Cash With Receipt Amount\n\n\n')
            self.textReceipt.insert(END,'Mini Statement')
            


        def balance():
            self.textReceipt.delete('1.0',END)
            self.textReceipt.insert(END,'\tWelcome to BOB Bank\n')
            self.textReceipt.insert(END,'Your Balance $129678' + '\n')
            

        def statement():
            pinNo1=str(self.textReceipt.get('1.0', 'end-1c'))
            pinNo2=str(pinNo1)
            pinNo3=str(pinNo2)
            pinNo4=str(pinNo3)
            self.textReceipt.delete('1.0',END)
            self.textReceipt.insert(END,'\n\t',str(pinNo4) + '\t\t')
            self.textReceipt.insert(END,'\t\t\t\n\n      Account Balance £ 56000',str(pinNo4),'\t\t\n\n')
            self.textReceipt.insert(END,'Rent \t\t\t\t   £1200' + '\n\n')
            self.textReceipt.insert(END,' Tesco \t\t\t\t   £79.36' + '\n\n')
            self.textReceipt.insert(END,'Sainabury \t\t\t\t   £45.92' + '\n\n')
            self.textReceipt.insert(END,'Student Loan \t\t\t\t 53.87' + '\n\n')


                


#++++++++++++++++++++++++++++++++++++++++widget+++++++++++++++++++++++++++++++++
        self.textReceipt=Text(TopFrame2Mid,height=17,width=42,bd=12,font=('arail',9,'bold'))
        self.textReceipt.grid(row=0,column=0)

        self.img_arrow_left=PhotoImage(file="C:/Users/Mudit Computer/Downloads/ATM_Icon/ATM_Icon/lArrow.png")
        self.btnArrowl1=Button(TopFrame2Left, width=160, height=60,state=NORMAL,command=withdrawcash,
        image=self.img_arrow_left).grid(row=0,column=0,padx=2,pady=2)
        
        self.btnArrowl2=Button(TopFrame2Left, width=160, height=60,state=NORMAL,command=Case_With_Reciept,
        image=self.img_arrow_left).grid(row=1,column=0,padx=2,pady=2)
        
        self.btnArrowl3=Button(TopFrame2Left, width=160, height=60,state=NORMAL,command=balance,
        image=self.img_arrow_left).grid(row=2,column=0,padx=2,pady=2)
        
        self.btnArrowl4=Button(TopFrame2Left, width=160, height=60,state=NORMAL,command=Case_With_Reciept,
        image=self.img_arrow_left).grid(row=3,column=0,padx=2,pady=2)       

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.img_arrow_Right=PhotoImage(file="C:/Users/Mudit Computer/Downloads/ATM_Icon/ATM_Icon/rArrow.png")
        self.btnArrowR1=Button(TopFrame2Right, width=160, height=60,state=NORMAL,command=Loan,
        image=self.img_arrow_Right).grid(row=0,column=0,padx=2,pady=2)
        
        self.btnArrowR2=Button(TopFrame2Right, width=160, height=60,state=NORMAL,command=deposit,
        image=self.img_arrow_Right).grid(row=1,column=0,padx=2,pady=2)
        
        self.btnArrowR3=Button(TopFrame2Right, width=160, height=60,state=NORMAL,command=request_new_pin,
        image=self.img_arrow_Right).grid(row=2,column=0,padx=2,pady=2)
        
        self.btnArrowR4=Button(TopFrame2Right, width=160, height=60,state=NORMAL,command=statement,
        image=self.img_arrow_Right).grid(row=3,column=0,padx=2,pady=2)
#++++++++++++++++++++++++++++ENSERT BUTTEN++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.img1=PhotoImage(file='C:/Users/Mudit Computer/Downloads/ATM_Icon/ATM_Icon/one.png')
        self.btn1=Button(TopFrame1, width=160, height=60,command=insert1,
        image=self.img1).grid(row=2,column=0,padx=6,pady=4)

        self.img2=PhotoImage(file='C:/Users/Mudit Computer/Downloads/ATM_Icon/ATM_Icon/two.png')
        self.btn2=Button(TopFrame1, width=160, height=60,command=insert2,
        image=self.img2).grid(row=2,column=1,padx=6,pady=4)

        self.img3=PhotoImage(file='C:/Users/Mudit Computer/Downloads/ATM_Icon/ATM_Icon/three.png')
        self.btn3=Button(TopFrame1, width=160, height=60,command=insert3,
        image=self.img3).grid(row=2,column=2,padx=6,pady=4)


        self.imgCE=PhotoImage(file='C:/Users/Mudit Computer/Downloads/ATM_Icon/ATM_Icon/cancel.png')
        self.btn4=Button(TopFrame1, width=160, height=60,command=cancel,
        image=self.imgCE).grid(row=2,column=3,padx=6,pady=4)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.img4=PhotoImage(file='C:/Users/Mudit Computer/Downloads/ATM_Icon/ATM_Icon/four.png')
        self.btn4=Button(TopFrame1, width=160, height=60,command=insert4,
        image=self.img4).grid(row=3,column=0,padx=6,pady=4)
        
        self.img5=PhotoImage(file='C:/Users/Mudit Computer/Downloads/ATM_Icon/ATM_Icon/five.png')
        self.btn5=Button(TopFrame1, width=160, height=60,command=insert5,
        image=self.img5).grid(row=3,column=1,padx=6,pady=4)
        
        self.img6=PhotoImage(file='C:/Users/Mudit Computer/Downloads/ATM_Icon/ATM_Icon/six.png')
        self.btn6=Button(TopFrame1, width=160, height=60,command=insert6,
        image=self.img6).grid(row=3,column=2,padx=6,pady=4)

        
        self.imgC1=PhotoImage(file='C:/Users/Mudit Computer/Downloads/ATM_Icon/ATM_Icon/clear.png')
        self.btn7=Button(TopFrame1, width=160, height=60,command=clear,
        image=self.imgC1).grid(row=3,column=3,padx=6,pady=4)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.img7=PhotoImage(file='C:/Users/Mudit Computer/Downloads/ATM_Icon/ATM_Icon/seven.png')
        self.btn8=Button(TopFrame1, width=160, height=60,command=insert7,
        image=self.img7).grid(row=4,column=0,padx=6,pady=4)

        self.img8=PhotoImage(file='C:/Users/Mudit Computer/Downloads/ATM_Icon/ATM_Icon/eight.png')
        self.btn9=Button(TopFrame1, width=160, height=60,command=insert8,
        image=self.img8).grid(row=4,column=1,padx=6,pady=4)
        
        self.img9=PhotoImage(file='C:/Users/Mudit Computer/Downloads/ATM_Icon/ATM_Icon/nine.png')
        self.btn10=Button(TopFrame1, width=160, height=60,command=insert9,
        image=self.img9).grid(row=4,column=2,padx=6,pady=4)
        
        self.imgE1=PhotoImage(file='C:/Users/Mudit Computer/Downloads/ATM_Icon/ATM_Icon/enter.png')
        self.btn11=Button(TopFrame1, width=160, height=60,command=enter_pin,
        image=self.imgE1).grid(row=4,column=3,padx=6,pady=4)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.imgSp1=PhotoImage(file='C:/Users/Mudit Computer/Downloads/ATM_Icon/ATM_Icon/empty.png')
        self.btn12=Button(TopFrame1, width=160, height=60,
        image=self.imgSp1).grid(row=5,column=0,padx=6,pady=4)

        self.img0=PhotoImage(file='C:/Users/Mudit Computer/Downloads/ATM_Icon/ATM_Icon/zero.png')
        self.btn13=Button(TopFrame1, width=160, height=60,command=insert0,
        image=self.img0).grid(row=5,column=1,padx=6,pady=4)
        
        self.imgSp2=PhotoImage(file='C:/Users/Mudit Computer/Downloads/ATM_Icon/ATM_Icon/empty.png')
        self.btn14=Button(TopFrame1, width=160, height=60,
        image=self.imgSp2).grid(row=5,column=2,padx=6,pady=4)
        
        self.imgSp3=PhotoImage(file='C:/Users/Mudit Computer/Downloads/ATM_Icon/ATM_Icon/empty.png')
        self.btn15=Button(TopFrame1, width=160, height=60,
        image=self.imgSp3).grid(row=5,column=3,padx=6,pady=4)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        
        
if __name__=='__main__':
    root=Tk()
    application=ATM(root)
    root.mainloop()
