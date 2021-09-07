//逻辑与“&&”在判断语句中只有两个条件都满足才会返回布尔值true。
if (10>5 && 12>10) {
    console.log("yes")
} else {
    console.log("no")
}
if (10>5 && 12>10 && 5>12) {
    console.log("yes")
} else {
    console.log("no")
}

//逻辑或“||”在判断语句中只要条件中有满足的就返回true。
if (10>12 || 5>12) {
    console.log("yes")
} else {
    console.log("no")
}
if (10>12 || 15>12) {
    console.log("yes")
} else {
    console.log("no")
}
if (5>10 || 5>12) {
    console.log("yes")
} else {
    console.log("no")
}