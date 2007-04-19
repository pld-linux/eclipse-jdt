Summary:	Eclipse Java Development Tools (JDT)
Name:		eclipse-jdt
Version:	3.1.2
Release:	0.1
License:	EPL v1.0
Group:		Development/Languages/Java
Source0:	http://archive.eclipse.org/eclipse/downloads/drops/R-%{version}-200601181600/eclipse-JDT-%{version}.zip
# Source0-md5:	f2c8066151de14c5ccdf420266ce9f39
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
