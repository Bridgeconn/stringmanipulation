# The script is for converting single .txt file to  multiple .usfm file by adding tags and more useful contents.

# The script is for adding the introduction to each books.

# Create a "Source" folder and add input .txt files into it.

# The script will generate new folder with the name "Target".

# The book name in the txt file should have an "\id" tag.

# Check the sample file.

# Make sure, you don't have any other folder.

# To run this scipt :
	1. create a folder and Paste the script, and add "Source" folder and file into it.
	2. Edit the script as you need.
	3. Run the script (python3 intro_txt_to_usfm.py).
	4. The script will generate a "Target" folder with multiple .usfm file.
	5. The generated .usfm file will have the edited content with new tags.
	6. Should have the excel file for the process i.e. "Book name 12 GL.xlsx".
	7. There is an another code which is used for renaming the files in order by adding the number.
	8. To run the script (python3 renameFiles_byID.py).


Developed by : Vipin Paul 
vipin.paul@bridgeconn.com 
vipinpaul95@gmail.com
Bridge Connectivity Solutions