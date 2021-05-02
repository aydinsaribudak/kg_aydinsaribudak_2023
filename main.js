
var inputList = [341,4, 32]; 
var i;
var j;
var numValArr = [];

for (i = 0; i < inputList.length; i++) {
    
    var remainder = [];
        
    var rem = inputList[i] % 10;
    //console.log(rem);
    remainder.push(rem);
    var quot = parseInt(inputList[i] / 10);
    //console.log(quot);

    while (quot >= 1) {
        rem = quot % 10;
        remainder.push(rem);
        quot = parseInt(quot / 10);
    }

    for (j = remainder.length-1; j >= 0; j--) { 
        if (remainder[j] == 1)
            numValArr.push("One");
        else if (remainder[j] == 2)
            numValArr.push("Two");
        else if (remainder[j] == 3)
            numValArr.push("Three");
        else if (remainder[j] == 4)
            numValArr.push("Four");
        else if (remainder[j] == 5)
            numValArr.push("Five");
        else if (remainder[j] == 6)
            numValArr.push("Six");
        else if (remainder[j] == 7)
            numValArr.push("Seven");
        else if (remainder[j] == 8)
            numValArr.push("Eight");
        else if (remainder[j] == 9)
            numValArr.push("Nine");
        else if (remainder[j] == 0)
            numValArr.push("Zero");
        else
            numValArr.push("NA");
    }
    if (i < inputList.length-1)
        numValArr.push(",");
    else
        numValArr.push("");

}

var printVal = "";
numValArr.forEach(function(element){
    printVal += element;
})
console.log(printVal);

