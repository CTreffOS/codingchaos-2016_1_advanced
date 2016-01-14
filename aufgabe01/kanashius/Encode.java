/**
 * Created by patrick on 14.01.16.
 */
public class Encode{
    private static String key="chaostreffosnabrueck";
    private static String alphabet="abcdefghijklmnopqrstuvwxyz";
    private static int aktKeyChar=0;
    /*
    	MainMethod
    	Give the encode string as Parameter
    */
    public static void main(String[] args){
        if(args.length!=1){
            System.out.println("Falsche Parameter!");
            return;
        }
        String message=args[0];
        for(int i=0;i<message.length();i++){
        	//iterate threw given string
            System.out.print(encode(message.charAt(i)));
        }
        System.out.println();
    }
    public static char encode(char x){
    	//if char is in alphabet
        if(alphabet.matches(".*?"+x+".*?")){
            int move=key.charAt(aktKeyChar)-'a';
            //encode char
            int number=(x+move);
            //check if range is correct
            if(number>122)
                number-=26;
            x = (char)number;
            aktKeyChar++;
            //move key forward
            if (aktKeyChar >= key.length())
                aktKeyChar = 0;
        }
        return x;
    }
}

