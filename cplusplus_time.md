## cplusplus time.h

Types
----
```cpp
clock_t // Alias of a fundamental arithmetic type capable of representing clock tick counts, CLOCKS_PER_SEC

time_t // Alias of a fundamental arithmetic type capable of representing times, as those returned by function time.

struct tm {
    int tm_sec;     // Seconds (0, 60)
    int tm_min;     // Minutes (0, 59)
    int tm_hour;    // Hours (0, 23)
    int tm_mday;    // Day of the month (1, 31)
    int tm_mon;     // Month (0, 11)
    int tm_year;    // Year - 1900
    int tm_wday;    // Day of the week (0-6, Sunday=0)
    int tm_yday;    // Day in the year (0-365, 1 Jan = 0)
    int tm_isdst;   // Daylight saving time
};
```

Relative function
----
```cpp
char* asctime(const struct tm *tm);
char* ctime(const time_t *timep);

struct tm* gmtime(const time_t *timep);
struct tm* localtime(const time_t *timep);

time_t mktime(struct tm *tm);
time_t time(time_t *timer);// Get current calendar time as value of type time_t
clock_t clock(void);    // Return the processor time consumed by the program
```

Examples
----
Print current localtime
```cpp
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    time_t rawtime;
    struct tm *timeinfo;
    time(&rawtime);     // same as rawtime = time(NULL);
    timeinfo = localtime(rawtime);
    printf("Current time and date: %s\n", asctime(timeinfo));
}
```

Calculate program calculating time
```cpp
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int frequency_of_primers(int);

int main() {
    int f;
    clock_t t;
    t = clock();
    printf("Calculating ...\n");
    f = frequency_of_primers(99999);
    printf("The number of primes lower than 100,000 is: %d\n",f);
    t = clock() - t;
    printf("It took me %d clicks(%f seconds).\n", t,((float)t)/CLOCKS_PER_SEC);
    return 0;
}

int frequency_of_primers(int n) {
    int freq = n - 1;
    for (int i = 2; i <= n; i++) {
        for (int j = sqrt(i); j > 1; j--) {
            if (i%j == 0) {
                --freq; break;
            }
        }
    }
    return freq;
}
```