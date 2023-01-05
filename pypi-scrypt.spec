#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-scrypt
Version  : 0.8.20
Release  : 2
URL      : https://files.pythonhosted.org/packages/48/38/9816ba98592b64ab3d50199699485912877d4e4507277e92ca312abf9e02/scrypt-0.8.20.tar.gz
Source0  : https://files.pythonhosted.org/packages/48/38/9816ba98592b64ab3d50199699485912877d4e4507277e92ca312abf9e02/scrypt-0.8.20.tar.gz
Summary  : Bindings for the scrypt key derivation function library
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-scrypt-filemap = %{version}-%{release}
Requires: pypi-scrypt-lib = %{version}-%{release}
Requires: pypi-scrypt-python = %{version}-%{release}
Requires: pypi-scrypt-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : openssl-dev
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
=========================
Python scrypt_ bindings
=========================
This is a set of Python_ bindings for the scrypt_ key derivation
function.

%package filemap
Summary: filemap components for the pypi-scrypt package.
Group: Default

%description filemap
filemap components for the pypi-scrypt package.


%package lib
Summary: lib components for the pypi-scrypt package.
Group: Libraries
Requires: pypi-scrypt-filemap = %{version}-%{release}

%description lib
lib components for the pypi-scrypt package.


%package python
Summary: python components for the pypi-scrypt package.
Group: Default
Requires: pypi-scrypt-python3 = %{version}-%{release}

%description python
python components for the pypi-scrypt package.


%package python3
Summary: python3 components for the pypi-scrypt package.
Group: Default
Requires: pypi-scrypt-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(scrypt)

%description python3
python3 components for the pypi-scrypt package.


%prep
%setup -q -n scrypt-0.8.20
cd %{_builddir}/scrypt-0.8.20
pushd ..
cp -a scrypt-0.8.20 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1669614025
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-scrypt

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
