#include "inc/return-codes.h"
#include "inc/funcs.h"
#include "inc/test.h"

int main() {
  Status test_result = test_function(&safe_log);
  Status passed = test_passed(test_result);

  test_result = test_function(&safe_sqrt);
  passed = test_passed(test_result);

  return passed;
}
