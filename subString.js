let input = "abcd";

function subStr_itr(str) {
    let result = [];
    for (let i = 0; i < str.length; i++) {
        for (let j = i + 1; j < str.length + 1; j++) {
            result.push(str.slice(i, j));
        }
    }
    return result.sort((a, b) => a.length - b.length);
}

console.log("Interative", subStr_itr(input));


function subStr_rec(i, j, result, str) {
    if (i == str.length || j == str.length + 1) return;

    let subStr = str.slice(i, j);
    if (!result.includes(subStr) && subStr != "") { result.push(subStr) };
    
    subStr_rec(i, j + 1, result, str);
    subStr_rec(i + 1, j, result, str);

    return result.sort((a, b) => a.length - b.length);
}

console.log("Recursive", subStr_rec(0, 1, [], input));