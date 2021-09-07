//用条件判断语句控制什么时候执行一些程序：
if(10>1){
    console.log("10 is greater than 1");
};

//用变量控制if:
let collectedc = true;
let score = 0
if (collectedc) {//条件必须是布尔值
    console.log(`score: ${++score}`)//当条件满足时执行
}

//if……else……语句：
collectedc = false;
if (collectedc) {
    console.log(`score: ${++score}`)
} else {//前面条件都不满足时执行
    console.log(`score: ${score}`)//当条件不满足时执行
    console.log("加油！")
}

//多次判断语句
if (score>1) {
    console.log("你完成任务了！")
} else if (score>0) {//多次判断语句中第二个判断句及以上判断用这个
    console.log("还有任务没完成，加油！")
    //这些判断句时有先后顺序的：
    //if (condition) {//先判断
    //    programs//当条件满足时执行
    //} else if (c) {//当上一判断句条件不满足时才判断
    //    programs//同29
    //} else if (c) {//同30
    //    programs//同29
    //}…… else {//以上条件都不满足时一定执行框内程序
    //    programs
    //}
    //
} else {//可以没有，或有1个
    console.log("快去完成第一个任务！")
}