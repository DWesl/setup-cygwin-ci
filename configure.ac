#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.69])
AC_INIT([setup-cygwin-ci], [0.0], [https://github.com/DWesl/setup-cygwin-ci])
AC_CONFIG_SRCDIR([app/hello.c])
AC_CONFIG_HEADERS([config.h])
AC_CONFIG_MACRO_DIR([m4])
AC_CONFIG_AUX_DIR([build-aux])
AM_INIT_AUTOMAKE([foreign dist-bzip2 dist-xz subdir-objects])

# Checks for programs.
AC_PROG_CC
AC_PROG_FC

# Checks for libraries.
LT_INIT()

# Checks for header files.
AC_CHECK_HEADERS([stdio.h])

# Checks for typedefs, structures, and compiler characteristics.

# Checks for library functions.

AC_CONFIG_FILES([Makefile])
AC_OUTPUT
