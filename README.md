<h1>Conference Badge Creator</h1>

Conference Badge Creator is a CLI tool written in Python 2.7. Although it can be used for wider purposes, it aims to automate the process of mass-creating the badge for any event of your liking. It takes an Excel File with the Names/Surnames/Occupations of the attendees (customizable) and the template badge as input. After minimal amount of time it generates a folder in your current working directory with a name of your liking and saves the badges depending on the attendees occupation.

e.g

Foo Bar Speaker

Foo1 Bar1 Volunteer

Foo2 Bar2 Random

Final folder structure:

* ConferenceName
  * Speakers
    * Foo1_Bar1.jpg
    * Foo4_Bar4.jpg
    * Foo2_Bar2.jpg
  * Volunteers
    * Foo6_Bar6.jpg
  * Other
    * Foo3_Bar3.jpg
    * Foo3_Bar5.jpg

Each one of the Foo Bar's will have his own folder along with other people who share the same occupation with them. This is done in order to ease the organizing of the badges post-print. The script also includes the option to combine each image to a grid of NxN size for ease at printing on various paper sizes.

usage:

python conference_badge_creator.py -t templateFile -e spreadsheetFile

Use -h as an argument to see all the available options.

Use absolute paths to the files in the arguments.
