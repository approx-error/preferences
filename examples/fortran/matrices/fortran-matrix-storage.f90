program matrix_storage
  !
  ! COMPILE THIS PROGRAM WITH: gfortran -Wall -Wextra -std=f2018 fortran-matrix-storage.f90 
  !  
  ! Let the matrix M be defined as:
  !     [  1  2  0  0  ]
  ! M = [ -2 -1  3  0  ]
  !     [  0 -3  1  4  ]
  !     [  0  0 -4  1  ]
  !
  ! This program will try to construct matrix M in two different ways
  ! and then show how where the elements of the contructed matrices ended
  ! up in memory

  implicit none

  integer, parameter :: N = 4
  integer, dimension(N,N) :: matrix1, matrix2
  integer, dimension(N**2) :: order1, order2
  integer :: row_major(N**2) = [1,2,0,0,-2,-1,3,0,0,-3,1,4,0,0,-4,-1]
  integer :: col_major(N**2) = [1,-2,0,0,2,-1,-3,0,0,3,1,-4,0,0,4,-1]
  integer :: i,j

  matrix1 = reshape(row_major, shape(matrix1))
  matrix2 = reshape(col_major, shape(matrix2))

  order1 = reshape(matrix1, shape(order1))
  order2 = reshape(matrix2, shape(order2))

  print '(a)', 'The matrix we want to construct, matrix M'
  print '(a)', 'expressed in mathematical notation:'
  print '(4("[",4(I2,1x),"]",/))', ((matrix2(i,j), j = 1,N), i = 1,N)

  print '(a)', 'Elements of M arranged in row-major order:'
  print '("[",16(I2,1x),"]",/)', (row_major(i), i = 1,N**2)

  print '(a)', 'Matrix M1 formed from row-major ordering of matrix M:'
  print '(4("[",4(I2,1x),"]",/))', ((matrix1(i,j), j = 1,N), i = 1,N)

  print '(a)', 'The elements of M1 arranged in the order they are laid out in memory:'
  print '("[",16(I2,1x),"]",/)', (order1(i), i = 1,N**2)

  print '(a)', 'Elements of M arranged in column-major order:'
  print '("[",16(I2,1x),"]",/)', (col_major(i), i = 1,N**2)

  print '(a)', 'Matrix M2 formed from column-major ordering of matrix M:'
  print '(4("[",4(I2,1x),"]",/))', ((matrix2(i,j), j = 1,N), i = 1,N)

  print '(a)', 'The elements of M2 arranged in the order they are laid out in memory:'
  print '("[",16(I2,1x),"]",/)', (order2(i), i = 1,N**2)

  print '(a)', 'Since M2 matches M, we know that the correct way to initialize matrices'
  print '(a)', 'is to write the data in column-major order and then reshape it to match'
  print '(a)', 'the dimensions of the desired matrix'
  
end program matrix_storage

 
