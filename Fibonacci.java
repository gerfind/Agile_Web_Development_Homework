public class Fibonacci{
    public static int of(int number){
        if ((number ==0)||(number ==1))
            return number;
        else
            return of(number - 1) + of(number -2);
    }
    public static void main(String[] args){
        for( int counter =0; counter <=12; counter++){
            System.out.printf("Fibonacci.of(%d) == %d",counter,Fibonacci.of(counter));
        }
    }
}