import streamlit as st
from docxtpl import DocxTemplate
import base64
from PIL import Image
# import pythoncom
import os
import subprocess
from subprocess import Popen
st.set_page_config(layout="wide")

# subprocess.call(['apt', 'install', 'libreoffice', '--no-install-recommends'])
# LIBRE_OFFICE =
path = os.getcwd()
path1 = path + "/documents"
path2 = path + "/generated documents"


image = Image.open(path+'/law diktat.png')
st.sidebar.image(image, width=280)


def convert_to_pdf(input_docx, out_folder):

    # libreoffice --headless --convert-to pdf MyWordFile.docx --outdir ./
    p = Popen(['libreoffice', '--headless', '--convert-to', 'pdf', '--outdir',
               out_folder, input_docx])
    # print([, '--convert-to', 'pdf', input_docx])
    p.communicate()


def displayPDF(file):
    #Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="900" height="1000" type="application/pdf"></iframe>'

   # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)


def triggerfunction(file, file_name):
    convert_to_pdf(file, path2+'/')
    with open(path2+"/"+file_name, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(label="Download PDF",
                       data=PDFbyte,
                       file_name= file_name+".pdf",
                       mime='application/octet-stream')


def DistributorSupplierAgreement(path1, path2):

    st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Consolas'; color: #FFFFFF; text-align: center} 
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">DISTRIBUTOR SUPPLIER AGREEMENT</p>',
                unsafe_allow_html=True)

    doc = DocxTemplate(path1 + "/Supplier Distributor AgreementR.docx")
    doc1 = DocxTemplate(path1 + "/Supplier Distributor Agreement.docx")

    context = {"Place": st.sidebar.text_input("Place", value="Place", placeholder="Place"),

               "Date": st.sidebar.date_input("Agreement Date"),

               "Supplier": st.sidebar.text_input("Supplier Name", value="Supplier Name"),

               "Address_Sup": st.sidebar.text_input("Supplier Registered at the Address", value="Supplier Registered at the Address"),

               "S_Sole_Proprietor_or_Partner_or_Duly_Authorized_Member_Of_Staff_or_NA": st.sidebar.selectbox("Supplier Represented By",
                                                                                                             ("Sole Proprietor", "Partner", "Duly Authorized Member of Staff", "NA")),

               "Supplier_Representative": st.sidebar.text_input("Supplier Representative Name", value="Supplier Representative Name"),

               "Distributor": st.sidebar.text_input("Distributorr Name", value="Distributor Name"),

               "Address_Dist": st.sidebar.text_input("Distributor Registered at the Addrsess", value="Distributor Addrsess"),

               "D_Sole_Proprietor_or_Partner_or_Duly_Authorized_Member_Of_Staff_or_NA": st.sidebar.selectbox("Distributor Represented By:",
                                                                                                             ("Sole Proprietor", "Partner", "Duly Authorized Member of Staff", "NA")),

               "Distributor_Representative": st.sidebar.text_input("Name of the Distributor Representative", value="Distributor Representative Name"),

               "Goods": st.sidebar.text_input("Name of the Goods to be supplied", value="Goods to be supplied"),

               "Purpose": st.sidebar.text_input("Purpose", value="Purpose"),

               "From_date": st.sidebar.date_input("Effective from date"),

               "To_Date": st.sidebar.date_input("Effective till date"),

               "Cost_or_unit": st.sidebar.text_input("Supplied at Cost per unit", value="Supplied at Cost per unit"),

               "Number": st.sidebar.text_input("Minimum purchase quantity", value="Minimum purchase quantity"),

               "Worth_of_Units_or_Units": st.sidebar.text_input("Units of Minimum purchase quantity", value="Units of Minimum purchase quantity"),

               "receiving_of_goods_or_sale_of_goods": st.sidebar.selectbox("Payment must be done after: ", ("Recieving of Goods", "Sale of Goods")),

               "method_of_payment": st.sidebar.selectbox("Method of Payment: ", ("Debit Card", "Credit Card", "Cash")),

               "reserves_or_does_not_reserve": st.sidebar.selectbox("Supplier Reserve Status:", ("reserves", "does not reserve")),

               "is_not_or_is": st.sidebar.selectbox("Agreement ___ an exclusive distribution agreement ", ("is", "is not")),

               "Supplier_or_Distributor": st.sidebar.selectbox("Who stores the goods in warehouse: ", ("Supplier", "Distributor")),

               "A_Supplier_or_Distributor_or_Both": st.sidebar.selectbox("Undertaker of storage expenses: ", ("Supplier", "Distributor")),

               "A_Percent_of_Expenses_undertaken": st.sidebar.text_input("Percent of storage expenses undertaken", value="Percent of storage expenses undertaken"),

               "B_Supplier_or_Distributor_or_Both": st.sidebar.selectbox("Undertaker of transport expenses: ", ("Supplier", "Distributor", "Both")),

               "B_Percent_of_Expenses_undertaken": st.sidebar.text_input("Percent of transport cost undertaken (0-100):", value="Percent of transport cost undertaken"),

               "at_the_request_of_the_other_party_or_periodically_or_both": st.sidebar.selectbox("Funrnish Information regarding sales: ",
                                                                                                 ("At the request of other party", "Periodically", "Both")),
               "Number_of_Days": st.sidebar.text_input("Claims must be settled within", value="Claims must be settled within"),

               "Name_of_State_or_District": st.sidebar.text_input("State/District Jusrisdiction", value="subject to which state/district jusrisdiction"),

               "Supplier_Representative_Position": st.sidebar.text_input("Supplier Representative Position", value="Supplier Representative Position"),

               "Distributor_Representative_Position": st.sidebar.text_input("Distributor Representative Position", value="Distributor Representative Position"),

               "Witness_1_Name": st.sidebar.text_input("First Witness Name", value="First Witness Name"),

               "Witness_2_Name": st.sidebar.text_input("Second Witness Name", value="Second Witness Name")
               }

    doc.render(context)
    doc1.render(context)
    doc.save(path2+"/Supplier Distributor GeneratedR.docx")
    doc1.save(path2+"/Supplier Distributor Generated.docx")
    convert_to_pdf(path2+"/Supplier Distributor GeneratedR.docx", path2+'/')
    # 
    f1 = path2+'/Supplier Distributor GeneratedR.pdf'
    if st.button('Done editing'):
        triggerfunction(path2+"/Supplier Distributor Generated.docx","Supplier Distributor Generated.pdf")

    displayPDF(f1)


def RentalAgreement(path1, path2):
    st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Consolas'; color: #FFFFFF; text-align: center} 
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">RENTAL AGREEMENT</p>', unsafe_allow_html=True)

    doc = DocxTemplate(path1+"/Rental AgreementR.docx")
    doc1 = DocxTemplate(path1 + "/Rental Agreement.docx")

    context = {"City": st.sidebar.text_input("City Name", value="City"),
               "State": st.sidebar.text_input("State Name", value="State"),
               "Date_Month_Year": st.sidebar.date_input("Date"),

               "Landlord_Name": st.sidebar.text_input("Name of Landlord", value="Landlord Name"),
               "Landlord_AddressLine1": st.sidebar.text_input("Landlord Address Line 1", value="Landlord Address Line 1"),
               "Landlord_AddressLine2": st.sidebar.text_input("Landlord Address Line 2", value="Landlord Address Line 2"),
               "Landlord_City": st.sidebar.text_input("Landlord City", value="Landlord City"),
               "Landlord_State": st.sidebar.text_input("Landlord State", value="Landlord State"),
               "Landlord_Pincode": st.sidebar.text_input("Landlord Pincode", value="Landlord Pincode"),

               "Tenant_Name": st.sidebar.text_input("Tenant Name", value="Tenant Name"),
               "Tenant_Address_Line1": st.sidebar.text_input("Tenant Address Line 1", value="Tenant Address Line 1"),
               "Tenant_Address_Line2": st.sidebar.text_input("Tenant Address Line 2", value="Tenant Address Line 2"),
               "Tenent_City": st.sidebar.text_input("Tenent City", value="Tenent City"),
               "Tenent_State": st.sidebar.text_input("Tenent State", value="Tenent State"),


               "Lease_Property_Address_Line1_Address_Line2_City_State_PinCode": st.sidebar.text_input("Address of XXXXXXX", value="", placeholder=""),
               "IndependentHouse_or_Apartment_or_FarmHouse_or_ResidentialProperty": st.sidebar.selectbox("Category",
                                                                                                         ("Independent House", "Apartment", "Farm House", "Residential Property")),
               "X_Bedrooms": st.sidebar.text_input("Number of Bedrooms", value="Number of Bedrooms") + " bedrooms",
               "X_Bathrooms": st.sidebar.text_input("Number of Bathrooms", value="Number of Bathrooms") + " bathrooms",
               "X_Carparks": st.sidebar.text_input("Number of Car Parks", value="Number of Car Parks") + " car Parks",
               "XXXX_Square_Feet": st.sidebar.text_input("Area", value="Area") + " sq.ft",
               "Lease_Term": st.sidebar.text_input("Lease Term", value="Lease Term"),
               "Lease_Start_Date": st.sidebar.date_input("Lease Start Date:"),
               "Lease_Period": st.sidebar.text_input("Lease Period", value="Lease Period"),
               "one_month`s_notice": st.sidebar.text_input("Notice Period (in months)", value="Notice Period") + " month's notice",
               "Monthly_Rental_in_Number_&_Words": st.sidebar.text_input("Monthly Rent (in words)", value="Monthly Rent", placeholder="Monthly Rent in Words"),
               "_stday": st.sidebar.text_input("Day (in numbers)", value="Day"),
               "Starting_Meter_Reading": st.sidebar.text_input("Electric Meter Reading (in numbers)", value="Electric Meter Reading"),
               "Rental_Deposit_in_Number": st.sidebar.text_input("Rental Deposits", value="Rental Deposits"),
               "Rental_Deposit_in_and_Words": st.sidebar.text_input("Rental Deposit", value="Rental Deposit"),
               "W1_Name": st.sidebar.text_input("Witness 1 Name", value="Witness 1 Name"),
               "W1_Address": st.sidebar.text_input("Witness 1 Address", value="Witness 1 Address"),
               "W2_Name": st.sidebar.text_input("Witness 2 Name", value="Witness 2 Name"),
               "W2_Address": st.sidebar.text_input("Witness 2 Address", value="Witness 2 Address")
               }

    doc.render(context)
    doc1.render(context)
    doc.save(path2+"/Rental Agreement GeneratedR.docx")
    doc1.save(path2+"/Rental Agreement Generated.docx")
    convert_to_pdf(path2+"/Rental Agreement GeneratedR.docx", path2+'/')
    
    #convert("C:/Users/roysm/Documents/Alpha AI/Law Updated/generated documents/Supplier Distributor Generated.docx","C:/Users/roysm/Documents/Alpha AI/Law Updated/generated documents/Supplier Distributor Generated.pdf")
    f1 = path2+'/Rental Agreement GeneratedR.pdf'

    if st.button('Done editing'):
        triggerfunction(path2+"/Rental Agreement Generated.docx","Rental Agreement Generated.pdf")

    displayPDF(f1)


def NonDisclosureAgreement(path1, path2):
    st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Consolas'; color: #FFFFFF; text-align:center} 
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">NON-DISCLOSURE AGREEMENT</p>',
                unsafe_allow_html=True)

    doc = DocxTemplate(path1+"/Non Disclosure AgreementR.docx")
    doc1 = DocxTemplate(path1+"/Non Disclosure Agreement.docx")
    day = st.sidebar.text_input("Enter day as 1st/2nd/3rd", value='Day')
    Month = st.sidebar.text_input("Name of the month", value='Month')
    Year = st.sidebar.text_input(
        "Enter the year (in the format 2022, 2021...):", value='Year')
    R_Name = st.sidebar.text_input(
        "Name of the Registered Company:", value='Registered company Name')
    I_Name = st.sidebar.text_input(
        "Name of the Incorporated Company:", value='Incorporated Company Name')

    context = {"day": day,
               "Month": Month,
               "Year": Year,

               "R_INSERT_NAME_OF_COMPANY": R_Name,
               "CIN_No": st.sidebar.text_input("CIN Number of the company: ", value="CIN No"),
               "R_INSERT_ADDRESS": st.sidebar.text_input("Address of the Registered Company: ", value="Address"),
               "R_INSERT_ABBREVIATION_IF_ANY": st.sidebar.text_input("Abbreviation of Registered company or NA", value="Abbreviation"),
               "I_INSERT_NAME_OF_COMPANY": I_Name,
               "I_INSERT_ADDRESS": st.sidebar.text_input("Address of the Incorporated Company:"),

               "I_INSERT_ABBREVIATION ": st.sidebar.text_input("Abbreviation of Incorporated company or NA", value='Abbreviation'),
               "R_Company": R_Name,
               "I_Company": I_Name,
               "R_INSERT": R_Name,
               "I_INSERT": I_Name,


               "Business_Arrangement_for_purpose_of": st.sidebar.text_input("Business Arrangement for purpose of: ", value='Purpose'),
               "R_Company_1": R_Name,
               "I_Company_1": I_Name,
               "Number_of_days": st.sidebar.text_input("Number of days", value=" N days"),
               "place_of_arbitration": st.sidebar.text_input("Place of Arbitration: ", value="Place of Arbitration"),
               "No_of_years": st.sidebar.text_input("Agreement Shall Continue for (no.of.years): "),
               "no_of_days": st.sidebar.text_input("with in __ days of termination:", value='No. of days of termination'),
               "R_NAME_OF_COMPANY": R_Name,
               "R_Name": st.sidebar.text_input("Name of the person from Registered Company:", value="Name of the Person"),
               "R_Title": st.sidebar.text_input("Designation/ Title of the above mentioned person", value="Title of the person"),
               "I_NAME_OF_COMPANY": I_Name,
               "I_Name": st.sidebar.text_input("Name of the person from Incorporated Company:", value="Name of the person"),
               "I_Title": st.sidebar.text_input("Designation/ Title of the above person", value="Title of the person"),
               }
    doc.render(context)
    doc1.render(context)
    doc.save(path2+"/NDA GeneratedR.docx")
    doc1.save(path2+"/NDA Generated.docx")
    convert_to_pdf(path2+"/NDA GeneratedR.docx", path2+'/')
    f1 = path2+'/NDA GeneratedR.pdf'
    if st.button('Done editing'):
        triggerfunction(path2+"/NDA Generated.docx","NDA Generated.pdf")
    displayPDF(f1)


def IndependentContractorAgreement(path1, path2):
    st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Consolas'; color: #FFFFFF; text-align: center} 
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">INDEPENDENT CONTRACTOR AGREEMENT</p>',
                unsafe_allow_html=True)
    doc = DocxTemplate(path1+"/Independent Contractor AgreementR.docx")
    doc1 = DocxTemplate(path1+"/Independent Contractor Agreement.docx")

    context = {"date": st.sidebar.date_input("Agreement Date:"),
               "Name_of_the_company": st.sidebar.text_input("Company Name", value="Company Name"),
               "c_state_or_province": st.sidebar.text_input("Company State/Province", value="Company State/Province"),
               "c_full_address_of_company": st.sidebar.text_input("Company Address", value="Company Address"),

               "Name_of_owner": st.sidebar.text_input("Owner Name", value="Owner Name"),
               "full_address_of_owner": st.sidebar.text_input("Owner Address", value="Owner Address"),
               "description_of_work_to_be_performed": st.sidebar.text_input("Description of the work", value="Description of the work"),
               "name": st.sidebar.text_input("Name", value="Name"),
               "amount": st.sidebar.text_input("Amount Owner need to pay", value="Amount Owner need to pay"),

               "description_of_timing_and_mode_of_payment": st.sidebar.selectbox("Method of Payment: ", ("Debit Card", "Credit Card", "Cash")),
               "completion_date": st.sidebar.date_input("Work Completion Date:"),
               "i_amount": st.sidebar.text_input("Amount Contractor has to pay", value="Amount Contractor has to pay"),
               "day_or_week_or_month": st.sidebar.selectbox("Duration of the payment for the Damages: ", ("Days", "Weeks", "Months")),
               "G_State_or_Province": st.sidebar.text_input("Governing State/Province", value="Governing State/Province"),
               "g_state_or_province": st.sidebar.text_input("governing State/Province", value="governing State/Province"),
               "number": st.sidebar.text_input("Duration (in numbers)", value="Duration"),
               "days_or_weeks_or_months": st.sidebar.text_input("days/weeks/months", value="days/weeks/months")
               }

    doc.render(context)
    doc1.render(context)
    doc.save(path2+"/Independent Contractor Agreement GeneratedR.docx")
    doc1.save(path2+"/Independent Contractor Agreement Generated.docx")
    convert_to_pdf(path2+"/Independent Contractor Agreement GeneratedR.docx", path2+'/')
    f1 = path2+'/Independent Contractor Agreement GeneratedR.pdf'

    if st.button('Done editing'):
        triggerfunction(path2+"/Independent Contractor Agreement Generated.docx","Independent Contractor Agreement Generated.pdf")

    displayPDF(f1)


def EmploymentContract(path1, path2):
    st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Consolas'; color: #FFFFFF; text-align: center} 
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">EMPLOYMENT CONTRACT</p>',
                unsafe_allow_html=True)

    doc = DocxTemplate(path1+"/Employment ContractR.docx")
    doc1 = DocxTemplate(path1+"/Employment Contract.docx")

    context = {"Place": st.sidebar.text_input("Place", value="Place"),
               "dd_mm_yy": st.sidebar.text_input("Agreement Date", value="Agreement Date"),
               "Employer": st.sidebar.text_input("Name of the Employee", value="Employer Name"),
               "Address_1": st.sidebar.text_input("Employer Address", value="Employer Address"),
               "S_Sole_Proprietor_or_Partner_or_Duly_Authorized_Member_Of_Staff_or_NA": st.sidebar.selectbox("Supplier Represented By",
                                                                                                             ("Represented BY", "Sole Proprietor", "Partner", "Duly Authorized Member of Staff", "NA")),
               "Mr_or_Ms": st.sidebar.selectbox("Title:", ("Mr.", "Mrs.")),
               "Employer_Representative": st.sidebar.text_input("Employer Representative", value="Employer Representative"),
               "Name_of_Employee": st.sidebar.text_input("Employee Name", value="Employee Name"),
               "Name": st.sidebar.text_input("Name", value="Name"),
               "Age": st.sidebar.text_input("Age", value="age"),
               "Address_2": st.sidebar.text_input("Address", value="Address"),
               "a_or_the": st.sidebar.text_input("a_or_the", value="a_or_the"),
               "Position": st.sidebar.text_input("Position", value="Position"),
               "Responsibility_1": st.sidebar.text_input("Responsibility", value="Responsibility"),
               "Duration": st.sidebar.text_input("Duration", value="Duration"),
               "from_time": st.sidebar.time_input("From Time:"),
               "to_time": st.sidebar.time_input("To Time:"),
               "from_day": st.sidebar.text_input("From Day", value="From Day"),
               "to_day": st.sidebar.text_input("To Day", value="To Day"),
               "Annual_Income": st.sidebar.text_input("Annual Income", value="Annual Income"),
               "daily_or_weekly_or_monthly_or_yearly": st.sidebar.selectbox("Duration: ", ("Daily", "Weekly", "Monthly", "Yearly")),
               "method_of_payment": st.sidebar.selectbox("Method of Payment: ", ("Debit Card", "Credit Card", "Cash")),
               "Option_for_additional_clauses_regarding_compensation_or_insurance": st.sidebar.text_input("Optional Clause else enter N/A", value="Optional Clause"),
               "Days_2": st.sidebar.text_input("Paid leaves", value="paid leaves"),
               "Days_3": st.sidebar.text_input("Sick leaves", value="sick leaves"),
               #"Duration": st.sidebar.text_input("", value="Duration", placeholder="Duration"),
               "week_or_month": st.sidebar.selectbox("Select:", ("Week", "Month")),
               "Name_of_State_or_District": st.sidebar.text_input("State/District", value="State/District"),
               "Option_to_add_more_clauses": st.sidebar.text_input("Optional Clauses", value="Optional Clauses"),
               "dd_mm_yy_1": st.sidebar.date_input("Date of sigining the agreement"),
               "Employer_Representative_Position": st.sidebar.text_input("Employer Representative Position", value="Employer Representative Position"),
               #"Employer_Representative_Signature": st.sidebar.text_input("", value="Employer Representative Signature", placeholder="Employer Representative Signature"),
               "Witness_1_Name": st.sidebar.text_input("Witness Name", value="Witness Name")
               #"Witness_1_Signature": st.sidebar.text_input("", value="Witness Signature ", placeholder="Witness Signature")
               }

    doc.render(context)
    doc1.render(context)
    doc.save(path2+"/Employment Contract GeneratedR.docx")
    doc1.save(path2+"/Employment Contract Generated.docx")
    convert_to_pdf(path2+"/Employment Contract GeneratedR.docx", path2+'/')
    f1 = path2+'/Employment Contract GeneratedR.pdf'

    if st.button('Done editing'):
        triggerfunction(path2+"/Employment Contract Generated.docx","Employment Contract Generated.pdf" )

    displayPDF(f1)


def FoundersAgreement(path1, path2):
    st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Consolas'; color: #FFFFFF; text-align: center} 
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">FOUNDERS AGREEMENT</p>',
                unsafe_allow_html=True)

    doc = DocxTemplate(path1+"/Founders AgreementR.docx")
    doc1 = DocxTemplate(path1+"/Founders Agreement.docx")

    context = {"date": st.sidebar.date_input("Date:"),
               "Name_of_the_company": st.sidebar.text_input("Company Name:", value="Company Name"),
               "Insert_Location": st.sidebar.text_input("Registered Office Location", value="Enter Address"),

               "Name1": st.sidebar.text_input("Name of Founder-1: ", value="Name of the Founder"),
               "Father_name_of_founder_1": st.sidebar.text_input("Father Name of the founder-1", value="Father Name"),
               "Location1": st.sidebar.text_input("Address of founder-1:", value="Address"),
               "CoFounder_or_Founder_1": st.sidebar.selectbox("Founder-1 reffered to as:", ("Co-Founder", "Founder-1")),
               "Name2": st.sidebar.text_input("Name of Founder-2:", value="Name of the Founder"),
               "Father_name_of_founder_2": st.sidebar.text_input("Father Name of the founder-2", value="Father Name"),
               "Location2": st.sidebar.text_input("Address of founder-2:", value="Address"),
               "CoFounder_or_Founder_2": st.sidebar.selectbox("Founder-2 reffered to as:", ("Co-Founder", "Founder-2")),
               "Description_of_business": st.sidebar.text_input("Description of Business: ", value="Business Description"),
               "Name_of_the_person_1": st.sidebar.text_input("Name of CEO & Director:", value="Name of CEO & Director"),
               "Responsibilities_of_CEO": st.sidebar.text_input("Responsibilites of CEO", value="Enter responsibilites seperated by ,"),

               "Name_of_the_person_2": st.sidebar.text_input("Name of COO & Director:", value="Name of COO & Director"),
               "Responsibilities_of_COO": st.sidebar.text_input("Responsibilites of COO", value="Enter responsibilites seperated by ,"),
               "Name_of_the_person_3": st.sidebar.text_input("Name of CMO & Director:", value="Name of CMO & Director"),
               "Responsibilities_of_CMO": st.sidebar.text_input("Responsibilites of CMO", value="Enter responsibilites seperated by ,"),
               "Chairman_and_board_of_directors_and_etc": st.sidebar.text_input("Enter the name of Board of Directors:", value="Enter name like Jhon, Henry..etc"),
               "Percentage_of_share ": st.sidebar.text_input("% of share held by each founder:", value="Enter percentage (0-100)"),
               "Founders_or_CoFounders_insert_his_or_her name_1": st.sidebar.text_input("Bank accounts on company name operated by:", value="Names of the persons seperated by comma(,)"),
               "Founders_or_CoFounders_insert_his_or_her name_2": st.sidebar.text_input("Persons whose signature will be valid:", value="Names of the persons seperated by comma(,)"),
               "Amount_of_Rupess": st.sidebar.text_input("Purchase/ Transactions above: ", value="Enter amount in Words"),
               "as_per_valuation_done_by_a_third_party_Valuation_firm": st.sidebar.text_input("Notice written with price as per: ", value="Make it empty if not applicable"),
               "Insert_the_amounts_of_days_1": st.sidebar.text_input("Accept/ Reject the offer within: ", value="Enter the number of days as N days"),
               "Insert_the_amounts_of_days_2": st.sidebar.text_input("If accepted complete transfer within: ", value="Enter the number of days as N days"),
               "Insert_days": st.sidebar.text_input("For Voluntary Termination, Notice should be sent within: ", value="Enter the number of days as N days"),
               "insert_percentage": st.sidebar.text_input("___ % More than approved budget ", value="enter % value b/w (0-100)"),
               "Insert_Rs_in_words": st.sidebar.text_input("Amount approved for capital expenditure: ", value="Enter amount in Words"),
               "Insert_position_and_his_or_her_name": st.sidebar.text_input("Invariance in Budget is aprroved by ", value="Enter the name and designation of the person"),
               "Insert_amount_In_words": st.sidebar.text_input("Indebtedness in excess of: ", value="Enter amount in Words"),

               }
    doc.render(context)
    doc1.render(context)
    doc.save(path2+"/Founders Agreement GeneratedR.docx")
    doc1.save(path2+"/Founders Agreement Generated.docx")
    convert_to_pdf(path2+"/Founders Agreement GeneratedR.docx", path2+'/')
    f1 = path2+'/Founders Agreement GeneratedR.pdf'

    if st.button('Done editing'):
        triggerfunction(path2+"/Founders Agreement Generated.docx","Founders Agreement Generated.pdf")

    displayPDF(f1)


def AgencyAgreement(path1, path2):
    st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Consolas'; color: #FFFFFF; text-align: center} 
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">AGENCY AGREEMENT</p>', unsafe_allow_html=True)

    doc = DocxTemplate(path1 + "/Agency AgreementR.docx")
    doc1 = DocxTemplate(path1 + "/Agency Agreement.docx")

    context = {"Place": st.sidebar.text_input("Place:", value="Place"),
               "dd_mm_yy": st.sidebar.date_input("Date:"),
               "Principal": st.sidebar.text_input("Principal Name:", value="Principal"),
               "Principal_Address": st.sidebar.text_input("Principal Address", value="Principal Address"),
               "P_Sole_Proprietor_or_Partner_or_Duly_Authorized_Member_Of_Staff_or_NA": st.sidebar.selectbox("Principle Represented By",
                                                                                                             ("Sole Proprietor", "Partner", "Duly Authorized Member of Staff", "NA")),
               "P_Mr_or_Ms": st.sidebar.selectbox("Title", ("Mr.", "Ms.")),
               "Principal_Representative": st.sidebar.text_input("Principal Representative:", value="Principal Representative"),
               "Agent": st.sidebar.text_input("Agent Name:", value="Agent"),
               "Agent_Address": st.sidebar.text_input("Agent Address", value="Agent Address"),
               "A_Sole_Proprietor_or_Partner_or_Duly_Authorized_Member_Of_Staff_or_NA": st.sidebar.selectbox("Agent Represented By",
                                                                                                             ("Sole Proprietor", "Partner", "Duly Authorized Member of Staff", "NA")),
               "A_Mr_or_Ms": st.sidebar.selectbox("Title", ("Mr.", "Ms."), key=1),
               "Agent_Representative": st.sidebar.text_input("Agent Representative:", value="Agent Representative"),
               "Purpose_of_Appointment": st.sidebar.text_input("Purpose of Appointment:", value="Purpose of Appointment"),
               "Will_or_Will_Not": st.sidebar.selectbox("Will_or_Will_Not:", ("will", "will not")),
               "Allowed_or_Not_allowed": st.sidebar.selectbox("Allowed_or_Not_allowed:", ("allowed", "not allowed")),
               "Responsibility_1": st.sidebar.text_input("Responsibilities of the Agent:", value="Agent Responsibilities"),
               "Authorized_Area_1": st.sidebar.text_input("Authorized areas for the Agent:", value="Authorized area for the Agent"),
               "minimum_valuation_of_stock_owned": st.sidebar.text_input("Minimum Stock Value:", value="Minimum Stock Value"),
               "Duration": st.sidebar.text_input("Duration of the Agent:", value="Agent Duration"),
               "A_Duration_of_prior_notice": st.sidebar.text_input("Agent Termination Notice:", value="Agent Termination Notice"),
               "A_week_or_month": st.sidebar.selectbox("Agent Termination within:", ("A Week", "A Month")),
               "number_of_days_to_deliver_unsold_stock_after_termination": st.sidebar.text_input("Days to deliver Unsold Stock (in numbers): ", value="Days to deliver Unsold Stock"),
               "Name_of_State_or_District": st.sidebar.text_input("Name of State/District:", value="Name of State/District"),
               "Option_to_add_more_clauses": st.sidebar.text_input("Optional Clauses:", value="Place for Optional Clauses"),
               "Principal_Representative_Position": st.sidebar.text_input("Principal Representative Position", value="Principal Representative Position"),
               #"Principal_Representative_Signature": st.sidebar.text_input("Principal Representative Signature", value = "Principal Representative Signature"),
               "Agent_Representative_Position": st.sidebar.text_input("Agent Representative Position", value="Agent Representative Position"),
               "Witness_1_Name": st.sidebar.text_input("Witness Name 1:", value="Witness Name 1"),
               #"Witness_1_Signature": st.sidebar.text_input("Witness 1 Signature:", value = "Witness Signature 1"),
               "Witness_2_Name": st.sidebar.text_input("Witness Name 2:", value="Witness Name 2")
               #"Witness_2_Signature": st.sidebar.text_input("Witness 2 Signature:", value = "Witness Signature 2")
               }
    doc.render(context)
    doc1.render(context)
    doc.save(path2+"/Agency Agreement GeneratedR.docx")
    doc1.save(path2+"/Agency Agreement Generated.docx")
    convert_to_pdf(path2+"/Agency Agreement GeneratedR.docx", path2+'/')
    f1 = path2+"/Agency Agreement GeneratedR.pdf"

    if st.button('Done editing'):
        triggerfunction(path2+"/Agency Agreement Generated.docx","Agency Agreement Generated.pdf")

    displayPDF(f1)


def PromissoryNote(path1, path2):
    st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Consolas'; color: #FFFFFF; text-align: center} 
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">PROMISSORY NOTE</p>', unsafe_allow_html=True)

    doc = DocxTemplate(path1+"/Promissory NoteR.docx")
    doc1 = DocxTemplate(path1+"/Promissory Note.docx")
    context = {"Place": st.sidebar.text_input("Place:", value="Place"),
               "dd_mm_yy": st.sidebar.date_input("Agreement made Date:"),
               "Name_of_Lender": st.sidebar.text_input("Lender Name:", value="Lender Name"),
               "son_or_daughter_or_wife_of_Lender": st.sidebar.selectbox("Relation with lender", ("Son", "Daughter", "Wife")),
               "Name_of_relative_Lender": st.sidebar.text_input("Relative Name:", value="Relative Name"),
               "Age_of_Lender": st.sidebar.text_input("Lender Age:", value="Lender Age"),
               "Address_of_Lender": st.sidebar.text_input("Lender Address:", value="Lender Address"),
               "Name_of_Borrower": st.sidebar.text_input("Borrower Name:", value="Borrower Name"),
               "son_or_daughter_or_wife_of_Borrower": st.sidebar.selectbox("Relation with borrower", ("Son", "Daughter", "Wife")),
               "Name_of_relative_Borrower": st.sidebar.text_input("Borrower Relative Name:", value="Borrower Relative Name"),
               "Age_of_Borrower": st.sidebar.text_input("Borrower Age:", value="Borrower Age"),
               "Address_of_Borrower": st.sidebar.text_input("Borrower Address:", value="Borrower Address"),
               "Sum_of_money_lent": st.sidebar.text_input("Amount Lent:", value="Amount Lent"),
               "percentage_of_interest": st.sidebar.text_input("Rate of Interest:", value="Rate of Interest"),
               "date_of_payment": st.sidebar.date_input("Payable After:"),
               "date_of_starting_of_agreement": st.sidebar.date_input("Start Date:"),
               "monthly_or_annual": st.sidebar.selectbox("Payment Interval", ("Weekly", "Monthly")),
               "Grace_period_Days": st.sidebar.text_input("Grace Period (Days):", value="Grace Period (Days)"),
               "Late_fee": st.sidebar.text_input("Late Fees:", value="Late Fees"),
               "Asset_Security_provided_by_Borrower": st.sidebar.text_input("Asset Security:", value="Asset Security"),
               "Amount_of_days_after_the_first_duration_of_non_repayment": st.sidebar.text_input("Lender Duration:", value="Lender Duration"),
               "Amount_of_days_after_the_second_duration_of_non_repayment": st.sidebar.text_input("Lender Owning Duration:", value="Lender Owning Duration"),
               "Name_of_State_or_District": st.sidebar.text_input("Judicial:", value="Judicial"),
               "Option_to_add_more_clauses": st.sidebar.text_input("Optional Clause:", value="Place for Optional Clause"),
               "dd_mm_yyyy": st.sidebar.date_input("Date:"),
               "Witness_1_Name": st.sidebar.text_input("Witness 1 Name:", value="Witness 1 Name")}
    doc.render(context)
    doc1.render(context)
    doc.save(path2+"/PromissoryNote_generatedR.docx")
    doc1.save(path2+"/PromissoryNote_generated.docx")
    convert_to_pdf(path2+"/PromissoryNote_generatedR.docx", path2+'/')
    f1 = path2+'/PromissoryNote_generatedR.pdf'

    if st.button('Done editing'):
        triggerfunction(path2+"/PromissoryNote_generated.docx","PromissoryNote_generated.pdf")

    displayPDF(f1)


def PropertySaleAgreement(path1, path2):

    st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Consolas'; color: #FFFFFF; text-align: center} 
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">PROPERTY SALE AGREEMENT</p>',
                unsafe_allow_html=True)

    doc = DocxTemplate(path1+"/Sale of Property AgreementR.docx")
    doc1 = DocxTemplate(path1+"/Sale of Property Agreement.docx")
    context = {"Place": st.sidebar.text_input("Place:", value="Place"),
               "dd_mm_yy": st.sidebar.date_input("Date:"),
               "Name_of_Seller": st.sidebar.text_input("Seller Name:", value="Seller Name"),
               "son_or_daughter_or_wife_of_Seller": st.sidebar.selectbox("Relation with seller", ("Son", "Daughter", "Wife")),
               "Name_of_relative_Seller": st.sidebar.text_input("Relative Name:", value="Relative Name"),
               "Age_of_Seller": st.sidebar.text_input("Seller Age:", value="Seller Age"),
               "Address_of_Seller": st.sidebar.text_input("Seller Address:", value="Seller Address"),
               "Name_of_Buyer": st.sidebar.text_input("Buyer Name:", value="Buyer Name"),
               "son_or_daughter_or_wife_of_Buyer": st.sidebar.selectbox("Relation with buyer", ("Son", "Daughter", "Wife")),
               "Name_of_relative_Buyer": st.sidebar.text_input("Buyer Relative Name:", value="Buyer Relative Name"),
               "Age_of_Buyer": st.sidebar.text_input("Buyer Age:", value="Buyer Age"),
               "Address_of_Buyer": st.sidebar.text_input("Buyer Address:", value="Buyer Address"),
               "Purchase_Fee": st.sidebar.text_input("Purchase Fees:", value="Purchase Fees"),
               "Basic_details_of_the_property": st.sidebar.text_input("Property Details:", value="Property Details"),
               "a_flat_fee_or_in_installements": st.sidebar.selectbox("Payment Method", ("Down/Flat Payment", "Installments")),
               "Installments": st.sidebar.text_input("Installment Amount:", value="Installment Amount"),
               "Number_of_Installments": st.sidebar.text_input("Number of Installments:", value="Number of Installments"),
               "annually_or_monthly_or_weekly": st.sidebar.selectbox("Payment Interval", ("Weekly", "Monthly", "Annually")),
               "Last_date_of_payment": st.sidebar.date_input("Last Date of Payment:"),
               "Number_of_days_to_handle_titular_deeds": st.sidebar.text_input("Number of days to handle Titular Deeds:", value="Number of days to handle Titular Deeds"),
               "Asset_Security_provided_by_Borrower": st.sidebar.text_input("Asset Security:", value="Asset Security"),
               "Number_of_days_to_refund_money_in_case_of_inability_to_transfer_titular_deeds": st.sidebar.text_input("Number of Days to refund Purchase Fees:", value="Number of Days to refund Purchase Fees"),
               "Applicable_Interest_rate_in_case_of_non_payment_of_refund": st.sidebar.text_input("Interest Rate on refund of Purchase Fees:", value="Interest Rate on refund of Purchase Fees"),
               "date_of_execution_of_absolute_sale_deed": st.sidebar.date_input("Date of Execution of Sale Deed:"),
               "Name_of_State_or_District": st.sidebar.text_input("Judicial:", value="Judicial"),
               "Type_of_Property": st.sidebar.text_input("Property Type:", value="Property Type"),
               "State": st.sidebar.text_input("State:", value="State"),
               "City": st.sidebar.text_input("City:", value="City"),
               "District": st.sidebar.text_input("District:", value="District"),
               "Municipal_No_or_Ward_No_or_Plot_No_or_Khasra_No": st.sidebar.text_input("Municipal No./Ward No./Plot No./Khasra No.:", value="Municipal No./Ward No./Plot No./Khasra No."),
               "Street_No": st.sidebar.text_input("Street No.:", value="Street No."),
               "Sub_District_or_Tehsil_or_Mandal": st.sidebar.text_input("Sub District/Tehsil/Mandal:", value="Sub District/Tehsil/Mandal"),
               "Police_Station": st.sidebar.text_input("Police Station:", value="Police Station"),
               "Total_Square_Footage_Number": st.sidebar.text_input("Total Square Footage Number:", value="Total Square Footage Number"),
               "Other_Measurements": st.sidebar.text_input("Other Measurements:", value="Other Measurements"),
               "Fixtures_and_Fittings_No1": st.sidebar.text_input("Fixtures and Fittings No.1:", value="Fixtures and Fittings No.1"),
               "dd_mm_yyyy": st.sidebar.date_input("Date of Signing:"),
               "Seller_Address": st.sidebar.text_input("Seller address:", value="Seller Address"),
               "Buyer_Address": st.sidebar.text_input("Buyer address:", value="Buyer Address"),
               "Witness_1_Name": st.sidebar.text_input("Witness 1 Name:", value="Witness 1 Name")}
    doc.render(context)
    doc1.render(context)
    doc.save(path2+"/Property sale agreement generatedR.docx")
    doc1.save(path2+"/Property sale agreement generated.docx")
    convert_to_pdf(path2+"/Property sale agreement generatedR.docx", path2+'/')
    f1 = path2+'/Property sale agreement generatedR.pdf'

    if st.button('Done editing'):
        triggerfunction(path2+"/Property sale agreement generated.docx","Property sale agreement generatedR.pdf")

    displayPDF(f1)


def GeneralServiceAgreement(path1, path2):
    st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Consolas'; color: #FFFFFF; text-align: center} 
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">GENERAL SERVICE AGREEMENT</p>',
                unsafe_allow_html=True)

    doc = DocxTemplate(path1+"/General Service AgreementR.docx")
    doc1 = DocxTemplate(path1+"/General Service Agreement.docx")
    context = {"Place": st.sidebar.text_input("Place:", value="Place"),
               "dd_mm_yy": st.sidebar.date_input("Date:"),
               "Client1": st.sidebar.text_input("Client Name:", value="Client"),
               "Address_cl": st.sidebar.text_input("Client Address:", value="Client Address"),
               "Sole_Proprietor_or_Partner_or_Duly_Authorized_Member_Of_Staff_or_NA_cl": st.sidebar.selectbox("Client Represented By",
                                                                                                              ("Sole Proprietor", "Partner", "Duly Authorized Member of Staff")),
               "Mr_or_Ms_cl": st.sidebar.selectbox("Title of Client Representor:", ("Mr.", "Mrs.")),
               "Client_Representative": st.sidebar.text_input("Client Representative", value="Client Representative"),
               "Contractor1": st.sidebar.text_input("Contractor Name:", value="Contractor Name"),
               "Address_co": st.sidebar.text_input("Contractor Address:", value="Contractor Address"),
               "Sole_Proprietor_or_Partner_or_Duly_Authorized_Member_Of_Staff_or_NA_co": st.sidebar.selectbox("Contractor Represented By",
                                                                                                              ("Sole Proprietor", "Partner", "Duly Authorized Member of Staff")),
               "Mr_or_Ms_co": st.sidebar.selectbox("Title of Contractor represntative:", ("Mr.", "Mrs.")),
               "Contractor_Representative": st.sidebar.text_input("", value="Contractor Representative"),
               "Goods": st.sidebar.text_input("Name of the Goods to be supplied", value="Name of the Goods to be supplied"),

               "Purpose": st.sidebar.text_input("Purpose", value="Purpose"),
               "From_date": st.sidebar.date_input("Effective from date"),

               "To_Date": st.sidebar.date_input("Effective till date"),
               "Duration": st.sidebar.text_input("Duration", value="Duration"),

               "Service_1": st.sidebar.text_input("Services provided by Contractor to Client", value="Services provided by Contractor to Client"),
               "Add_any_Additional_Services": st.sidebar.text_input("Add if there are any additional services else leave it empty"),
               "A_flat_fee_or_In_installments_or_Other_Consideration": st.sidebar.selectbox("Payment Method", ("Down/Flat Payment", "Installments", "Other Considerations")),
               "AmountF": st.sidebar.text_input("In case of Flat Fee: (Enter Amount)", value="Flat Fee Amount"),
               "Amount_of_Installments": st.sidebar.text_input("Incase of Installments: (Enter Amount)", value="Installments Amount"),
               "AmountI": st.sidebar.text_input("First Installment Amount: ", value="Enter Amount"),
               "AmountS": st.sidebar.text_input("Second Installment Amount: ", value="Enter Amount"),
               "Additional_Installments": st.sidebar.text_input("Additional Installmetns(if any) or leave it empty: "),
               "Consideration": st.sidebar.text_input("Consideration: "),
               "Before_or_After_or_During_or_In_Installments": st.sidebar.selectbox("sevice by contractor must be given: ", ("Before", "After", "During / In Installments")),
               "method_of_payment": st.sidebar.selectbox("Method of Payment: ", ("Debit Card", "Credit Card", "Cash")),

               "Amount_cl": st.sidebar.text_input("Amount client need to pay", value="Amount Client need to pay"),
               "Client_or_Contractor_or_Both_Parties": st.sidebar.selectbox("Material developed /produced will be the property of: ", ("Client", "Contractor", "Both Parties")),
               "Amount_Re": st.sidebar.text_input("Client reimburse to extent of: ", value="Amount Reimbursed"),
               "Number_of_Days": st.sidebar.text_input("Claims must be settled within", value="N days"),
               "Name_of_State_or_District": st.sidebar.text_input("State/District", value="State/District"),
               "Number": st.sidebar.text_input("Duration N days: ", value="Duration (in numbers)"),
               "Court_of_Law_or_Arbitral_tribunal": st.sidebar.selectbox("May seek compensation in appropriate: ", ("Court of Law", "Arbitral Tribunal")),
               "Additional Clauses": st.sidebar.text_input("Add Additional Clause if any / Leave it empty"),

               "dd_mm_yy_1": st.sidebar.date_input("Date of sigining the agreement"),


               "Client": st.sidebar.text_input("", value="Client Name", placeholder="Client Name"),
               "Client_Representative_Name": st.sidebar.text_input("Client Representative Name", value="Client Representative Name"),
               "Client_Representative_Position": st.sidebar.text_input("Client Representative Position", value="Client Representative Position"),


               "Contractor": st.sidebar.text_input("Contractor Name", value="Contractor Name"),
               "Contractor_Representative_Name": st.sidebar.text_input("Contractor Representative Name", value="Contractor Representative Name"),
               "Contractor_Representative_Position": st.sidebar.text_input("Contractor Representative Position", value="Contractor Representative Position"),
               "Contractor_Representative_Signature": st.sidebar.text_input("Contractor Representative Signature", value="Contractor Representative Signature"),
               "Witness_1_Name": st.sidebar.text_input("Witness Name", value="Witness Name"),


               "Witness_2_Name": st.sidebar.text_input("Witness Name 2:", value="Witness Name 2 or NA")

               }
    doc.render(context)
    doc1.render(context)
    doc.save(path2+"/General Service agreement generatedR.docx")
    doc1.save(path2+"/General Service agreement generated.docx")
    convert_to_pdf(path2+"/General Service agreement generatedR.docx", path2+'/')
    f1 = path2+'/General Service agreement generatedR.pdf'

    if st.button('Done editing'):
        triggerfunction(path2+"/General Service agreement generated.docx","General Service agreement generated.pdf")
    displayPDF(f1)


def SaleofGoodsAgreement(path1, path2):
    st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Consolas'; color: #FFFFFF; text-align: center} 
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">SALE OF GOODS AGREEMENT</p>',
                unsafe_allow_html=True)

    doc = DocxTemplate(path1+"/Sale of Goods AgreementR.docx")
    doc1 = DocxTemplate(path1+"/Sale of Goods Agreement.docx")
    context = {"Place": st.sidebar.text_input("Place:", value="Place"),
               "dd_or_mm_or_yy": st.sidebar.date_input("Date:"),
               "Seller": st.sidebar.text_input("Seller Name:", value="Seller Name"),
               "Address_s": st.sidebar.text_input("Seller Address:", value="Seller Address"),
               "Sole_Proprietor_or_Partner_or_Duly_Authorized_Member_Of_Staff_or_NA_s": st.sidebar.selectbox("Seller Represented By",
                                                                                                             ("Sole Proprietor", "Partner", "Duly Authorized Member of Staff")),
               "Mr_or_Ms_S": st.sidebar.selectbox("Title of seller represntative:", ("Mr.", "Mrs.", "Miss")),
               "Seller_Representative": st.sidebar.text_input("Name of Seller Representative", value="Seller Representative"),
               "Buyer": st.sidebar.text_input("Buyer name:", value="Buyer Name"),
               "Address_b": st.sidebar.text_input("Buyer Address:", value="Buyer Address"),
               "Sole_Proprietor_or_Partner_or_Duly_Authorized_Member_Of_Staff_or_NA_b": st.sidebar.selectbox("Buyer Represented By",
                                                                                                             ("Sole Proprietor", "Partner", "Duly Authorized Member of Staff")),
               "Mr_or_Ms_b": st.sidebar.selectbox("Title of Buyer Representative:", ("Mr.", "Mrs.", "Miss")),
               "Buyer_Representative": st.sidebar.text_input("Name of Buyer Represntative", value="Buyer Representative"),
               "Goods": st.sidebar.text_input("Name of the Goods to be supplied", value="Name of the Goods to be supplied"),
               "Purpose": st.sidebar.text_input("Purpose", value="Purpose"),
               "From_date": st.sidebar.date_input("Effective from date"),

               "To_Date": st.sidebar.date_input("Effective till date"),
               "Duration": st.sidebar.text_input("Duration", value="Duration"),
               "Cost_or_unit": st.sidebar.text_input("Supplied at Cost per unit", value="Supplied at Cost per uni"),
               "receiving_of_goods_or_sale_of_goods": st.sidebar.selectbox("Payment must be done after: ", ("Recieving of Goods", "Sale of Goods")),
               "method_of_payment": st.sidebar.selectbox("Method of Payment: ", ("Debit Card", "Credit Card", "Cash")),
               "Seller_or_Buyer_or_Both": st.sidebar.selectbox("Transportation Costs", ("Seller", "Buyer", "Both")),
               "Number_of_days": st.sidebar.text_input("Claims must be settled within", value="Claims must be settled within"),
               "Buyer_or_Seller_or_Both": st.sidebar.selectbox("Responsibility", ("Seller", "Buyer", "Both")),
               "Number_of_days_t": st.sidebar.text_input("termination Claims must be settled within", value="Claims must be settled within"),
               "Name_of_State_or_District": st.sidebar.text_input("Name of State/District:", value="Name of State/District"),
               "Number": st.sidebar.text_input("", value="Duration", placeholder="Duration (in numbers)"),
               "Court_of_Law_or_Arbitral_tribunal": st.sidebar.selectbox("May seek compensation in appropriate: ", ("Court of Law", "Arbitral Tribunal")),
               "dd_or_mm_or_yy_1 ": st.sidebar.date_input("Date of sigining the agreement"),

               "Seller1": st.sidebar.text_input("Name of the Seller", value="Seller Name"),
               "Seller_Representative_Name": st.sidebar.text_input("Seller Representative Name", value="Seller Representative Name"),
               "Seller_Representative_Position": st.sidebar.text_input("Seller Representative Position", value="Seller Representative Position"),


               "Buyer1": st.sidebar.text_input("Buyer Name", value="Buyer Name"),
               "Buyer_Representative_Name": st.sidebar.text_input("Buyer Representative Name", value="Buyer Representative Name"),
               "Buyer_Representative_Position": st.sidebar.text_input("Buyer Representative Position", value="Buyer Representative Position"),

               "Witness_1_Name": st.sidebar.text_input("Witness-1 Name", value="Witness Name"),

               "Witness_2_Name": st.sidebar.text_input("Witness Name 2:", value="Witness Name 2 or NA"),

               }
    doc.render(context)
    doc1.render(context)
    doc.save(path2+"/Sale of Goods generated AgreementR.docx")
    doc1.save(path2+"/Sale of Goods generated Agreement.docx")
    convert_to_pdf(path2+"/Sale of Goods generated AgreementR.docx", path2+'/')
    f1 = path2+'/Sale of Goods generated AgreementR.pdf'

    if st.button('Done editing'):
        triggerfunction(path2+"/Sale of Goods generated Agreement.docx","Sale of Goods generated Agreement.pdf")
    displayPDF(f1)


def Home(path1, path2):
    # CSS - Points INSTRUCTIONS TO FILL THE AGREEMENT
    st.markdown(""" <style> .font {
        font-size:17px ; font-family: 'Consolas'; color: #FFFFFF; text-align: justify} 
        </style> """, unsafe_allow_html=True)

    # CSS - Heading INSTRUCTIONS TO FILL THE AGREEMENT
    st.markdown(""" <style> .font1 {
        font-size:26px ; font-family: 'Consolas'; color: #FFFFFF; text-align: center}
        /style> """, unsafe_allow_html=True)

    st.markdown(""" <style> .font2 {
        font-size:18px ; font-family: 'Consolas'; color: #FF0000; text-align: justify} 
        </style> """, unsafe_allow_html=True)

    # Disclaimer
    st.markdown(""" <style> .font3 {
        font-size:18px ; font-family: 'Consolas'; color: #FF0000; text-align: center} 
        </style> """, unsafe_allow_html=True)

    # Disclaimer Body
    st.markdown(""" <style> .font4 {
        font-size:19px ; font-family: 'Consolas'; color: #FF8C00; text-align: justify} 
        </style> """, unsafe_allow_html=True)

    instruct = st.container()

    with instruct:
        #st.markdown('<p class="font4">Welcome to Law Diktat Agreement builder. We are providing various contracts which the user can fill and use it for their own legal purpose.</p>', unsafe_allow_html=True)
        st.markdown('<p class="font1">INSTRUCTIONS</p>',
                    unsafe_allow_html=True)
        st.markdown('<p class="font">1. After selecting the respective agreement, you will be getting the text boxes to fill in the details for the contract.</p>', unsafe_allow_html=True)
        st.markdown(
            '<p class="font">2. You must read the agreement and fill it in accordingly.</p>', unsafe_allow_html=True)
        st.markdown('<p class="font">3. Details entered in the text boxes will be populated in the agreement preview right after pressing the "Enter" or "Tab" key.</p>', unsafe_allow_html=True)
        st.markdown(
            '<p class="font">4. Entered text will appear in red-colored texts in the preview box on your right.</p>', unsafe_allow_html=True)
        st.markdown(
            '<p class="font">5. The input fields are Case-Sensetive.</p>', unsafe_allow_html=True)
        st.markdown(
            '<p class="font">6. You may change the details if required.</p>', unsafe_allow_html=True)
        st.markdown('<p class="font">7. After filling all the fields, you will be able to download the agreement in pdf format.</p>', unsafe_allow_html=True)

        st.sidebar.markdown(
            '<p class="font3"><b><u>DISCLAIMER</u></b></p>', unsafe_allow_html=True)
        #st.sidebar.markdown('<p class="font2"><b>The data you input will be processed by us for our internal usage. We treat your personal information as confidential and will handle it with the utmost care in accordance with the data protection legislation.</b></p>', unsafe_allow_html=True)
        st.sidebar.markdown('<p class="font2"><b>THE DATA YOU INPUT WILL BE PROCESSED BY US FOR OUR INTERNAL USAGE. WE TREAT YOUR PERSONAL INFORMATION AS CONFIDENTIAL AND WILL HANDLE IT WITH THE UTMOST CASE IN ACCORDANCE WITH THE DATA PROTECTION LEGISLATION.</b></p>', unsafe_allow_html=True)


agreements = ['Home', 'Distributor Supplier Agreement', 'Rental Agreement', 'Non Disclosure Agreement', 'Independent Contractor Agreement', 'Employment Contract',
              'Founders Agreement', 'Agency Agreement', 'Promissory Note', 'Property Sale Agreement', 'General Service Agreement', 'Sale of Goods Agreement']
agreement_type = st.sidebar.selectbox(
    "SELECT THE AGREEMENT", agreements)
agreement = agreement_type.replace(" ", "")

# pythoncom.CoInitialize()
eval(agreement + "(path1, path2)")
# pythoncom.CoInitialize()
