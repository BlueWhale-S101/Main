//当异步程序过多时，还用Callback会出现Callback hell,
//简单来说就是Callback代码需要一层层嵌套
//Promise可以简化代码，避免Callback hell。

let promiseDone = false;//手动更改true/false以展示
let have_pms = new Promise(function(resolve, reject){
    //类似在Callback里使用的可能堵住程序的程序，这里只是举例
    if (promiseDone) {
        console.log("yes")
        resolve("Y");
        //执行回调
    } else {
        console.log("No")
        reject("N");
        //爽约
        //在默认中执行完reject()就会报错
    };
    //Promise Object 在创建后就开始执行。
});

//PromiseVerb.then(回调函数)表示执行完Promise后执行的回调函数。
have_pms
.then(
    function(YRN){
        console.log("Done!")
        console.log(YRN)
    }
)
.catch(
    //Catch语句用于不显示默认的报错，而是执行语句内的回调函数
    function(YRN){
        console.log("Rejected!")
        console.log(YRN)
    }
)

//补充：
//JS里有一个fetch(url)函数，用于想网络发送请求。
//它的返回值就是Promise。
//
//当Promise的第一个.then也是异步执行的Promise，后面还有程序需要等待返回值时，
//可以在第一个.then最后用return将数据传递至第二个.then(回调函数(返回数据储存变量){回调程序})。