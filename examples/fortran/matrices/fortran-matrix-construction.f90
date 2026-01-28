program matrix_construcrion
  ! 
  ! COMPILE THIS PROGRAM WITH: gfortran -Wall -Wextra -std=f2018 fortran-matrix-construction.f90 
  !
  ! Consider the following tridiagonal matrix M:
  !     [  1  2  0  0  0  0  ] 
  !     [ -2 -1  3  0  0  0  ] 
  ! M = [  0 -3  1  4  0  0  ] 
  !     [  0  0 -4 -1  5  0  ] 
  !     [  0  0  0 -5  1  6  ]
  !     [  0  0  0  0 -6 -1  ]
  !
  ! The aim is to construct the same matrix using fortran given the three diagonals
  ! as arrays of integers. The main diagonal is the diagonal that runs from the top-left
  ! corner of the matrix to the bottom-right corner of the matrix. The diagonal below
  ! that is known as the subdiagonal and the diagonal above is known as the supradiagonal
  !
  ! To test that the construction was successful, the following vector v will be defined:
  !     [  2  ]
  !     [ -1  ]
  ! v = [  3  ]
  !     [  1  ]
  !     [ -3  ]
  !     [ -2  ]
  ! 
  ! The mathematically correct value w for the multiplication M*v is:
  !     [  0  ]
  !     [  6  ]
  ! w = [  10 ]
  !     [ -28 ]
  !     [ -20 ]
  !     [  20 ]
  !
  ! If the construction accidentally produces the transpose of M (as is possible when
  ! a different memory ordering is assumed when another is used), the result will be:
  !     [  4  ]
  !     [ -4  ]
  ! w = [ -4  ]
  !     [  26 ]
  !     [  14 ]
  !     [ -16 ]
  !
  
  implicit none

  integer, parameter :: N = 6
  integer :: sub(N-1) = [-2, -3, -4, -5, -6]
  integer :: main(N) = [1, -1, 1, -1, 1, -1]
  integer :: sup(N-1) = [2, 3, 4, 5, 6]
  integer :: matrix1(N,N) = 0
  integer :: matrix2(N,N) = 0
  integer :: vector(N) = [2, -1, 3, 1, -3, -2]
  integer, dimension(N) :: res1, res2
  integer :: i, j

  ! Matrix 1:
  ! Edge cases
  matrix1(1,1) = main(1)
  matrix1(1,2) = sup(1)
  matrix1(N,N) = main(N)
  matrix1(N,N-1) = sub(N-1)

  ! Interior
  do i = 2,N-1
    matrix1(i,i) = main(i)
    matrix1(i,i+1) = sup(i)
    matrix1(i,i-1) = sub(i-1)
  end do

  ! Matrix 2:
  ! Edge cases
  matrix2(1,1) = main(1)
  matrix2(2,1) = sup(1)
  matrix2(N,N) = main(N)
  matrix2(N-1,N) = sub(N-1)

  ! Interior
  do i = 2,N-1
    matrix2(i,i) = main(i)
    matrix2(i+1,i) = sup(i)
    matrix2(i-1,i) = sub(i-1)
  end do

  res1 = matmul(matrix1, vector)
  res2 = matmul(matrix2, vector)

  print '(a)', 'The matrix we want to construct,'
  print '(a)', 'matrix M expressed in mathematical notation:'
  print '(6("[",6(I2,1x),"]",/))', ((matrix1(i,j), j = 1,N), i = 1,N)

  print '(a)', 'Vector v:'
  print '(6("[",I2,"]",/))', (vector(i), i = 1,N)

  print '(a)', 'The mathematically correct result w of the multiplication M*v'
  print '(6("[",I3,"]",/))', (res1(i), i = 1, N)

  print '(a)', 'The main diagonal of M:'
  print '("[",6(I2,1x),"]",/)', (main(i), i = 1, N)

  print '(a)', 'The subdiagonal of M:'
  print '("[",5(I2,1x),"]",/)', (sub(i), i = 1, N-1)

  print '(a)', 'The supradiagonal of M:'
  print '("[",5(I2,1x),"]",/)', (sup(i), i = 1, N-1)

  print '(a)', 'Matrix M1 constructed naively:'
  print '(6("[",6(I2,1x),"]",/))', ((matrix1(i,j), j = 1,N), i = 1,N)

  print '(a)', 'Result w1 of the multiplication M1*v:'
  print '(6("[",I3,"]",/))', (res1(i), i = 1,N)

  print '(a)', 'Matrix M2 constructed trying to account for weird ordering:'
  print '(6("[",6(I2,1x),"]",/))', ((matrix2(i,j), j = 1,N), i = 1,N)

  print '(a)', 'Result w2 of the multiplication M2*v:'
  print '(6("[",I3,"]",/))', (res2(i), i = 1, N)

  print '(a)', 'Result w1 matches the expected result w and thus constructing matrices'
  print '(a)', 'naively is the correct practice to ensure that matrix multiplications'
  print '(a)', 'produce expected results'

end program matrix_construcrion
