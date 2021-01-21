#
# Conditional build:
%bcond_with	tests	# unit tests (not included in dist)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Simple Python URL class
Summary(pl.UTF-8):	Prosta klasa URL dla Pythona
Name:		python-purl
Version:	1.5
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/purl/
Source0:	https://files.pythonhosted.org/packages/source/p/purl/purl-%{version}.tar.gz
# Source0-md5:	2a10782a6f0c771f3f3319956d41f7ff
URL:		https://pypi.org/project/purl/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-six
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple, immutable URL class with a clean API for interrogation and
manipulation.

%description -l pl.UTF-8
Prosta, niezmienna klasa URL z czystym API do zapytań i operacji.

%package -n python3-purl
Summary:	Simple Python URL class
Summary(pl.UTF-8):	Prosta klasa URL dla Pythona
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-purl
A simple, immutable URL class with a clean API for interrogation and
manipulation.

%description -n python3-purl -l pl.UTF-8
Prosta, niezmienna klasa URL z czystym API do zapytań i operacji.

%prep
%setup -q -n purl-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/purl
%{py_sitescriptdir}/purl-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-purl
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/purl
%{py3_sitescriptdir}/purl-%{version}-py*.egg-info
%endif
