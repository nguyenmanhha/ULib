Name: tsaserver
Summary: server TSA
Version: 1.4.2
Release: 1
Epoch: 0
License: LGPL
Group: Applications
URL: http://www.unirel.com
Source0: %{name}-%{version}.tar.gz
Source1: tsaserver.start
BuildRoot: %{_tmppath}/%{name}-%{version}
Provides: tsaserver
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
This package provides the program for manage a server TSA

%prep
%setup

%build
%configure --enable-static --enable-shared
cd src/ulib
make LDFLAGS="-s"
cd ../../examples/userver
make LDFLAGS="-s"
cd ../..

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/srv/TSA/bin
mkdir -p %{buildroot}/srv/TSA/etc
mkdir -p %{buildroot}/srv/TSA/var/TSA_command
mkdir -p $RPM_BUILD_ROOT/%{_initrddir}
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig
SRC=tests/examples
DST=%{buildroot}/srv/TSA
autoconf/install-sh -c -m 755 examples/userver/tsaserver.start			$RPM_BUILD_ROOT/%{_initrddir}/tsaserver
autoconf/install-sh -c -m 755 examples/userver/.libs/userver_tcp		$DST/bin/tsaserver
autoconf/install-sh -c -m 644 $SRC/userver.cfg								$DST/etc/userver.cfg.dist
autoconf/install-sh -c -m 644 $SRC/mod_tsa.cfg								$DST/etc/mod_tsa.cfg.dist
autoconf/install-sh -c -m 644 $SRC/tsa_http.cfg								$DST/etc/tsa_http.cfg.dist
autoconf/install-sh -c -m 644 $SRC/TSA/TSA_command/.function			$DST/var/TSA_command
autoconf/install-sh -c -m 755 $SRC/TSA/TSA_command/tsa_REPLY_BIN.sh	$DST/var/TSA_command
autoconf/install-sh -c -m 755 $SRC/TSA/TSA_command/tsa_REPLY_B64.sh	$DST/var/TSA_command

cat > $RPM_BUILD_ROOT/etc/sysconfig/tsaserver << EOF
#ld_library_path=/usr/lib64
exe=/srv/TSA/bin/tsaserver
confdir=/srv/TSA/etc
EOF

%post
/sbin/chkconfig --add tsaserver

%preun
%{_initrddir}/tsaserver stop
/sbin/chkconfig --del tsaserver

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_initrddir}/tsaserver
/etc/sysconfig/tsaserver
/srv/TSA/bin/tsaserver
/srv/TSA/etc/*.cfg.dist
/srv/TSA/var/TSA_command/*.sh
/srv/TSA/var/TSA_command/.function