#!/usr/bin/python3
# -*- coding: utf-8 -*-
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def labelbooklets(
    labels,
    pagecount,
    booklets="booklets.pdf",
    output="labeled_booklets.pdf",
    colfname="fname",
    collname="lname",
    colid="netID",
):
    """
    Outputs a PDF containing labeled exams given a data frame of labels,
    a PDF of unlabeled booklets, and the number of pages in each exam.
    """

    # Extract pages from booklet pdf
    pages = PdfReader(booklets, decompress=False).pages
    pagex = [pagexobj(i) for i in pages]

    # Set output path
    c = canvas.Canvas(output, pagesize=letter)

    # Select columns (order is important)
    labels = labels[[colfname, collname, colid]]

    # Truncate any string longer than 17 chars
    labels = labels.applymap(func="{:.17}".format)

    # Loop over all students to apply labels
    for (i, fname, lname, netid) in labels.itertuples():

        # Set font to fixed-wdith and set font size
        c.setFont("Courier", 32)

        # Extract the first page of this student's exam
        c.doForm(makerl(c, pagex[i * pagecount]))
        c.drawString(76, 481, fname.upper(), charSpace=7.8)
        c.drawString(76, 418, lname.upper(), charSpace=7.8)
        c.drawString(76, 355, netid.upper(), charSpace=7.8)
        c.showPage()

        # Loop over the rest of the pages in this student's exam
        for page in pagex[i * pagecount + 1 : (i + 1) * pagecount]:
            c.doForm(makerl(c, page))
            c.showPage()

    # Save the PDF file after processing all students
    c.save()
    print("Attempting to save output to " + output)
