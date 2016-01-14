import java.io.IOException;


public class TimingAttack {

	public static String guessPassword() throws IOException {
		StringBuilder guessedPassword = new StringBuilder(String.valueOf((char) 1));
		long lastTimeDiff = -1;
		int currCharIdx = 0;
		while (true) {
			
			long start = System.currentTimeMillis();
			Process p = new ProcessBuilder("./crypto", guessedPassword.toString()).start();
			try {
				p.waitFor();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			int exitValue = p.exitValue();
			long diff = System.currentTimeMillis() - start;
			
			boolean newCharCorrect = lastTimeDiff != -1 && Math.abs(diff - lastTimeDiff) > 90;
			if (newCharCorrect) System.out.println(guessedPassword.toString());
			switch (exitValue) {
			case 0:	return guessedPassword.toString();
			case 2: 
				guessedPassword = guessedPassword.deleteCharAt(guessedPassword.length() - 1);
				currCharIdx = 0;
				break;
			}
			
			if (newCharCorrect) {currCharIdx++;}
			if (guessedPassword.length() <= currCharIdx) guessedPassword.append(((char) 1));
			guessedPassword.replace(currCharIdx, currCharIdx + 1, String.valueOf((char) (guessedPassword.charAt(currCharIdx) + 1 % Character.MAX_VALUE)));
			lastTimeDiff = diff;
		}
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		try {
			guessPassword();
			System.out.println("Passwort gefunden");
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
