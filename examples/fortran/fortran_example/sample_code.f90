program input_validation
  ! Ask the user for an integer until they provide one    
  ! Importing modules
  use sample_kinds
  use sample_module
 
  implicit none
 
  ! Validation parameter
  logical :: validated = .false.

  ! Input stored here
  integer(kind = ik) :: input1, input2

  ! Error handling variables
  integer :: read_status
  character(len = 80) :: read_message

  ! Date and time variables
  character(len = 8) :: date
  character(len = 10) :: time
  character(len = 5) :: zone
  integer(kind = ik) :: values(8)
  
  ! Iterator variable
  integer(kind = ik) :: i

  ! Subroutine return variable
  integer(kind = ik) :: res

  do while (.not. validated)
    write(*, '(a)', advance = 'no') 'Please input two integers: '
    read(*,*, iostat = read_status, iomsg = read_message) input1, input2
    if (read_status == 0) then
      validated = .true.
      print '(a,x,i0,x,a,x,i0)', 'Thank you for writing the integers:', input1, 'and', input2
    else
      print '(a,x,a,/)', 'At least one of the inputs is not an integer! Please try again.\n\nError messagge:', trim(read_message)
    end if
  end do
  
  print *
  print '(a)', 'Calculating the square sum of the integers:'
  call square_sum(input1, input2, res)
  print '(a,x,i0,2(a,x,i0))', 'Result of calculation:', input1, '^2 +', input2, '^2 =', res
  print *
  print '(a)', 'Showing current date:'
  call date_and_time(date, time, zone, values)
  print '(a,x,a)', 'Current date:', date
  print '(a,x,a)', 'Current time:', time
  print '(a,x,a)', 'Local timezone:', zone
  print *

  !print '(a)', 'Additional information:'
  !do i = 1,8
  !  print '(i0)', values(i)
  !end do
end program input_validation
