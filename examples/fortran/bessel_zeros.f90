program bessel_zeros
  implicit none
  ! This program calculates the zeros of a given Bessel function of the first kind (J_n(x)) by using Newton's method

  ! Using 16 byte integers and floats:
  integer, parameter :: ik16 = selected_int_kind(19) ! -1.70e38 to 1.70e38
  integer, parameter :: rk16 = selected_real_kind(20,100) ! -1.18e4932 to 1.18e4932 

  ! User input variables
  integer :: order
  real (kind = rk16) :: initial_guess

  ! Error handling variables
  logical :: validated = .false.
  integer :: input_error
  character(len = 100) :: error_message

  print '(a)', 'This program will try to find a zero of any integer order bessel function of the first kind given an initial guess'
  print '(a,2/)', 'by using Halleys method (Second order Newtons method)'

  ! Ask the user for an integer to be used as the Bessel function order:
  do while (.not. validated)
    write(*, '(a)', advance = 'no') 'Input preferred order of bessel J_n(x) function (integer) and initial guess for a root (real): '
    read(*, *, iostat = input_error, iomsg = error_message) order, initial_guess
    if (input_error == 0) then
      validated = .true.
    else
      print '(a)', 'Invalid input!'
      print '(a,x,a)', 'Error message:', trim(error_message)   
    end if

    
  end do

  print '(a,x,i0,x,a)', 'Using integer', order, 'as the order of the bessel function'
  print '(a,x,f6.3,x,a,2/)', 'and', initial_guess, 'as the initial guess for a root'

  print '(a,x,f15.12)', 'Root near initial guess:', halleys_method(order, initial_guess)
  contains

    ! Maclaurin series of J_n(x) up to 100 terms
    real (kind = rk16) pure function bessel_first_kind(order, input) 
      implicit none

      ! Input variables
      integer, intent(in) :: order 
      real (kind = rk16), intent(in) :: input

      ! Iteration variables
      integer :: i
      integer, parameter :: ITERATION_COUNT = 100 

      ! Auxiliary variable declarations 
      real (kind = rk16) :: coeff
      real (kind = rk16) :: x_term
      real (kind = rk16) :: current_value

      ! Assigning values to auxiliary variables
      coeff = 0.0
      x_term = 0.0
      current_value = 0.0
      
      ! Summing the first ITERATION_COUNT terms
      do i = 0, ITERATION_COUNT
        coeff = (-1_ik16)**i / (gamma(i + 1.0_rk16) * gamma(i + order + 1.0_rk16))
        x_term = (input / 2_ik16) ** (2_ik16 * i + order)
        current_value = current_value + (coeff * x_term)
      end do

      bessel_first_kind = current_value
    end function bessel_first_kind

    ! d/dx(J_n(x)) using a recurrence relation
    real (kind = rk16) pure function bessel_first_derivative(order, input)
      implicit none
      ! Input variables
      integer, intent(in) :: order
      real (kind = rk16), intent(in) :: input
      
      if (order == 0) then
        bessel_first_derivative = -bessel_first_kind(1, input)
      else
        bessel_first_derivative = 0.5_rk16 * (bessel_first_kind(order - 1, input) - bessel_first_kind(order + 1, input))
      end if
    end function bessel_first_derivative

    ! d^2/dx^2(J_n(x)) using recurrence relation
    real (kind = rk16) pure function bessel_second_derivative(order, input)
      implicit none
      ! Input variables
      integer, intent(in) :: order
      real (kind = rk16), intent(in) :: input

      if (order == 0) then
        bessel_second_derivative = 0.5_rk16 * (-bessel_first_kind(0, input) + bessel_first_kind(2, input))
      else if (order == 1) then
        bessel_second_derivative = 0.25_rk16 * (-3_ik16 * bessel_first_kind(1, input) + bessel_first_kind(3, input))
      else
        bessel_second_derivative = 0.25_rk16 * (bessel_first_kind(order - 2, input) - 2_ik16 * bessel_first_kind(order, input) + &
        bessel_first_kind(order + 2, input))
      end if  
  
    end function bessel_second_derivative

    ! Hallyes's method function
    real (kind = rk16) pure function halleys_method(bessel_order, init_guess)

      ! Input variables
      integer, intent(in) :: bessel_order
      real (kind = rk16), intent(in) :: init_guess

      ! Iteration variables and constants
      integer :: i
      integer,parameter :: MAX_ITERATIONS = 10000
      integer,parameter :: SAMPLE_FREQUENCY = 5
      real (kind = rk16),parameter :: ITERATION_TOLERANCE = 10e-12

      ! Auxiliary variables
      real (kind = rk16) :: sample
      real (kind = rk16) :: current_value
      real (kind = rk16) :: func_value
      real (kind = rk16) :: first_derivative_value
      real (kind = rk16) :: second_derivative_value
      real (kind = rk16) :: numerator
      real (kind = rk16) :: denominator
      
      current_value = init_guess
      sample = init_guess

      ! Iterating
      do i = 0, MAX_ITERATIONS
        func_value = bessel_first_kind(bessel_order, current_value)
        first_derivative_value = bessel_first_derivative(bessel_order, current_value)
        second_derivative_value = bessel_second_derivative(bessel_order, current_value)

        numerator = 2_ik16 * func_value * first_derivative_value
        denominator = 2_ik16 * (first_derivative_value ** 2) - (func_value * second_derivative_value)

        current_value = current_value - (numerator / denominator)
        if (modulo(i, SAMPLE_FREQUENCY) == 0) then
          if (current_value - sample <= ITERATION_TOLERANCE) then
            exit
          else
            sample = current_value
          end if
        end if
      end do
      
      halleys_method = current_value
        
    end function halleys_method  
end program bessel_zeros
  
