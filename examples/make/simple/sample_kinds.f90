module sample_kinds
    implicit none

    ! Integer and real kinds (64-bit)
    integer, parameter, public :: ik = selected_int_kind(38)
    integer, parameter, public :: rk = selected_real_kind(33,1)

end module sample_kinds
