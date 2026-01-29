program calculate
  use kinds
  use parameters
  use convert_form

  implicit none

  complex(r64) :: num1 = IMAG
  complex(r64) :: num2 = cmplx(sqrt(2.0_r64), sqrt(2.0_r64),r64)
  real(r64) :: mod3 = 5
  real(r64) :: arg3 = PI/2

  real(r64) :: mod1, arg1, mod2, arg2
  complex(r64) :: num3


  call cart_to_pol(num1, mod1, arg1)
  call cart_to_pol(num2, mod2, arg2)

  call pol_to_cart(mod3, arg3, num3)

  print '(a)', 'num1:'
  print complex_fmt, num1
  print '(a)', 'num1 in polar form:'
  print '(f10.6,1x,"*",1x,"exp(i*",f10.6,")")', mod1, arg1
  print *
  print '(a)', 'num2:'
  print complex_fmt, num2
  print '(a)', 'num2 in polar form:'
  print '(f10.6,1x,"*",1x,"exp(i*",f10.6,")")', mod2, arg2
  print *
  print '(a)', 'num3 in polar form:'
  print '(f10.6,1x,"*",1x,"exp(i*",f10.6,")")', mod3, arg2
  print '(a)', 'num3 in cartesian form:'
  print complex_fmt, num3

  

end program calculate
