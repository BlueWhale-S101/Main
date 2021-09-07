//数组Array
//          |     |     |这些都是数组元素element。有n个元素长度length就是n。
let ary1 = ["Aa", "Ss", "Ww"];
//索引：     |0    |1    |2
//每个元素都有索引index，是按先后顺序从0开始类推。索引是数字。

console.log(ary1);
console.log(ary1.length);//检查长度

//用索引提取元素：
console.log(ary1[0]);
console.log(ary1[1]);
console.log(ary1[2]);

//替换数组数据：
ary1[1] = "Tt";
console.log(ary1);

//尾部添加新元素：
ary1.push("Kk");//添加到数组末尾
console.log(ary1);
ary1.push("Gg", "Jj");//可在末尾一次加多个
console.log(ary1)
//头部添加新元素
ary1.unshift("Oo");
console.log(ary1);
//在尾部添加数据比在头部添加数据高效，
//应为在尾部添加数据只需添加n个位给数据。
//儿在头部添加数据时要先添加n个位，然走把已有数据都往后移n个位，最后添加数据。

//尾部删除数据：
ary1.pop();
console.log(ary1);
//头部删除数据：
ary1.shift();
console.log(ary1);
//shift和unshift一样要移动数据，比较低效。

//使用数组实例：
let SalesData = [100, 50, 30, 60, 200, 300, 90];
let TotSales = 0;
for (let i = 0; i < SalesData.length; i++) {
    TotSales += SalesData[i];
};
console.log(`Total sales: $${TotSales}.`)