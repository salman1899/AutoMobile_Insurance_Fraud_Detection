import streamlit as st
import pickle
import numpy as np
from streamlit_option_menu import option_menu


model=pickle.load(open("automobile_insurance_detect.pkl","rb"))



def Month(value):
    if value=="Select the Month":
        return 000
    elif value=="January":
        return 4
    elif value=="February":
        return 3
    elif value=="March":
        return 7
    elif value=="April":
        return 0
    elif value=="May":
        return 8
    elif value=="June":
        return 6
    elif value=="July":
        return 5
    elif value=="Auguest":
        return 1
    elif value=="September":
        return 11
    elif value=="October":
        return 10
    elif value=="November":
        return 9
    elif value=="December":
        return 2
    else:
        return "Invalid Input"
  
    
def DayOfWeek(value):
    if value=="Select the DayOfWeek":
        return 000
    elif value=="Sunday":
        return 3
    elif value=="Monday":
        return 1
    elif value=="Tuesday":
        return 5
    elif value=="Wednesday":
        return 6
    elif value=="Thursday":
        return 4
    elif value=="Friday":
        return 0
    elif value=="Saturday":
        return 2
    else:
        return "Invalid Input"
  
def Make(value):
    if value=="Select the Make":
        return 000
    elif value=="Pontiac":
        return 13
    elif value=="Toyota":
        return 17
    elif value=="Honda":
        return 6
    elif value=="Mazda":
        return 9
    elif value=="Chevrolet":
        return 2
    elif value=="Accura":
        return 0
    elif value=="Ford":
        return 5
    elif value=="VW":
        return 18
    elif value=="Dodge":
        return 3
    elif value=="Saab":
        return 15
    elif value=="Mercury":
        return 11
    elif value=="Saturn":
        return 16
    elif value=="Nisson":
        return 12
    elif value=="BMW":
        return 1
    elif value=="Jaguar":
        return 7
    elif value=="Porche":
        return 14
    elif value=="Mecedes":
        return 10
    elif value=="Ferrari":
        return 4
    elif value=="Lexus":
        return 8
    else:
        return "Invalid Input"
  
     
def AccidentArea(value):
    if value=="Select the AccidentArea":
        return 000
    elif value=="Urban":
        return 1
    elif value=="Rural":
        return 0
    else:
        return "Invalid Input"
  
    
    
def DayOfWeekClaimed(value):
    if value=="Select the DayOfWeekClaimed":
        return 000
    elif value=="Sunday":
        return 3
    elif value=="Monday":
        return 1
    elif value=="Tuesday":
        return 5
    elif value=="Wednesday":
        return 6
    elif value=="Thursday":
        return 4
    elif value=="Friday":
        return 0
    elif value=="Saturday":
        return 2
    else:
        return "Invalid Input"  

     
def MonthClaimed(value):
    if value=="Select the MonthClaimed":
        return 000
    elif value=="January":
        return 4
    elif value=="February":
        return 3
    elif value=="March":
        return 7
    elif value=="April":
        return 0
    elif value=="May":
        return 8
    elif value=="June":
        return 6
    elif value=="July":
        return 5
    elif value=="Auguest":
        return 1
    elif value=="September":
        return 11
    elif value=="October":
        return 10
    elif value=="November":
        return 9
    elif value=="December":
        return 2
    else:
        return "Invalid Input"      

    
def Sex(value):
    if value=="Select the Sex":
        return 000
    elif value=="Male":
        return 1
    elif value=="Female":
        return 0
    else:
        return "Ivalid Input"
    
  
     
def MaritalStatus(value):
    if value=="Select the MaritalStatus":
        return 000
    elif value=="Married":
        return 1
    elif value=="Single":
        return 2
    elif value=="Divorced":
        return 0
    elif value=="Widow":
        return 3
    else:
        return "Ivalid Input"
    
        
        
def Fault(value):
    if value=="Select the Fault":
        return 000
    elif value=="Policy Holder":
        return 0
    elif value=="Third Party":
        return 1
    else:
        return "Ivalid Input"
    
    
        
def PolicyType(value):
    if value=="Select the PolicyType":
        return 000
    elif value=="Sedan - Collision":
        return 1
    elif value=="Sedan - Liability":
        return 2
    elif value=="Sedan - All Perils":
        return 0
    elif value=="Sport - Collision":
        return 4
    elif value=="Utility - All Perils":
        return 6
    elif value=="Utility - Collision":
        return 7
    elif value=="Sport - All Perils":
        return 3
    elif value=="Utility - Liability":
        return 8
    elif value=="Sport - Liability":
        return 5
    else:
        return "Ivalid Input"
      
  
def VehicleCategory(value):
    if value=="Select the VehicleCategory":
        return 000
    elif value=="Sedan":
        return 0
    elif value=="Sport":
        return 1
    elif value=="Utility":
        return 2
    else:
        return "Ivalid Input"
    
  
def VehiclePrice(value):
    if value=="Select the VehiclePrice":
        return 000
    elif value=="20000 to 29000":
        return 0
    elif value=="30000 to 39000":
        return 1
    elif value=="more than 69000":
        return 5
    elif value=="less than 20000":
        return 4
    elif value=="40000 to 59000":
        return 2
    elif value=="60000 to 69000":
        return 3
    else:
        return "Ivalid Input"
    
def Deductible(value):
    if value=="Select the Deductible":
        return 000
    elif value=="400":
        return 1
    elif value=="700":
        return 3
    elif value=="500":
        return 2
    elif value=="300":
        return 0
    else:
        return "Ivalid Input"

def PastNumberOfClaims(value):
    if value=="Select the PastNumberOfClaims":
        return 000
    elif value=="2 to 4":
        return 1
    elif value=="none":
        return 3
    elif value=="1":
        return 0
    elif value=="more than 4":
        return 2
    else:
        return "Ivalid Input"
    
    
    
def AgeOfVehicle(value):
    if value=="Select the AgeOfVehicle":
        return 000
    elif value=="7 years":
        return 5
    elif value=="more than 7":
        return 6
    elif value=="6 years":
        return 4
    elif value=="5 years":
        return 3
    elif value=="new":
        return 7
    elif value=="4 years":
        return 2
    elif value=="3 years":
        return 1
    elif value=="2 years":
        return 0
    else:
        return "Ivalid Input"
    
def PoliceReportFiled(value):
    if value=="Select the PoliceReportFiled":
        return 000
    elif value=="Yes":
        return 1
    elif value=="No":
        return 0
    else:
        return "Ivalid Input"
 
    
def AgentType(value):
    if value=="Select the AgentType":
        return 000
    elif value=="External":
        return 0
    elif value=="Internal":
        return 1
    else:
        return "Ivalid Input"
    
def NumberOfCars(value):
    if value=="Select the NumberOfCars":
        return 000
    elif value=="1 vehicle":
        return 0
    elif value=="2 vehicles":
        return 1
    elif value=="3 to 4":
        return 2
    elif value=="5 to 8":
        return 3
    elif value=="more than 8":
        return 4
    else:
        return "Ivalid Input"
    
def BasePolicy(value):
    if value=="Select the BasePolicy":
        return 000
    elif value=="Collision":
        return 1
    elif value=="Liability":
        return 2
    elif value=="All Perils":
        return 0
    else:
        return "Ivalid Input"
    
def prediction(value):
    if value==0:
        return "Genuine CLAIM ✅"
    else:
        return "FRAUD CLAIM ❌ DETECTED"
    
def main():
    
   # with st.sidebar:
    selected = option_menu("Main Menu",["Home",'Settings',"Contact"], 
        icons=['house','gear-fill',"envelope"], menu_icon="cast", default_index=0,orientation="horizontal")
    #selected
    st.image("fraud_pic4.png",width=900)

   # st.title("Automobile Insurance Fraud Detection")
    #Menu=["Home","About","Help"]
    #choice=st.sidebar.selectbox("Menu",Menu)
    
   

    if selected == "Home":
        st.subheader("Home")
        with st.form(key="emotion_clf_form"):   
         submit_text=st.form_submit_button(label="submit")
        a=st.sidebar.selectbox("Month",("Select the Month","January","February","March","April","May","June","July","Auguest","September","October","November","December"))
        b=st.sidebar.selectbox("DayOfWeek",("Select the DayOfWeek","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"))
        c=st.sidebar.selectbox("Make",("Select the Make","Pontiac","Toyota","Honda","Mazda","Chevrolet","Accura","Ford","VW","Dodge","Saab","Mercury","Saturn","Nisson","BMW","Jaguar","Porche","Mecedes","Ferrari","Lexus"))
        d=st.sidebar.selectbox("AccidentArea",("Select the AccidentArea","Urban","Rural"))
        e=st.sidebar.selectbox("DayOfWeekClaimed",("Select the DayOfWeekClaimed","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"))      
        f=st.sidebar.selectbox("MonthClaimed",("Select the MonthClaimed","January","February","March","April","May","June","July","Auguest","September","October","November","December")) 

        
        g=st.sidebar.selectbox("Sex",("Select the Sex","Male","Female"))
        h=st.sidebar.selectbox("MaritalStatus",("Select the MaritalStatus","Married","Single","Divorced","Widow"))
        i=st.sidebar.number_input("Age")
        j=st.sidebar.selectbox("Fault",("Select the Fault","Policy Holder","Third Party"))
        k=st.sidebar.selectbox("PolicyType",("Select the PolicyType","Sedan - Collision","Sedan - Liability","Sedan - All Perils","Sport - Collision","Utility - All Perils","Utility - Collision","Sport - All Perils","Utility - Liability","Sport - Liability"))
        l=st.sidebar.selectbox("VehicleCategory",("Select the VehicleCategory","Sedan","Sport","Utility"))
        m=st.sidebar.selectbox("VehiclePrice",("Select the VehiclePrice","20000 to 29000","30000 to 39000","more than 69000","less than 20000","40000 to 59000","60000 to 69000"))
        n=st.sidebar.selectbox("Deductible",("Select the Deductible","400","700","500","300"))
        o=st.sidebar.selectbox("PastNumberOfClaims",("Select the PastNumberOfClaims","2 to 4","none","1","more than 4"))
        p=st.sidebar.selectbox("AgeOfVehicle",("Select the AgeOfVehicle","7 years","more than 7","6 years","new","4 years","3 years","2 years"))
        q=st.sidebar.selectbox("PoliceReportFiled",("Select the PoliceReportFiled","Yes","No"))
        r=st.sidebar.selectbox("AgentType",("Select the AgentType","External","Internal"))
        s=st.sidebar.selectbox("NumberOfcars",("Select the NumberOfCars","1 vehicle","2 vehicles","3 to 4","5 to 8","more than 8"))
        t=st.sidebar.selectbox("BasePolicy",("Select the BasePolicy","Collision","Liability","All Perils")) 
     
        a1=Month(a)
        b1=DayOfWeek(b)
        c1=Make(c)
        d1=AccidentArea(d)
        e1=DayOfWeekClaimed(e)
        f1=MonthClaimed(f)
        g1=Sex(g)
        h1=MaritalStatus(h)
        #i1
        j1=Fault(j)
        k1=PolicyType(k)
        l1=VehicleCategory(l)
        m1=VehiclePrice(m)
        n1=Deductible(n)
        o1=PastNumberOfClaims(o)
        p1=AgeOfVehicle(p)
        q1=PoliceReportFiled(q)
        r1=AgentType(r)
        s1=NumberOfCars(s)
        t1=BasePolicy(t)
        
        value1=a1,b1,c1,d1,e1,f1,g1,h1,i,j1,k1,l1,m1,n1,o1,p1,q1,r1,s1,t1
        value2=np.asarray(value1)
        value3=value2.reshape(1,-1)
        pred1=model.predict(value3)
        pred2=prediction(pred1)
        pred3=model.predict_proba(value3)
       # print(value1)
        if submit_text:
         col1,col2=st.columns(2)
         with col1:
          st.success("Prediction")
          st.write(pred2) 
          
         with col2:
          st.success("Prediction Proba")
          st.write(pred3)
    
    elif selected == "Settings":
        st.subheader("You have entered in Settings")
         
    elif selected == "Contact":
        st.subheader("You have entered in Contact") 
        
       
    #elif choice=="About":
       # st.header("About")
   # else:
       # st.header("Help")
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
if __name__=="__main__":
     main()    
