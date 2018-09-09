Name: workflow
Summary: action for workflow
Version: 1.4.2
Release: 1
Epoch: 0
License: LGPL
Group: Applications
URL: http://www.unirel.com
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}
Provides: action
Packager: Stefano Casazza <stefano.casazza@unirel.com>
Requires: ULib
Requires: zlib
Requires: expat
Requires: file
Requires: pcre
Requires: uuid
Requires: openssl
Requires: libstdc++
BuildRequires: expat
BuildRequires: zlib-devel
BuildRequires: file-devel
BuildRequires: pcre-devel
BuildRequires: openssl-devel
BuildRequires: libstdc++-devel

%description
This package provides the action for workflow

%prep
%setup

%build
%configure --enable-static --enable-shared
cd src/ulib
make LDFLAGS="-s"
cd ../../examples/workflow
make LDFLAGS="-s"
cd ../..

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/workflow/action/bin
autoconf/install-sh -c -m 755 examples/workflow/.libs/error			%{buildroot}/workflow/action/bin
autoconf/install-sh -c -m 755 examples/workflow/.libs/validation	%{buildroot}/workflow/action/bin
autoconf/install-sh -c -m 755 examples/workflow/.libs/production	%{buildroot}/workflow/action/bin

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/workflow/action/bin/error
/workflow/action/bin/validation
/workflow/action/bin/production
