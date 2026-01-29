module sample_module
    
    use sample_kinds

    contains

        subroutine square_sum(num1, num2, sq_sum)
        
            implicit none

            integer(kind = ik), intent(in) :: num1, num2

            integer(kind = ik), intent(out) :: sq_sum

            sq_sum = num1 ** 2 + num2 ** 2

        end subroutine square_sum
end module sample_module
