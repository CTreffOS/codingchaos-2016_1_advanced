public class Common
{

	private static String key = "chaostreffosnabrueck";
	private static String al = "abcdefghijklmnopqrstuvwxyz";

	public static char[] getkey()
	{

		return key.toCharArray();

	}

	public static char[] getal()
	{

		return al.toCharArray();

	}

	public static int getindex(char c)
	{

		for (int i = 0; i < getal().length; i++) {
			if (getal()[i] == c) {
				return i;
			}
		}
		return -1;

	}

}
