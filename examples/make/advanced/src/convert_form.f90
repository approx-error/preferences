module convert_form 
  
  use kinds
  use parameters

  implicit none

  public

  contains

    subroutine cart_to_pol(complex_num, modulus, argument)
      implicit none
      complex(r64), intent(in) :: complex_num
      real(r64), intent(out) :: modulus, argument

      modulus = sqrt(complex_num%re**2 + complex_num%im**2)
      argument = atan2(complex_num%im, complex_num%re)
    end subroutine cart_to_pol

    subroutine pol_to_cart(modulus, argument, complex_num)
      implicit none
      real(r64), intent(in) :: modulus, argument
      complex(r64), intent(out) :: complex_num

      complex_num = modulus * exp(IMAG * argument)
    end subroutine pol_to_cart
end module convert_form
