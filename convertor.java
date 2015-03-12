// Source by Ada Solcan
// http://www.infoarena.ro/job_detail/1360382
// Java was expected to get only 70 points because it is sloooooooooooow

import java.io.*;
import java.util.*;
import java.lang.*;

public class Main {
  public static void main(String args[]) throws IOException {
    FileInputStream f = new FileInputStream("convertor.in");
    FileWriter g = new FileWriter("convertor.out");

    char c = '\0';
    int pos;
    int state = 0;
    String buffer = "";
    while ((f.available() > 0) && (c!='}')) {
        c = (char)f.read();
        if ((c == '[') && (state == 0))
            state = 1;
        else if ((c == '{') && (state == 1))
            state = 2;
        else if ((c == '\"') && (state == 2))
            state = 3;
        else if ((c == '\"') && (state == 3)) {
            state = 2;
            g.write(buffer);
            buffer = "";
            g.write(",");
        } else if ((c == ':') && (state == 2))
            state = 4;
        else if ((c == ',') && (state == 4))
            state = 2;
        else if (state == 3)
            buffer+=c;
    }
    g.write("\n");
    f.close();

    f = new FileInputStream("convertor.in");
    state = 0;
    while ((f.available() > 0) && (c!=']')) {
        c = (char)f.read();
        if ((c == '[') && (state == 0))
            state = 1;
        else if ((c == '{') && (state == 1))
            state = 2;
        else if ((c == '\"') && (state == 2))
            state = 3;
        else if ((c == '\"') && (state == 3))
            state = 2;
        else if ((c == ':') && (state == 2))
            state = 4;
        else if ((c == '\"') && (state == 4))
            state = 5;
        else if ((c == '\"') && (state == 5))
            state = 4;
        else if ((c == ',') && (state == 4)) {
            state = 2;
            g.write(buffer);
            buffer = "";
            g.write(",");
        } else if ((c == '}') && (state == 4)) {
            state = 1;
            g.write(buffer);
            buffer = "";
            g.write(",");
        } else if ((c == '}') && (state == 2))
            state = 1;
        else if ((c == ',') && (state == 1))
            g.write("\n");
        else if (state == 5)
            buffer+=c;
        else if ((Character.isDigit(c)) && (state == 4))
            buffer+=c;
        }
        f.close();
        g.close();
    }
}
