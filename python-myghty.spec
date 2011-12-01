%if !(0%{?fedora} >= 13 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%endif

Name:           python-myghty
Version:        1.1
Release:        11%{?dist}
Summary:        Python-based templating system derived from HTML::Mason

Group:          Development/Libraries
License:        MIT
URL:            http://www.myghty.org
Source0: http://pypi.python.org/packages/source/M/Myghty/Myghty-%{version}.tar.gz
# Fix import hook to work with python-2.6+
Patch0: myghty-importer.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires: python2-devel
%if 0%{?fedora} <= 12
BuildRequires: python-setuptools-devel
%else
BuildRequires: python-setuptools
%endif


%description
Myghty is a Python based web and templating framework originally based on
HTML::Mason, the enterprise-level framework used by Amazon.com, del.icio.us
and Salon.com, among many others. Myghty fully implements Mason's templating
language, component-based architecture, and caching system, and goes beyond,
adding new paradigms such the Module Components controller paradigm, full
Python whitespace syntax, threading support, WSGI support, session support,
and much more.

%prep
%setup -q -n Myghty-%{version}
%patch0 -p1

sed -i 's!/usr/local/bin/python!/usr/bin/python!' examples/zblog/bin/server.py

%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT
(cd doc ; %{__python} genhtml.py)

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc doc/html/* examples LICENSE README
%{python_sitelib}/*


%changelog
* Fri Jun 25 2010 Toshio Kuratomi - 1.1-11
- Add README file
- Update old way of invoking setup.py
- Fix conditionals for python-setuptools
- Comment what myghty-importer.patch does

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 13 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 1.1-9
- Fix for building with python2.6

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.1-7
- Rebuild for Python 2.6

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.1-6
- fix license tag

* Sat Oct 27 2007 Luke Macken <lmacken@redhat.com> 1.1-5
- Fix broken Source0

* Sun Sep  2 2007 Luke Macken <lmacken@redhat.com> 1.1-4
- Update for python-setuptools changes in rawhide

* Sat Dec  9 2006 Luke Macken <Lmacken@redhat.com> 1.1-2
- Rebuild for python 2.5

* Wed Oct 18 2006 Luke Macken <lmacken@redhat.com> 1.1-1
- 1.1

* Sun Sep  3 2006 Luke Macken <lmacken@redhat.com> 1.0.2-2
- Rebuild for FC6

* Mon Aug 14 2006 Luke Macken <lmacken@redhat.com> 1.0.2-1
- 1.0.2

* Thu Mar 16 2006 Luke Macken <lmacken@redhat.com> 1.0.1-1
- 1.0.1; build requires python-setuptools

* Wed Jan 04 2006 Luke Macken <lmacken@redhat.com> 1.0-1
- 1.0

* Wed Jan 04 2006 Luke Macken <lmacken@redhat.com> 0.99a-1
- Bump to 0.99a
- Install with --old-and-unmanageable to avoid Python Eggs annoyance

* Wed Oct 05 2005 Luke Macken <lmacken@redhat.com> 0.99-1
- Bump to version 0.99

* Mon Sep 12 2005 Luke Macken <lmacken@redhat.com> 0.98c-1
- Bump to version 0.98c

* Tue Aug 16 2005 Luke Macken <lmacken@redhat.com> 0.98a-1
- Packaged for Fedora Extras
