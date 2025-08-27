int value(char a) {
    switch (a) {
        case 'I': return 1;
        case 'V': return 5;
        case 'X': return 10;
        case 'L': return 50;
        case 'C': return 100;
        case 'D': return 500;
        case 'M': return 1000;
        default: return 0;
    }
}

int romanToInt(char* s) {
    int i, b1, b2, c = 0;
    int d = strlen(s);

    for (i = 0; i < d; i++) {
        b1 = value(s[i]);

        if (i + 1 < d) {
            b2 = value(s[i + 1]);

            if (b1 >= b2) {
                c += b1;
            } else {
                c += b2 - b1;
                i++; // Skip the next character
            }
        } else {
            c += b1;
        }
    }

    return c;
}