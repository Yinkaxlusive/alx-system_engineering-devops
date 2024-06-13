exec { 'modify_max_open_files_limit_setting':
  command => "sed -i 's/#\\s*worker_rlimit_nofile\\s*1024;/worker_rlimit_nofile 10000;/' /etc/nginx/nginx.conf && service nginx restart",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => "grep -q '^\\s*worker_rlimit_nofile\\s*10000;' /etc/nginx/nginx.conf || echo 'worker_rlimit_nofile 10000;' >> /etc/nginx/nginx.conf",
  require => Package['nginx'],
}

