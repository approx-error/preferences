program transform
  ! Compute 1D fourier transform and inverse fourier transform with fftw version 3

  use kinds
  use parameters
  use fftw3

  implicit none

  ! Define constants
  real(r64), parameter :: LOW_BOUND = 0.0
  real(r64), parameter :: HIGH_BOUND = 5.0

  ! Define size of the data array
  integer(C_SIZE_T), parameter :: N = 256
  ! Define step size between data points on interval
  real(r64), parameter :: step_size = (HIGH_BOUND - LOW_BOUND) / N

  ! Define auxilliary arrays
  real(r64), dimension(0:N-1) :: input_points
  real(r64), dimension(0:N-1) :: sample_freqs
  real(r64), dimension(0:N-1) :: forward_output_real, forward_output_imag

  ! Define loop variables
  integer :: i

  ! Define pointers to store data for input and output
  complex(C_DOUBLE_COMPLEX), pointer, dimension(:) :: forward_input, forward_output, backward_input, backward_output
  ! Define C-style pointers that will hold the fortran pointers 'input' and 'output'
  ! This is done because we want to align data in memory for better performance and 
  ! standard fortran does not guarantee array alignment so an external C function
  ! needs to be used to guarantee aligned memory allocation
  type(C_PTR) :: forward_input_holder, forward_output_holder
  type(C_PTR) :: backward_input_holder, backward_output_holder

  ! Define pointers to store the method the fft is calculated with as determined by fftw3
  ! This is known as the 'plan' in fftw3 documentation
  type(C_PTR) :: plan_forward, plan_backward

  ! Allocating complex number memory with the C-function 'fftw_alloc_complex'
  forward_input_holder = fftw_alloc_complex(N)
  forward_output_holder = fftw_alloc_complex(N)
  backward_input_holder = fftw_alloc_complex(N)
  backward_output_holder = fftw_alloc_complex(N)

  ! Associating the C-pointers with the Fortran-pointers
  call c_f_pointer(forward_input_holder, forward_input, [N])
  call c_f_pointer(forward_output_holder, forward_output, [N])
  call c_f_pointer(backward_input_holder, backward_input, [N])
  call c_f_pointer(backward_output_holder, backward_output, [N])

  ! Producing some input data
  do i = 0,N-1
    input_points(i) = LOW_BOUND + i*step_size
  end do

  forward_input = 3.0_r64 * sin(PI * input_points) + 0.5_r64 * sin(PI * 3 * input_points)

  ! Determining fft plans
  plan_forward = fftw_plan_dft_1d(256, forward_input, forward_output, FFTW_FORWARD, FFTW_ESTIMATE)
  plan_backward = fftw_plan_dft_1d(256, backward_input, backward_output, FFTW_BACKWARD, FFTW_ESTIMATE)

  ! Performing fft
  call fftw_execute_dft(plan_forward, forward_input, forward_output)

  ! Copying forward_output to backward input
  backward_input = forward_output

  ! performing ifft
  call fftw_execute_dft(plan_backward, backward_input, backward_output)

  ! Destroying the plans as we are done computing ffts
  call fftw_destroy_plan(plan_forward)
  call fftw_destroy_plan(plan_backward)

  ! Creating sample frequencies
  do i = 0,N-1
    if (i <= N/2-1) then
      sample_freqs(i) = i
    else
      sample_freqs(i) = -(N - i)
    end if
  end do
  sample_freqs = sample_freqs * 1.0_r64 / (N * step_size)

  ! Taking the real (and imaginary, if applicable,) part of the transforms
  forward_input = real(forward_input)
  forward_output_real = real(forward_output)
  forward_output_imag = aimag(forward_output)
  ! Scaling the output by 1/N in order to preserve normalization
  backward_output = (1.0_r64 / N) * real(backward_output)

  ! Writing the data to files

  open(10, file='untransformed.dat', status='REPLACE', action='WRITE')
  open(20, file='transformed.dat', status='REPLACE', action='WRITE')
  open(30, file='backtransformed.dat', status='REPLACE', action='WRITE')

  do i = 0,N-1
    write(10, '(f10.5,a,f10.5)') input_points(i), ';', forward_input(i)
    write(20, '(f10.5,a,f10.5,a,f10.5)') sample_freqs(i), ';', forward_output_real(i), ';', forward_output_imag(i)
    write(30, '(f10.5,a,f10.5)') input_points(i), ';', backward_output(i)
  end do

  close(10)
  close(20)
  close(30)

  ! Deallocating the memory used by the input and output arrays by deallocating
  ! the C-pointers they are associated with
  call fftw_free(forward_input_holder)
  call fftw_free(forward_output_holder)
  call fftw_free(backward_input_holder)
  call fftw_free(backward_output_holder)

  print '(a)', 'Original signal is in file untransformed.dat'
  print '(a)', 'Transformed signal is in file transformed.dat'
  print '(a)', 'Restored signal is in file backtransformed.dat'
end program transform
