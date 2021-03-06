# TODO:
# - base package sould contain actual jdt, but update clipse.spec first not to
#   bundle itself jdt
# - build the jar, not use prebuilt
Summary:	Eclipse Java Development Tools (JDT) libraries
Summary(pl.UTF-8):	Biblioteki Eclipse JDT
Name:		eclipse-jdt
Version:	4.4.2
Release:	1
License:	EPL v1.0
Group:		Libraries/Java
# http://archive.eclipse.org/eclipse/downloads/
Source0:	http://archive.eclipse.org/eclipse/downloads/drops4/R-%{version}-201502041700/org.eclipse.jdt.source-%{version}.zip
# Source0-md5:	f32680fd5130e677366c249811671db9
URL:		http://www.eclipse.org/jdt/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	java-eclipse-jdt = %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Empty package for upgrades.

If you are looking for JDT plugin for Eclipse, it is included in main
eclipse package.

%package -n java-eclipse-jdt
Summary:	Eclipse Java Development Tools (JDT) libraries
Summary(pl.UTF-8):	Biblioteki Eclipse JDT
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
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javadir}
cp -a plugins/org.eclipse.jdt.core_*.jar $RPM_BUILD_ROOT%{_javadir}/org.eclipse.jdt.core-%{version}.jar
ln -s org.eclipse.jdt.core-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/org.eclipse.jdt.core.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%files -n java-eclipse-jdt
%defattr(644,root,root,755)
%{_javadir}/*.jar
