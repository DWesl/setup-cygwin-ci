module multiply_two
  implicit none
  integer, parameter, public :: two = 2
contains
  function multiply_two_numbers(a, b) result(c)
    real, intent(in) :: a, b
    real :: c
    c = a * b
    return
  end function multiply_two_numbers
end module multiply_two
