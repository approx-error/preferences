program matrix_access
  !
  ! COMPILE THIS PROGRAM WITH: gfortran -Wall -Wextra -std=f2018 fortran-matrix-access.f90 
  !
  ! Consider the following tridiagonal matrix M:
  !     [  1  2  0  0  0  0  ] 
  !     [ -2 -1  3  0  0  0  ] 
  ! M = [  0 -3  1  4  0  0  ] 
  !     [  0  0 -4 -1  5  0  ] 
  !     [  0  0  0 -5  1  6  ]
  !     [  0  0  0  0 -6 -1  ]
  !
  ! Assuming that we have constructed the matrix correctly (using the techniques in the 
  ! other fortran-matrix-*.f90 files) we now wish to extract the main diagonal, subdiagonal
  ! and the supradiagonal such that we get the correct values stored in each of them
  !
  ! Here are the expected values for the subdiagonal (a), main diagonal(b) and supradiagonal (c):
  !
  ! a = [ -2 -3 -4 -5 -6  ]
  ! b = [  1 -1  1 -1  1 -1  ]
  ! c = [  2  3  4  5  6] 

  implicit none

  integer, parameter :: N = 6
  integer :: correct_form(N**2) = [1,-2,0,0,0,0,2,-1,-3,0,0,0,0,3,1,-4,0,0,0,0,4,-1,-5,0,0,0,0,5,1,-6,0,0,0,0,6,-1]
  integer :: matrix(N,N)
  integer, dimension(N) :: main1, main2
  integer, dimension(N-1) :: sub1, sup1, sub2, sup2
  integer :: i, j

  matrix = reshape(correct_form, shape(matrix))

  ! Extraction 1:
  ! Bounds
  main1(1) = matrix(1,1)
  sup1(1) = matrix(1,2)
  main1(N) = matrix(N,N)
  sub1(N-1) = matrix(N,N-1)

  ! Interior
  do i = 2,N-1
    main1(i) = matrix(i,i)
    sup1(i) = matrix(i,i+1)
    sub1(i-1) = matrix(i,i-1)
  end do

  ! Extraction 2:
  ! Bounds
  main2(1) = matrix(1,1)
  sup2(1) = matrix(2,1)
  main2(N) = matrix(N,N)
  sub2(N-1) = matrix(N-1,N)

  ! Interior
  do i = 2,N-1
    main2(i) = matrix(i,i)
    sup2(i) = matrix(i+1,i)
    sub2(i-1) = matrix(i-1,i)
  end do

  print '(a)', 'The matrix we want to extract diagonals from,'
  print '(a)', 'matrix M expressed in mathematical notation:'
  print '(6("[",6(I2,1x),"]",/))', ((matrix(i,j), j = 1,N), i = 1,N)

  print '(a)', 'The correct subdiagonal (a), main diagonal (b) and supradiagonal (c):'
  print '("[",5(I2,1x),"]",/)', (sub1(i), i = 1,N-1)
  print '("[",6(I2,1x),"]",/)', (main1(i), i = 1,N)
  print '("[",5(I2,1x),"]",/)', (sup1(i), i = 1,N-1)

  print '(a)', 'The naively constructed subdiagonal (a1), main diagonal (b1) and supradiagonal (c1):'
  print '("[",5(I2,1x),"]",/)', (sub1(i), i = 1,N-1)
  print '("[",6(I2,1x),"]",/)', (main1(i), i = 1,N)
  print '("[",5(I2,1x),"]",/)', (sup1(i), i = 1,N-1)

  print '(a)', 'The "cleverly" constructed subdiagonal (a2), main diagonal (b2) and supradiagonal (c2)'
  print '("[",5(I2,1x),"]",/)', (sub2(i), i = 1,N-1)
  print '("[",6(I2,1x),"]",/)', (main2(i), i = 1,N)
  print '("[",5(I2,1x),"]",/)', (sup2(i), i = 1,N-1)
  
  print '(a)', 'The results a1, b1 and c1 match the expected results a, b and c respectively'
  print '(a)', 'and thus extracting data from matrices naively is the correct practice to'
  print '(a)', 'ensure that the correct data is extracted. This of course assumes that the matrix'
  print '(a)', 'has been constructed in the correct way to begin with'
  
end program matrix_access
