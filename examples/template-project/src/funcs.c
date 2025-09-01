#include <math.h>
#include "inc/return-codes.h"

float safe_log(float input, Status *exit_status) {
  if (input < 0 || input == NAN) {
    *exit_status = ERR_INVALID_ARG;
    return NAN;
  } else if (input == 0) {
    *exit_status = ERR_DIVERGES;
    return -INFINITY;
  }

  *exit_status = SUCCESS;
  return logf(input);
}

float safe_sqrt(float input, Status *exit_status) {
  if (input < 0) {
    *exit_status = ERR_INVALID_ARG;
    return NAN;
  }

  *exit_status = SUCCESS;
  return sqrtf(input);
}

