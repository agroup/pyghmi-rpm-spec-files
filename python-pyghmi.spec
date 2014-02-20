%global pypi_name pyghmi
%global lpypi_name pyghmi

Name:           python-%{lpypi_name}
Version:        0.5.8
Release:        1%{?dist}
Summary:        Python General Hardware Management Initiative (IPMI and others)

License:        ASL 2.0
URL:            http://xcat.sf.net/
Source0:        http://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-pbr
BuildRequires:  python-subunit
BuildRequires:  python-setuptools
BuildRequires:  python-testrepository

Requires:       python-pbr
Requires:       python-crypto >= 2.6

%description
This is a pure python implementation of IPMI protocol.


%prep
%setup -q -n %{pypi_name}-%{version}


%build
%{__python} setup.py build


%install
%{__python} setup.py install --skip-build --root %{buildroot}


%files
%doc README LICENSE
%{python_sitelib}

%changelog
* Wed Mar 13 2013 Lucas Alvares Gomes <lucasagomes@gmail.com> - 0.5.8-1
- Initial package.
