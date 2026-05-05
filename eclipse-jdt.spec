# TODO:
# - base package should contain actual jdt, but update eclipse.spec first not to
#   bundle itself jdt

%{?use_default_jdk:%use_default_jdk 17}

%define		orgname		eclipse-jdt

# 4.20 is the last Eclipse JDT release that runs on JDK 8.
# 4.21+ requires Java 11+; do not bump on this branch.
%define		drop	R-%{version}-202106111600
Summary:	Eclipse Compiler for Java (ECJ) - JDK 8 compatible
Summary(pl.UTF-8):	Kompilator Eclipse dla Javy (ECJ) - kompatybilny z JDK 8
Name:		%{orgname}8
Version:	4.20
Release:	3
License:	EPL v2.0
Group:		Libraries/Java
Source0:	https://archive.eclipse.org/eclipse/downloads/drops4/%{drop}/ecjsrc-%{version}.jar
# Source0-md5:	83890b79848fcadb25479a13b9d6de16
Source1:	ecj-build.xml
URL:		https://www.eclipse.org/jdt/
BuildRequires:	ant
%buildrequires_jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 2.021
Requires:	java-%{name} = %{version}-%{release}
Conflicts:	%{orgname}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Empty package for upgrades.

If you are looking for JDT plugin for Eclipse, it is included in main
eclipse package.

%package -n java-%{name}
Summary:	Eclipse Compiler for Java (ECJ) libraries - JDK 8 compatible
Summary(pl.UTF-8):	Biblioteki kompilatora Eclipse dla Javy (ECJ) - kompatybilne z JDK 8
Group:		Libraries/Java
Requires:	jpackage-utils
Conflicts:	java-%{orgname}

%description -n java-%{name}
This package contains library needed to build and run some java
applications developed with Eclipse IDE (most notably tomcat). This
build is the last release of Eclipse JDT that still runs on JDK 8.

If you are looking for JDT plugin for Eclipse, it is included in main
eclipse package.

%description -n java-%{name} -l pl.UTF-8
Ten pakiet zawiera bibliotekę potrzebną do zbudowania i uruchomienia
niektórych aplikacji pewnych aplikacji napisanych w javie przy użyciu
Eclipse IDE (przykładowo tomcata). Ta wersja to ostatnie wydanie
Eclipse JDT działające na JDK 8.

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

%files -n java-%{name}
%defattr(644,root,root,755)
%{_javadir}/*.jar
