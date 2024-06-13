exec { 'modify_max_open_files_limit_setting':
  command => 'sed -i "s/# worker_rlimit_nofile 1024;/worker_rlimit_nofile 10000;/" /etc/nginx/nginx.conf && sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
