//八大JavaScript数据类型：
//bigint、number、boolean、string、undefined、null、object、symbol。

//数字number包括整数（integer）、浮点数（floating point）、无穷大（Infinity）、非数值（NaN）。
let number = 10;
number = 5.1;
number = -6;
console.log(1/0);//Infinity
console.log("hello" - 1);//NaN
//一般运算在遇到超大数字时会失去精度（正常范围：正负9,007,199,254,740,991）。
//在超大数字后加上“n”变为bigint，保持精度（如99999999999999999n）。

//字符串string是任何非特殊符号字符。
let string1 = "123Abc.?;]/=&(";//用双引号括起字符
let string2 = '123Abc.?;]/=&(';//用单引号括起字符
let string3 = `123abc.?;]/=&(`;//用反引号括起字符，可含有变量。

console.log(`v:${number}.`);//用“${变量}”在反引号字符串中添加变量。
console.log("v:"+number+".");//单引号和双引号需要用加法添加变量。

//布尔值boolean包含两个值：真（true）和假（false）。
let boolean = true;
boolean = false;

//空值null很特殊，它只表示赋予的空值。
let nullv = null;//进行赋值，但赋予的是空值

//未赋值undefined是变量没被赋值时的状态。
let udf;//没有进行赋值
console.log(udf);//会输出undefined。

//唯一标识符symbol是唯一标识。
let syb = Symbol("SelfName")//创建唯一标识符。

//以上数据类型为原始类型，值只含一个单独数据。

//对象类型object是JS中的最重要数据类型。
let user = {
    name: "Ben",//键:值,
    age: 18,
};//创建对象数据。
//对象属性格式是“键（属性名）值对”（key-value pair）。
console.log(user);
console.log(user.name);
//提取对象数据user中的name值。