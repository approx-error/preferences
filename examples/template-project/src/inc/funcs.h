#ifndef FUNCS_H
#define FUNCS_H

#include "return-codes.h"

// Typedef to make using function pointers easier
typedef float SafeOperation(float input, Status *exit_status);

// Interfaces
float safe_log(float input, Status *exit_status);
float safe_sqrt(float input, Status *exit_status);

#endif
