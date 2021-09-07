package Java_Kwdg;

//变量记录的值可以在运行过程中进行改变。
/*Java基本数据类型：
|类型   |关键字              |内存占用/字节    |取值范围
整数    byte                 1                -128~127
       short                2                -32768~32767
       int（默认）           4                -2³¹~2³¹-1
       long                 8                -2⁶³~2⁶³-1
浮点数  float（单精度）       4                -1.401298e-45~3.402823e+38
       double（双精度，默认） 8                4.9000000e-324~1.797693e+308
字符    char                 2                0-65535
布尔    boolean              1                true/false
*/

public class class4 {
    public static void main(String[] args) {
        //变量定义格式：数据类型 变量名 = 值
        byte num1 = 3;
        //使用变量例
        System.out.println(num1);
        num1 = 5;//修改变量值，不用写数据类型
        System.out.println(num1);

        //注意事项：
        //·变量名不允许被重复定义
        //·同一条语句内定义多个变量要用逗号隔开
        //注：Java用分号来作为一条语句的结束标志
        char cr1 = 'a', cr2 = '我';
        System.out.println(cr1);
        System.out.println(cr2);
        //·使用变量前一定要赋值
        //·定义float和long的注意事项：
            //定义浮点数变量（float/double）时要在数据末尾添加f或F
        float fot1 = 12.3f, fot2 = 38.1F;
        System.out.println(fot1);
        System.out.println(fot2);
            //定义long变量时要在数据末尾添加l或L
        long lg1 = 184628984792034l, lg2 = 3132467L;
        System.out.println(lg1);
        System.out.println(lg2);
        //·变量的作用域范围
            //变量只在它定义时所在的大括号内有效
        {
            //当这个大括号执行完毕后，变量数据会消失
            int it1 = 33;
            System.out.println(it1);
        }
    //这里不能用变量it1
    }
}