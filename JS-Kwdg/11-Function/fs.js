//函数Function

//创建函数：
//       |函数名 
function showM() {
    //函数被使用时要执行的代码
    console.log("Hi!");
    console.log("Welcome!");
};
showM();

//                  |参数列表
function showMwithN(username) {
    console.log(`User ${username}, hi!`);
};
showMwithN("John");

function eror1 (name) {
    console.log(`User ${name}, hi!`);
};
eror1();//由于参数没输入，参数会变成undefined

function showMwithUserN(username = "Visitor") {
    //这里设置了默认值，当调用函数不传递参数信息时参数就为默认值，参数有传递时则不影响。
    console.log(`User ${username}, hi!`);
};
showMwithUserN();
showMwithUserN("Alice");

function playMath_Multiply (num1, num2) {
    let total = num1 * num2;
    return total;//返回信息
    //程序将不再执行return以后的属于框内的代码。
};
//把函数“playMath_Multiply”的返回值赋予新变量“outp”。
let outp = playMath_Multiply(135, 842);
console.log(`Total is ${outp}`);