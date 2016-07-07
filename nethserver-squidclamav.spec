Summary: NethServer squidclamav configuration
Name: nethserver-squidclamav
Version: 1.3.0
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: nethserver-c-icap, nethserver-antivirus, nethserver-httpd, nethserver-squidguard
Requires: squidclamav

BuildRequires: perl
BuildRequires: nethserver-devtools 

%description
NethServer squidclamav configuration

%prep
%setup

%build
%{makedocs}
perl createlinks

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist
mkdir -p %{buildroot}/var/lib/squidclamav

%post

%preun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%dir %attr(0755,clamupdate,clamupdate) %{_sharedstatedir}/squidclamav
%doc COPYING


%changelog
* Thu Jul 07 2016 Stefano Fancello <stefano.fancello@nethesis.it> - 1.3.0-1
- First NS7 release

* Thu Feb 18 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.0-1
- Web filter antivirus whitelist - Enhancement #3354 [NethServer]

* Tue Sep 29 2015 Davide Principi <davide.principi@nethesis.it> - 1.1.1-1
- Make Italian language pack optional - Enhancement #3265 [NethServer]

* Tue Jan 20 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.0-1.ns6
- squidGuard: support multiple profiles - Enhancement #2958 [NethServer]
- Enhance visual appearance of proxy block pages - Feature #2866 [NethServer]

* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.4-1.ns6
- Enable logging to /var/log/c-icap/server.log - Enhancement #2289 [NethServer]

* Tue Jul 30 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.3-1.ns6
- Move antivirus proxy web ui from nethserver-antivirus package

* Mon Jul 29 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1.ns6
- Fix typo for nethserver-httpd requires #1959
- Add nethserver-squid dependency #1959

* Fri Jul 26 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1.ns6
- Set default status to disabled #1959
- Add nethserver-httpd dependency  #1959

* Thu Jun 20 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1.ns6
- First release - Feature #1959


