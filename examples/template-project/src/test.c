#include <stdio.h>
#include "inc/return-codes.h"
#include "inc/funcs.h"

static char *status_to_msg(Status status) {
  switch (status) {
    case SUCCESS:
      return "success";
    case ERR_INVALID_ARG:
      return "invalid argument";
    case ERR_DIVERGES:
      return "output diverges";
    default:
      return "invalid status";
  }
}

static Status test_log() {
  printf("testing function safe_log:\n");
  float inputs[] = {-1.1, -0.5, 0, 0.5, 1.1};
  Status expected_status[] = {ERR_INVALID_ARG, ERR_INVALID_ARG, ERR_DIVERGES, SUCCESS, SUCCESS};
  Status status;
  for (int i = 0; i < 5; i++) {
    float res = safe_log(inputs[i], &status);
    printf("input %d: %.1f -> expected status: %s\n", i+1, inputs[i], status_to_msg(expected_status[i]));
    printf("result %d: %.5f -> resulting status: %s\n", i+1, res, status_to_msg(status));
    if (expected_status[i] != status) {
      return TEST_FAIL;
    }
  }
  return SUCCESS;
}

static Status test_sqrt() {
  printf("testing function safe_sqrt:\n");
  float inputs[] = {-1.1, -0.5, 0, 0.5, 1.1};
  Status expected_status[] = {ERR_INVALID_ARG, ERR_INVALID_ARG, SUCCESS, SUCCESS, SUCCESS};
  Status status;
  for (int i = 0; i < 5; i++) {
    float res = safe_sqrt(inputs[i], &status);
    printf("input %d: %1.1f -> expected status: %s\n", i+1, inputs[i], status_to_msg(expected_status[i]));
    printf("result %d: %1.5f -> resulting status: %s\n", i+1, res, status_to_msg(status));
    if (expected_status[i] != status) {
      return TEST_FAIL;
    }
  }
  return SUCCESS;
}

Status test_function(SafeOperation *function) {
  if (function == &safe_log) {
    return test_log();
  } else if (function == &safe_sqrt) {
    return test_sqrt();
  } else {
    return INVALID_FUNCTION; 
  }
}

Status test_passed(Status test_status) {
  if (test_status == SUCCESS) {
    printf("All tests passed!\n");
    return SUCCESS;
  } else {
    printf("Test(s) failed\n");
    return TEST_FAIL;
  }
}
