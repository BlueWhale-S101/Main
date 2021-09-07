package Java_Kwdg;

//导入程序包
import java.util.Scanner;

public class class5 {
    //实现键盘输入值
    public static void main(String[] args) {
        //创建对象
        Scanner inpt = new Scanner(System.in);
        //使用变量接受数据
        int num = inpt.nextInt();
        System.out.println("Input number: " + num);
    }
}