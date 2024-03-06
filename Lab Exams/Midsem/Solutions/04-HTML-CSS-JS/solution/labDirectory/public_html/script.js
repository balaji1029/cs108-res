/* JavaScript */

function isPrime(num) {
    if (num < 0) {
        return isPrime(-num);
    }
    if (num == 1) {
        return 0;
    }
    if (num == 2) {
        return 1;
    }
    var i = 2;
    while (i <= Math.sqrt(num)) {
        if (num % i == 0) {
            return 0;
        }
        i++;
    }
    return 1;
}
