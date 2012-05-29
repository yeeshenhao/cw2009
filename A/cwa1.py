##filename: cwa1a.py
##author: Yee Shen Hao
##date:
##description: Program CREATESTAFF to get and validate 

import re
import os

def CREATESTAFF():
    try:
        if os.path.exists("STAFF.DAT"):
            print("WARNING: File exists. Will be overwritten.")


        '''ValidStaffID = False
        while ValidStaffID == False:
            StaffID = input("Enter Student ID (digits only): ")
            if len(StaffID) == 0: #presence check 
                print("Please enter something!")
            elif not StaffID.isdigit(): #data type check
                print("Please enter digits!")
            elif not 0 < int(StaffID) < 100000: #range check
                print("Student ID must be between 00001 and ")
            elif not StaffID.re.match("[12][0-9]{2}[01-99]{2}"):
                print("RE fail")
            else:
                ValidStaffID = True'''

        #get and validate StaffID
        ValidStaffID = False
        StaffIDPattern = re.compile("[12][01][89012][0-9][0-9]")
        while not ValidStaffID:
            StaffID = input("Enter staff id: ")
            if len(StaffID) == 0: #presence check
                print("Empty input. Try again.")
            elif not StaffID.isdigit(): #data type check
                print("Please enter digits!")
            elif len(StaffID) != 5: #length check
                print("Staff ID must be exactly 5 digit. Try again.")
            elif not (StaffIDPattern.match(StaffID)): #pattern check
                print("Invalid Staff ID. Try again.")
            elif not StaffID[0:1] != 1 or 2: #Sex check
                print("First digit must be 1 or 2")
            elif not StaffID[2:3] 
            else:
                ValidStaffID = True
                StaffID = StaffID.upper()
                print(StaffID)

    except IOError:
        print("Unable to create or write to file")

if __name__ == "__main__":
    CREATESTAFF()
