Summary:	Eclipse Java Development Tools (JDT)
Summary(pl.UTF-8):	Narzędzia programistyczne JDT (Java Development Tools) dla Eclipse
Name:		eclipse-jdt
Version:	3.1.2
Release:	0.1
License:	EPL v1.0
Group:		Development/Languages/Java
Source0:	http://archive.eclipse.org/eclipse/downloads/drops/R-%{version}-200601181600/eclipse-JDT-%{version}.zip
# Source0-md5:	5425b78525b6f0b01416b78cdef4d50e
URL:		http://www.eclipse.org/jdt/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The JDT project provides the tool plug-ins that implement a Java IDE
supporting the development of any Java application, including Eclipse
plug-ins. It adds a Java project nature and Java perspective to the
Eclipse Workbench as well as a number of views, editors, wizards,
builders, and code merging and refactoring tools. The JDT project
allows Eclipse to be a development environment for itself.

%description -l pl.UTF-8
Projekt JDT udostępnia wtyczki narzędziowe implementujące IDE dla Javy
wspierające tworzenie dowolnych aplikacji w Javie, włącznie z
wtyczkami dla Eclipse. Dodają one rodzaj projektu Java i perspektywę
Java do Eclipse Workbench, a także wiele widoków, edytorów,
asystentów oraz narzędzi do budowania, łączenia i refaktoryzacji
kodu. Projekt JDT pozwala Eclipse być środowiskiem programistycznym
dla samego siebie.

%prep
%setup -q -n eclipse

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
cp -a plugins/org.eclipse.jdt.core_%{version}.jar $RPM_BUILD_ROOT%{_javadir}/org.eclipse.jdt.core-%{version}.jar
ln -s org.eclipse.jdt.core-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/org.eclipse.jdt.core.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc epl-v10.html notice.html
%{_javadir}/*.jar