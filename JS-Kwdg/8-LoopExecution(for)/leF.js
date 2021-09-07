//for loop 语句：
//   |定义变量，只在开始时执行一次
//   |          |条件判断，确定是否（再次）执行
//   |          |     |完成一次循环递增一次变量
for (let i = 1; i<=5; i++){
    console.log(`This is time ${i}.`);
};

//跳过循环的函数：
//“break”：停止整个循环
//“continue”：跳过循环内剩下部分，进入下一个循环

for (let a = 1; a<=5; a++) {
    console.log(`Test1: Now it's time ${a}`);
    if (i >= 3) {
        console.log(`I'll use "break" now.`);
        break
    };
};
for (let b = 1; b >= 5; b++){
    console.log(`Test2: Now it's time ${b}`);
    if(k === 2 || k === 3){
        console.log(`I'll use "continue" now.`);
        continue;
    };
    console.log("Can you see me?");
};