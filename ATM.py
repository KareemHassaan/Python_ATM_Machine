#---------------------------------------------------------------------------------------------------------------------------------------#
# LOG:                                               							   								  						#
# VERSION					AUTHOR           					DATE 						DESCRIPTION    					  			#
# 1.0.0 					Kareem Hassaan						10 DEC,2021					- Initial Creation				  			#
#---------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------#
# ! Title      	: ATM Project                                                        							  						#
# ! File Name	: ATM.py                                                     							  								#
# ! Description : This file has the Definitions needed		         		        							  						#
# ! Version  	: Python 3.9.7                                            							  									#
#---------------------------------------------------------------------------------------------------------------------------------------#


#***************************************************************************************************************************************#
#												/* Importing the tkinter GUI library */													#
#***************************************************************************************************************************************#
import tkinter	
from tkinter import *											

#***************************************************************************************************************************************#
#	  													   /* Bank Database */															#	
#***************************************************************************************************************************************#
BankDataBase = {'215321701332':{'NAME':'Ahmed Abdelrazek Mohamed', 'Password': '1783', 'Balance': 3500166,'Locker':0},
				'203659302214':{'NAME':'Salma Mohamed Foaad'	 , 'Password': '1390', 'Balance': 520001 ,'Locker':1},
				'126355700193':{'NAME':'Adel Khaled Abdelrahman' , 'Password': '1214', 'Balance': 111000 ,'Locker':0},
				'201455998011':{'NAME':'Saeed Amin Elsawy'       , 'Password': '2001', 'Balance': 1200   ,'Locker':0},
				'201122369851':{'NAME':'Amir Salama Elgendy'     , 'Password': '8935', 'Balance': 178933 ,'Locker':1},
				'201356788002':{'NAME':'Wael Mohamed khairy'     , 'Password': '3420', 'Balance': 55000  ,'Locker':1},
				'203366789564':{'NAME':'Mina Sameh Bishoy'       , 'Password': '1179', 'Balance': 18000  ,'Locker':0},
				'201236787812':{'NAME':'Omnia Ahmed Awad'        , 'Password': '1430', 'Balance': 180350 ,'Locker':0}}

#***************************************************************************************************************************************#
#	    										 	/* Main Window Construction GUI */													#
#***************************************************************************************************************************************#				
#Creation a new Empty window
Main_Window = tkinter.Tk()									
#Renaming the Window title
Main_Window.title("ATM")									
#Relocating the window
Main_Window.geometry("400x150+600+50")						
#Disable resizing the window
Main_Window.resizable(False,False) 							
#changing the window color 
Main_Window.configure(background = "olive") 						 

#***************************************************************************************************************************************#
#												         /* Global Variables */      												    #
#***************************************************************************************************************************************#
NewPassword 		= tkinter.IntVar()
ConfirmNewPassword  = tkinter.IntVar()
CashAmount 			= tkinter.IntVar()
Selected_Radio 		= tkinter.IntVar()
Selected_Network	= tkinter.IntVar()
PhoneNumber 		= tkinter.IntVar()
Amount 				= tkinter.IntVar()

TryNum = 3

#***************************************************************************************************************************************#
#												      /* Cash Withdraw Functions */   												    #
#***************************************************************************************************************************************#
	
#----------------------------------------------------------------------------------------------------------#
# Function Name		: CashWithdrawPopUp																	   #
# Parameters (in)	: None          						 										       #
# Description		: Function to Popup the cash withdraw window to enter the amount with some restriction #
#----------------------------------------------------------------------------------------------------------#
def CashWithdrawPopUp():

	#-----------------------------------------------* Creating a new Empty PopUp *----------------------------------------------------#
	
	global CashPopUp
	
	#Creation a new Empty window
	CashPopUp = tkinter.Toplevel()
	#Renaming the Window title
	CashPopUp.title("Cash withdraw")
	#Relocating the window
	CashPopUp.geometry("400x200+600+50")
	#changing the window color
	CashPopUp.configure(background = "green")
	
	#------------------------------------------------* Message Labels of the PopUp *---------------------------------------------------#
	
	#Create and Place the label for Restriction message in Pop Up 
	CashLabel1 = tkinter.Label(CashPopUp, text = "Enter the desired amount in multiple of 100 EGP", width = 40, bg = "white", fg = "black")
	CashLabel1.place(x = 25, y = 20)
	
	#Create and Place the label for Restriction message in Pop Up 
	CashLabel2 = tkinter.Label(CashPopUp, text = "In which the max amount is 5k/ transaction :", width = 40, bg = "white", fg = "black")
	CashLabel2.place(x = 25, y = 40)
	
	#----------------------------------------------* Scaning the Amount from user *---------------------------------------------------#
	
	#Create and Place the label for Restriction message in Pop Up 
	CashLabel3 = tkinter.Label(CashPopUp, text = "EGP", width = 4, bg = "white", fg = "black")
	CashLabel3.place(x = 350, y = 100)

	#Create and Place the Entry for the Amount in Pop Up 
	CashAmountEntry = tkinter.Entry(CashPopUp, width = 30, bg = "white", fg = "black",textvariable = CashAmount)
	CashAmountEntry.place(x = 160, y = 100)
	#Clear the Entry
	CashAmountEntry.delete(0, END)
	
	#--------------------------------------------------* Buttons of the PopUp *-------------------------------------------------------#
	
	#Create and Place the Button to Proceed the Proccess in Pop Up 
	Enter = tkinter.Button(CashPopUp, text = "Proceed", width = 10 , bg = "white", fg = "black", command = CashWithdraw)
	Enter.place(x = 210, y = 150)
	
	#Create and Place the Button for Back in the main window
	BackButton = tkinter.Button(CashPopUp, text="Cancel", width = 10 , bg = "white", fg = "black", command = CashPopUp.destroy)
	BackButton.place(x = 100, y = 150)

#----------------------------------------------------------------------------------------------------------#
# Function Name		: CashWithdraw    																	   #
# Parameters (in)	: None          						 											   #
# Description		: Function to Proceed the cash withdraw Process 									   #
#   				  and PoPup an error message if the restrictions broke		     					   #
#----------------------------------------------------------------------------------------------------------#
def CashWithdraw():

	global CashAmount
	
	#Getting the Account Number
	AccGet = str(Account.get())
	
	#Getting the Cash Amount
	Cash = CashAmount.get()
	
	#Checking some restrictions if the balance is sufficient, Amount does not exceed 5k per transaction 
	#and Amount multiple of 100
	if BankDataBase[AccGet]['Balance'] >= Cash:
		if Cash <= 5000:
			if Cash%100 == 0:
				
				#Deduct the Amount from Balance
				BankDataBase[AccGet]['Balance'] -= Cash
				
				#PopUp a Message that the process proceeded successfully
				ATM_Actuator_Out()
				
				#Delay function to close Automatic after some seconds the Popup message 
				ProcessPopUp.after(3000,lambda : ProcessPopUp.destroy())
				
				#Delay function to close Automatic after some seconds the Cash withdraw window 
				CashPopUp.after(3000,lambda : CashPopUp.destroy())
				
			else:
			
				#Popup Message with error that Amount not multiple of 100 with OK button
				ErrorPopUp("Sorry Please Enter amount multiple of 100 EGP")
		else:
		
			#Popup Message with error that Amount more that 5k with OK button
			ErrorPopUp("Sorry Please Enter amount Less than 5k EGP")
	else:
	
		#Popup Message with error that Amount more than the balance
		CashProcessPopUp("Sorry there is no sufficient balance ")
		#Delay function to close Automatic after some seconds the Popup message 
		ProcessPopUp.after(3000,lambda : ProcessPopUp.destroy())
		#Delay function to close Automatic after some seconds the Cash withdraw window
		CashPopUp.after(3000,lambda : CashPopUp.destroy())

#----------------------------------------------------------------------------------------------------------#
# Function Name		: ATM_Actuator_Out    																   #
# Parameters (in)	: None          						 											   #
# Description		: Reserved Function 												 				   #  				  
#----------------------------------------------------------------------------------------------------------#
def ATM_Actuator_Out():
	CashProcessPopUp("Proceeded Successfully, Thank you")

#***************************************************************************************************************************************#	
	
	
#***************************************************************************************************************************************#
#												   /* Balance Inquiry Functions */	    												#
#***************************************************************************************************************************************#
	
#----------------------------------------------------------------------------------------------------------#
# Function Name		: BalanceInquiryPopUp    															   #
# Parameters (in)	: None          						 											   #
# Description		: Function to Print	the full name and the total Balance in the Account				   #
#----------------------------------------------------------------------------------------------------------#
def BalanceInquiryPopUp():

	#-----------------------------------------------* Creating a new Empty PopUp *----------------------------------------------------#
	
	#Creation a new Empty window
	BalancePopUp = tkinter.Toplevel()
	#Renaming the Window title
	BalancePopUp.title("Balance Inquiry")
	#Relocating the window
	BalancePopUp.geometry("400x150+600+50")
	#changing the window color
	BalancePopUp.configure(background = "green")
	
	#--------------------------------------------------* Displaying the Balance *-----------------------------------------------------#
	
	#Getting the Account Number
	AccGet = str(Account.get())
	
	#Create and Place the label for Wthe full name in Pop Up 
	NameLabel = tkinter.Label(BalancePopUp, text = "Full Name : " + BankDataBase[AccGet]['NAME'], width = 50, bg = "white", fg = "black")
	NameLabel.place(x = 25, y = 20)
	
	#Create and Place the label for Wthe Total Balance in Pop Up
	BalanceLabel = tkinter.Label(BalancePopUp, text = "Your Balance is " + str(BankDataBase[AccGet]['Balance'])+" EGP", width = 50, bg = "white", fg = "black")
	BalanceLabel.place(x = 25, y = 40)
	
	#--------------------------------------------------* Buttons of the PopUp *-------------------------------------------------------#
	
	#Create and Place the Button to Close the Pop Up
	Enter = tkinter.Button(BalancePopUp, text="OK", width = 10 , bg = "white", fg = "black", command = BalancePopUp.destroy)
	Enter.place(x = 270, y = 100)	

#***************************************************************************************************************************************#

	
#***************************************************************************************************************************************#
#												   /* Change Password Functions */	    												#
#***************************************************************************************************************************************#

#----------------------------------------------------------------------------------------------------------#
# Function Name		: ChangePassword    								     			   			       #
# Parameters (in)	: None          						 											   #
# Description		: Function to Change the Password in the DataBase									   #
#----------------------------------------------------------------------------------------------------------#
def ChangePassword():
	
	#Getting the New Password
	global NewPassword 
	
	#Getting the Confirmation of New Password
	global ConfirmNewPassword 
	
	#Getting the Account Number
	AccGet = str(Account.get())
	
	#Checking on the Password that it is 4 digits and NewPassword is equal to its Confirmation
	if (int(NewPassword.get()) > 1000) and (int(NewPassword.get()) < 9999):
		if(NewPassword.get() == ConfirmNewPassword.get()):
			
			#Changing the Password in the DataBase
			BankDataBase[AccGet]['Password'] = str(NewPassword.get())
			
			#PopUp message that the Password changed in the DataBase successfully with Ok Button 
			ErrorPopUp("Password Changed Successfully")
			
			#Closing the Password change window
			PasswordPopUp.destroy()
			
		else:
		
			#Error Popup message New Password Not equal its Confirmation
			ErrorPopUp("Error : New Password must equal its Confirmation")
	else:
	
		#Error Popup message New Password is not 4 digits
		ErrorPopUp("Error : Password must be 4 digits")

#----------------------------------------------------------------------------------------------------------#
# Function Name		: ChangePasswordPopUp    								     			   			   #
# Parameters (in)	: None          						 											   #
# Description		: Function to open the change password window to scane it from the user				   #
#----------------------------------------------------------------------------------------------------------#		
def ChangePasswordPopUp():
	
	#-----------------------------------------------* Creating a new Empty PopUp *----------------------------------------------------#
	
	global PasswordPopUp
	
	#Creation a new Empty window
	PasswordPopUp = tkinter.Toplevel()
	#Renaming the Window title
	PasswordPopUp.title("Change Password")
	#Relocating the window
	PasswordPopUp.geometry("400x150+600+50")
	#changing the window color
	PasswordPopUp.configure(background = "green")
	
	#-----------------------------------------* Scaning the new password from the user *----------------------------------------------#
	
	#Getting Account Number
	AccGet = str(Account.get())
	
	#Create and Place the label for the New password in Pop Up 
	NewpasswordLabel1 = tkinter.Label(PasswordPopUp, text = "New Password", width = 25, bg = "white", fg = "black")
	NewpasswordLabel1.place(x = 25, y = 30)
	
	#Create and Place the Entry for the New password in Pop Up 
	NewPasswordEntry1 = tkinter.Entry(PasswordPopUp, width = 10, bg = "white", fg = "black",show ='*',textvariable = NewPassword)
	NewPasswordEntry1.place(x = 220, y = 30)
	#Clearing New Password Entery
	NewPasswordEntry1.delete(0, END)
	
	#Create and Place the label to Confirm the New password in Pop Up 
	NewpasswordLabel2 = tkinter.Label(PasswordPopUp, text = "Confirm New Password", width = 25, bg = "white", fg = "black")
	NewpasswordLabel2.place(x = 25, y = 60)
	
	#Create and Place the Entry to Confirm the New password in Pop Up
	NewPasswordEntry2 = tkinter.Entry(PasswordPopUp, width = 10, bg = "white", fg = "black",show ='*', textvariable = ConfirmNewPassword)
	NewPasswordEntry2.place(x = 220, y = 60)
	#Clearing the confirmation of the New Password Entery
	NewPasswordEntry2.delete(0, END)
	
	#--------------------------------------------------* Buttons of the PopUp *-------------------------------------------------------#
	
	#Create and Place the Button to proceed the change in Pop Up
	Enter = tkinter.Button(PasswordPopUp, text="Change", width = 10 , bg = "white", fg = "black", command = ChangePassword)
	Enter.place(x = 300, y = 100)
	
	#Create and Place the Button for Back in Pop Up
	BackButton = tkinter.Button(PasswordPopUp, text="Cancel", width = 10 , bg = "white", fg = "black", command = PasswordPopUp.destroy)
	BackButton.place(x = 200, y = 100)

#***************************************************************************************************************************************#


#***************************************************************************************************************************************#
#												    /* Fawry Services Functions*/	        												#
#***************************************************************************************************************************************#
	
#----------------------------------------------------------------------------------------------------------#
# Function Name		: Recharging    															           #
# Parameters (in)	: None          						 											   #
# Description		: Function to proceed the Recharging Process throuh Fawry Services  				   #
#----------------------------------------------------------------------------------------------------------#
def Recharging():

	#Getting Account Number
	AccGet = str(Account.get())
	
	#Checking that the phone number is 12 digits and the Balance is sufficient to cover the amount
	if int(Amount.get()) <= BankDataBase[AccGet]['Balance']:
		if (int(PhoneNumber.get()) > 100000000000) and int((PhoneNumber.get()) < 999999999999):
		
			#Deducting the Recharging Amount from the balance
			BankDataBase[AccGet]['Balance'] -= int(Amount.get())
			
			#PopUp message that the Recharging process done successfully 
			CashProcessPopUp("The mobile Number Recharged Successfully")
			
			#Delay function to close Automatic after some seconds the Popup message 
			ProcessPopUp.after(3000,lambda : ProcessPopUp.destroy())
			
			#Delay function to close Automatic after some seconds the Recharging window 
			CompanyPopUp.after(3000,lambda : CompanyPopUp.destroy())
			
		else:
			
			#Popup Message with error that Mobile number not 12 digits
			ErrorPopUp("Sorry The mobile Number Must be 12 digit")
	else:
	
		#Popup Message with error that Amount more than the balance
		CashProcessPopUp("Sorry there is no sufficient balance ")
		
		#Delay function to close Automatic after some seconds the Popup message 
		ProcessPopUp.after(3000,lambda : ProcessPopUp.destroy())
		
		#Delay function to close Automatic after some seconds the Recharging window
		CompanyPopUp.after(3000,lambda : CompanyPopUp.destroy())
	
#----------------------------------------------------------------------------------------------------------#
# Function Name		: Company    															   			   #
# Parameters (in)	: CompanyName to write a header          						 					   #
# Description		: Function to PopUp a message to scan the number and amount from the user			   #
#----------------------------------------------------------------------------------------------------------#
def Company(CompanyName):

	#-----------------------------------------------* Creating a new Empty PopUp *----------------------------------------------------#
	
	global CompanyPopUp
	
	#Creation a new Empty window
	CompanyPopUp = tkinter.Toplevel()
	#Renaming the Window title
	CompanyPopUp.title("Recharge")
	#Relocating the window
	CompanyPopUp.geometry("400x300+600+50")
	#changing the window color
	CompanyPopUp.configure(background = "green")
	
	#----------------------------------------------* Name of the company in a lebel *-------------------------------------------------#
	
	#Getting the Account Number
	AccGet = str(Account.get())
	
	#Create and Place the label for Header in Pop Up 
	HeadMsg = tkinter.Label(CompanyPopUp, text = CompanyName , width = 50, bg = "white", fg = "maroon")
	HeadMsg.place(x = 25, y = 20)
	
	#------------------------------------* Scaning th Phone number and Amount from the user *-----------------------------------------#
	
	#Create and Place the label for the Phone Number in Pop Up 
	PhoneNumLabel = tkinter.Label(CompanyPopUp, text = "Phone Number with code : ", width = 25, bg = "white", fg = "black")
	PhoneNumLabel.place(x = 25, y = 100)
	
	#Create and Place the Entry for the Phone Number in Pop Up 
	PhoneNumEntry = tkinter.Entry(CompanyPopUp, width = 25, bg = "white", fg = "black",textvariable = PhoneNumber)
	PhoneNumEntry.place(x = 220, y = 100)
	#Clearing the Phone Number Entry
	PhoneNumEntry.delete(0, END)
	
	#Create and Place the Label for the Amount in Pop Up
	ChargeLabel = tkinter.Label(CompanyPopUp, text = "Amount : ", width = 25, bg = "white", fg = "black")
	ChargeLabel.place(x = 25, y = 150)
	
	#Create and Place the Entry for the Amount in Pop Up 
	ChargeEntry = tkinter.Entry(CompanyPopUp, width = 25, bg = "white", fg = "black", textvariable = Amount)
	ChargeEntry.place(x = 220, y = 150)
	#Clearing the Amount Entry
	ChargeEntry.delete(0, END)
	
	#--------------------------------------------------* Buttons of the PopUp *-------------------------------------------------------#
	
	#Create and Place the Button to Proceed the Recharging in Pop Up
	Charge = tkinter.Button(CompanyPopUp, text="Recharge >>", width = 10 , bg = "white", fg = "black", command = Recharging)
	Charge.place(x = 300, y = 250)
	
	#Create and Place the Button for Back in Pop Up
	BackButton = tkinter.Button(CompanyPopUp, text="<< Cancel", width = 10 , bg = "white", fg = "black", command = CompanyPopUp.destroy)
	BackButton.place(x = 200, y = 250)

#----------------------------------------------------------------------------------------------------------#
# Function Name		: FawryOptions    															   		   #
# Parameters (in)	: None          						 											   #
# Description		: Function to Redirect to a function according to the user choice				       #
#----------------------------------------------------------------------------------------------------------#
def FawryOptions():

	global Selected_Network
	
	if Selected_Network.get() == 1:
		Company("Orange Recharge")
		
	elif Selected_Network.get() == 2:
		Company("Etisalat Recharge")
		
	elif Selected_Network.get() == 3:
		Company("Vodafone Recharge")
		
	elif Selected_Network.get() == 4:
		Company("We Recharge")
	else:
		ErrorPopUp("Please Choose an option")

#----------------------------------------------------------------------------------------------------------#
# Function Name		: FawryService    															           #
# Parameters (in)	: None          						 											   #
# Description		: Function to PopUp a Window with the options in Fawry services				           #
#----------------------------------------------------------------------------------------------------------#
def FawryService():

	#-----------------------------------------------* Creating a new Empty PopUp *----------------------------------------------------#
	
	#Creation a new Empty window
	FawryPopUp = tkinter.Toplevel()
	#Renaming the Window title
	FawryPopUp.title("Fawry Services")
	#Relocating the window
	FawryPopUp.geometry("400x300+600+50")
	#changing the window color
	FawryPopUp.configure(background = "green")
	
	#---------------------------------------------------------------------------------------------------------------------------------#
	
	#Getting the Account Number
	AccGet = str(Account.get())
	
	#Create and Place the label for Header message in Pop Up 
	HeadMsg = tkinter.Label(FawryPopUp, text = " Fawry Services " , width = 50, bg = "white", fg = "maroon")
	HeadMsg.place(x = 25, y = 20)
	
	#-------------------------* Radio Buttons to Choose the Company to Recharge through Fawry Services *------------------------------#
	
	#Create and Place the Radio Button for Orange_Recharge in Pop Up 
	Orange_Recharge   = tkinter.Radiobutton(FawryPopUp,  text = "Orange Recharge       ",    variable = Selected_Network, value = 1)
	Orange_Recharge.place(x = 25, y = 80)
	#Create and Place the Radio Button for Etisalat_Recharge in Pop Up
	Etisalat_Recharge  = tkinter.Radiobutton(FawryPopUp, text = "Etisalat Recharge        ", variable = Selected_Network, value = 2)
	Etisalat_Recharge.place(x = 25, y = 120)
	#Create and Place the Radio Button for Vodafone_Recharge in Pop Up
	Vodafone_Recharge  = tkinter.Radiobutton(FawryPopUp, text = "Vodafone Recharge   ",      variable = Selected_Network, value = 3)
	Vodafone_Recharge .place(x = 25, y = 160)
	#Create and Place the Radio Button for We_Recharge in Pop Up
	We_Recharge = tkinter.Radiobutton(FawryPopUp,   text = " We Recharge              ",     variable = Selected_Network, value = 4)
	We_Recharge .place(x = 25, y = 200)
	
	#--------------------------------------------------* Buttons of the PopUp *-------------------------------------------------------#
	
	#Create and Place the Button get the Companies options in Pop Up
	Option = tkinter.Button(FawryPopUp, text="Select >>", width = 10 , bg = "white", fg = "black", command = FawryOptions)
	Option.place(x = 300, y = 250)
	
	#Create and Place the Button for Back in Pop Up
	BackButton = tkinter.Button(FawryPopUp, text="<< Cancel", width = 10 , bg = "white", fg = "black", command = FawryPopUp.destroy)
	BackButton.place(x = 200, y = 250)

#***************************************************************************************************************************************#


#***************************************************************************************************************************************#
#														  /* PopUp Messages */	    													#
#***************************************************************************************************************************************#

#----------------------------------------------------------------------------------------------------------#
# Function Name		: ErrorPopUp																	       #
# Parameters (in)	: Text to write	it						 											   #
# Description		: Function to Popup an error message to the user with OK Button to Close it			   #
#----------------------------------------------------------------------------------------------------------#
def ErrorPopUp(Text):

	#-----------------------------------------------* Creating a new Empty PopUp *----------------------------------------------------#

	global NotInPopUp
	#Creatin a new Empty window
	NotInPopUp = tkinter.Toplevel()
	#Renaming the Window title
	NotInPopUp.title("Warning Message")
	#Relocating the window
	NotInPopUp.geometry("400x100+600+50")
	#changing the window color
	NotInPopUp.configure(background = "maroon")		
	
	#--------------------------------------------------* Message of the PopUp *-------------------------------------------------------#
	
	#Create and Place the label for error message in Pop Up 
	ErrorAcc = tkinter.Label(NotInPopUp, text = Text, width = 50, bg = "white", fg = "black")
	ErrorAcc.place(x = 25, y = 20)
	#--------------------------------------------------* Buttons of the PopUp *-------------------------------------------------------#
	
	#Create and Place the Button for Exit Pop Up
	Exit = tkinter.Button(NotInPopUp, text="OK", width = 10 , bg = "white", fg = "black", command = NotInPopUp.destroy)
	Exit.place(x = 160, y = 60)

#----------------------------------------------------------------------------------------------------------#
# Function Name		: CashProcessPopUp																	   #
# Parameters (in)	: Text to write	it						 											   #
# Description		: Function to Popup an error message to the user without OK Button, Closed Automatic   #
#----------------------------------------------------------------------------------------------------------#
def CashProcessPopUp(Text):
	
	#-----------------------------------------------* Creating a new Empty PopUp *----------------------------------------------------#
	
	global ProcessPopUp
	
	#Creatin a new Empty window
	ProcessPopUp = tkinter.Toplevel()
	#Renaming the Window title
	ProcessPopUp.title("Warning Message")
	#Relocating the window
	ProcessPopUp.geometry("400x80+600+50")
	#changing the window color
	ProcessPopUp.configure(background = "maroon")

	#--------------------------------------------------* Message of the PopUp *-------------------------------------------------------#
	
	#Create and Place the label for error message in Pop Up 
	ErrorAcc = tkinter.Label(ProcessPopUp, text = Text, width = 50, bg = "white", fg = "black")
	ErrorAcc.place(x = 25, y = 20)

#***************************************************************************************************************************************#


#***************************************************************************************************************************************#
#												    	/* Login Functions*/		        											#
#***************************************************************************************************************************************#

#----------------------------------------------------------------------------------------------------------#
# Function Name		: Options																	   		   #
# Parameters (in)	: None						 											   			   #
# Description		: Function to Redirect to the option that the user choosed							   #
#----------------------------------------------------------------------------------------------------------#	
def Options():

	global Selected_Radio
	
	if Selected_Radio.get() == 1:
		CashWithdrawPopUp()
		
	elif Selected_Radio.get() == 2:
		BalanceInquiryPopUp()
		
	elif Selected_Radio.get() == 3:
		ChangePasswordPopUp()
		
	elif Selected_Radio.get() == 4:
		FawryService()
		
	else:
		ErrorPopUp("Please Choose an option")

#----------------------------------------------------------------------------------------------------------#
# Function Name		: OptionsPopUp																	       #
# Parameters (in)	: None						 											   			   #
# Description		: Function to Choose the option you want from the avaliable ones   					   #
#----------------------------------------------------------------------------------------------------------#		
def OptionsPopUp():

	#-----------------------------------------------* Creating a new Empty PopUp *----------------------------------------------------#
	
	#Creation a new Empty window
	SuccessPopUp = tkinter.Toplevel()
	#Renaming the Window title
	SuccessPopUp.title("Home Page")
	#Relocating the window
	SuccessPopUp.geometry("400x300+600+50")
	#changing the window color
	SuccessPopUp.configure(background = "green")
	
	#-----------------------------------------------------* Welcome Message *---------------------------------------------------------#
	
	#Getting the Account Number
	AccGet = str(Account.get())
	
	#Create and Place the label for Welcome message in Pop Up 
	WelcomeMsg = tkinter.Label(SuccessPopUp, text = "Welcome MR\MRs " + BankDataBase[AccGet]['NAME'], width = 50, bg = "white", fg = "black")
	WelcomeMsg.place(x = 25, y = 20)
	
	#-------------------------* Radio Buttons to Choose the Company to Recharge through Fawry Services *------------------------------#
	
	#Create and Place the Radio Button for Cash_Withdraw in Pop Up
	Cash_Withdraw  = tkinter.Radiobutton(SuccessPopUp,  text = "Cash Withdraw      ",     variable = Selected_Radio, value = 1)
	Cash_Withdraw.place(x = 25, y = 80)
	#Create and Place the Radio Button for Balance_Inquiry in Pop Up
	Balance_Inquiry = tkinter.Radiobutton(SuccessPopUp, text = "Balance Inquiry      ",   variable = Selected_Radio, value = 2)
	Balance_Inquiry.place(x = 25, y = 120)
	#Create and Place the Radio Button for Password_Change in Pop Up
	Password_Change = tkinter.Radiobutton(SuccessPopUp, text = "Password Change  ",       variable = Selected_Radio, value = 3)
	Password_Change .place(x = 25, y = 160)
	#Create and Place the Radio Button for Fawry_Service in Pop Up
	Fawry_Service = tkinter.Radiobutton(SuccessPopUp,   text = "Fawry Service          ", variable = Selected_Radio, value = 4)
	Fawry_Service .place(x = 25, y = 200)
	
	#--------------------------------------------------* Buttons of the PopUp *-------------------------------------------------------#
	
	#Create and Place the Button for Enter in Pop Up
	Option = tkinter.Button(SuccessPopUp, text="Enter >>", width = 10 , bg = "white", fg = "black", command = Options)
	Option.place(x = 300, y = 250)
	
	#Create and Place the Button for Back in Pop Up
	BackButton = tkinter.Button(SuccessPopUp, text="<< Back", width = 10 , bg = "white", fg = "black", command = SuccessPopUp.destroy)
	BackButton.place(x = 200, y = 250)
	
#----------------------------------------------------------------------------------------------------------#
# Function Name		: PasswordLoginFunc																	   #
# Parameters (in)	: None					 											   				   #
# Description		: Function to check the Password is valid or not giving 3 trials to enter it           #
#----------------------------------------------------------------------------------------------------------#	
def PasswordLoginFunc():

	global TryNum
	
	#Getting Account Number
	AccGet = str(Account.get())
	
	#Getting the Password
	passwordGet = Password.get()
	
	#Checking on the Password that it is 4 digits and is exist
	if (int(passwordGet) > 1000) and (int(passwordGet) < 9999):
		if BankDataBase[AccGet]['Password'] == passwordGet:
			
			#Opening the Options Window
			OptionsPopUp()
			
		else:	
		
			#create and place a label to PopUp an Error message that Password is wrong
			TryLabel = tkinter.Label(Main_Window, text = "Sorry Password incorrect, try again ", width = 35, bg = "olive", fg = "black")
			TryLabel.place(x = 136, y = 220)
			#Clearing the Password Entry
			Password.delete(0, END)
			#Decreasing the number of trials
			TryNum -= 1

			#the number of trials ran out
			if TryNum == 0:
			
				#Locking the account
				BankDataBase[AccGet]['Locker'] = 1
				#Error message that Account Locked and visit the branch 
				ErrorPopUp("Sorry your Account is locked, Please visit the branch")
				#Clearing the Account Entry
				Account.delete(0, END)
				#Clearing the Password window
				Main_Window.geometry("400x150+600+50")	
	else:
	
		#Error Popup message that Password is not 4 digits
		ErrorPopUp("Error : Password must be 4 digits")
		
#----------------------------------------------------------------------------------------------------------#
# Function Name		: LoginFunc																	           #
# Parameters (in)	: None					 											   				   #
# Description		: Function to check that the Account is registered and not locked 					   #
#                     with opening the password window 													   #
#----------------------------------------------------------------------------------------------------------#			
def LoginFunc():

	#Getting Account Number
	AccGet = str(Account.get())
	
	#Checking that the Account Number is exist and Not locked
	if AccGet in BankDataBase:
		if BankDataBase[AccGet]['Locker'] == 0:
			
			#Opening the Password Window
			Main_Window.geometry("400x350+600+50")
		else:
		
			#PopUp Message with an Error that the Account is locked
			ErrorPopUp("Sorry your Account is locked, Please visit the branch")
			Account.delete(0, END)
	else:
		
		#PopUp Message with an Error that the Account is not registerd
		ErrorPopUp("Sorry This Account is not registerd")
		Account.delete(0, END)

#----------------------------------------------------------------------------------------------------------#
# Function Name		: ShrinkMainWindow																	   #
# Parameters (in)	: None					 											   				   #
# Description		: Function to cancel the Password window and shrink the main window					   #
#----------------------------------------------------------------------------------------------------------#
def ShrinkMainWindow():
	#Resizing the window
	Main_Window.geometry("400x150+600+50")
	
	#Clearing the Password Entry
	Password.delete(0, END)

#***************************************************************************************************************************************#

	
#***************************************************************************************************************************************#		
#	 							/* Create and Place the Account Partition Items in the Main Window */		   							#	
#***************************************************************************************************************************************#

#Create and Place the label for the Account Number in the Main Window
AccLabel = tkinter.Label(Main_Window, text = "Enter your Bank Account Number :", width = 30, bg = "white", fg = "black")
AccLabel.place(x = 25, y = 20)

#Create and Place the Entry for the Account Number in the Main Window
Account = tkinter.Entry(Main_Window, width = 30, bg = "white", fg = "maroon")
Account.place(x = 170, y = 60)

#Create and Place the Button for Checking the Account Number in the Main Window
Enter = tkinter.Button(Main_Window, text="Enter", width = 10 , bg = "white", fg = "black", command = LoginFunc)
Enter.place(x = 160, y = 100)

#***************************************************************************************************************************************#		
#	 							/* Create and Place the Password Partition Items in the Main Window */			    					#	
#***************************************************************************************************************************************#

#Create and Place the Label for the Password in the main window	
passLabel = tkinter.Label(Main_Window, text = "Enter your Passwod Please :", width = 25, bg = "white", fg = "black")
passLabel.place(x = 25, y = 190)

#Create and Place the Entry for the Password in the main window	
Password = tkinter.Entry(Main_Window, width = 30, bg = "white", fg = "maroon",show ='*')
Password.place(x = 170, y = 240)

#Create and Place the Button for Login in the main window
Login = tkinter.Button(Main_Window, text="Login", width = 10 , bg = "white", fg = "black", command = PasswordLoginFunc)
Login.place(x = 200, y = 290)

#Create and Place the Button for Back in the main window
BackButton = tkinter.Button(Main_Window, text="Cancel", width = 10 , bg = "white", fg = "black", command = ShrinkMainWindow)
BackButton.place(x = 100, y = 290)

	
#***************************************************************************************************************************************#		
#	 										/* Create the main loop for the main window */												#	
#***************************************************************************************************************************************#

#To keep the window
Main_Window.mainloop() 	

#***************************************************************************************************************************************#									