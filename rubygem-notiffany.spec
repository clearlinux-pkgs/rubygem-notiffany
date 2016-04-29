#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-notiffany
Version  : 0.0.7
Release  : 4
URL      : https://rubygems.org/downloads/notiffany-0.0.7.gem
Source0  : https://rubygems.org/downloads/notiffany-0.0.7.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rdoc

%description
# Notiffany
Notification library supporting popular notifiers, such as:
- Growl
- libnotify
- TMux
- Emacs
- rb-notifu
- notifysend
- gntp
- TerminalNotifier

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n notiffany-0.0.7
gem spec %{SOURCE0} -l --ruby > rubygem-notiffany.gemspec

%build
gem build rubygem-notiffany.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
notiffany-0.0.7.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/notiffany-0.0.7.gem
/usr/lib64/ruby/gems/2.3.0/gems/notiffany-0.0.7/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/notiffany-0.0.7/README.md
/usr/lib64/ruby/gems/2.3.0/gems/notiffany-0.0.7/images/failed.png
/usr/lib64/ruby/gems/2.3.0/gems/notiffany-0.0.7/images/pending.png
/usr/lib64/ruby/gems/2.3.0/gems/notiffany-0.0.7/images/success.png
/usr/lib64/ruby/gems/2.3.0/gems/notiffany-0.0.7/lib/notiffany.rb
/usr/lib64/ruby/gems/2.3.0/gems/notiffany-0.0.7/lib/notiffany/notifier.rb
/usr/lib64/ruby/gems/2.3.0/gems/notiffany-0.0.7/lib/notiffany/notifier/base.rb
/usr/lib64/ruby/gems/2.3.0/gems/notiffany-0.0.7/lib/notiffany/notifier/detected.rb
/usr/lib64/ruby/gems/2.3.0/gems/notiffany-0.0.7/lib/notiffany/notifier/emacs.rb
/usr/lib64/ruby/gems/2.3.0/gems/notiffany-0.0.7/lib/notiffany/notifier/file.rb
/usr/lib64/ruby/gems/2.3.0/gems/notiffany-0.0.7/lib/notiffany/notifier/gntp.rb
/usr/lib64/ruby/gems/2.3.0/gems/notiffany-0.0.7/lib/notiffany/notifier/growl.rb
/usr/lib64/ruby/gems/2.3.0/gems/notiffany-0.0.7/lib/notiffany/notifier/libnotify.rb
/usr/lib64/ruby/gems/2.3.0/gems/notiffany-0.0.7/lib/notiffany/notifier/notifysend.rb
/usr/lib64/ruby/gems/2.3.0/gems/notiffany-0.0.7/lib/notiffany/notifier/rb_notifu.rb
/usr/lib64/ruby/gems/2.3.0/gems/notiffany-0.0.7/lib/notiffany/notifier/terminal_notifier.rb
/usr/lib64/ruby/gems/2.3.0/gems/notiffany-0.0.7/lib/notiffany/notifier/terminal_title.rb
/usr/lib64/ruby/gems/2.3.0/gems/notiffany-0.0.7/lib/notiffany/notifier/tmux.rb
/usr/lib64/ruby/gems/2.3.0/gems/notiffany-0.0.7/lib/notiffany/version.rb
/usr/lib64/ruby/gems/2.3.0/specifications/notiffany-0.0.7.gemspec
