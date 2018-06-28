# The script is for converting txt file in BCV format to USFM files by adding the required tags and contents like book ID and book full name in the same language for multiple bible's.

# The csv file should be name as bible_language_version i.e. "eng_bib_irv.txt".

# The script will generate new folder with the same name of the file.

# The content in the file should be in BCV format.

# Check the sample file.

# Make sure, you don't have any other .txt files.

# To run this scipt :
	1. create a folder, Paste the script and add input txt files.
	2. Edit the script as you need.
	3. Run the script (python3 txt_BCV_to_usfm.py).
	4. The script will generate folder with same name of .csv file.
	5. The generated .usfm file will have the edited content with tags.
	6. Should have the excel file for the process i.e. "Book name 12 GL.xlsx".
	7. There is an another code which is used for renaming the files in order by adding the number.
	8. To run the script (python3 renameFiles_byID.py).


Developed by : Vipin Paul 
vipin.paul@bridgeconn.com 
vipinpaul95@gmail.com
Bridge Connectivity Solutions