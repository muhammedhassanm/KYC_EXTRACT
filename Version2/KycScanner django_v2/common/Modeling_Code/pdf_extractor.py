# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 18:19:45 2019

@author: Vishnu Anilkumar
"""
import os
import urllib
from tika import parser

WORKING_DIR = os.getcwd()


def pdftype3(text):
    ''' Get data from  text content'''

    name = ''
    age = ''
    gender = ''
    date_of_policy_commencement = ''
    policy_term = ''
    premium_paying_term = ''
    premium_frequency = ''

    if text.find('This is the official illustration issued by HDFC Life Insurance Company Limited'):
        if (text.find("Name") or text.find("Age is taken as on last birthday")) != -1:
            temp = text[text.find("Name"):text.find("Age is taken as on last birthday")].split('Life 1')
            gender = temp[1].split()[-1].strip()
            age = temp[1].replace(gender, "").split()[-1].strip()
            name = temp[1].replace(gender, "").replace(age, "").strip()
        else:
            gender = None
            age = None
            name = None
        #Date of Policy Commencement:
        if (text.find("\nPolicy Term:") or text.find("Date of Policy Commencement")) != -1:
            date_of_policy_commencement = text[text.find("Date of Policy Commencement:"):text.find("\nPolicy Term:")].replace("Date of Policy Commencement:", "").strip()
        else:
            date_of_policy_commencement = text[text.find("Date of Policy Commencement:"):text.find("\nPremium Frequency:")].replace("Date of Policy Commencement:", "").strip()
        #Policy Term:
        if (text.find("\nPolicy Term:") or text.find("\nPremium Paying Term:")) != -1:
            policy_term = text[text.find("\nPolicy Term:"):text.find("\nPremium Paying Term:")].replace("Policy Term:", "").strip()
        else:
            policy_term = 'NAN'
        #Premium Paying Term:
        if (text.find("\nPremium Paying Term:") or text.find("\nPremium Frequency:")) != -1:
            premium_paying_term = text[text.find("\nPremium Paying Term:"):text.find("\nPremium Frequency:")].replace("\nPremium Paying Term:", "").strip()
        else:
            premium_paying_term = None
        #Premium Frequency:
        if (text.find("\nPremium Frequency:") or text.find("\nPREMIUM AND BENEFIT DETAILS")) != -1:
            premium_frequency = text[text.find("\nPremium Frequency:"):text.find("\nPREMIUM AND BENEFIT DETAILS")].replace("\nPremium Frequency:", "").strip()
        else:
            premium_frequency = None

#        output = {"name" : name, "age" : age, "gender": gender,
#                  "POLICY TERM" : policy_term,
#                  "PREMIUM FREQUENCY" : premium_frequency,
#                  "PREMIUM PAYING TERM" : premium_paying_term,
#                  "DATE OF POLICY COMMENCEMENT" : date_of_policy_commencement}

        output = {"name" : name, "age" : age, "gender": gender,
                  "policyTerm" : policy_term,
                  "policyCommencement" : date_of_policy_commencement}

    return output


def pdftype4(text):

    name = None
    age = None
    policy_term = None
    amount_of_installment_premium = None
    mode = None
    proposal_no = None
    name_of_product = None
    unique_id = None
    gst_rate = None
    quote_no = None
    application_no = None
#     elif text.find('Benefit Illustartion for HDFC Life Sanchay Plus'):
    if (text.find('Name of the Prospect/Policyholder:') or text.find('\nAge:')) != -1:
        name = text[text.find('Name of the Prospect/Policyholder:'):text.find('\nAge:')].replace("Name of the Prospect/Policyholder:", "").replace("\n", "").strip()
    else:
        name = None
    if (text.find('\nAge:') or text.find('\nPolicy Term:')) != -1:
        age = text[text.find('\nAge:'):text.find('\nName of Life Assured:')].replace("\nAge:", "").replace("\n", " ").strip()
    else:
        age = None
    if (text.find('\nPolicy Term:') or text.find('\nPremium Paying Term:')) != -1:
        policy_term = text[text.find('\nPolicy Term:'):text.find('\nAmount of Instalment Premium:')].replace("\nPolicy Term:", "").replace("\n", " ").strip()
    else:
        policy_term = None
    if (text.find('\nAmount of Instalment Premium:') or text.find('\nMode:')) != -1:
        amount_of_installment_premium = text[text.find('\nAmount of Instalment Premium:'):text.find('\nMode:')].replace("\nAmount of Instalment Premium:", "").replace("\n", " ").strip()
    else:
        amount_of_installment_premium = None
    if (text.find('\nMode:') or text.find('\nProposal No:')) != -1:
        mode = text[text.find('\nMode:'):text.find('\nProposal No:')].replace("\nMode:", "").replace("\n", " ").strip()
    else:
        mode = None
    if (text.find('\nProposal No:') or text.find('\nName of Product:')) != -1:
        proposal_no = text[text.find('\nProposal No:'):text.find('\nName of Product:')].replace("\nProposal No:", "").replace("\n", " ").strip()
    else:
        proposal_no = None
    if (text.find('\nName of Product:') or text.find('\nTag Line:')) != -1:
        name_of_product = text[text.find('\nName of Product:'):text.find('\nTag Line:')].replace("\nName of Product:", "").replace("\n", " ").strip()
    else:
        name_of_product = None
    if (text.find('\nUnique Identification No:') or text.find('\nGST Rate:')) != -1:
        unique_id = text[text.find('\nUnique Identification No:'):text.find('\nGST Rate:')].replace("\nUnique Identification No:", "").replace("\n", " ").strip()
    else:
        unique_id = None
    if (text.find('\nGST Rate:') or text.find('%')) != -1:
        gst_rate = text[text.find('\nGST Rate'):text.find('%')].replace("\nGST Rate", "").replace("\n", " ").strip()
    else:
        gst_rate = None
    if (text.find('\nQuote No') or text.find('Application No')) != -1:
        quote_no = text[text.find('\nQuote No'):text.find
                        ('Application No :')].replace("\nQuote No", "").replace("\n", " ").strip()
    else:
        quote_no = None
    if (text.find('Application No :') or text.find('\nBenefit Illustartion for HDFC Life Sanchay Plus')) != -1:
        application_no = text[text.find
                              ('Application No :'):text.find
                              ('\nBenefit Illustartion for HDFC Life Sanchay Plus')].replace("Application No :", "").replace("\n", " ").strip()
    else:
        application_no = None

#    output = {"name" : name,
#    "age" : age,
#    "POLICY TERM" : policy_term,
#    "AMOUNT OF INSTALLMENT PREMIUM" : amount_of_installment_premium,
#    "MODE" : mode,
#    "PROPOSAL NO" : proposal_no,
#    "NAME OF PRODUCT" : name_of_product,
#    "UNIQUE ID" : unique_id,
#    "GST RATE" : gst_rate,
#    "QUOTE NUMBER" : quote_no,
#    "APPLICATION NUMBER" : application_no}

    output = {"name" : name,
              "age" : age,
              "policyTerm" : policy_term,
              "installPremium" : amount_of_installment_premium}

    return output


def pdftype1(TEXT):

    Name = []
    Age = []
    Gender = []
    Uin1 = []
    Uin2 = []
    Sum_Assured1 = []
    Sum_Assured2 = []
    Policy_term1 = []
    Policy_term2 = []
    Premium_Payment_Term1 = []
    Premium_Payment_Term2 = []
    Premium_Frequency = []
    chosen_plan_option1 = []
    Plan_Option_Chosen2 = []
    Top_Up_Option1 = []
    Top_Up_Option2 = []
    Premium_Exclusive_Of_Taxes1 = []
    Premium_Exclusive_Of_Taxes2 = []
    Taxes1 = []
    Taxes2 = []
    Premium_Inclusive_Of_Taxes1 = []
    Premium_Inclusive_Of_Taxes2 = []

    Total_Premium_Inclusive_Of_taxes = []
    Next_Premium_Due_Date = []
    Premium_Payment_Method = []

    NAME = TEXT[TEXT.find('\nName:'): TEXT.find
                ('\nAge last Birthday:')].replace('\nName:', "").replace("\n", '').strip()
    try:
        Name.append(NAME)
    except:
        Name.append(None)

    AGE = TEXT[TEXT.find('\nAge last Birthday:'): TEXT.find
               ('\nGender')].replace('\nAge last Birthday:', "").replace("\n", '').strip()
    try:
        Age.append(AGE)
    except:
        Age.append(None)

    GENDER = TEXT[TEXT.find('\nGender:'): TEXT.find
                  ('\nYour Policy details\n')].replace('\nGender:', "").replace("\n", '').strip()
    try:
        Gender.append(GENDER)
    except:
        Gender.append(None)

    if len(Uin1) == 0 and len(Uin2) == 0:
        if TEXT[TEXT.find('\nDetails:'):TEXT.find('\nUIN:')].replace('\nDetails:', "").replace("\n", '').strip() == "HDFC Life Click 2 Protect 3D Plus":
            UIN = TEXT[TEXT.find('UIN:'): TEXT.find
                       ('Sum Assured:')].replace('UIN:', "").replace("\n", '').strip().split()
            try:
                Uin1.append(UIN[0])
            except:
                Uin1.append(None)

            try:
                Uin2.append(UIN[1])
            except:
                Uin2.append(None)

        elif TEXT[TEXT.find('\nDetails:'):TEXT.find('\nUIN:')].replace('\nDetails:', "").replace("\n", '').strip() != "HDFC Life Click 2 Protect 3D Plus":
            UIN = TEXT[TEXT.find('UIN:'): TEXT.find
                       ('Sum Assured:')].replace('UIN:', "").replace("\n", '').strip().split()
            try:
                Uin1.append(UIN[0])
            except:
                Uin1.append(None)

            try:
                Uin2.append(UIN[1])
            except:
                Uin2.append(None)

        else:
            Uin1.append(UIN[0])
            Uin2.append(None)


        if TEXT[TEXT.find('\nDetails:'):TEXT.find('\nUIN:')].replace('\nDetails:', "").replace("\n", '').strip() == "HDFC Life Click 2 Protect 3D Plus":
            SUM_ASSURED = TEXT[TEXT.find('Sum Assured:'): TEXT.find('Policy Term:')].replace('Sum Assured:', "").replace("\n", '').strip().split()

            try:
                Sum_Assured1.append(SUM_ASSURED[0])
            except:
                Sum_Assured1.append(None)
            try:
                Sum_Assured2.append(SUM_ASSURED[1])
            except:
                Sum_Assured2.append(None)
        elif TEXT[TEXT.find('\nDetails:'):TEXT.find('\nUIN:')].replace('\nDetails:', "").replace("\n", '').strip() != "HDFC Life Click 2 Protect 3D Plus":
            SUM_ASSURED = TEXT[TEXT.find('Sum Assured:'): TEXT.find('Policy Term:')].replace('Sum Assured:', "").replace("\n", '').strip().split()
            try:
                Sum_Assured1.append(SUM_ASSURED[0])
            except:
                Sum_Assured1.append(None)
            try:
                Sum_Assured2.append(SUM_ASSURED[1])
            except:
                Sum_Assured2.append(None)
        else:

            Sum_Assured1.append(SUM_ASSURED[0])
            Sum_Assured2.append(None)

        if TEXT[TEXT.find('\nDetails:'):TEXT.find('\nUIN:')].replace('\nDetails:', "").replace("\n", '').strip() == "HDFC Life Click 2 Protect 3D Plus":
            POLICY_TERM = TEXT[TEXT.find('Policy Term:'): TEXT.find
                               ('Premium Payment Term:')].replace('Policy Term:', "").replace("\n", '').strip()
            POLICY_TERM = POLICY_TERM.split("year(s)")

            try:
                Policy_term1.append(POLICY_TERM[0].strip())
            except:
                Policy_term1.append(None)

            if POLICY_TERM[1] == '':
                try:
                    Policy_term2.append(None)
                except:
                    Policy_term2.append(None)
            else:
                Policy_term2.append(POLICY_TERM[1].strip())
        elif TEXT[TEXT.find('\nDetails:'):TEXT.find('\nUIN:')].replace('\nDetails:', "").replace("\n", '').strip() != "HDFC Life Click 2 Protect 3D Plus":
            POLICY_TERM = TEXT[TEXT.find('Policy Term:'): TEXT.find
                               ('Premium Payment Term:')].replace('Policy Term:', "").replace("\n", '').strip()
            POLICY_TERM = POLICY_TERM.split("year(s)")

            try:
                Policy_term1.append(POLICY_TERM[0].strip())
            except:
                Policy_term1.append(None)

            if POLICY_TERM[1] == '':

                try:
                    Policy_term2.append(None)
                except:
                    Policy_term2.append(None)
            else:
                Policy_term2.append(POLICY_TERM[1].strip())
        else:
            Policy_term1.append(POLICY_TERM[0])
            Policy_term2.append(None)

          #TODO split year(s)
          #re.split('(year(s))',  SUM_ASSURED)

        if TEXT[TEXT.find('\nDetails:'):TEXT.find('\nUIN:')].replace('\nDetails:', "").replace("\n", '').strip() == "HDFC Life Click 2 Protect 3D Plus":
            PREMIUM_PAYMENT_TERM = TEXT[TEXT.find('Premium Payment Term:'): TEXT.find
                                        ('Premium Frequency:')].replace('Premium Payment Term:', "").replace("\n", '').strip()

            PREMIUM_PAYMENT_TERM = PREMIUM_PAYMENT_TERM.split("year(s)")
            try:
                Premium_Payment_Term1.append(PREMIUM_PAYMENT_TERM[0].strip())
            except:
                Premium_Payment_Term1.append(None)
            if PREMIUM_PAYMENT_TERM[1] == '':
                try:
                    Premium_Payment_Term2.append(None)
                except:
                    Premium_Payment_Term2.append(None)
            else:
                Premium_Payment_Term2.append(PREMIUM_PAYMENT_TERM[1].strip())
        elif TEXT[TEXT.find('\nDetails:'):TEXT.find('\nUIN:')].replace('\nDetails:', "").replace("\n", '').strip() != "HDFC Life Click 2 Protect 3D Plus":
            PREMIUM_PAYMENT_TERM = TEXT[TEXT.find('Premium Payment Term:'): TEXT.find
                                        ('Premium Frequency:')].replace('Premium Payment Term:', "").replace("\n", '').strip()

            PREMIUM_PAYMENT_TERM = PREMIUM_PAYMENT_TERM.split("year(s)")
            try:
                Premium_Payment_Term1.append(PREMIUM_PAYMENT_TERM[0].strip())
            except:
                Premium_Payment_Term1.append(None)
            if PREMIUM_PAYMENT_TERM[1] == '':
                try:
                    Premium_Payment_Term2.append(None)
                except:
                    Premium_Payment_Term2.append(None)
            else:
                Premium_Payment_Term2.append(PREMIUM_PAYMENT_TERM[1].strip())
        else:
            Premium_Payment_Term1.append(PREMIUM_PAYMENT_TERM[0])
            Premium_Payment_Term2.append(None)

    else:
        if TEXT[TEXT.find('\nDetails:'):TEXT.find('\nUIN:')].replace('\nDetails:', "").replace("\n", '').strip() != "HDFC Life Click 2 Protect 3D Plus":

            UIN = TEXT[TEXT.find('UIN:'): TEXT.find
                       ('Sum Assured:')].replace('UIN:', "").replace("\n", '').strip().split()
            try:
                Uin1.append(UIN[0])
            except:
                Uin1.append(None)

            try:
                Uin2.append(UIN[1])
            except:
                Uin2.append(None)

        else:
            Uin1.append(UIN[0])
            Uin2.append(None)

        if TEXT[TEXT.find('\nDetails:'):TEXT.find('\nUIN:')].replace('\nDetails:', "").replace("\n", '').strip() != "HDFC Life Click 2 Protect 3D Plus":
            SUM_ASSURED = TEXT[TEXT.find('Sum Assured:'): TEXT.find
                               ('Policy Term:')].replace('Sum Assured:', "").replace("\n", '').strip().split()
            try:
                Sum_Assured1.append(SUM_ASSURED[0])
            except:
                Sum_Assured1.append(None)
            try:
                Sum_Assured2.append(SUM_ASSURED[1])
            except:
                Sum_Assured2.append(None)
        else:
            Sum_Assured1.append(SUM_ASSURED[0])
            Sum_Assured2.append(None)

        if TEXT[TEXT.find('\nDetails:'):TEXT.find('\nUIN:')].replace('\nDetails:', "").replace("\n", '').strip() != "HDFC Life Click 2 Protect 3D Plus":
            POLICY_TERM = TEXT[TEXT.find('Policy Term:'): TEXT.find
                               ('Premium Payment Term:')].replace('Policy Term:', "").replace("\n", '').strip()
            POLICY_TERM = POLICY_TERM.split("year(s)")

            try:
                Policy_term1.append(POLICY_TERM[0].strip())
            except:
                Policy_term1.append(None)

            if POLICY_TERM[1] == '':
                try:
                    Policy_term2.append(None)
                except:
                    Policy_term2.append(None)
            else:
                Policy_term2.append(POLICY_TERM[1].strip())

        else:
            Policy_term1.append(POLICY_TERM[0])
            Policy_term2.append(None)

          #TODO split year(s)
          #re.split('(year(s))',  SUM_ASSURED)

        if TEXT[TEXT.find('\nDetails:'):TEXT.find('\nUIN:')].replace('\nDetails:', "").replace("\n", '').strip() != "HDFC Life Click 2 Protect 3D Plus":
            PREMIUM_PAYMENT_TERM = TEXT[TEXT.find('Premium Payment Term:'): TEXT.find
                                        ('Premium Frequency:')].replace('Premium Payment Term:', "").replace("\n", '').strip()

            PREMIUM_PAYMENT_TERM = PREMIUM_PAYMENT_TERM.split("year(s)")
            try:
                Premium_Payment_Term1.append(PREMIUM_PAYMENT_TERM[0].strip())
            except:
                Premium_Payment_Term1.append(None)
            if PREMIUM_PAYMENT_TERM[1] == '':
                try:
                    Premium_Payment_Term2.append(None)
                except:
                    Premium_Payment_Term2.append(None)
            else:
                Premium_Payment_Term2.append(PREMIUM_PAYMENT_TERM[1].strip())

        else:
            Premium_Payment_Term1.append(PREMIUM_PAYMENT_TERM[0])
            Premium_Payment_Term2.append(None)

    PREMIUM_FREQUENCY = TEXT[TEXT.find('Premium Frequency:'): TEXT.find
                             ('Plan Option Chosen:')].replace('Premium Frequency:', "").replace("\n", '').strip()
    try:
        Premium_Frequency.append(PREMIUM_FREQUENCY)
    except:
        Premium_Frequency.append(None)
    try:
        PLAN_OPTION_CHOSEN = TEXT[TEXT.find('Plan Option Chosen:'): TEXT.find('Top Up Option:')].replace('Plan Option Chosen:', "").replace("\n", '').strip()
    except:
        print("Plan Option Not Available")

    if PLAN_OPTION_CHOSEN != "Life Option" or PLAN_OPTION_CHOSEN != "Not Applicable":
        #  Plan_Option_Chosen.append(PLAN_OPTION_CHOSEN)
        print("asdf")
        TOP_UP_OPTION = TEXT[TEXT.find('Top Up Option:'): TEXT.find
                             ('Premium Exclusive of Taxes:')].replace('Top Up Option:', "").replace("\n", '').strip()
        TOP_UP_OPTION = TOP_UP_OPTION.split(" ", 1)
        try:
            Top_Up_Option1.append(TOP_UP_OPTION[0])
        except:
            Top_Up_Option1.append(None)
        try:
            Top_Up_Option2.append(TOP_UP_OPTION[1])
        except:
            Top_Up_Option2.append(None)
    else:
        Top_Up_Option1.append(TOP_UP_OPTION[0])

    if PLAN_OPTION_CHOSEN != "Life Option" or PLAN_OPTION_CHOSEN != "Not Applicable":
        #  Plan_Option_Chosen.append(PLAN_OPTION_CHOSEN)
        print("asdf")
        PREMIUM_EXCLUSIVE_OF_TAXES = (TEXT[TEXT.find('Premium Exclusive of Taxes:'): TEXT.find
                                           ('\nTaxes:')].replace('Premium Exclusive of Taxes:', "").replace("\n", '').strip()).split()
        try:
            Premium_Exclusive_Of_Taxes1.append(PREMIUM_EXCLUSIVE_OF_TAXES[0])
        except:
            Premium_Exclusive_Of_Taxes1.append(None)
        try:
            Premium_Exclusive_Of_Taxes2.append(PREMIUM_EXCLUSIVE_OF_TAXES[1])
        except:
            Premium_Exclusive_Of_Taxes2.append(None)

    else:
        Premium_Exclusive_Of_Taxes1.append(PREMIUM_EXCLUSIVE_OF_TAXES[0])



    if PLAN_OPTION_CHOSEN != "Life Option" or PLAN_OPTION_CHOSEN != "Not Applicable":

        TAXES = (TEXT[TEXT.find('\nTaxes:'): TEXT.find
                      ('Premium Inclusive of Taxes:')].replace('Taxes:', "").replace("\n", '').strip()).split()
        try:
            Taxes1.append(TAXES[0])
        except:
            Taxes1.append(None)
        try:
            Taxes2.append(TAXES[1])
        except:
            Taxes2.append(None)
    else:
        Taxes1.append(TAXES[0])

    if PLAN_OPTION_CHOSEN != "Life Option" or PLAN_OPTION_CHOSEN != "Not Applicable":

        PREMIUM_INCLUSIVE_OF_TAXES = (TEXT[TEXT.find('Premium Inclusive of Taxes:'): TEXT.find
                                           ('\nTotal Premium Inclusive of Taxes:')].replace('Premium Inclusive of Taxes:', "").replace("\n", '').strip()).split()
        try:
            Premium_Inclusive_Of_Taxes1.append(PREMIUM_INCLUSIVE_OF_TAXES[0])
        except:
            Premium_Inclusive_Of_Taxes1.append(None)
        try:
            Premium_Inclusive_Of_Taxes2.append(PREMIUM_INCLUSIVE_OF_TAXES[1])
        except:
            Premium_Inclusive_Of_Taxes2.append(None)
    else:
        Premium_Inclusive_Of_Taxes1.append(PREMIUM_INCLUSIVE_OF_TAXES[0])

    if TEXT[TEXT.find('\nDetails:'):TEXT.find('\nUIN:')].replace('\nDetails:', "").replace("\n", '').strip() != "HDFC Life Click 2 Protect 3D Plus":

        PLAN_OPTION_CHOSEN = TEXT[TEXT.find('Plan Option Chosen:'): TEXT.find('Top Up Option:')].replace('Plan Option Chosen:', "").replace("\n", '').strip()
        PLAN_OPTION_CHOSEN = PLAN_OPTION_CHOSEN.split(" ", 1)
        try:
            chosen_plan_option1.append(PLAN_OPTION_CHOSEN[0])
        except:
            chosen_plan_option1.append(None)

        try:
            Plan_Option_Chosen2.append(PLAN_OPTION_CHOSEN[1])
        except:
            Plan_Option_Chosen2.append(None)

    elif TEXT[TEXT.find('\nDetails:'):TEXT.find('\nUIN:')].replace('\nDetails:', "").replace("\n", '').strip() == "HDFC Life Click 2 Protect 3D Plus":
        PLAN_OPTION_CHOSEN = TEXT[TEXT.find('Plan Option Chosen:'): TEXT.find('Top Up Option:')].replace('Plan Option Chosen:', "").replace("\n", '').strip()
        try:
            chosen_plan_option1.append(PLAN_OPTION_CHOSEN)
            Plan_Option_Chosen2.append(None)
        except:
            chosen_plan_option1.append(None)
            Plan_Option_Chosen2.append(None)
    else:
        pass

  ###
    try:
        TOTAL_PREMIUM_INCLUSIVE_OF_TAXES = (TEXT[TEXT.find('Total Premium Inclusive of Taxes:'): TEXT.find
                                                 ('\nNext Premium Due Date:')].replace('Total Premium Inclusive of Taxes:', "").replace("\n", '').strip()).split()
        Total_Premium_Inclusive_Of_taxes.append(TOTAL_PREMIUM_INCLUSIVE_OF_TAXES[0])
        NEXT_PREMIUM_DUE_DATE = (TEXT[TEXT.find('Next Premium Due Date:'): TEXT.find
                                      ('\nPremium Payment Method:')].replace('Next Premium Due Date:', "").replace("\n", '').strip()).split()
        Next_Premium_Due_Date.append(NEXT_PREMIUM_DUE_DATE[0])
        PREMIUM_PAYMENT_METHOD = TEXT[TEXT.find('Premium Payment Method:'): TEXT.find
                                      ('\nIllustration Of Future Benefits')].replace('Premium Payment Method:', "").replace("\n", '').strip()
        Premium_Payment_Method.append(PREMIUM_PAYMENT_METHOD)
    except:
        TOTAL_PREMIUM_INCLUSIVE_OF_TAXES = None
        NEXT_PREMIUM_DUE_DATE = None
        PREMIUM_PAYMENT_METHOD = None

        Total_Premium_Inclusive_Of_taxes.append(TOTAL_PREMIUM_INCLUSIVE_OF_TAXES)
        Next_Premium_Due_Date.append(NEXT_PREMIUM_DUE_DATE)
        Premium_Payment_Method.append(PREMIUM_PAYMENT_METHOD)
#  details = {"name":Name[0], "age":Age[0], "gender":Gender[0], "UIN1":Uin1[0], "UIN2":Uin2[0],
#         "sumAssured1":Sum_Assured1[0], "sumAssured2":Sum_Assured2[0],
#         "policyTerm1":Policy_term1[0], "policyTerm2":Policy_term2[0],
#         "premiumPaymentTerm1":Premium_Payment_Term1[0],
#         "premiumPaymentTerm2":Premium_Payment_Term2[0],
#         "premiumFrequency":Premium_Frequency[0],
#         "planOptionChosen1":chosen_plan_option1[0],
#         "planOptionChosen2":Plan_Option_Chosen2[0],
#         "topUpOption1":Top_Up_Option1[0], "topUpOption2":Top_Up_Option2[0],
#         "premiumExclusiveOfTaxes1":Premium_Exclusive_Of_Taxes1[0],
#         "premiumExclusiveOfTaxes2":Premium_Exclusive_Of_Taxes2[0],
#         "taxes1":Taxes1[0], "taxes2":Taxes2[0],
#         "premiumInclusiveOfTaxes1":Premium_Inclusive_Of_Taxes1[0],
#         "premiumInclusiveOfTaxes2":Premium_Inclusive_Of_Taxes2[0],
#         "totalPremiumInclusiveOftaxes1":Total_Premium_Inclusive_Of_taxes[0],
#         "nextPremiumDueDate":Next_Premium_Due_Date[0],
#         "premiumPaymentMethod":Premium_Payment_Method[0]}
    details = {"name":Name[0], "age":Age[0], "gender":Gender[0],
               "totalPremium":Total_Premium_Inclusive_Of_taxes[0],
               "premiumDueDate":Next_Premium_Due_Date[0]}

    return details


def get_pdf_details(firebase_url):
    '''converts pdf to text and calls extractors based on formats'''

    pdf_file, _ = urllib.request.urlretrieve(firebase_url, os.path.join(WORKING_DIR, 'common/Modeling_Code/temp.pdf'))
    text_data = parser.from_file(pdf_file)
    text = text_data['content']
    output = {}

    # for type 4
    if text.find('Benefit Illustartion for HDFC Life Sanchay Plus') != -1:
        print("Calling pdftype4")
        output['sanchay'] = pdftype4(text)

    # for type 1
    elif text.find('\nIllustration for your HDFC Life Click 2 Protect 3D Plus\n') != -1:
        print("Calling pdftype1")
        output['protect3D'] = pdftype1(text)

    # for type 3
    elif text.find('\nThis is the sample illustration issued by HDFC Life Insurance Company Limited.\n') != -1:
        print("Calling pdftype3")
        output['proGrowth'] = pdftype3(text)

    else:
        output = {"error" : "Input format not added"}
    return output
