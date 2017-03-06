/*
 * =====================================================================================
 *
 *       Filename:  add_by_bit.c
 *
 *    Description:  caculate sum of two numbers, without + - * /
 *
 *        Version:  1.0
 *        Created:  2017年03月05日 17时32分14秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Gestorm Bukn (GB), zhcfreesea@gmail.com
 *        Company:  sina
 *
 * =====================================================================================
 */
#include <stdio.h>

int add(int x, int y)
{
    int one = 1;
    int c = 0;
    int x_bit = 0;
    int y_bit = 0;
    int sum_bit = 0;
    int sum = 0;
    int minus_sign = ~(~0 >> 1);

    while (1) {
        x_bit = x & one ? 1 : 0;
        y_bit = y & one ? 1 : 0;
        sum_bit = x_bit ^ y_bit ^ c ? 1 : 0;
        c = (x_bit & y_bit) || (x_bit & c) || (y_bit & c)  ? 1 :0;
        if (sum_bit)
            sum |= one;
        one <<= 1;
        if (one == 0)
            break;
    }
    return sum;
}

int main(int argc, char *argv[])
{
    int x = atoi(argv[1]);
    int y = atoi(argv[2]);
    printf("%d, %d\n", add(x, y), x + y);
    return 0;
}
