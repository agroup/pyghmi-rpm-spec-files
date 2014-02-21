%global sname pyghmi

Name:           python-%{sname}
Version:        0.5.9
Release:        1%{?dist}
Summary:        Python General Hardware Management Initiative (IPMI and others)

License:        ASL 2.0
URL:            https://github.com/stackforge/pyghmi
Source0:        http://pypi.python.org/packages/source/p/%{sname}/%{sname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr

Requires:       python-crypto >= 2.6

%description
This is a pure python implementation of the IPMI protocol.


%prep
%setup -q -n %{sname}-%{version}

# Remove bundled egg-info
rm -rf %{sname}.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%files
%doc README LICENSE
%{python2_sitelib}/pyghmi
%{python2_sitelib}/*.egg-info


%changelog
* Thu Feb 20 2014 Lucas Alvares Gomes <lucasagomes@gmail.com> - 0.5.9-1
- Initial package.
