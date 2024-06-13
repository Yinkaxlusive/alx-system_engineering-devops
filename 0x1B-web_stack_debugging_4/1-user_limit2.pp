# Puppet manifest to adjust file descriptor limits for holberton user

# Define the exec resource to update limits.conf
exec { 'update_limits_conf':
  command => 'echo "holberton soft nofile 10000" >> /etc/security/limits.conf && echo "holberton hard nofile 10000" >> /etc/security/limits.conf',
  path    => ['/bin', '/sbin', '/usr/bin', '/usr/sbin'],
  unless  => 'grep -E "^holberton[[:space:]]+hard[[:space:]]+nofile[[:space:]]+10000" /etc/security/limits.conf',
}

# Define the exec resource to reload sysctl settings
exec { 'reload_sysctl':
  command     => 'sysctl -p',
  refreshonly => true,
  subscribe   => Exec['update_limits_conf'],
}

# Define the user resource for holberton user
user { 'holberton':
  ensure => present,
}

# Define the file resource for .bash_profile
file { '/home/holberton/.bash_profile':
  ensure  => file,
  owner   => 'holberton',
  content => "# .bash_profile\n# Get the aliases and functions\nif [ -f ~/.bashrc ]; then\n\t. ~/.bashrc\nfi\n\n# User specific environment and startup programs\nPATH=$PATH:$HOME/bin\nexport PATH",
}

