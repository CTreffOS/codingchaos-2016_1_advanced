import java.lang.*;

public class timing
{

    public static void main(String[] args)
    {

        char[] c = new String("ABCDEFGHIJKLMNOPQRSTUVWXYZ").toCharArray();
        String pass = "";
        int pchars = 1;
        int i = 0;
        
        while (true) {
            String npass = pass + c[i];
            int chars = 0;
            Process p = null; 
            try {
                p = Runtime.getRuntime().exec("./crypto " + npass);
            } catch (Exception ex) { }
            boolean running = true;
            while (running) {
                try {
                    int ret = p.exitValue();
                    if (ret == 0) {
                        return;
                    } else if (ret == 1) {
                        if (chars > pchars) {
                            System.out.println(npass);
                            pass = npass;
                            pchars = chars;
                            i = -1;
                        }
                    } else {
                        System.out.println("Nicht gefunden!");
                        return;
                    }
                    running = false;
                } catch (Exception ex2) {
                    chars++;
                    try {
                        Thread.sleep(100);
                    } catch (Exception ex) { }
                }
            }
            i++;
        }
        
    }

}
