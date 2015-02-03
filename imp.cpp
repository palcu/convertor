#include <cstdio>
#include <cstring>

using namespace std;

const int MAX_LG = 1024*1024*1024,
          MAX_LG_LINE = 1024;

char s[MAX_LG];

int main() {
    FILE * pIn = fopen("grader_test10.in", "r");
    freopen("grader_test10.ok", "w", stdout);

    char line[MAX_LG_LINE];
    while(fgets(line, MAX_LG_LINE, pIn) > 0) {
        strcpy(s + strlen(s), line);
    }

    int state = 0;
    // states
    // 0 - waiting for [
    // 1 - waiting for {
    // 2 - waiting for start "
    // 3 - writing the character and waiting for the end "
    // 4 - waiting for :
    // 5 - waiting for start " or start integer
    // 61 - reading bullshit string
    // 62 - reading bullshit int
    // 8 - waiting for end ,
    // go back to 2 till }
    // 9 - waiting

    int i = 0, n = strlen(s), x;
    bool finishedFile = false;
    while (i < n && !finishedFile) {
        switch (state) {
            case 0:
                if (s[i] == '[') state++;
                break;
            case 1:
                if (s[i] == '{') state++;
                break;
            case 2:
                if (s[i] == '"') state++;
                break;
            case 3:
                if (s[i] == '"') {
                    state++;
                } else {
                    printf("%c", s[i]);
                }
                break;
            case 4:
                if (s[i] == ':') {
                    state++;
                    printf(",");
                }
                break;
            case 5:
                if (s[i] == '"') state = 6;
                if ('0' <= s[i] && s[i] <= '9') {
                    state = 7;
                }
                break;
            case 6:
                if (s[i] == '"') state = 7;
                break;
            case 7:
                if (s[i] == ',') state = 8;
                if (s[i] == '}') finishedFile=true;
                break;
            case 8:
                if (s[i] == '}') finishedFile=true;
                if (s[i] == '"') state = 3;
                break;
        }
        i++;
    }
    printf("\n");

    state = 0; i = 0; finishedFile = false;
    while (i < n && !finishedFile) {
        switch (state) {
            case 0:
                if (s[i] == '[') state++;
                break;
            case 1:
                if (s[i] == '{') state++;
                break;
            case 2:
                if (s[i] == '"') state++;
                break;
            case 3:
                if (s[i] == '"') {
                    state++;
                }
                break;
            case 4:
                if (s[i] == ':') {
                    state++;
                }
                break;
            case 5:
                if (s[i] == '"') state = 6;
                if ('0' <= s[i] && s[i] <= '9') {
                    printf("%c", s[i]);
                    state = 61;
                }
                break;
            case 6:
                if (s[i] == '"') state = 7;
                else {
                    printf("%c", s[i]);
                }
                break;
            case 61:
                if ('0' <= s[i] && s[i] <= '9') {
                    printf("%c", s[i]);
                } else if (s[i] == ',') {
                    state = 8;
                } else if (s[i] == '}') {
                    state = 9;
                } else {
                    // caz "sex": 3143249  , "bla"
                    state = 7;
                }
                break;
            case 7:
                if (s[i] == ',') state++;
                if (s[i] == '}') state = 9;
                break;
            case 8:
                if (s[i] == '}') state++;
                if (s[i] == '"') {
                    printf(",");
                    state = 3;
                }
                break;
            case 9:
                if (s[i] == ']') {
                    finishedFile = true;
                    printf(",\n");
                }
                if (s[i] == '{') {
                    printf(",\n");
                    state = 3;
                }
                break;
        }
        i++;
    }
    return 0;
}
