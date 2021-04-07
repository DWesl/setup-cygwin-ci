# ACLOCAL_AMFLAGS=-I m4

bin_PROGRAMS=hello
lib_LTLIBRARIES=libprint_hello.la libmultiply_two.la
include_HEADERS=src/print_hello.h

libprint_hello_la_SOURCES=src/print_hello.c
libprint_hello_la_LDFLAGS=-no-undefined

libmultiply_two_la_SOURCES=src/multiply_two.f90
libmultiply_two_la_LDFLAGS=-no-undefined

hello_SOURCES=app/hello.c
hello_LDADD=libprint_hello.la

AM_CPPFLAGS=-I@top_srcdir@/src
