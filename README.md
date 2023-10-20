# ScreenshotToRemarkable
A short script to send a screenshot to a remarkable2 Tablet

# Setup
- Download rmapi, the CLI for the remarkable cloud, [here](https://github.com/juruen/rmapi)
- Setup the connection to the remarkable cloud, [Instructions here](https://github.com/juruen/rmapi/blob/master/docs/tutorial-print-macosx.md)
- change the value of RMAPI_EXEC_PATH in main.py to match the location of your rmapi-executable
- Install requirements for python

# Usage
- Call the python script without any arguments to generate a random filename
- Call the script with a string to set the filename of the uploaded file
- When running the script, your middle mouse button is used to select the screenshot area: press to start, hold while dragging, release to stop - directly after releasing of the button, the file is converted to pdf and uploaded to the connected remarkable tablet

# Various
- change the button to select the area in main.py:18

# ToDo-List
- [ ] Overlay while screenshoting to avoid manipulating screen
- [ ] Indicate selected area with rectangle overlay
- [ ] Take multiple screenshots, put in one file (Timer to finish?)
- [ ] Put file in specific folder on remarkable
- [ ] Make sure, file does not exist, if so, retry
