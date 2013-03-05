Summary: vmcatcher specifics for interfacing with glancepush
Name: glancepush-vmcatcher
Version: 0.1
Release: 1
Group: Applications/System
Packager: Mattieu Puel
License: GPL2
BuildRoot: %{_builddir}/osimgpublish
BuildArch: noarch
Requires: glancepush, python-confparser



%description
glancepush automates images testing and publishing into Openstack Glance images catalog. glancepush-vmcatcher implements interface between glancepush and vmcatcher.




%install
rsync --exclude .svn -av %{_sourcedir}/ $RPM_BUILD_ROOT/




%clean 
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT




%files
%defattr(0755,root,root)
/usr/bin/gpvmcupdate
/usr/share/man/man5/gpvmcmapping.5.gz
%defattr(0644,root,root)
%config(noreplace)
/etc/gpvmcmapping



%changelog
* Fri Feb 01 2013 Mattieu Puel 0.1-1
- first release
