public class Main
{
    private static int x;
	public static void main(String[] args) {
		System.out.println(fun());
	}
	static int fun(){
	    return x++;
	}

}