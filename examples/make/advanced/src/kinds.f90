module kinds
  implicit none

  ! Kind parameters for 8, 16, 32, 64 and 128 bit ints
  integer, parameter, public :: i8 = selected_int_kind(0)
  integer, parameter, public :: i16 = selected_int_kind(3)
  integer, parameter, public :: i32 = selected_int_kind(6)
  integer, parameter, public :: i64 = selected_int_kind(10)
  integer, parameter, public :: i128 = selected_int_kind(19)
  ! Kind parameter for double precision floats
  integer, parameter, public :: r64 = selected_real_kind(14, 100)
end module kinds
