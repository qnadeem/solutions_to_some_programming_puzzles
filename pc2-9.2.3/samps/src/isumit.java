import java.io.*;

//
// File:    isumit.java
// Purpose: to sum the integers from stdin
// Author:  pc2@ecs.csus.edu or http://www.ecs.csus.edu/pc2
// 
// Thu Oct  2 20:25:28 PDT 2003
// 
// $Id: isumit.java 1962 2009-11-25 03:42:12Z boudreat $
//

public class isumit {
    public static void main(String[] args) 
    {
	try
	{	
		BufferedReader br = new BufferedReader (
			new InputStreamReader (System.in), 1);
		
		String line;
		int sum = 0;
		int rv = 0;
		while((line = br.readLine()) != null) 
		{			
			rv = new Integer(line.trim()).intValue();
			if (rv > 0)
				sum = sum + rv;
			// System.out.println(line);
		}
		System.out.print("The sum of the integers is ");
		System.out.println(sum);
	}
	catch(Exception e)
	{
		System.out.println("Possible trouble reading sumit.dat");
		System.out.println("Message: "+ e.getMessage());
	}			
    }
}

// eof isumit.java $Id: isumit.java 1962 2009-11-25 03:42:12Z boudreat $
