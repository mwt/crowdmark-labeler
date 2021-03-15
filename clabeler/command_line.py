#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import pandas as pd
import clabeler as cl


def main():
    parser = argparse.ArgumentParser(
        description="Label exam PDFs from Crowdmark with names of students."
    )
    parser.add_argument(
        "labels", type=str, nargs=1, help="path to a csv containing labels"
    )
    parser.add_argument(
        "booklets", type=str, nargs=1, help="path to PDF of unlabeled exams"
    )
    parser.add_argument("pagecount", type=int, nargs=1, help="number of pages per exam")
    parser.add_argument(
        "-O",
        dest="output",
        type=str,
        nargs=1,
        default="labeled_booklets.pdf",
        help="path to output unlabeled exams",
    )
    parser.add_argument(
        "--colfname",
        type=str,
        default="fname",
        help="column label for student's first name",
    )
    parser.add_argument(
        "--collname",
        type=str,
        default="lname",
        help="column label for student's last name",
    )
    parser.add_argument(
        "--colid",
        type=str,
        default="netID",
        help="column label for student ID",
    )

    args = parser.parse_args()

    if args.labels[0].endswith(".csv"):
        labels = pd.read_csv(args.labels[0])
    elif args.labels[0].endswith(".xlsx"):
        labels = pd.read_excel(args.labels[0], sheet_name=0)
    else:
        raise ValueError("labels must be a csv or xlsx file")

    cl.labelbooklets(
        labels=labels,
        pagecount=args.pagecount[0],
        booklets=args.booklets[0],
        output=args.output,
        colfname=args.colfname,
        collname=args.collname,
        colid=args.colid,
    )


if __name__ == "command_line":
    main()
