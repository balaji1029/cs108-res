/* JavaScript */

function isPrime(num) {
    console.log(num)
    // keep this condition as-is, you can refer for syntax
    if (num < 0) {
        return isPrime(-num);
    }

    // Start
    if (num == 0 || num == 1) {
        return false
    }
    // End

    var i = 2;
    while (
        // Start
        i < num // this has been added to remove error of compiling, you need to write correct code
        // End
    ) {
        // Start
        if (num % i == 0) {
            return false
        }
        // End
    }

    // Start
    return true
    // End
}
