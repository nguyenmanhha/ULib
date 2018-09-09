Name: wagsmserver
Summary: RPC server for manage GSM message
Version: 1.4.2
Release: 1
Epoch: 0
License: LGPL
Group: Applications
URL: http://www.unirel.com
Source0: %{name}-%{version}.tar.gz
Source1: wagsmserver.start
BuildRoot: %{_tmppath}/%{name}-%{version}
Provides: wagsmserver
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
This package provides the program for manage one RPC server for manage GSM message

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
mkdir -p %{buildroot}/srv/WAGSM/bin
mkdir -p %{buildroot}/srv/WAGSM/etc
mkdir -p %{buildroot}/srv/WAGSM/var/WAGSM_command
mkdir -p $RPM_BUILD_ROOT/%{_initrddir}
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig
SRC=tests/examples
DST=%{buildroot}/srv/WAGSM
autoconf/install-sh -c -m 755 examples/userver/wagsmserver.start				$RPM_BUILD_ROOT/%{_initrddir}/wagsmserver
autoconf/install-sh -c -m 755 examples/userver/.libs/userver_tcp				$DST/bin/wagsmserver
autoconf/install-sh -c -m 644 $SRC/userver.cfg										$DST/etc/userver.cfg.dist
autoconf/install-sh -c -m 644 $SRC/WAGSM_server.cfg								$DST/etc/wagsmserver.cfg.dist
autoconf/install-sh -c -m 644 $SRC/mod_soap_or_rpc_WAGSM.cfg					$DST/etc/mod_soap_or_rpc_WAGSM.cfg.dist
autoconf/install-sh -c -m 644 $SRC/WAGSM/WAGSM_command/.function				$DST/var/WAGSM_command
autoconf/install-sh -c -m 755 $SRC/WAGSM/WAGSM_command/card_activation.sh	$DST/var/WAGSM_command

cat > $RPM_BUILD_ROOT/etc/sysconfig/wagsmserver << EOF
#ld_library_path=/usr/lib64
exe=/srv/WAGSM/bin/wagsmserver
confdir=/srv/WAGSM/etc
EOF

%post
/sbin/chkconfig --add wagsmserver

%preun
%{_initrddir}/wagsmserver stop
/sbin/chkconfig --del wagsmserver

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_initrddir}/wagsmserver
/etc/sysconfig/wagsmserver
/srv/WAGSM/bin/wagsmserver
/srv/WAGSM/etc/*.cfg.dist
/srv/WAGSM/var/WAGSM_command/.function
/srv/WAGSM/var/WAGSM_command/*.sh
