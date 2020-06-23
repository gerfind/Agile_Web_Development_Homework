public class FizzBuzz{
    int number=0;
    public static boolean fizz(int self){
        if(self%3==0)
            return true;
        else
            return false;
    }
    public static boolean buzz(int self){
        if(self%5==0)
            return true;
        else
            return false;
    }
    public static void main(String[] args){
        for(int number=0;number<100;number++){
            if(FizzBuzz.fizz(number)==true)
                System.out.print("Fizz ");
            if(FizzBuzz.buzz(number)==true)
                System.out.print("Buzz ");
            System.out.println(number);
        }
    }
}