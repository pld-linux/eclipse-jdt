# TODO:
# - base package should contain actual jdt, but update eclipse.spec first not to
#   bundle itself jdt
%define		drop	R-%{version}-202512010920
Summary:	Eclipse Compiler for Java (ECJ)
Summary(pl.UTF-8):	Kompilator Eclipse dla Javy (ECJ)
Name:		eclipse-jdt
Version:	4.38
Release:	1
License:	EPL v2.0
Group:		Libraries/Java
Source0:	https://archive.eclipse.org/eclipse/downloads/drops4/%{drop}/ecjsrc-%{version}.jar
# Source0-md5:	29df435c80c010694012de442474ad88
Source1:	ecj-build.xml
URL:		https://www.eclipse.org/jdt/
BuildRequires:	ant
BuildRequires:	jdk >= 23
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	java-eclipse-jdt = %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Empty package for upgrades.

If you are looking for JDT plugin for Eclipse, it is included in main
eclipse package.

%package -n java-eclipse-jdt
Summary:	Eclipse Compiler for Java (ECJ) libraries
Summary(pl.UTF-8):	Biblioteki kompilatora Eclipse dla Javy (ECJ)
Group:		Libraries/Java
Requires:	jpackage-utils

%description -n java-eclipse-jdt
This package contains library needed to build and run some java
applications developed with Eclipse IDE (most notably tomcat).

If you are looking for JDT plugin for Eclipse, it is included in main
eclipse package.

%description -n java-eclipse-jdt -l pl.UTF-8
Ten pakiet zawiera bibliotekę potrzebną do zbudowania i uruchomienia
niektórych aplikacji pewnych aplikacji napisanych w javie przy użyciu
Eclipse IDE (przykładowo tomcata).

Jeżeli szukasz pluginu JDT dla środowiska programistycznego IDE, to
jest on zawarty w głównym pakiecie eclipse.

%prep
%setup -qc -n ecj-%{version}
cp -p %{SOURCE1} build.xml

%build
%ant

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javadir}
cp -a ecj.jar $RPM_BUILD_ROOT%{_javadir}/org.eclipse.jdt.core-%{version}.jar
ln -s org.eclipse.jdt.core-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/org.eclipse.jdt.core.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%files -n java-eclipse-jdt
%defattr(644,root,root,755)
%{_javadir}/*.jar
