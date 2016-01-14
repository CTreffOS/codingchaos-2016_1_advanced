import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.Scanner;



public class GitHubRepositories {

	private static final String TOKEN = "61b4f2b140d03dc7403c51fe601fc81171b74909";
	
	public static String getPullRequestsOf(String owner, String repoId) {
		String result = "";
		try {
			HttpURLConnection con = (HttpURLConnection) new URL("https://api.github.com/repos/" + owner + "/" + repoId + "/pulls?state=open").openConnection();
			con.addRequestProperty("Authorization", "token " + TOKEN);
			
			Scanner sc = new Scanner(con.getInputStream());
//			sc.useDelimiter("\\A");
//			System.out.println(sc.next());
			
			while (sc.findWithinHorizon("\"number\":", 0) != null); {
				
				String id = sc.findWithinHorizon("\\d+", 0);
				
				sc.findWithinHorizon("\"user\":", 0);
				sc.findWithinHorizon("\"login\":", 0);
				String user = sc.findWithinHorizon("\"[^\"]*\"", 0);
				
				sc.findWithinHorizon("\"body\":", 0);
				String commitMsg = sc.findWithinHorizon("\"[^\"]*\"", 0);
				
				result += id + "  " + user + " " + commitMsg + "\n";
				System.out.println(result);
			}
			
			
			
			
		} catch (MalformedURLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return result;
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		System.out.println(getPullRequestsOf(args[0], args[1]));
	}

}
