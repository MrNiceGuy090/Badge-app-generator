# Badge-app-generator
An automazation for writing badges.

#Preprocessing

In the root folder of the app, there has to be an 'badge.jpg' image representing the model of badge, as well as the font files which to be used for creating labels
Each photo has to respect the following convetion:
  - to be in .jpg format
  - the labels that are to be shown on the badge have to be present in the file name
  - each label has to be seperated from the other by a "_"
  - for the best results, the color mode should be the with the badge itself
  - at the end of the file name, there has to be an number that indicates the way each photo will pe croped, 1 is for the left/upper, 2 is for the center, 3 is for the right/bottom part of the photo (in corelation with the format of the place dedicated for people's photo)
  - example: 'Name Surname_postion_company_1.jpg' it has 3 labels that represent the name, position and the company of the given person.
  
#Interface

The inputFolder is the folder path to where are the initial photos. 
The outputFolder is the folder path to where the badges will be saved.

In the top left corner there are 4 fields. These indicate the coordonates that mark the place where the photos will pe placed.
The first 2 indicate the top-right corner and the last 2 indicate the bottom-left corner.

There are 6 lines index from 1 to 6. Each of those represent a label to be written on the badge and has the following options:
  - width min: the leftmost point where the label can start
  - width max: the rightmost point where the label can end
  - height: the position ,from top to bottom, where the label will be
  - font size: the label font size 
  - font name: the name of the label's font
  !!Important!! 
      The font file has to be added in the application folder
   - cmyk color: the color of the label in cmyk format. The default is white
   - text-align: the alignment of the text within the given width min and width max variables. The default is left and can be changed to center and right.
   - see button: this button registrate the changes made and display/update the label in the left preview window
   
The number of labels field indicates how many labels are to be written on the badge.
