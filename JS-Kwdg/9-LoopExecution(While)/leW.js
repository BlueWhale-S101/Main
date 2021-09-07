//while loop 语句：
let ptn = 1;
while (ptn <= 5 ) {//判断是否执行
    console.log(ptn);
    ++ptn;
};

//区别什么时候用for loop，什么时候用while loop：
//可以提前知道循环几次建议用for loop，
//程序不易预测循环几次用while loop。

//建议用while loop示例：
let ttl = 0;
let ipt = prompt("Input a number:");
while (Number(input) != NaN) {
    ttl += parseInt(ipt);
    ipt = prompt("Input a number:");//在网页弹出输入框
};
console.log(`Total: ${ttl}`)

//相似语句do-while loop示例：
let num = 1;
do {//先执行循环体代码再判断
    console.log(num++);
} while (num<5);

//温馨提示：注意防范while loop语句无限循环！
//要确定条件可以触发跳出循环！
//break、continue都适用。