%{!?version: %define version 4.60}
%{!?build_number: %define build_number 1}

Name:           glpk
Version:        %{version}
Release:        %{build_number}%{?dist}
Summary:        GNU Linear Programming Kit

Group:          System Environment/Libraries
License:        GPLv3
URL:            http://www.gnu.org/software/glpk/glpk.html
Source0:        ftp://ftp.gnu.org/gnu/glpk/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The GLPK (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

GLPK supports the GNU MathProg language, which is a subset of the AMPL
language.

The GLPK package includes the following main components:

 * Revised simplex method.
 * Primal-dual interior point method.
 * Branch-and-bound method.
 * Translator for GNU MathProg.
 * Application program interface (API).
 * Stand-alone LP/MIP solver.

%package        doc
Summary:        Documentation for %{name}
Group:          Documentation

%description    doc
Documentation subpackage for %{name}.


%package devel
Summary:        Development headers and files for GLPK
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
The glpk-devel package contains libraries and headers for developing
applications which use GLPK (GNU Linear Programming Kit).


%package utils
Summary:        GLPK-related utilities and examples
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description utils
The glpk-utils package contains the standalone solver programs glpksol
and tspsol that use GLPK (GNU Linear Programming Kit).


%package static
Summary:        Static version of GLPK libraries
Group:          Development/Libraries
Requires:       %{name}-devel = %{version}-%{release}

%description static
The glpk-static package contains the statically linkable version of
the GLPK (GNU Linear Programming Kit) libraries.


%prep
%setup -q

%build
export LIBS=-ldl
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT%{_prefix} \
  bindir=$RPM_BUILD_ROOT%{_bindir} libdir=$RPM_BUILD_ROOT%{_libdir} \
  includedir=$RPM_BUILD_ROOT%{_includedir}/%name
## Clean up directories that are included in docs
make clean
rm -Rf examples/.deps examples/Makefile* doc/*.dvi doc/*.latex

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYING README
%{_libdir}/*.so*

%files devel
%defattr(-,root,root)
%doc ChangeLog AUTHORS NEWS
%{_includedir}/glpk

%files utils
%defattr(-,root,root)
%{_bindir}/*

%files static
%defattr(-,root,root)
%{_libdir}/*.a
%exclude %{_libdir}/*.la

%files doc
%defattr(-,root,root)
%doc doc examples


%changelog
