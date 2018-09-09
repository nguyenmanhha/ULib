Name: PEC_log
Summary: programs for processing log files for PEC
Version: 1.4.2
Release: 1
Epoch: 0
License: LGPL
Group: Applications
URL: http://www.unirel.com
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}
Provides: PEC_log
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
This package provides the programs for processing log files for PEC

%prep
%setup

%build
%configure --enable-static --enable-shared
cd src/ulib
make LDFLAGS="-s"
cd ../../examples/PEC_log
make LDFLAGS="-s"
cd ../..

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/PEC_log/bin
autoconf/install-sh -c -m 755 examples/PEC_log/.libs/PEC_report_virus     %{buildroot}/PEC_log/bin
autoconf/install-sh -c -m 755 examples/PEC_log/.libs/PEC_check_namefile   %{buildroot}/PEC_log/bin
autoconf/install-sh -c -m 755 examples/PEC_log/.libs/PEC_date_generator   %{buildroot}/PEC_log/bin
autoconf/install-sh -c -m 755 examples/PEC_log/.libs/PEC_report_messaggi  %{buildroot}/PEC_log/bin
autoconf/install-sh -c -m 755 examples/PEC_log/.libs/PEC_report_rejected  %{buildroot}/PEC_log/bin
autoconf/install-sh -c -m 755 examples/PEC_log/.libs/PEC_report_anomalie1 %{buildroot}/PEC_log/bin
autoconf/install-sh -c -m 755 examples/PEC_log/.libs/PEC_report_anomalie2 %{buildroot}/PEC_log/bin

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/PEC_log/bin/PEC_report_virus
/PEC_log/bin/PEC_check_namefile
/PEC_log/bin/PEC_date_generator
/PEC_log/bin/PEC_report_messaggi
/PEC_log/bin/PEC_report_rejected
/PEC_log/bin/PEC_report_anomalie1
/PEC_log/bin/PEC_report_anomalie2
