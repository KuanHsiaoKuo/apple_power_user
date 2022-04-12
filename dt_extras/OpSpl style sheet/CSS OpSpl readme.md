# Customizing a CSS<br>The minimum to know

I’m not a designer, nor a programmer. So I went through some tutorials and some reference material in order to arrive to something satisfactory, at least for me — and it took some time. So, I’d like, here, to give other laymen/laywomen in CSS the barely minimal knowledge so they can edit a CSS to their personal taste.

Let’s dive in.

* An HTML rendered page — and a text, for this matter — is made up of semantic elements : headers of different levels (H1 to H]), paragraphs (P), unorderd lists (UL = bulleted), ordered lists (OL = numbered), and so on.

* There are also components identified by names starting with a dot `.` These names are defined only in a certain context : a *Wordpress* site, a *Marked* rendered document for example.

* All these elements and components are styled by the CSS in a set of rules enclosed in brackets `{…}`

* Inside the brackets, the rules are made up of pairs of :
	* `property` and `value`
	* the syntax is important :
		* “property” is followed by a colon `:`
		* “value” is followed by a semicolon `;`
	
* In the whole CSS, all that is not “significant characters and words” is considered “blank” :
	* every added “space character”
	* every “end of line”
	* every “tab”
	
* So, for readability, one can add all the suitable empty lines, spaces and tabs that renders the code pleasing to the eye.

* It is very advisable to add comments. A comment is “everything between `/*` (start of  comment) and  `*/` (end of comment)”. A comment is considered “blank space“ by the rendering engine.

* Any HTML element my be defined multiple times, by differing rules. When a property for a given element is defined more than once, it’s the last definition (the lowest down the CSS) that will be taken in consideration / applied.

* The colors are defined mainly in three formats, that you can use at will :

  * Hexadecimal : a hash followed by six hexadecimal digits. For example :
    * `#6DB2E8` (a light blue)
  * explicit RGB (red, green and blue components) :
    * rgb(109, 178, 232) (the same light blue)
  * a conventional name that you can find [here](https://www.colorschemer.com/color-names/) along with the hexadecimal values

  Don’t forget to put a semicolon `;` after the name or the value !

  The OS gives you different possibilities to choose colors and get the hex values. But there are also nice websites dedicated to this purpose, such as [ColorSchemer](https://www.colorschemer.com/).

* The units must be put right after the values, without space :

  * `14px` is correct
  * `14 px` won’t work !

* Common units :

  * `px` = pixels — not true pixels on a retina display, but rather “ordinary pixels on a non-retina display” ; useful mostly for graphic elements, not type (font) elements ;
  * `pt` = points — useful for type and font related items ;
  * `rem` = relative ems — relative to “size of the type of the basic paragraph” ; it’s better to use this rather than pixels for everything related to typography, because you don’t know beforehand the zoom level the user will choose nor the size of his display (from the smallest smartphone to the most gigantic 49" monitor).

* About font families : one gives a succession of font family names. The first family available on the current system will be effectively used. When the name is a single word — like “Candara” — it can be left alone ; when it’s a compound name — like “Helvetica Neue”, it must be enclosed in **straight** quotes : `"Helvetica Neue"`.

  

## Some hints about OpSpl.CSS

* At the top of the file, you’ll find some variables beginning with `--` . It’s a commodity that allows one to modify there, in a central position, different values that wil be used elsewhere in the CSS. I hope everything is self explanatory and easy to understand.
* The choice of the font families is mine… You can of course adjust to your taste. But don’t be too much surprised if you also have to adjust *font size*, *line spacing* and *line length* accordingly. Theses parameters have a *very big* influence on aesthetics and readability, and they a highly dependent on the character shapes of the choosen font.
* There are two graphical elements in use : a white paper pattern for the background and a swirl for the *Horizontal Ruler* (`hr`) element. They are defined by a special sequence of characters. Be very careful not to change these characters, not even changing their count !



## History and credentials

In order to arrive where I wanted, I started, some years ago, by exploring the different style sheets prepared by [Brett Terpstra](https://brettterpstra.com/) for his great [*Marked 2*](https://marked2app.com/) software. I decided that the “GitHub” one was closest to my vision. So I made a copy of it and started editing it. Some observations :

* Since I undertook this project, Brett Terpstra has further refined  both *Marked* and its style sheets. So this attempt of mine may not be 100 % compatible with every current feature.
* I haven’t touched what I don’t use or don’t fully understand.
* In the end, please be benevolent with the shortcomings of this CSS. Again, I’m neither a professional designer, nor a programmer, nor a webmaster.
* If you are more proficient than myself in CSS and feel like improving further this style sheet, by any mean feel free ! You’re most welcome. And please, let me know and benefit from your talent(s) !

Thank you for your interest and for your understanding.



<p style="text-align: center;">&emsp;</p>
<p style="text-align: center;"><a href="https://dr-spinnler.ch"><img src="http://dr-spinnler.ch/myfiles/logos/Olivier-Spinnler.png"/></a></p>
<p style="text-align: center; font-style: italic;">October the 10th, 2020.
</p>
<p style="text-align: center;">&emsp;</p>
<p style="text-align: center;">&emsp;</p>