package Java_Kwdg;
public class class6 {
    //数据类型转换
    public static void main(String[] args) {
        //隐式转换：数据类型取值小的给取值大的赋值，可以直接赋值
        //小数取值范围一律比整数大
        byte num1 = 10;//4个字节
        double num2 = num1;//8个字节
        System.out.println(num2);//不是10，是10.0
        int n1 = 5;
        double n2 = n1 - 1.3;//程序会先做隐式转换再运算
        System.out.println(n2);
        //byte、short、char都会先提升到int再计算，接收至少用int
    };
};