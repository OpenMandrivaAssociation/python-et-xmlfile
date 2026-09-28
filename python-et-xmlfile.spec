Name:		python-et-xmlfile
Version:	2.0.0
Release:	1
Summary:	An implementation of lxml.xmlfile for the standard library
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/et-xmlfile/
Source0:	et_xmlfile-2.0.0.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch
%description
An implementation of lxml.xmlfile for the standard library.

%files
%{py_sitedir}/*
