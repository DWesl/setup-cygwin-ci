# ACLOCAL_AMFLAGS=-I m4

bin_PROGRAMS=hello
lib_LTLIBRARIES=libprint_hello.la
include_HEADERS=src/print_hello.h

libprint_hello_la_SOURCES=src/print_hello.c
libprint_hello_la_LDFLAGS=-no-undefined

hello_SOURCES=app/hello.c
hello_LDADD=libprint_hello.la

AM_CPPFLAGS=-I@top_srcdir@/src
