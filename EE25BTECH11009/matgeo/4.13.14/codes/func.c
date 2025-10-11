
#include <stdio.h>
void compute_bisector(double *P, double *Q, double *results)
{
    // Step 1: Midpoint M = (P + Q) / 2
    double Mx = (P[0] + Q[0]) / 2.0;
    double My = (P[1] + Q[1]) / 2.0;

    // Step 2: Direction vector of PQ
    double a = Q[0] - P[0];  // Δx
    double b = Q[1] - P[1];  // Δy

    // Step 3: Equation of bisector → a*x + b*y = c
    double c = a * Mx + b * My;

    // Store results
    results[0] = a;  // a
    results[1] = b;  // b
    results[2] = c;  // c

    // Step 4: Compute slope (m) and y-intercept
    if (b != 0) {
        results[3] = -a / b;   // slope
        results[4] = c / b;    // intercept
    } else {
        // Vertical line case
        results[3] = 1e9;  // Use a large value to represent infinity
        results[4] = 0;
    }
}

