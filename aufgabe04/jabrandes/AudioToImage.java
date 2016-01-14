import java.awt.Color;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.TreeSet;


public class AudioToImage {
	
	private static final Color WAVE_COLOR = new Color(255, 0, 0);

	
	public static void makeImage(String audioPath, String outPath) throws IOException {
		File audioFile = new File(audioPath);
		long samples = audioFile.length() / 2;
		TreeSet<Integer>[] samplesData = new TreeSet[255];
		InputStream stream = new FileInputStream(outPath);
		
		int in = -1;
		int allSampleNum = 0;
		double pixelHeightRatio = 255.0 / Math.pow(2, 17);
		double sampleWidthRatio = 1000.0 / (double) samples;
		int maxValue = 1;
		while ((in = stream.read()) != -1) {
			in = in + stream.read() << 8;
			
			int x = (int) (((double) allSampleNum) * sampleWidthRatio);
			if (in > maxValue) maxValue = in;
			int index = (int) (pixelHeightRatio * (double) in);
			if (samplesData[index] ==  null) samplesData[index] = new TreeSet<Integer>();
			samplesData[index].add(x);
			
			allSampleNum++;
		}
		
		BufferedWriter out = new BufferedWriter(new FileWriter(audioPath + "_img.pbm"));
		
		
		out.write("P1 1000 255 ");
		for (int j = 0; j < 255; j++) {
			TreeSet<Integer> row = samplesData[j];
			int ctr = 0;
			for (int i = 0; i < 1000; i++) {
				if (row != null && row.contains(ctr)) {
					out.write("1 ");
				} else {
					out.write("0 ");
				}
				ctr++;
			}
		}
		
		System.out.println("Fertig!");
		
		stream.close();
		out.close();
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		try {
			makeImage(args[0], args[1]);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
