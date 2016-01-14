
public class ViginereEncrypt {
	
	private static final String KEY = "chaostreffosnabrueck";
	
	public static String encrypt(String text) {
		text = text.toLowerCase();
		
		String result = "";
		int keyPos = 0;
		int asciiStart = ((int) 'a');
		int asciiLength = ((int) 'z') - asciiStart + 1;
		for (char c : text.toCharArray()) {
			if (c >= asciiStart && c < asciiStart + asciiLength) {
				result += (char) (((((int) c - asciiStart) + ((int) Main.key.charAt(keyPos) - asciiStart)) % asciiLength) + asciiStart);
				keyPos = (keyPos + 1) % KEY.length();
			} else {
				result += c;
			}
		}
		return result;
	}
		
	public static void main(String[] args) {
		if (args.length == 0) {
			System.out.println("Es wurde kein Klartext angegeben!");
		} else {
			System.out.println(encrypt(args[0]));
		}
	}
}
