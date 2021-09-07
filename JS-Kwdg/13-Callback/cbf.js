//回调Callback
//JS有两种程序执行方式：同步执行和异步执行。

console.log("Hello")
console.log("world")
//同步执行：有序执行程序

//当程序出现导致系统堵塞（需要等待结果）的程序时，
//可用异步执行使后续程序在前面程序等待时执行。
//回调函数：程序等待一段时间后才回来执行的程序
console.log(1)
setTimeout(function () {
    console.log(2)
}, 500);
console.log(3)
//setTimeout(回调函数, 等待时间/毫秒（1000:1）)
//等待时会先执行下面的程序
//回调函数可以在里面也可以在外面
function show2() {
    console.log(2)
}
console.log(1)
setTimeout(show2, 1100);
console.log(3)