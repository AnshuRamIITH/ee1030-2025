// func.c
#include <stdio.h>

void find_plane(double *out) {
    // Given normals and constants
    double n1[3] = {1, 2, 3};
    double n2[3] = {2, 1, -1};
    double n3[3] = {5, 3, -6};
    double c1 = -4, c2 = 5;  // constants from first two planes

    // Compute λ
    double num = 7.0;
    double den = 19.0;
    double lambda = num / den;

    // Compute normal of required plane
    double n[3];
    n[0] = n1[0] + lambda * n2[0];
    n[1] = n1[1] + lambda * n2[1];
    n[2] = n1[2] + lambda * n2[2];

    // Compute constant term
    double d = c1 + lambda * c2;

    // Store result: [n_x, n_y, n_z, d]
    out[0] = n[0];
    out[1] = n[1];
    out[2] = n[2];
    out[3] = d;
}
