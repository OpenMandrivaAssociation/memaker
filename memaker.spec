Name:		memaker
# revision number..
Version:	r49
Release:	2
Summary:	An avatar creator

Group:		Graphics
License:	GPLv3+
URL:		https://launchpad.net/memaker 
# bzr branch lp:memaker && bzr export --format=tar - memaker --root=memaker-%{version}/ | xz > memaker-%{version}.tar.xz
Source0:	%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:	python-distutils-extra intltool
BuildRequires:	desktop-file-utils
Requires:	python-mate-rsvg pkgconfig(notify-python) python-numpy pythonegg(pil)
Requires:	gnome-python-gnomevfs

%description
MeMaker gives users a wide variety of images that, when placed 
together, create an avatar. This avatar is intended to represent 
the way that this person is in some way. The goal of the project 
is to have enough images that anyone can create an image that 
they feel would closely represent them without having to use a photo
in the image itself.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --skip-build --root=%{buildroot}

# not copied by setup script
cp -av data/labels %{buildroot}%{_datadir}/%{name}/

# icons and desktop files
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/

desktop-file-install --dir=%{buildroot}%{_datadir}/applications build/share/applications/%{name}.desktop

cp -av data/icons/scalable/apps/%{name}.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
cp -av data/icons/48x48/apps/%{name}.png %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/

%files
%doc AUTHORS README TODO
%{_datadir}/%{name}/
%{_bindir}/%{name}
%{python_sitelib}/MeMaker/
%{python_sitelib}/%{name}-?.?-py?.?.egg-info
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/applications/%{name}.desktop 


%changelog
* Sat Dec  1 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> r49-1
- cleaned up and adapted for Mandriva Linux

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100110-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 07 2012 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 20100110-3
- https://bugzilla.redhat.com/show_bug.cgi?id=772346
- Add requires

* Fri Jan 06 2012 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 20100110-2
- spec bump for gcc 4.7 rebuild

* Mon May 09 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 20100110-1
- Correcting the directory ownership
- #608319
- replaced "memaker" with name macro 
- changed cp -v to cp -av to preserve timestamps
- update to upstream dev 

* Tue Jun 22 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5-1
- initial rpm build
