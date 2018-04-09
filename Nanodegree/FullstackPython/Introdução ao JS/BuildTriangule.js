/*
 * Programming Quiz: Build A Triangle (5-3)
 */

// creates a line of * for a given length
function makeLine(length) {
    var line = "";
    for (var i = 0; i <= length-1; i++) {
        for(var j = 0; j<=i; j++){
            line += "* ";
        }
        line += "\n";
    }
    return line + "\n";
}

function buildTriangle(lenght){
    console.log(makeLine(lenght));
}

buildTriangle(10);
