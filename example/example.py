#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

# Add parent directory (repo root) to Python path
sys.path.append("..")

# Import the main function defined in the root
import clabeler as cl

# Import pandas to read list of students
import pandas as pd

# Read list of students
labels = pd.read_excel("labels.xlsx", sheet_name=0)

# new data frame with split value columns
foo = labels["Student"].str.split(", ", n=1, expand=True)

# making separate first name column from new data frame
labels["fname"] = foo[1]

# making separate last name column from new data frame
labels["lname"] = foo[0]

# Run function
cl.labelbooklets(labels, pagecount=8)
