module parameters
  use kinds

  implicit none

  ! Numerical parameters
  real(r64), parameter, public :: PI = 4.0_r64 * atan2(1.0_r64, 1.0_r64)
  complex(r64), parameter, public :: IMAG = (0,1) ! imaginary unit i 

  ! String parameters
  character(*), parameter, public :: complex_fmt = '(f10.6,sp,f10.6,"*i")'

end module parameters

