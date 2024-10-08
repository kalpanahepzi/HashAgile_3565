function firstNonRepeatingChar(str) {
    for (let i = 0; i < str.length; i++) {
        let count = 0; 
        let currentChar = str[i];
        for (let j = 0; j < str.length; j++) {
            if (str[j] === currentChar) {
                count++; 
            }
        }
        if (count === 1) {
            return currentChar;
        }
    }
    return null;
}
let inputStr1 = "onion";
let result1 = firstNonRepeatingChar(inputStr1);
console.log(`The first non-repeating character in "${inputStr1}" is:`, result1);
let inputStr2 = "teeter";
let result2 = firstNonRepeatingChar(inputStr2);
console.log(`The first non-repeating character in "${inputStr2}" is:`, result2);
let inputStr3 = "racecar";
let result3 = firstNonRepeatingChar(inputStr3);
console.log(`The first non-repeating character in "${inputStr3}" is:`, result3);





