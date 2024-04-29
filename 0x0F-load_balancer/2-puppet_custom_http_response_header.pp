#!/usr/bin/env puppet

# Puppet manifest to add a custom HTTP header with Puppet
# The custom HTTP header name is X-Served-By
# The value of the custom HTTP header is the hostname of the server Nginx is running on

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define custom HTTP header configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "# Custom HTTP header configuration\nserver {\n  listen 80 default_server;\n  listen [::]:80 default_server;\n  server_name _;\n\n  location / {\n    add_header X-Served-By $::hostname;\n    # Additional configuration\n  }\n}\n",
}

# Enable the custom configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

# Restart Nginx service to apply changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-enabled/default'],
}

