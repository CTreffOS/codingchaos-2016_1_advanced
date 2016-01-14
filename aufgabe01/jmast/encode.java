public class encode
{

	public static void main(String[] args)
	{

		if (args.length != 1) {
			System.out.println("Falsche Parameter!");
			return;
		}

		System.out.println(encrypt(args[0]));

	}

	private static String encrypt(String text) {

		char[] ctext = text.toCharArray();
		for (int i = 0; i < ctext.length; i++) {
			char keychar = Common.getkey()[i % Common.getkey().length];
			int index = Common.getindex(ctext[i]);
			if (index != -1) {
				int index2 = Common.getindex(keychar);
				ctext[i] = Common.getal()[(index + index2) % Common.getal().length];
			}
		}
		return new String(ctext);

	}

}
