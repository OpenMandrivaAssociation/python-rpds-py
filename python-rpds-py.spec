Summary:	Python bindings to
Name:		python-rpds-py
Version:	0.17.1
Release:	1
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/rpds-py/
Source0:	https://pypi.org/packages/source/r/rpds_py/rpds_py-%{version}.tar.gz
BuildRequires:  cargo
BuildRequires:	python%{pyver}dist(maturin)
BuildRequires:	python%{pyver}dist(pip)

%description
Python bindings to Rust's persistent data structures (rpds)

%files
%{py_platsitedir}/rpds
%{py_platsitedir}/rpds_py-*.*-info

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n rpds_py-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
%py_build

%install
%py_install

