/**
 * Created by patrick on 14.01.16.
 */
public class Decode{
    private static String key="chaostreffosnabrueck";
    private static String alphabet="abcdefghijklmnopqrstuvwxyz";
    private static int aktKeyChar=0;
    /*
    	MainMethod
    	Give the decode string as Parameter
    */
    public static void main(String[] args){
        if(args.length!=1){
            System.out.println("Falsche Parameter!");
            return;
        }
        String message=args[0];
        for(int i=0;i<message.length();i++){
			//iterate threw given string
            System.out.print(decode(message.charAt(i)));
        }
        System.out.println();
    }
    public static char decode(char x){
        if(alphabet.matches(".*?"+x+".*?")){
            int move=key.charAt(aktKeyChar)-'a';
            //decode char
            int number=(x-move);
            //check if range is correct
            if(number<97)
                number+=26;
            x = (char)number;
            aktKeyChar++;
            //move key forward
            if (aktKeyChar >= key.length())
                aktKeyChar = 0;
        }
        return x;
    }
}

