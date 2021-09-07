//JS的加减乘除和数学类似，
//但乘号用“*”，除号用“/”，
//还有取余符号“%”获取除法余数、求幂符号“**”求一个数的n次方。
console.log(3%2);//求3/2的余数。
console.log(2**3)//求2的3次方。

let num1 = 10+5;//加法运算
console.log(`10+5=${num1}`);
let num2 = 10-5;//减法
console.log(`10-5=${num2}`);
let num3 = 10*5;//乘法
console.log(`10*5=${num3}`);
let num4 = 10/5;//除法
console.log(`10/5=${num4}`);

console.log(`10%3=${10%3}`);
console.log(`10**3=${10**3}`);

let vab = 10;
vab = vab+10;//变量加法。
console.log(vab)
vab += 10//简化的变量加法。
console.log(vab)
//减法、乘法、除法写法相同。

let intv1 = 0;
++intv1;//前置递增，给变量加1
console.log(intv1);
let intv2 = 0;
intv2++;//后置递增，给变量加1
console.log(intv2);
let new_intv1 = ++intv1;//先递增再取值
console.log(new_intv1);
let new_intv2 = intv2++;//先取值再递增
console.log(new_intv2);
//递减原理与递加一样