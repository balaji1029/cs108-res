function validateName() {
    /*Check whether name is entered or not.
    Throw an error if name field is empty.
    Error message will be "Full name is required."*/
    var name = document.getElementById("fullName").value;
    if (name==""){
        throw "Full name is required.";
    }

}

function validateEmail() {
    /*Check whether email is valid or not, as per the rules stated in problem statement.
    Use regex and test() function to validate the email address.
    Throw an error if email is invalid.
    Error message will be "Invalid Email Address."*/
    var email = document.getElementById("email").value;

    let pattern=/([a-z]|[0-9])+@[a-z]+.[a-z]{3}/g;
    let result = pattern.test(email);
    if (result==false){
        throw "Invalid Email Address."

    }

}

function validatePassword() {
    /*Check whether password is made of atleast 8 characters.
    /If not, throw an error.
    Error message will be "Password must be at least 8 characters"*/
    var pwd = document.getElementById("password").value;
    if (pwd.length<8){
        throw "Password must be at least 8 characters"
    }
}

function ConfirmPassword() {
    /*Check whether the re-entered password is same as the password entered first.
    If not, throw an error.
    Error message will be "Passwords do not match"*/
    var pwd = document.getElementById("password").value;
    var cpwd = document.getElementById("confirmPassword").value;  
    if(pwd!=cpwd){
        throw "Passwords do not match."
    }
}

function validateForm() {
    

        /*Check whether all fields are entered or not*/
        var name = document.getElementById("fullName").value;
        var email = document.getElementById("email").value;
        var pwd = document.getElementById("password").value;
        var cpwd = document.getElementById("confirmPassword").value;     
    try {
        if(name=="" || email=="" || pwd=="" || cpwd==""){    
            throw "All fields are required.";
        }     
        validateName();
        validateEmail();
        validatePassword();
        ConfirmPassword();
        
        // Additional validation rules can be added here

        //After checking all the rules, if the program throws no error, it will reach this part of code.
        document.getElementById("feefoo").innerHTML='<span style="color: green">Registration successful!</span>';
        //Using "innerHTML" and "span" tag, give the message "Registration successful!" in GREEN colour to the div container "feedback" in index.html.
        //Your code here
    } catch (error) {            
            document.getElementById("feefoo").innerHTML='<span style="color: red">'+"Error: " +error+'</span>';
        //After checking all the rules, if the program throws an error, it will reach this part of code.
        //Using "innerHTML" and "span" tag, give the error message in RED colour to the div container "feedback" in index.html.
       
    }
}
