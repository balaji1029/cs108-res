// JavaScript example file
// You do not need to edit this
// This is only for syntax reference

function sqrtFibo(num) {

    // if condition
    if (num == 0 || num == 1) {
        return num;
    }
    var a = 0, b = 1, c = 1;

    // for loop (while loop is also very similar)
    for (var i = 2; i < num; i++) {
        c = b + c;
        b = c;
        a = b;
    }

    // return square root
    return Math.sqrt(c);

}
