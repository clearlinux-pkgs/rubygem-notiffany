#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-notiffany
Version  : 0.0.7
Release  : 1
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
/usr/lib64/ruby/gems/2.2.0/cache/notiffany-0.0.7.gem
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Base/RequireFailed/cdesc-RequireFailed.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Base/RequireFailed/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Base/UnavailableError/cdesc-UnavailableError.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Base/UnavailableError/message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Base/UnavailableError/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Base/UnsupportedPlatform/cdesc-UnsupportedPlatform.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Base/UnsupportedPlatform/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Base/_check_available-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Base/_check_host_supported-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Base/_gem_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Base/_image_path-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Base/_notification_type-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Base/_notify_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Base/_perform_notify-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Base/_require_gem-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Base/_supported_hosts-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Base/cdesc-Base.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Base/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Base/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Base/notify-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Base/options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Base/title-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Detected/NoneAvailableError/cdesc-NoneAvailableError.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Detected/UnknownNotifier/cdesc-UnknownNotifier.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Detected/UnknownNotifier/message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Detected/UnknownNotifier/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Detected/UnknownNotifier/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Detected/_notifiers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Detected/_to_module-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Detected/add-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Detected/available-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Detected/cdesc-Detected.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Detected/detect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Detected/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Detected/reset-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Emacs/Client/available%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Emacs/Client/cdesc-Client.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Emacs/Client/emacs_eval-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Emacs/Client/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Emacs/Client/notify-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Emacs/_check_available-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Emacs/_emacs_color-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Emacs/_gem_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Emacs/_perform_notify-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Emacs/cdesc-Emacs.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/File/_check_available-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/File/_gem_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/File/_perform_notify-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/File/cdesc-File.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/GNTP/_check_available-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/GNTP/_gem_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/GNTP/_gntp_client-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/GNTP/_perform_notify-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/GNTP/_supported_hosts-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/GNTP/cdesc-GNTP.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Growl/_check_available-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Growl/_perform_notify-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Growl/_supported_hosts-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Growl/cdesc-Growl.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Libnotify/_check_available-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Libnotify/_perform_notify-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Libnotify/_supported_hosts-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Libnotify/cdesc-Libnotify.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/NotServer/cdesc-NotServer.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Notifu/_check_available-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Notifu/_gem_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Notifu/_notifu_type-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Notifu/_perform_notify-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Notifu/_supported_hosts-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Notifu/cdesc-Notifu.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/NotifySend/_check_available-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/NotifySend/_gem_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/NotifySend/_notifysend_urgency-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/NotifySend/_perform_notify-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/NotifySend/_supported_hosts-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/NotifySend/_to_arguments-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/NotifySend/cdesc-NotifySend.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/TerminalNotifier/_check_available-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/TerminalNotifier/_gem_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/TerminalNotifier/_perform_notify-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/TerminalNotifier/_supported_hosts-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/TerminalNotifier/cdesc-TerminalNotifier.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/TerminalTitle/_check_available-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/TerminalTitle/_gem_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/TerminalTitle/_perform_notify-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/TerminalTitle/cdesc-TerminalTitle.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/TerminalTitle/turn_off-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/Client/_capture-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/Client/_capture-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/Client/_parse_option-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/Client/_run-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/Client/_run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/Client/cdesc-Client.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/Client/clients-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/Client/display_message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/Client/display_time%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/Client/message_bg%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/Client/message_fg%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/Client/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/Client/parse_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/Client/set-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/Client/title%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/Client/unset-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/Client/version-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/Error/cdesc-Error.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/Session/cdesc-Session.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/Session/close-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/Session/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/_check_available-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/_display_message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/_display_title-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/_end_session-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/_gem_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/_perform_notify-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/_session-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/_start_session-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/_tmux_color-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/cdesc-Tmux.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/client-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/turn_off-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/Tmux/turn_on-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/_check_server%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/_client%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/_env-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/active%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/available-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/cdesc-Notifier.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/disconnect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/enabled%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/notify-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/turn_off-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/Notifier/turn_on-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/cdesc-Notiffany.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/Notiffany/connect-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/notiffany-0.0.7/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/gems/notiffany-0.0.7/LICENSE.txt
/usr/lib64/ruby/gems/2.2.0/gems/notiffany-0.0.7/README.md
/usr/lib64/ruby/gems/2.2.0/gems/notiffany-0.0.7/images/failed.png
/usr/lib64/ruby/gems/2.2.0/gems/notiffany-0.0.7/images/pending.png
/usr/lib64/ruby/gems/2.2.0/gems/notiffany-0.0.7/images/success.png
/usr/lib64/ruby/gems/2.2.0/gems/notiffany-0.0.7/lib/notiffany.rb
/usr/lib64/ruby/gems/2.2.0/gems/notiffany-0.0.7/lib/notiffany/notifier.rb
/usr/lib64/ruby/gems/2.2.0/gems/notiffany-0.0.7/lib/notiffany/notifier/base.rb
/usr/lib64/ruby/gems/2.2.0/gems/notiffany-0.0.7/lib/notiffany/notifier/detected.rb
/usr/lib64/ruby/gems/2.2.0/gems/notiffany-0.0.7/lib/notiffany/notifier/emacs.rb
/usr/lib64/ruby/gems/2.2.0/gems/notiffany-0.0.7/lib/notiffany/notifier/file.rb
/usr/lib64/ruby/gems/2.2.0/gems/notiffany-0.0.7/lib/notiffany/notifier/gntp.rb
/usr/lib64/ruby/gems/2.2.0/gems/notiffany-0.0.7/lib/notiffany/notifier/growl.rb
/usr/lib64/ruby/gems/2.2.0/gems/notiffany-0.0.7/lib/notiffany/notifier/libnotify.rb
/usr/lib64/ruby/gems/2.2.0/gems/notiffany-0.0.7/lib/notiffany/notifier/notifysend.rb
/usr/lib64/ruby/gems/2.2.0/gems/notiffany-0.0.7/lib/notiffany/notifier/rb_notifu.rb
/usr/lib64/ruby/gems/2.2.0/gems/notiffany-0.0.7/lib/notiffany/notifier/terminal_notifier.rb
/usr/lib64/ruby/gems/2.2.0/gems/notiffany-0.0.7/lib/notiffany/notifier/terminal_title.rb
/usr/lib64/ruby/gems/2.2.0/gems/notiffany-0.0.7/lib/notiffany/notifier/tmux.rb
/usr/lib64/ruby/gems/2.2.0/gems/notiffany-0.0.7/lib/notiffany/version.rb
/usr/lib64/ruby/gems/2.2.0/specifications/notiffany-0.0.7.gemspec
