program matrix_initialization
  !
  ! COMPILE THIS PROGRAM WITH: gfortran -Wall -Wextra -std=f2018 fortran-matrix-initialization.f90 
  !
  ! Let the matrix M be defined as:
  !     [  1  2  0  0  ] 
  ! M = [ -2 -1  3  0  ] 
  !     [  0 -3  1  4  ] 
  !     [  0  0 -4 -1  ] 
  !
  ! Let the vector v be defined as:
  !     [  2  ]
  ! v = [ -1  ]
  !     [  3  ]
  !     [  1  ]
  !
  ! The aim is to calculate the following matrix-vector product:
  ! Mv = w
  !
  ! The mathematically correct value for the resulting vector w is:
  !     [  0  ]
  ! w = [  6  ]
  !     [  10 ]
  !     [ -13 ]
  !
  ! If the value for the resulting vector w happens to be this:
  !     [  4  ]
  ! w = [ -4  ]
  !     [ -4  ]
  !     [  11 ]
  !
  ! Then we know that the calculation that actually took place was:
  ! transpose(M)*v = w
  ! 
  ! Q: Why would the second case ever happen? 
  !
  ! A: The way in which many-dimensional arrays are stored in Fortran is
  ! different to how we usually imagine arrays to be stored and how it is done
  ! in many other programming launguages (ie. C, Python). The storing convention
  ! in Fortran is known as column-major order whereas the more familiar convention
  ! of C & co. is known as row-major order. First things first: how do they work?
  !
  ! Consider this 3x3 matrix A:
  !     [  11  12  13  ] 
  ! A = [  21  22  23  ]
  !     [  31  32  33  ]
  !
  ! The entries of A reflect the indexing used to label matrix elements in mathematics
  ! ie. the first number tells you the row, and the second number tells you the column
  ! Now, since computer memory is not two-dimensional, we have two choices on how we want to
  ! store the elements of A in memory. The first (and more closely related to the mathematical notation) option is to
  ! store A row by row like this:
  ! A (in memory, row-major order) = [  11  12  13  21  22  23  31  32  33  ]  
  ! This is known as row-major order since we are essentially sorting the matrix by row index from smallest to largest
  ! and then sorting each row by column index from smallest to largest and then storing the result. Row-major reflects
  ! the fact that we are doing the sorting by rows first and the sorting by columns second
  ! 
  ! You can probably guess then, that if we were to store the A column by column, the order would be called column-major ordering:
  ! A (in memory, column-major order) = [  11  21  31  12  22  32  13  23  33  ]
  ! 
  ! Now, if you look at the elements of A stored in column-major order and interpret it as if it was stored in row-major order
  ! (ie. 11 21 31 is the first row, 12 22 32 is the second row and 13 23 33 is the third row) the matrix B you would get is:
  !     [  11  21  31  ]  
  ! B = [  12  22  32  ]
  !     [  13  23  33  ]
  !
  ! If you compare B with A you can see that you can get B by reflecting the elements of A around the main diagonal. This is
  ! essentially what the transposition operator of linear algebra does! This means that depending on how the data is laid out
  ! the matrix that is constructed might actually be the transpose of the matrix the programmer wished to define and thus care
  ! must be given to how matrices are defined
  ! 
  ! In the code below, the entries of matrix M are stored in two arrays in row-major and column-major order
  ! and later the arrays are reshaped into two 4x4 matrices. In addition to that the vector v is defined like above
  ! Finally the matrix product is calculated using both forms of the matrix M and the results are printed.
  ! The mathematically correct result is achieved when the origininal data layout is column-major order meaning that
  ! if a matrix needs to be defined, giving it in column-major order from the beginning will ensure that the calculations
  ! produce results that match expectations

  implicit none

  integer, parameter :: N = 4
  integer, dimension(N,N) :: matrix1, matrix2
  integer :: row_major(N**2) = [1,2,0,0,-2,-1,3,0,0,-3,1,4,0,0,-4,-1]
  integer :: col_major(N**2) = [1,-2,0,0,2,-1,-3,0,0,3,1,-4,0,0,4,-1]
  integer :: vector(N) = [2, -1, 3, 1]
  integer, dimension(N) :: res1, res2
  integer :: i, j


  matrix1 = reshape(row_major, shape(matrix1))
  matrix2 = reshape(col_major, shape(matrix2))

  res1 = matmul(matrix1, vector)
  res2 = matmul(matrix2, vector)

  print '(a)', 'The matrix we want to use in calculations,'
  print '(a)', 'matrix M expressed in mathematical notation:'
  print '(4("[",4(I2,1x),"]",/))', ((matrix2(i,j), j = 1,N), i = 1,N)

  print '(a)', 'Vector v:'
  print '(4("[",I2,"]",/))', (vector(i), i = 1,N)

  print '(a)', 'The mathematically correct result w of the multiplication M*v'
  print '(4("[",I3,"]",/))', (res2(i), i = 1, N)

  print '(a)', 'Elements of M arranged in row-major order:'
  print '("[",16(I2,1x),"]",/)', (row_major(i), i = 1,N**2)

  print '(a)', 'Matrix M1 formed from row-major ordering of matrix M:'
  print '(4("[",4(I2,1x),"]",/))', ((matrix1(i,j), j = 1,N), i = 1,N)

  print '(a)', 'Result w1 of the multiplication M1*v:'
  print '(4("[",I2,"]",/))', (res1(i), i = 1,N)

  print '(a)', 'Elements of M arranged in column-major order:'
  print '("[",16(I2,1x),"]",/)', (col_major(i), i = 1,N**2)

  print '(a)', 'Matrix M2 formed from column-major ordering of matrix M:'
  print '(4("[",4(I2,1x),"]",/))', ((matrix2(i,j), j = 1,N), i = 1,N)

  print '(a)', 'Result w2 of the multiplication M2*v:'
  print '(4("[",I3,"]",/))', (res2(i), i = 1, N)

  print '(a)', 'Result w2 matches the expected result w and thus arranging data'
  print '(a)', 'in COLUMN-MAJOR order is the correct practice to ensure that'
  print '(a)', 'matrix multiplications produce expected results'

end program matrix_initialization
