# Lab-4 Activities

## Activity 1

In this activity, you need to find the largest prime number which is less than or equal to the number which is received as input. The HTML code is already provided to you in the file basic.html. You need to write javascript code in the same file, and submit. (If there is no prime number less than or equal to the given number, just print 0.) (Also, your final result string should be stored in the paragraph with id "result", see the HTML Code for you reference!)

The website before giving an input looks like as follows.

Suppose we give 10 as the value of n, then the website will look like as follows. (after clicking the button)

Please make sure that the format of the result is as shown above.

## Activity 2

Let’s talk about 22 January 2024. Suppose there were “n” priests present in Ayodhya on the occasion of “Ram Mandir Pran Pratishtha”. Everyone has brought a gift for this auspicious event. (A single person has brought a single gift.) The idea is that everybody will get a gift which has been brought by someone else.

You need to find out the number of ways in which this is possible. (Looks similar to JEE stuff, doesn't it?)

Write your code in the script.html file provided. (Javascript code should also be written in that file only.) (Also, your final result string should be stored in the paragraph with id "result", see the HTML Code for you reference!)

A simple look of the website is shown below.

Suppose, if you type 3 in the space provided and click on the Calculate button, then the look will be as shown below.

In the case of 3 priests (A, B, C), the possible matchings are (A gives B, B gives C, C gives A) and (A gives C, C gives B, B gives A). So, the result=2 has been printed.

## Activity 3

**Objective**:

Create a user registration form with an input validation using JavaScript. Handle errors and provide appropriate feedback to users.

**HTML**:

Begin by completing the “index.html” file with a user registration form. Include the following fields with appropriate labels and input boxes/button with “id” strictly the same as:

Full Name, id = “fullName”
Email Address, id = “email”
Password, id = “password”
Confirm Password, id = “confirmPassword”
Submit Button, id = “submit”
The submit button on clicking should call the function “validateForm()” from the script.js file.

**Note**:- If the same ids are not followed, you will face problem(s) in evaluation.

Use the appropriate “type” attribute for each input box. The full name input box will have the type “text”, the email address input box will have the type “email”, and the password and confirm password input boxes will have the type “password”. The submit button will have the type “button”. Follow this link to look at possible input field “type” attributes.

**Important Note**:- An empty <div> container with id “feedback” is provided in index.html. Do not modify it. Use that container in your JavaScript file to give back error messages/feedback.



**CSS**:

In “style.css” just make sure that every component is centered and keep the background colour of the body as “azure”, as shown in this pic:-





**JavaScript**:

Complete the script.js file. Most of the instructions are written as comments in that file.

You must complete the validateName, validateEmail, validatePassword, ConfirmPassword, and validateForm functions. These functions don’t return anything.

Whenever you have to give “feedback” about a successful entry or an error message, refer to the instructions in the “How to give your feedback/error message to the HTML page from a JavaScript file?”

Now, read the content below to learn more about the functions of the script.js file.

When validateForm() is called, the try block has code that runs in the following order:-

Checks if all fields are non-empty/filled or not. If not, throw the error message “Error: All fields are required.”.
Calls the validateName() function
Calls the validateEmail() function
Calls the validatePassword() function
Calls the ConfirmPassword() function
Gives the feedback “Registration successful!” (in green colour) to the HTML page.
The catch block contains the code that gives feedback to the HTML page about the error message it catches. The error message, if caught, will either be “Error: All fields are required.” or those thrown by any one of the validateName(), validateEmail(), validatePassword() or ConfirmPassword() functions.
Note:- The try block will reach step (6) successfully only if none of the steps (1) - (5) throw an error message.

The validateName() function :-

Check if the name is entered or not. If not, throw the error “Error: Full name is required.”.
The validateEmail() function :-

Check if the email entered is valid or not. An email is valid if and only if:-
It contains exactly 1 “@” and,
There should be atleast one character to the left of “@”. If yes, those characters should only be a-z or 0-9, and,
To the right of “@” there should be exactly one “.” and,
Between”@” and “.” there should be atleast one character. If yes, those characters should be only from a to z, and,
To the right of “.”, there should be exactly 3 lowercase English characters.
This check is conveniently possible by Regex. Use the test() function of JavaScript to make it happen. Follow this link to learn more about it.
If the email is invalid, throw the error message “Error: Invalid Email Address.”.
The validatePassword() function :-

Check if the password entered is atleast 8 characters long. If not, throw the error message “Error: Password must be at least 8 characters.”
The ConfirmPassword() function :-

Check if the re-entered password matches or not. If not, throw the error message “Error: Passwords do not match.”
How to give your feedback/error message to the HTML page from a JavaScript file?

Using “innerHTML”, we can use the <div> “feedback” container of HTML to give the error messages/responses back. Follow this link to learn more about “innerHTML”.

When all fields are validated successfully, then on clicking “Submit”, “Registration successful!” should be printed in green color. If any one of the fields is invalidated, then on clicking “Submit”, an error message should appear in red.

We can use the “span” tag along with the “innerHTML” to adjust the color of the feedback. Follow this link to learn more about the “span” tag.

## Activity 4

In this activity we will use javascript to manipulate html files provided.

There is one sample.html file provided to you, which has its script linked to dom.js. You need to write your code in dom.js, to manipulate the html webpage as follows:

1. For all images (with <img> tag), change the source of the image to be timepass.png

2. Delete all the <h1> heading tags. (Remember, no other headings should get deleted.)

3. For all paragraphs (with <p> tags), change the content of the paragraphs to be “Enough of JavaScript, let’s stop.”

4. Change all the <h2> content to make it uppercase. So, suppose you have a h2 heading saying “Don’t Stop”, then it should be converted to “DON’T STOP”

5. For all <div> containers with element id = “div1”, add a heading (<h3>) with no text.



All these changes will happen when you click the “Change” button. The change button in your html file will call a function in your javascript code. So, you need to edit that function in dom.js.

Once you click the Evaluate button, the results will be shown after a few seconds, so please wait.