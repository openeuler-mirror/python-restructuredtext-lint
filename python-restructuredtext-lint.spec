%global _empty_manifest_terminate_build 0
Name:           python-restructuredtext-lint
Version:        1.3.2
Release:        3
Summary:        reStructuredText linter
License:        Public Domain
URL:            https://github.com/twolfson/restructuredtext-lint
Source0:        https://files.pythonhosted.org/packages/45/69/5e43d0e8c2ca903aaa2def7f755b97a3aedc5793630abbd004f2afc3b295/restructuredtext_lint-1.3.2.tar.gz
BuildArch:      noarch

%description
Lint reStructuredText linter files with an API or a CLI.

%package -n python3-restructuredtext-lint
Summary:        reStructuredText linter
Provides:       python-restructuredtext-lint
# Base build requires
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-pip
BuildRequires:  python3-wheel

BuildRequires:  python3-docutils >= 0.11
BuildRequires:  python3-docutils < 1.0

%description -n python3-restructuredtext-lint
Lint reStructuredText linter files with an API or a CLI.

%package help
Summary:        reStructuredText linter
Provides:       python3-restructuredtext-lint-doc

%description help
Lint reStructuredText linter files with an API or a CLI.

%prep
%autosetup -n restructuredtext_lint-1.3.2 -p1

%build
%py3_build

%install
%py3_install
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

%files -n python3-restructuredtext-lint -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Thur Jan 27 2022 lijiawei <ljw1101.vip@gmail.com> - 1.3.2-3
- Remove check because python3-nose has entered a recession

* Fri Jul 30 2021 chenyanpanHW <chenyanpan@huawei.com> - 1.3.2-2
- DESC: delete -S git from %autosetup

* Tue Jul 13 2021 OpenStack_SIG <openstack@openeuler.org> - 1.3.2-1
- Package Spec generate
