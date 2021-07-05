%global _empty_manifest_terminate_build 0
Name:		python-restructuredtext-lint
Version:	1.1.3
Release:	1
Summary:	reStructuredText linter
License:	Public Domain
URL:		https://github.com/twolfson/restructuredtext-lint
Source0:	https://files.pythonhosted.org/packages/7e/b5/d28da439210e7f35e4f58f743e2d1fa9c7f34fb5ab9a0532e0bb3a77274a/restructuredtext_lint-1.1.3.tar.gz
BuildArch:	noarch
%description
restructuredtext-lint reStructuredText linterThis was created out of frustration
with PyPI; it sucks finding out your reST is invalid **after*uploading it. It is
being developed in junction with a Sublime Text linter... _reStructuredText: ..
_linter: .. _reST: reStructuredText .. _PyPI: .. _Sublime Text: .

%package -n python2-restructuredtext-lint
Summary:	reStructuredText linter
Provides:	python2-restructuredtext-lint
BuildRequires:	python2-devel
BuildRequires:	python2-setuptools
%description -n python2-restructuredtext-lint
restructuredtext-lint reStructuredText linterThis was created out of frustration
with PyPI; it sucks finding out your reST is invalid **after*uploading it. It is
being developed in junction with a Sublime Text linter... _reStructuredText: ..
_linter: .. _reST: reStructuredText .. _PyPI: .. _Sublime Text: .

%package help
Summary:	Development documents and examples for restructuredtext-lint
Provides:	python2-restructuredtext-lint-doc
%description help
restructuredtext-lint reStructuredText linterThis was created out of frustration
with PyPI; it sucks finding out your reST is invalid **after*uploading it. It is
being developed in junction with a Sublime Text linter... _reStructuredText: ..
_linter: .. _reST: reStructuredText .. _PyPI: .. _Sublime Text: .

%prep
%autosetup -n restructuredtext_lint-1.1.3

%build
%py2_build

%install
%py2_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python2-restructuredtext-lint -f filelist.lst
%dir %{python2_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Tue May 11 2021 OpenStack_SIG <openstack@openeuler.org>
- Package Spec generated
