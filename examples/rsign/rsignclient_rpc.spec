Name: rsignclient_rpc
Summary: general client RPC for manage Remote Sign
Version: 1.4.2
Release: 1
Epoch: 0
License: LGPL
Group: Applications
URL: http://www.unirel.com
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}
Provides: rsignclient_rpc
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
This package provides the program client for manage one general server RPC for manage Remote Sign

%prep
%setup

%build
%configure --enable-static --enable-shared
cd src/ulib
make LDFLAGS="-s"
cd ../../contrib/RSIGN
make LDFLAGS="-s"
cd ../../examples/rsign
make LDFLAGS="-s"
cd ../..

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/srv/RSIGN/bin
mkdir -p %{buildroot}/srv/RSIGN/lib
mkdir -p %{buildroot}/srv/RSIGN/etc
SRC=tests/examples
DST=%{buildroot}/srv/RSIGN
autoconf/install-sh -c -m 755 examples/rsign/.libs/rsignclient_rpc	$DST/bin
autoconf/install-sh -c -m 644 contrib/RSIGN/.libs/RSIGN.so				$DST/lib
autoconf/install-sh -c -m 644 $SRC/rsignclient_rpc.cfg					$DST/etc/rsignclient_rpc.cfg.dist

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/srv/RSIGN/lib/RSIGN.so
/srv/RSIGN/bin/rsignclient_rpc
/srv/RSIGN/etc/rsignclient_rpc.cfg.dist
