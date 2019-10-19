# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 02:06:03 2019

@author: Sayak
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import Image

import csv

data_file = 'data.csv'

def import_data(data_file):
    patient_data = csv.reader(open(data_file))
    for row in patient_data:
        name = row[6]
        date = row[0]
        reason = row[1]
        prescription = row[2]
        cost = row[3]
        description = row[4]
        transaction_id = row[5]
        pdf_file_name = name+'_'+transaction_id+'.pdf'
        generate_receipt(name,date,reason,prescription,cost,description,transaction_id,pdf_file_name)
        
def generate_receipt(name,date,reason,prescription,cost,description,transaction_id,pdf_file_name):
    patient_name = name
    c = canvas.Canvas(pdf_file_name, pagesize = A4)
    
    #text
    c.setFont("Helvetica", size = 28, leading = None)
    c.drawCentredString(300,750, "Medical Store")
    c.setFont("Helvetica", size = 14, leading = None)
    c.drawCentredString(100,650, "This Receipt is generated for")
    c.setFont("Helvetica", size = 16, leading = None)
    c.drawCentredString(100,620, patient_name)
    c.setFont("Helvetica", size = 14, leading = None)
    c.drawCentredString(180,620, "on")
    c.setFont("Helvetica", size = 16, leading = None)
    c.drawCentredString(230,620, date)
    c.setFont("Helvetica", size = 14, leading = None)
    c.drawCentredString(232,590, "He/She has been suffering from "+reason+' and has a valid prescription')
    c.setFont("Helvetica", size = 14, leading = None)
    c.drawCentredString(255,530,"He/She has been precribed the medicine "+description+" which costs "+cost)    
    c.setFont("Helvetica", size = 16, leading = None)
    c.drawCentredString(75,480, "Price-"+cost)
    c.setFont("Helvetica", size = 16, leading = None)
    c.drawCentredString(100,450, "Transaction ID:- "+transaction_id)    
    c.showPage()
    c.save()
    
'''import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")'''

import_data(data_file)
    