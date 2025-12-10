Summary:	Python bindings to
Name:		python-rpds-py
Version:	0.30.0
Release:	1
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/rpds-py/
Source0:	https://pypi.org/packages/source/r/rpds_py/rpds_py-%{version}.tar.gz
Source1:	vendor.tar.xz
BuildSystem:	python
BuildRequires:  cargo
BuildRequires:	python%{pyver}dist(maturin)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	rust-packaging

%description
Python bindings to Rust's persistent data structures (rpds)

%files
%{py_platsitedir}/rpds
%{py_platsitedir}/rpds_py-*.*-info

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n rpds_py-%{version} -a1 -p1
%cargo_prep -v vendor

%build -p
export RUSTFLAGS="%{build_rustflags}"
%cargo_build
