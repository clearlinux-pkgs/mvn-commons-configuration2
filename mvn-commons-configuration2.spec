#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-commons-configuration2
Version  : 2.1.1
Release  : 2
URL      : https://repo1.maven.org/maven2/org/apache/commons/commons-configuration2/2.1.1/commons-configuration2-2.1.1.jar
Source0  : https://repo1.maven.org/maven2/org/apache/commons/commons-configuration2/2.1.1/commons-configuration2-2.1.1.jar
Source1  : https://repo1.maven.org/maven2/org/apache/commons/commons-configuration2/2.1.1/commons-configuration2-2.1.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-commons-configuration2-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-commons-configuration2 package.
Group: Data

%description data
data components for the mvn-commons-configuration2 package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-configuration2/2.1.1
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-configuration2/2.1.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-configuration2/2.1.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-configuration2/2.1.1


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/commons/commons-configuration2/2.1.1/commons-configuration2-2.1.1.jar
/usr/share/java/.m2/repository/org/apache/commons/commons-configuration2/2.1.1/commons-configuration2-2.1.1.pom
