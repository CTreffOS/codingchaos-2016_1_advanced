import java.io.*;
import java.nio.*;
import java.nio.file.*;

public class audio
{

    public static void main(String[] args)
    {

        if (args.length != 2) {
            System.out.println("Falsche Argumente!");
        }
        
        byte[] data = null;
        try {
            data = Files.readAllBytes(Paths.get(args[0]));
        } catch (Exception ex) {
            return;
        }
        byte[] px = new byte[1000];
        int step = data.length / 2 / px.length;
        ByteBuffer bb = ByteBuffer.wrap(data);
        bb.order(ByteOrder.LITTLE_ENDIAN);
        
        for (int p = 0; p < px.length; p++) {
            int sum = 0;
            for (int i = 0; i < step; i++) {
                short val = bb.getShort();
                if (val < 0) {
                    val *= -1;
                }
                sum += val;
            }
            sum /= step;
            double cpx = ((double)sum / (double)Short.MAX_VALUE);
            if (cpx > 1) {
                cpx = 1;
            }
            px[p] = (byte)(cpx * 255.0);
        }
    
        PrintWriter writer;
        try { 
            writer = new PrintWriter(args[1], "ASCII");
        } catch (Exception ex) {
            return;
        }
        writer.println("P1 1000 255 ");
        for (int y = 127; y >= 0; y--) {
            for (int x = 0; x < 1000; x++) {
                writer.println((px[x] >= y) ? "1 " : "0 ");
            }
        }
        for (int y = 0; y <= 127; y++) {
            for (int x = 0; x < 1000; x++) {
                writer.println((px[x] >= y) ? "1 " : "0 ");
            }
        }
        writer.close();

    }

}