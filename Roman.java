
import java.util.*;
import java.lang.String;


/**
 *
 * @author DELL
 */
public class Roman {

    static int roman(String s) {
        Map<Character, Integer> rom = new HashMap<>();
        rom.put('I', 1);
        rom.put('V', 5);
        rom.put('X', 10);
        rom.put('L', 50);
        rom.put('C', 100);
        rom.put('D', 500);
        rom.put('M', 1000);

        int n = s.length();
        int num = rom.get(s.charAt(n - 1));

        for (int i = n - 2; i >= 0; i--) {
            // Check if the character at right of current character is
            // bigger or smaller
            if (rom.get(s.charAt(i)) >= rom.get(s.charAt(i + 1))) {
                num += rom.get(s.charAt(i));
            } else {
                num -= rom.get(s.charAt(i));
            }
        }

        return num;

    }

    public static void main(String args[]) {
        // TODO code application logic here

        Scanner in = new Scanner(System.in);

        System.out.print("Enter roman number: ");
        String s = in.nextLine();
        
        
        roman(String s);

    }
}
