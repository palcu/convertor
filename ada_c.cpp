// Sursa Adei cu citire din stdio
// Scrierea e tot cu stdio
#include <fstream>
#include <string>
#include <cstdio>

using namespace std;

int main() {
    ofstream g;
    FILE * pIn = fopen("convertor.in", "r");
    FILE * pOut = fopen("convertor.out", "w");

    g.open("convertor.out");

    // identificare chei
    char c;
    string buffer;
    int pos;
    int state = 0;
    while ((c = fgetc(pIn)) && c != EOF && (c!='}')) {
        if ((c == '[') && (state == 0))
            state = 1;
        else if ((c == '{') && (state == 1))
            state = 2;
        else if ((c == '\"') && (state == 2))
            state = 3;
        else if ((c == '\"') && (state == 3)) {
            state = 2;
            fputs(buffer.c_str(), pOut);
            fputc(',', pOut);
            // g << buffer << ",";
            buffer = "";
        } else if ((c == ':') && (state == 2))
            state = 4;
        else if ((c == ',') && (state == 4))
            state = 2;
        else if (state == 3)
            buffer += c;
    }
    fputc('\n', pOut);
    // g<<"\n";
    fseek(pIn, 0, SEEK_END);
    rewind(pIn);
    state = 0;
    while ((c = fgetc(pIn)) && c != EOF && (c!=']')) {
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
            fputs(buffer.c_str(), pOut);
            fputc(',', pOut);
            // g << buffer << ",";
            buffer = "";
        } else if ((c == '}') && (state == 4)) {
            state = 1;
            fputs(buffer.c_str(), pOut);
            fputc(',', pOut);
            // g << buffer << ",";
            buffer = "";
        } else if ((c == '}') && (state = 2))
            state = 1;
        else if ((c == ',') && (state = 1))
            // g << "\n";
            fputc('\n', pOut);
        else if (state == 5)
            buffer += c;
        else if ((isdigit(c)) && (state == 4))
            buffer += c;
    }
    return 0;
}
