import sqlite3
import pandas as pd
import streamlit as st 
from streamlit_option_menu import option_menu
import random
import datetime
from datetime import datetime
from AloPsolutionsMain import (Business,TransactionInputForm,ProductEditForm,AddTransactionTypeForm,View_Profit_Loss,View_StocksReports,
                        TransactionEditForm,TransactionDeleteForm,ProductDeleteForm,EditTransactionTypeForm,SettlingPayableForm,
                        DeleteTransactionTypeForm,AddProductForm,AddExpensesForm,DeleteExpensesForm,ReceivablesColloectionForm)
from datetime import datetime,timedelta,date
from PIL import Image
import io



# App Layout
st.set_page_config(page_title="AloyceP Business App",
                   page_icon="",
                   layout="wide",
                   initial_sidebar_state="expanded")

# Images
Author = Image.open("./Pictures/aloyce.jpg")
BackImage = Image.open("./Pictures/Background.jpg")
ProductsImage = Image.open("./Pictures/ProductsImage.jpg")
TransTypesImage = Image.open("./Pictures/TransactionTypesImage.jpg")

Now = datetime.now().strftime("%d %B %Y | %a %I : %M %p ")
Today = date.today()
now = datetime.now().strftime("%d_%m_%y-%I-%M-%S-%p")
default_date_PY = Today - timedelta(days=365)

## Open Stylish file
with open("style.css") as stylefile:
    st.markdown(f"<style>{stylefile.read()}</style>",unsafe_allow_html=True)

## Function to download data
def DownloadData(viewlabel,df,file_name,locator=st):
    return locator.download_button(label=f"{viewlabel}",
                             data= df.to_csv().encode('utf-8'),
                             file_name=f'{file_name}_{now}.csv',
                              mime='text/csv')

## Function to Gnerate Horizontal Line
def Horizontal_Line():
    return st.markdown("<hr>",unsafe_allow_html=True)

# Class of Business Name
NestoryBusiness = Business("Nestory")

# Create Transaction Tables
# NestoryBusiness.TransactionTable()
# NestoryBusiness.OtherTransactionTable(tablename="SalesTable")
# NestoryBusiness.OtherTransactionTable(tablename="StocksTable")
#NestoryBusiness.OtherTransactionTable(tablename="COGSTable")
# NestoryBusiness.CreateAccount("ReceivablesAccount")
# NestoryBusiness.CreateAccount("PayablesAccount")
# NestoryBusiness.CreateAccount("CashAccount")

# NestoryBusiness.ProductTable()
# NestoryBusiness.TransactionTypeTable()
#NestoryBusiness.ExpensesTable()


# Top Header
st.markdown('<p class="TopIntro">Financial Solutions</p>',unsafe_allow_html=True)

empt, desc, dat = st.columns([6,2,3])
desc.error("Today's Date & Time")
dat.info(f"{Now}")
    
# Main Nav Bar
with st.sidebar:
    choice = option_menu(menu_title="Main Menu",menu_icon="",
              options=["Home","Stocking & Selling","Business Expenses","Receivables & Payables",
                        "Manage Products","Manage Transactions","Reporting & Analytics"],
               icons=["bookmarks","bi bi-bookmarks-fill","bi bi-briefcase-fill","bi bi-credit-card-fill",
                      "bi-cart-fill","bi bi-grid-3x3-gap-fill","bi bi-bar-chart-fill"],
               default_index= 0,
               #orientation="horizontal",
               styles={
                        "container":{"padding": "5px","background-color": "#fafafa"},
                        "icon": {"color": "orange", "font-size": "25px"}, 
                        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "#02ab21"},
                         } )


# Start WELCOME Page
if choice == "Home":

    st.markdown('''<p class="head">This App is desgined to provide financial solutions to retailer with small and medium scall business.
                                   The App will enable the owner to manage stock, sales, assets, liabilites and drawings of the business.
                                   Among other benefits the App is aiding the owner to trace the fasting moving products and taking appropriate actions
                                   like increase the stock. It also provides alerts the owner about the minimum balance of merchandise, cash, and other items. 
                                   It also provides the financial position of the business at any point in time.</p>''', 
                     unsafe_allow_html=True)
    
    with st.expander("About the Creator"):
        Image, profile = st.columns([1,3])
       
        Image.image(Author)
      
        profile.markdown('''<p class="profile">My Name is Aloyce Mbepera, A Banking Professional with vast experience in Business Analystics & Reporting</p>''', 
                     unsafe_allow_html=True)
        profile.markdown('<p class="profile">Phone: +255759431531 Email: aloycebosco2011@gmail.com, </p>', 
                     unsafe_allow_html=True)
# End WELCOME Page


# Start Transactions Page
elif choice == "Stocking & Selling":

    Horizontal_Line()

    choiceBT = option_menu(menu_title="",menu_icon="",
              options=["Record Transaction","Edit Transactions","Delete Transactions"],
               icons=["bi bi-journal-plus","bi bi-pen-fil","bi bi-journal-x"],
               default_index= 0,
               orientation="horizontal",
               styles={
                        "container":{"padding": "5px","background-color": "#fafafa"},
                        "icon": {"color": "orange", "font-size": "25px"}, 
                        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "#02ab21"},
                         } )

    # Transaction View Func
    def AllTransactionview():
        #Run Transactions View Function 
        # Transactions Table to DF
        AllTransactions = NestoryBusiness.ViewTable("TransactTable")
        Transactions_df = pd.DataFrame(AllTransactions, columns = ['Transaction ID', 'Product Name', 'Product Quantity',"Product Unit Price",
                                                                    "Transaction Type","Tranasction Date","Product Unit Measure","Total Transaction Value",
                                                                    "Transaction Description","System Transaction Date","Customer/Supplier Name"],
                                      ).set_index("Transaction ID")
      
        with st.expander("View All Transactions"):

            st.table(Transactions_df.sort_index(ascending=False).head(6))
            st.info(f"The Business has a Total of:: {len(Transactions_df)} Transactions" )
            DownloadData(viewlabel="Download Transactions",df=Transactions_df,file_name="Transactions")
        
        # st.info("SALES TABLE")
        # st.table(NestoryBusiness.ViewTable("SalesTable"))
        # st.info("STOCKS BAL TABLE")
        # st.table(NestoryBusiness.ViewTable("StocksTable"))
        # st.info("COST OF SALES TABLE")
        # st.table(NestoryBusiness.ViewTable("COGSTable"))
        # st.table(NestoryBusiness.ViewTable("ClosingStockBalTable"))
        # st.info("RECEIVABLE ACCOUNT")
        # st.table(NestoryBusiness.ViewTable("ReceivablesAccount")) 
        # # st.info("PAYABLE ACCOUNT")
        # st.table(NestoryBusiness.ViewTable("PayablesAccount")) 
        st.info("CASH ACCOUNT")
        st.table(NestoryBusiness.ViewTable("CashAccount")) 
        
          

    if choiceBT  == "Record Transaction":
        
        #Run Transactions Input Table
        TransactionInputForm()

        #Run Transactions View Function 
        AllTransactionview()

        st.image(BackImage,width=100,use_column_width=True)

    elif choiceBT  == "Edit Transactions":

       #Run Transaction Edit Func
       TransactionEditForm()

       #Run Transactions View Function 
       AllTransactionview()

       
    elif choiceBT  == "Delete Transactions":

        #Run Transaction Delete Func
        TransactionDeleteForm()

        #Run Transactions View Function 
        AllTransactionview()

# Start Receivables & Payables
elif choice == "Receivables & Payables":
    Horizontal_Line()

    choiceRecPay = option_menu(menu_title="",menu_icon="",
              options=["Update Debtors","Update Payables"],
               icons=["bi bi-journal-plus","bi bi-pen-fil"],
               default_index= 0,
               orientation="horizontal",
               styles={
                        "container":{"padding": "5px","background-color": "#fafafa"},
                        "icon": {"color": "orange", "font-size": "25px"}, 
                        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "#02ab21"},
                         } )
    
    if choiceRecPay == "Update Debtors":
        # Transaction View Receivables
        def ViewReceivables():
            #Run Transactions View Receivable Account 
            # Transactions Table to DF
            AllReceivables = NestoryBusiness.ViewTable("ReceivablesAccount")
            Receivables_df = pd.DataFrame(AllReceivables, columns = ['Transaction ID', "Tranasction Date", "Transaction Details", "Debt Amount",
                                                                "Credit Amount","Book Balance","Customer Name", "System Transaction Date"],
                                                                    ).set_index("Transaction ID")
            with st.expander("View Debtors Statement"):

                st.table(Receivables_df.sort_index(ascending=True).head(10))
                # st.info(f"The Business has a Total of:: {len(Receivables_df)} Receivables" )
                DownloadData(viewlabel="Download Receivables Statement",df=Receivables_df,file_name="Receivables")
        
        # Receivable Recovery Form
        ReceivablesColloectionForm()

        # View Receivable
        ViewReceivables()

    if choiceRecPay == "Update Payables":
        def ViewPayables():
            # Transactions Table to DF
            AllPayables = NestoryBusiness.ViewTable("PayablesAccount")
            Payables_df = pd.DataFrame(AllPayables, columns = ['Transaction ID', "Tranasction Date", "Transaction Details", "Debt Amount",
                                                                "Credit Amount","Book Balance","Supplier Name", "System Transaction Date"],
                                                                    ).set_index("Transaction ID")
            with st.expander("View Payables Statement"):

                st.table(Payables_df.sort_index(ascending=True).head(10))
                # st.info(f"The Business has a Total of:: {len(Receivables_df)} Receivables" )
                DownloadData(viewlabel="Download Payables Statement",df=Payables_df,file_name="Payables")
        
        # Payables Settlement Form
        SettlingPayableForm()
         # View Payables
        ViewPayables()

# Start Business Expenses
elif choice == "Business Expenses":

    # Expenses View & Download Func
    def AllExpensesView():
        AllExpenses = NestoryBusiness.ViewTable("ExpensesTable")
        AllExpenses_df = pd.DataFrame(AllExpenses, columns = ['Transaction ID', 'Expense Name', 'Expense Category',"Expense Amount",
                                                                "Payment Mode","Transaction Date","Description"
                                                            ],
                                        ).set_index("Transaction ID")

        with st.expander("View All Expenses"):
            st.table(AllExpenses_df.sort_index(ascending=False).head(6))
            st.info(f"The Business has a Total of:: {len(AllExpenses_df)} Expenses Types" )
            DownloadData(viewlabel="Download Expenses",df=AllExpenses_df,file_name="Expenses")
    
    Horizontal_Line()

    choiceExp = option_menu(menu_title="",menu_icon="",
              options=["Record Expenses","Delete Expenses"],
               icons=["bi bi-journal-plus","bi bi-journal-x"],
               default_index= 0,
               orientation="horizontal",
               styles={
                        "container":{"padding": "5px","background-color": "#fafafa"},
                        "icon": {"color": "orange", "font-size": "25px"}, 
                        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "#02ab21"},
                         } )

    if choiceExp == "Record Expenses":
        # Run Expenses Form
        AddExpensesForm()

        # View Expenses Func
        AllExpensesView()

    elif choiceExp == "Delete Expenses":
        # Delete Expenses Form
        DeleteExpensesForm()

        # View Expenses Func
        AllExpensesView()



# End Business Expenses

# Start Products Page
elif choice == "Manage Products":
    
    
    st.image(ProductsImage,width=100,use_column_width=True)

    choiceProducts = option_menu(menu_title="",menu_icon="",
              options=["Add Product","Edit Product", "Delete Product"],
               icons=["bi-cart-plus-fill","bi bi-eraser-fill","bi-cart-x-fill"],
               default_index= 0,
               orientation="horizontal",
               styles={
                        "container":{"padding": "5px","background-color": "#fafafa"},
                        "icon": {"color": "orange", "font-size": "25px"}, 
                        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "#02ab21"},
                         } )

    #Run Products View Function 
    def ProductViewFunc():
        Products = NestoryBusiness.ViewTable("ItemTable")
        with st.expander("View All Products"):
            Products_df = pd.DataFrame(Products, columns = ['Product_ID', 'Product_Name', 'Product_Measure',
                                                                "Description","Creation_Date"],
                                                                ).set_index("Product_ID")

            st.table(Products_df.sort_index(ascending=False).head(6))
            st.info(f"The Business has a Total of:: {len(Products_df)} Products" )
            
            DownloadData(viewlabel="Download All Products",df=Products_df,file_name="Products")
    if choiceProducts  == "Add Product":
        #Run Add Product Func
        AddProductForm()

       #Run Products View Function 
        ProductViewFunc()    
                                                                         
       
    elif choiceProducts  == "Edit Product":
        #Run Product Edit Func
        ProductEditForm()

        #Run Products View Function 
        ProductViewFunc()  
    
       
    elif choiceProducts  == "Delete Product":
        #Run Products Delete Function 
        ProductDeleteForm()

        #Run Products View Function 
        ProductViewFunc() 


# Start Manage Transactions Page
elif choice == "Manage Transactions":

    st.image(TransTypesImage,width=100,use_column_width=True)

    choiceMT = option_menu(menu_title="",menu_icon="",
              options=["Add Transaction Type","Edit Transaction Type", "Delete Transaction Type"],
               icons=["bi-cart-plus-fill","bi bi-eraser-fill","bi-cart-x-fill"],
               default_index= 0,
               orientation="horizontal",
               styles={
                        "container":{"padding": "5px","background-color": "#fafafa"},
                        "icon": {"color": "orange", "font-size": "25px"}, 
                        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "#02ab21"},
                         } )

    #Run Products View Function 
    def TransTypeViewFunc():
        TransTypes = NestoryBusiness.ViewTable("TransactionTypeTable")
        with st.expander("View All Transaction Types"):
            TransType_df = pd.DataFrame(TransTypes, columns = ['TransactionType_ID', 'Transaction_Type_Name','Transaction_Type_Category',
                                                             'Financial_Statement_Part',"Creation_Date"],
                                        ).set_index("TransactionType_ID")

            st.table(TransType_df.sort_index(ascending=False).head(6))
            st.info(f"The Business has a Total of:: {len(TransType_df)} Transaction Types" )
            
            DownloadData(viewlabel="Download All Transactions Types",df=TransType_df,file_name="TransactionTypes")

    if choiceMT  == "Add Transaction Type":
        #Run Add Transaction Type Function 
        AddTransactionTypeForm()

        #Run Transactions Type View Function 
        TransTypeViewFunc()


    elif choiceMT  == "Edit Transaction Type":
        #Run Edit Transaction Type Function 
        EditTransactionTypeForm()

        #Run Transactions Type View Function 
        TransTypeViewFunc()

    elif choiceMT  == "Delete Transaction Type":
        #Run Delete Transaction Type Function 
        DeleteTransactionTypeForm()

        #Run Transactions Type View Function 
        TransTypeViewFunc()

elif choice == "Reporting & Analytics":

    # st.image(TransTypesImage,width=100,use_column_width=True)
    Horizontal_Line()

    choiceReports = option_menu(menu_title="",menu_icon="",
              options=["Inventory","Profit & Loss", "Financial Position","Financial Ratios"],
               icons=["bi bi-database-fill-add","bi bi-reception-4","bi bi-file-spreadsheet-fill","bi-cart-x-fill"],
               default_index= 0,
               orientation="horizontal",
               styles={
                        "container":{"padding": "5px","background-color": "#fafafa"},
                        "icon": {"color": "orange", "font-size": "25px"}, 
                        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "#02ab21"},
                         } )
    
    # View Closing Stock Balance
    if choiceReports == "Inventory":

        # View Reports
        View_StocksReports()

    if choiceReports == "Profit & Loss":
        
        # View Reports
        View_Profit_Loss()

         
    