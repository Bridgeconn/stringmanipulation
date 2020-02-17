## Other Tasks
- __Lexicon Search app using Python GUI__ _(LexiconSearchScript)_
	
	-- If you want to use the app directly, unzip the files present in the folder and run the exe file if you are on Windows, and the application file if you are on Linux

	-- Else, you can directly run the script. Note: The existing directory structure should not be changed.

- __Format translation of QA in XLSX and copy to target file__ _(formatQAfromXlsx)_

	-- This script runs only for one file at a time. Place the source file in "Source" and "Urdu" folders. 

	-- Open the script and add the name of source files

	-- Ensure that the structure of the source files are as given in the demo file that is available in the folder

	-- Run the script
- __Rectify USFM errors__ _(rectify_USFM)_
- __Parse Strong's Lexicon__ _(parseStrongsLexicon)_ 
- __Open Bible Stories__ _(OBS)_

   -- Script for placing links to images from the target language column to source language column in a docx files

   -- DOCX to MD (OBS)

- __Translation Words Project__ _(translation_Words)_

   It consists of the following scripts:

   --	MD to XLSX (TW)

   --	MD to XLSX for Titus (TW)

   --	Place links in MD files (TW)

   -- 	Remove links in MD files for Titus (TW)

   --	Remove links in MD files for remaining files (all files except Titus) (TW)

   --	Count number of words in MD files (TW)

   --	Translate MD files (Available under the heading below)

   --	Create config.yaml from the TW by searching in the ULB bible files (.usfm) 

- __Google Translate API to translate files (only md/text files)__ _(using_Google_Translate)_
		
   Steps to connect to Google Cloud API: Pre-requisite: Python 2.7 should be installed

		1. Run: pip install --upgrade google-cloud

		2. Now, download google cloud sdk installer (https://cloud.google.com/sdk/), extract it

		3. Run: ./google-cloud-sdk/install.sh

		4. Restart the shell: exec -l $SHELL

		5. Add gloud to the environment variable, by adding in bashrc : export PATH="Give your path/google-cloud-sdk/bin:$PATH"

		6. Run: gloud init and enter your configuration settings

		7. Create a new key and download the generated key file file, in Service Accounts tab, under IAND & admin page (It is accessible when you login to the Google Cloud Platform).

		8. Run: gcloud auth activate-service-account --key-file "KEY FILE"

		7. Add the key file to the environment variable: export GOOGLE_APPLICATION_CREDENTIALS=/path/to/credential.json

		8. Reload bash: source ~/.bashrc

   Now, run the script. You can place your files inside the Source folder.

- __USFM tag validator__ _(validate_usfm_tags)_

Note: Unless specifically mentioned, you can directly download the required folder, and run the script. The structure of the existing folders should not be altered. Folders have demo files, that give you the required format of the input file.